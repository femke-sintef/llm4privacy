"""NOTES:

We created gold
standard data for this problem using a simplified
consolidation approach: if two or more annotators
agreed that a category is present in a segment, then
we labeled that segment with the category

"""

import os
from glob import glob

import pandas as pd
import numpy as np
import json
from tqdm import tqdm
import re

PATH_TO_DATA = "data"

CATEGORY_NAMES = [
    "Other",
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


def remove_html_tags(text):
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def get_df_annotations(dataset_name):
    # read all annotation files into single df
    header_names = [
        "annotation_ID",
        "batch_ID",
        "annotator_ID",
        "policy_ID_other",
        "segment_ID",
        "category_name",
        "attribute_value_pairs",
        "date",
        "policy_URL",
    ]
    df_annotations = []
    for path, subdir, files in os.walk(
        os.path.join(PATH_TO_DATA, dataset_name, "annotations")
    ):
        for file_path in glob(os.path.join(path, "*.csv")):
            annotation = pd.read_csv(file_path, header=None, names=header_names)
            annotation["policy_ID"] = os.path.basename(file_path).split("_")[0]
            df_annotations.append(annotation)
    df_annotations = pd.concat(df_annotations, axis=0, ignore_index=True)
    df_annotations["complete_segment_ID"] = (
        df_annotations["policy_ID"].astype(str)
        + "_"
        + df_annotations["segment_ID"].astype(str)
    )

    # make sure data agrees with paper
    assert len(df_annotations["annotator_ID"].unique()) == 10
    assert len(df_annotations["policy_ID"].unique()) == 115
    assert all(df_annotations.groupby("policy_ID")["annotator_ID"].nunique() == 3)
    assert len(df_annotations) == 23194

    return df_annotations


def get_df_segments(dataset_name):
    # read all sanatized html files and obtain df with policy_ID, segment_ID and the sentences
    list_of_df_dicts = []
    for path, subdir, files in os.walk(
        os.path.join(PATH_TO_DATA, dataset_name, "sanitized_policies")
    ):
        for file_path in glob(os.path.join(path, "*.html")):
            policy_ID = os.path.basename(file_path).split("_")[0]
            file_contents = open(file_path, "r")
            segments = file_contents.read().split("|||")
            for ind, segment in enumerate(segments):
                list_of_df_dicts.append(
                    {
                        "policy_ID": int(policy_ID),
                        "segment_ID": ind,
                        "segment_text": segment,
                    }
                )
    df_segments = pd.DataFrame.from_dict(list_of_df_dicts)
    df_segments["complete_segment_ID"] = (
        df_segments["policy_ID"].astype(str)
        + "_"
        + df_segments["segment_ID"].astype(str)
    )
    return df_segments


def get_df_segments_with_gt(dataset_name,df_annotations):
    # obtain df_segments with groundtruth
    df_segments = get_df_segments(dataset_name)
    tqdm.pandas()
    df_segments["gt"] = df_segments["complete_segment_ID"].progress_apply(
        get_ground_truth, args=(df_annotations,)
    )
    df_segments = df_segments.join(df_segments["gt"].str.join("|").str.get_dummies())
    return df_segments

def get_df_results(file_path):
    # obtain df_segments with pred
    df_results = pd.read_excel(file_path)
    tqdm.pandas()
    df_results["pred"] = df_results["llm_response"].progress_apply(
        detect_categories
    )
    df_results = df_results.join(df_results["pred"].str.join("|").str.get_dummies())
    return df_results

def detect_categories(llm_response_value):
    pred = []
    for category in CATEGORY_NAMES:
        if category == "International and Specific Audiences":
            cat_to_check = "International & Specific Audiences"
        elif category =="User Access, Edit and Deletion":
            cat_to_check = "User Access, Edit, & Deletion"
        else:
            cat_to_check = category
        if cat_to_check in llm_response_value:
            pred.append(category)
    return pred
def get_ground_truth(complete_segment_ID_value, df_annotations):
    annotations = df_annotations.loc[
        df_annotations["complete_segment_ID"] == complete_segment_ID_value
    ]
    annotations = annotations[["annotator_ID", "category_name"]].drop_duplicates()
    annotations = annotations["category_name"].value_counts()[
        annotations["category_name"].value_counts() >= 2
    ]
    return annotations.index.to_list()


if __name__ == "__main__":
    # obtain dfs
    df_segments = get_df_segments("OPP-115")
    df_annotations = get_df_annotations("OPP-115")
    df_segments_with_gt = get_df_segments_with_gt("OPP-115",df_annotations)
    df_results = get_df_results("results/gpt-4/OPP-115/20240208_113137/results.xlsx")
    # merge dfs to obtain one df with both tags and sentences
    df = df_annotations.merge(df_segments, how="left", on="complete_segment_ID")

    # interpret results

    print(df)
