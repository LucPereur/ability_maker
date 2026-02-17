import pandas as pd
import json

with open("/Users/dendarii/Documents/Code/ability_maker/parapsy_lists.json", mode="r") as f:
    data = json.load(f)

columns = ["item_index","name","description","description_alt"]
data_lists = []
for schema in data['schemas']:
    data_lists.append({
        "item_index":"",
        "name":schema["noun"],
        "description":schema["general_description"],
        "description_alt":""
        })
    for parapsy_list in schema['lists']:
        data_lists.append({
            "item_index":"",
            "name":parapsy_list["list_name"],
            "description":parapsy_list["list_description"],
            "description_alt":""
            })
        for parapsy_sublist in parapsy_list['sublists']:
            data_lists.append({
                "item_index":"",
                "name":parapsy_sublist["sublist_name"],
                "description":parapsy_sublist["sublist_description"],
                "description_alt":""
                })
            for items in parapsy_sublist['items']:
                data_lists.append({
                    "item_index":items["item_value"],
                    "name":items["item_name"],
                    "description":items["item_description"],
                    "description_alt":items["item_description_alt"]
                    })
    print(schema)


dataframe = pd.DataFrame(data_lists, columns=columns)
dataframe.to_csv("/Users/dendarii/Documents/Code/ability_maker/parapsy_details/schema.csv")
print(dataframe)