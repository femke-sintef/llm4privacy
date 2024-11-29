from read import get_df_results, get_df_segments_with_gt, get_df_annotations, get_df_segments
from sklearn import metrics
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

from read import get_ground_truth
from analysis import get_confidence_intervals

RELEVANT_COLUMNS = [  # "Other",
    "User Choice/Control",
    "First Party Collection/Use",
    "Third Party Sharing/Collection",
    "Do Not Track",
    "User Access, Edit and Deletion",
    "Data Security",
    "Data Retention",
    "International and Specific Audiences",
    "Policy Change",
]
RELEVANT_COLUMNS_SHORT = [  # "Other",
    "User Choice...",
    "First Party...",
    "Third Party...",
    "Do Not Track...",
    "User Access...",
    "Data Security",
    "Data Retention",
    "International...",
    "Policy Change",
]

result_paths_base = "results/OPP-115/multianalysis"
if __name__ == "__main__":
    # obtain data
    print("Obtaining saved data for analysis...")
    df_annotations = get_df_annotations("OPP-115")
    df_segments_with_gt = get_df_segments_with_gt("OPP-115", df_annotations=df_annotations, remove_html_tags=True)
    df_results = get_df_segments("OPP-115", remove_html_tags=True)
    
    result_paths = []
    for path, subdirs, files in os.walk(result_paths_base):
        for name in files:
            if name == "results.xlsx":
                result_paths.append(os.path.join(path, name))
    
    # combine result data from all runs
    dfs = []
    for result_path in result_paths:
        df_results_all = get_df_results(result_path, return_dummies=False)
        df_results_all["annotator_ID"] = result_path.split("/")[-2]
        dfs.append(df_results_all)
    df_results_all = pd.concat(dfs, axis=0, ignore_index=True)

    
    # explode results so that there is one row for each llm annotation
    df_results_all=df_results_all.explode("pred")

    # filter results so that prediction only counts if it was provided at least twice
    kwargs = {"column_name":"pred"}
    df_results["pred_filtered"] = df_results[
        "complete_segment_ID"
    ].progress_apply(get_ground_truth, args=(df_results_all, ), **kwargs)

    df_results = df_results.sort_values(by=['complete_segment_ID'])
    df_segments_with_gt = df_segments_with_gt.sort_values(by=['complete_segment_ID'])

    # obtain dummy arrays, removing other category
    df_results = df_results.join(df_results["pred_filtered"].str.join("|").str.get_dummies())
    y_true = df_segments_with_gt[RELEVANT_COLUMNS].values
    y_pred = df_results[RELEVANT_COLUMNS].values
    ind_only_other = np.sum(y_true, axis=1) == 0
    y_true = y_true[~ind_only_other]
    y_pred = y_pred[~ind_only_other]
    df_results = df_results[~ind_only_other]
    df_segments_with_gt = df_segments_with_gt[~ind_only_other]

    # generate report of performance metrics in df form
    report = metrics.classification_report(
        y_true,
        y_pred,
        target_names=RELEVANT_COLUMNS,
        output_dict=True,
        zero_division=0.0,
    )
    report = pd.DataFrame(report).transpose()
    report  = get_confidence_intervals(df_segments_with_gt, df_results, report)
    f1s =[]
    for i, df in enumerate(dfs):
        # check consistency
        df_0 = dfs[0].sort_values(by=['complete_segment_ID'])
        df = df.sort_values(by=['complete_segment_ID'])
        if i==0:
            consistent = df_0['pred'].eq(df_0['pred'])
        else:
            consistent = np.equal(df_0["pred"].values,df["pred"].values) & consistent
        # find f1s
        y_pred_sdf = df.join(df["pred"].str.join("|").str.get_dummies())
        y_pred_sdf = y_pred_sdf[RELEVANT_COLUMNS].values   
        y_pred_sdf = y_pred_sdf[~ind_only_other]
        report_this_round = metrics.classification_report(
            y_pred,
            y_pred_sdf,
            target_names=RELEVANT_COLUMNS,
            output_dict=True,
            zero_division=0.0,
        )
        f1s.append(report_this_round["micro avg"]["f1-score"])
        
    consistency = np.sum(consistent) / len(consistent) * 100

    # create an overview over the misclassified samples
    print("Create an overview over the misclassified samples...")
    correctly_classified = np.all(np.equal(y_pred, y_true), axis=1)
    ground_truth = y_true[~correctly_classified]
    ground_truth_list = []
    for idx in range(len(ground_truth)):
        ground_truth_list.append(
            list(np.asarray(RELEVANT_COLUMNS)[ground_truth[idx] == 1])
        )
    ground_truth_list = ["&".join(item) for item in ground_truth_list]
    pred = y_pred[~correctly_classified]
    pred_list = []
    for idx in range(len(pred)):
        pred_list.append(list(np.asarray(RELEVANT_COLUMNS)[pred[idx] == 1]))
    pred_list = ["&".join(item) for item in pred_list]
    df_misclassified = df_results[~correctly_classified]
    df_misclassified.loc[:, ["gt"]] = ground_truth_list
    df_misclassified.loc[:, ["pred"]] = pred_list
    df_misclassified = df_misclassified.drop(RELEVANT_COLUMNS, axis=1)
    df_misclassified = df_misclassified.drop("Other", axis=1, errors="ignore")

    # obtaining confusion matrix removing multibale samples
    print("Obtain confusion matrix...")
    ind_multilabel_true = np.sum(y_true, axis=1) == 1
    y_true = y_true[ind_multilabel_true]
    y_pred = y_pred[ind_multilabel_true]
    ind_multilabel_pred = np.sum(y_pred, axis=1) == 1
    y_true = y_true[ind_multilabel_pred]
    y_pred = y_pred[ind_multilabel_pred]
    disp = metrics.ConfusionMatrixDisplay.from_predictions(
        y_true.argmax(axis=1),
        y_pred.argmax(axis=1),
        display_labels=RELEVANT_COLUMNS_SHORT,
        # normalize="true",
    ).plot(
        xticks_rotation="vertical"
    )  # ,values_format=".2f")
    plt.tight_layout()
    plt.show()

    # saving output
    print("Saving ouput...")
    df_misclassified.to_excel(
        os.path.join(result_paths_base, "misclassified.xlsx")
    )
    report.to_excel(os.path.join(result_paths_base, "report.xlsx"))
    plt.savefig(os.path.join(result_paths_base, "confusion.png"))
    print("Done!")
    # print report with all data
    print(report)

    print(str(consistency) + " of segments are labelled exactly the same all " + str(len(dfs)) + " rounds")
    print("Average f1 compared to own gt: " + str(np.mean(np.asarray(f1s))) + " max: " + str(np.max(np.asarray(f1s))) + " min: "+ str(np.min(np.asarray(f1s))))
