import json
import pandas as pd
from pathlib import Path
import numpy as np

def read_parapsy_csv(path: Path) -> list:

    def read_sublist_csv(sublist: pd.DataFrame):
        result = {"sublist_name":sublist[2].values[0]}
        sublist = sublist.iloc[1:]
        sublist_content = [
            {
                "item_name":item,
                "item_description":description,
                "item_description_alt":description_alt
            }
            for item, description, description_alt in zip(sublist[1].to_list(),sublist[2].to_list(),sublist[3].to_list())
        ]
        result['items'] = sublist_content
        return result
    
    result = []
    df = pd.read_csv(path, sep=";", header=None)
    split_indices = df[df[0].isna()].index.tolist()

    dfs = []
    start = 0
    for idx in split_indices:
        dfs.append(df.iloc[start:idx])
        start = idx
    dfs.append(df.iloc[start:])

    for sub_df in dfs:
        if sub_df.index.size == 1:
            list_name = sub_df[1].values[0]
            result.append({
                "list_name":list_name,
                "sublists":[]
            })
        elif sub_df.index.size == 6:
            next((item for item in result if item['list_name'] == list_name), None)["sublists"].append(read_sublist_csv(sub_df))
    
    return result

def clean_data(obj):
    if isinstance(obj, dict):
        return {k: clean_data(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_data(item) for item in obj]
    elif isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    return obj


if "__name__" == "__main__":
    CSV_PATH = "/Users/frengineer/Documents/Other/ability_maker/parapsy_details/"
    JSON_PATH_FROM = "/Users/frengineer/Documents/Other/ability_maker/parapsy_lists.json"
    JSON_PATH_TO = "/Users/frengineer/Documents/Other/ability_maker/parapsy_lists2.json"

    with open(Path(JSON_PATH_FROM), mode="r") as f:
        lists = json.load(f)
        for key, item in lists.items():
            csv_data = read_parapsy_csv(Path(f"{CSV_PATH}{key}.csv"))
            for parapsy_list in item['lists']:
                sublists = next((item for item in csv_data if item['list_name'] == parapsy_list['list_name']), None)["sublists"]
                parapsy_list['sublists'] = sublists

    lists = clean_data(lists)

    with open(Path(JSON_PATH_TO), mode="w") as f:
        json.dump(lists, f, allow_nan=True, ensure_ascii=False, indent=4)