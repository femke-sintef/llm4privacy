from read import get_df_results, get_df_segments_with_gt, get_df_annotations
from sklearn import metrics

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

if __name__ == "__main__":
    # obtain dfs
    df_annotations = get_df_annotations("OPP-115")
    df_segments_with_gt = get_df_segments_with_gt("OPP-115", df_annotations)
    df_segments_with_gt.set_index("complete_segment_ID", inplace=True)
    y_true = df_segments_with_gt[["Other",
        "User Choice/Control",
        "First Party Collection/Use",
        "Third Party Sharing/Collection",
        "Do Not Track",
        "User Access, Edit and Deletion",
        "Data Security",
        "Data Retention",
        "International and Specific Audiences",
        "Policy Change",]].values
    df_results = get_df_results("results/gpt-4/OPP-115/20240228_111958/results_25.xlsx") # PROMPT_III
    df_results.set_index("complete_segment_ID", inplace=True)
    df_segments_with_gt = df_segments_with_gt.loc[df_results.index]
    for column in RELEVANT_COLUMNS:
        if column not in df_results.columns:
            df_results[column] = 0

    y_true = df_segments_with_gt[RELEVANT_COLUMNS].values
    y_pred = df_results[RELEVANT_COLUMNS].values

    print(metrics.classification_report(y_true, y_pred, target_names=RELEVANT_COLUMNS))
