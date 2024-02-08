import os
from glob import glob

import pandas as pd
import numpy as np
import json

import re

PATH_TO_DATA = "data"


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

    return df_annotations

    # merge dfs to obtain one df with both tags and sentences
    df = df_annotations.merge(df_segments, how="left", on="complete_segment_ID")
    return df_segments, df


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


if __name__ == "__main__":
    # obtain dfs
    df_segments = get_df_segments("OPP-115")
    df_annotations = get_df_annotations("OPP-115")
    # merge dfs to obtain one df with both tags and sentences
    df = df_annotations.merge(df_segments, how="left", on="complete_segment_ID")
    print(df)
