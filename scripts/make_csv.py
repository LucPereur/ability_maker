import pandas as pd
import json
from pathlib import Path


def parapsy_json_to_csv(json_path: str, output_path: str):
    with open(json_path, mode="r") as f:
        data = json.load(f)

    columns = ["item_type","name","description","description_alt","quantitative_effect"]
    data_lists = []
    for schema in data['schemas']:
        data_lists.append({
            "item_type":"mode",
            "name":schema["noun"],
            "description":schema["general_description"],
            "description_alt":"",
            "quantitative_effect":""
            })
        for parapsy_list in schema['lists']:
            data_lists.append({
                "item_type":"list",
                "name":parapsy_list["list_name"],
                "description":parapsy_list["list_description"],
                "description_alt":"",
                "quantitative_effect":""
                })
            for parapsy_sublist in parapsy_list['sublists']:
                data_lists.append({
                    "item_type":"sublist",
                    "name":parapsy_sublist["sublist_name"],
                    "description":parapsy_sublist["sublist_description"],
                    "description_alt":"",
                    "quantitative_effect":""
                    })
                for items in parapsy_sublist['items']:
                    data_lists.append({
                        "item_type":items["item_value"],
                        "name":items["item_name"],
                        "description":items["item_description"],
                        "description_alt":items["item_description_alt"],
                        "quantitative_effect":items["item_quantitative_effect"]
                        })

    dataframe = pd.DataFrame(data_lists, columns=columns)
    dataframe.to_csv(output_path)


if __name__ == "__main__":
    base_dir = Path("/Users/frengineer/Documents/Other/ability_maker")
    output_path = base_dir / "schema.csv"
    json_path = base_dir / "parapsy_lists2.json"

    parapsy_json_to_csv(str(json_path), str(output_path))
