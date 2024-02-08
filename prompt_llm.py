import os
from yaml import safe_load
import openai
from read_data import get_df_segments
from datetime import datetime
import json
from tqdm import tqdm
from prompts import get_context
import csv
from copy import deepcopy


def call_api(messages, engine):
    return openai.chat.completions.create(
        model=engine, messages=messages, max_tokens=50
    )


def call_with_context(context: list, sentence: str, engine: str, role="user") -> str:
    current_context = deepcopy(context)
    current_context.append({"role": role, "content": sentence})
    response = call_api(current_context, engine)
    message = response.choices[0].message
    return message.content


def get_llm_response(sentence, context, engine):
    try:
        answer = call_with_context(context, sentence, engine)
        print(answer)
        return answer
    except:
        print("Error")
        return "ERROR"


if __name__ == "__main__":
    # connect to api
    with open("openai.credential", "r") as stream:
        credential_data = safe_load(stream)
    openai_config = credential_data["openai"]
    openai.api_type = "azure"
    openai.azure_endpoint = openai_config["endpoint"]
    openai.api_version = "2023-03-15-preview"
    openai.api_key = openai_config["key"]
    print(openai.version.VERSION)

    # load config
    with open("config.json", "r") as f:
        config = json.load(f)

    # select prompt
    context = get_context(config["prompt_id"])

    # get df with segments to be queried
    df_segments = get_df_segments(config["dataset_name"])
    df_segments["prompt_id"] = config["prompt_id"]
    df_segments["engine"] = config["engine"]
    df_segments["dataset_name"] = config["dataset_name"]
    # df_segments = df_segments[0:10]

    # get save location ready
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_path = os.path.join(
        "results", config["engine"], config["dataset_name"], timestamp
    )
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    # query llm and save progress
    for index, row in tqdm(df_segments.iterrows(), total=df_segments.shape[0]):
        answer = get_llm_response(row["segment_text"], context, config["engine"])
        df_segments.loc[index, "llm_response"] = answer
        with open(os.path.join(result_path, "progress.csv"), "a") as file:
            writer = csv.writer(file)
            writer.writerow([row["complete_segment_ID"], answer])
    # tqdm.pandas()
    # df_segments["llm_response"] = df_segments["segment_text"].progress_apply(
    #     get_llm_response, args=(context, config["engine"])
    # )

    # save final results
    with open(os.path.join(result_path, "config.json"), "w") as f:
        json.dump(config, f)
    df_segments.to_csv(os.path.join(result_path, "results.csv"))
    df_segments.to_excel(os.path.join(result_path, "results.xlsx"))
