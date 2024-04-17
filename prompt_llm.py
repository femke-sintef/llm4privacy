import os
from yaml import safe_load
import openai
from read import get_df_segments
from datetime import datetime
import json
from tqdm import tqdm
from prompts import get_context
import csv
from copy import deepcopy


def call_api(llm_location, messages, engine):
    assert llm_location in ["azure", "local"]
    if llm_location == "azure":
        return openai.chat.completions.create(
            model=engine, messages=messages, max_tokens=500
        )
    else:
        return client.chat.completions.create(
            model=engine, messages=messages, max_tokens=500
        )


def call_with_context(
    llm_location, context: list, sentence: str, engine: str, role="user"
) -> str:
    current_context = deepcopy(context)
    current_context.append({"role": role, "content": sentence})
    response = call_api(llm_location, current_context, engine)
    message = response.choices[0].message
    return message.content


def get_llm_response(llm_location, sentence, context, engine):
    try:
        answer = call_with_context(llm_location, context, sentence, engine)
        print(answer)
        return answer
    except Exception as e:
        print(e)
        return "ERROR"


if __name__ == "__main__":
    # load config
    with open("config.json", "r") as f:
        config = json.load(f)

    if config["llm_location"] == "azure":
        # connect to api
        with open("openai.credential", "r") as stream:
            credential_data = safe_load(stream)
        openai_config = credential_data["openai"]
        openai.api_type = "azure"
        openai.azure_endpoint = openai_config["endpoint"]
        openai.api_version = "2024-02-15-preview"
        openai.api_key = openai_config["key"]
        print(openai.version.VERSION)
    else:
        client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # select prompt
    context = get_context(config["prompt_id"])

    # get df with segments to be queried
    if not "remove_HTML" in config:
        config["remove_HTML"] = False
    df_segments = get_df_segments(
        config["dataset_name"],
        n_policies=config["n_policies"],
        remove_html_tags=config["remove_HTML"],
    )
    df_segments["prompt_id"] = config["prompt_id"]
    df_segments["engine"] = config["engine"]
    df_segments["dataset_name"] = config["dataset_name"]
    # df_segments = df_segments[0:10]

    # get save location ready
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if config["n_policies"] is None:
        mode = "complete"
    else:
        mode = "partial"
    result_path = os.path.join(
        "results",
        config["dataset_name"],
        config["engine"],
        config["prompt_id"],
        mode,
        timestamp,
    )
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    # query llm and save progress
    for index, row in tqdm(df_segments.iterrows(), total=df_segments.shape[0]):
        answer = get_llm_response(
            config["llm_location"],
            row["segment_text"],
            context,
            config["engine"],
        )
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
    if config["n_policies"] is None:
        df_segments.to_csv(os.path.join(result_path, "results.csv"))
        df_segments.to_excel(os.path.join(result_path, "results.xlsx"))
    else:
        df_segments.to_csv(
            os.path.join(result_path, "results_" + str(config["n_policies"]) + ".csv")
        )
        df_segments.to_excel(
            os.path.join(result_path, "results_" + str(config["n_policies"]) + ".xlsx")
        )
