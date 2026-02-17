from app.api.models import abilityComposition

def print_composition(ability_composition: abilityComposition):
    print(f"Mode : {ability_composition.parapsy_mode.value}\n")
    for composition_item in ability_composition.composition:
        print(f'{composition_item.list_name} -> {composition_item.sublist_name} -> {composition_item.sublist_selection.item_value} = {composition_item.sublist_selection.item_name}')