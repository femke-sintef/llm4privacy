from read import get_df_results, get_df_segments_with_gt, get_df_annotations
from sklearn import metrics
if __name__ == "__main__":
    # obtain dfs
    df_annotations = get_df_annotations("OPP-115")
    df_segments_with_gt = get_df_segments_with_gt("OPP-115",df_annotations)
    df_results = get_df_results("results/gpt-4/OPP-115/20240208_113137/results.xlsx")

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

    y_pred = df_results[["Other",
        "User Choice/Control",
        "First Party Collection/Use",
        "Third Party Sharing/Collection",
        "Do Not Track",
        "User Access, Edit and Deletion",
        "Data Security",
        "Data Retention",
        "International and Specific Audiences",
        "Policy Change",]].values

    print(metrics.classification_report(y_true, y_pred, target_names=["Other",
        "User Choice/Control",
        "First Party Collection/Use",
        "Third Party Sharing/Collection",
        "Do Not Track",
        "User Access, Edit and Deletion",
        "Data Security",
        "Data Retention",
        "International and Specific Audiences",
        "Policy Change",]))


        "https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-harkous.pdf"
        "https://cdn.aaai.org/ocs/14113/14113-62070-1-PB.pdf"
        "https://dl.acm.org/doi/pdf/10.1145/3487553.3524663"
        "https://usableprivacy.org/static/files/CMU-ISR-17-118R.pdf"