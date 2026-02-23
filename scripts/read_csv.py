import pandas as pd
import json
from pathlib import Path

def csv_to_parapsy_json(csv_path: str, output_path: str):
    """
    Converts schema.csv to parapsy_list.json format.

    Args:
        csv_path: Path to the input CSV file
        output_path: Path to the output JSON file
    """
    # Read the CSV
    df = pd.read_csv(csv_path, sep=";")
    df = df.drop(columns=["Unnamed: 0"])

    # Mode metadata mapping
    mode_metadata = {
        "télépathie": {
            "name": "telepathy",
            "noun": "télépathie",
            "adjective": "télépathique"
        },
        "télékinésie": {
            "name": "telekinesis",
            "noun": "télékinésie",
            "adjective": "télékinétique"
        }
    }

    schemas = []
    current_mode = None
    current_list = None
    current_sublist = None

    for _, row in df.iterrows():
        item_type = row["item_type"]
        name = row["name"]
        description = row["description"] if pd.notna(row["description"]) else ""
        description_alt = row["description_alt"] if pd.notna(row["description_alt"]) else None
        quantitative_effect = row["quantitative_effect"] if pd.notna(row["quantitative_effect"]) else None

        if item_type == "mode":
            # Start a new mode
            if current_mode is not None:
                schemas.append(current_mode)

            mode_meta = mode_metadata.get(name, {
                "name": name,
                "noun": name,
                "adjective": name
            })

            current_mode = {
                "name": mode_meta["name"],
                "noun": mode_meta["noun"],
                "adjective": mode_meta["adjective"],
                "general_description": description,
                "lists": []
            }
            current_list = None
            current_sublist = None

        elif item_type == "list":
            # Start a new list
            current_list = {
                "list_name": name,
                "list_description": description,
                "sublists": []
            }
            current_mode["lists"].append(current_list)
            current_sublist = None

        elif item_type == "sublist":
            # Start a new sublist

            current_sublist = {
                "sublist_name": name,
                "sublist_description": description,
                "items": []
            }
            current_list["sublists"].append(current_sublist)

        else:
            # It's an item (numeric value 0-5)
            try:
                item_value = int(item_type)
                item = {
                    "item_name": name,
                    "item_description": description,
                    "item_description_alt": description_alt,
                    "item_quantitative_effect": quantitative_effect,
                    "item_value": item_value
                }
                current_sublist["items"].append(item)
            except (ValueError, TypeError):
                # Skip rows that don't fit the expected format
                pass

    # Append the last mode
    if current_mode is not None:
        schemas.append(current_mode)

    # Create final JSON structure
    final_json = {"schemas": schemas}

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=4)

    print(f"Successfully converted {csv_path} to {output_path}")
    print(f"Total schemas: {len(schemas)}")
    for schema in schemas:
        print(f"  - {schema['noun']}: {len(schema['lists'])} lists")


if __name__ == "__main__":
    # Define paths
    base_dir = Path("/Users/frengineer/Documents/Other/ability_maker")
    csv_path = base_dir / "schema.csv"
    output_path = base_dir / "parapsy_lists2.json"

    # Convert CSV to JSON
    csv_to_parapsy_json(str(csv_path), str(output_path))
