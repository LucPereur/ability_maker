from app.api.models import parapsyMode, abilityDescription, parapsyMode, abilityComposition, itemDetails

def print_composition(ability_composition: abilityComposition):
    print(f"Mode : {ability_composition.parapsy_mode.value}\n\n")
    for list_name, list_contents in ability_composition.composition.items():
        print(f'{list_name} -> {list_contents.from_sublist} -> {list_contents.item_value} = {list_contents.item_name}')