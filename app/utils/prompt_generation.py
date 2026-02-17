from app.core.config import settings
from app.api.models import parapsyMode, abilityDescription, parapsyMode
from app.core.prompts import PROMPT_TEMPLATE

import json
from pathlib import Path
from typing import Iterator


class promptGenerator():
    def __init__(
        self,
        parapsy_mode: parapsyMode,
        ability_input: abilityDescription
    ):
        self.mode = parapsy_mode
        self.ability_input = ability_input
        self.instructions_path = settings.PATH_TO_JSON

    def lazy_prompt_generator(self) -> Iterator[Iterator[dict[str,str]]]:

        with open(self.instructions_path, "r") as f:
            details = json.load(f)
        details = details[self.mode.value]

        list_names = {}
        for index, parapsy_list in enumerate(details['lists']):
            list_names[f'list_name_{index+1}'] = parapsy_list['list_name']
            list_names[f'list_description_{index+1}'] = parapsy_list['list_description']

        for parapsy_list in details['lists']:

            prompt_terms_iterator = []

            for parapsy_sublist in parapsy_list['sublists']:

                prompt_terms = {
                    "ability_description":self.ability_input,
                    "mode_adjective":details['adjective'],
                    "mode_noun":details['noun'],
                    "mode_general_description":details['general_description'],
                    "list_name_1":list_names['list_name_1'],
                    "list_description_1":list_names['list_description_1'],
                    "list_name_2":list_names['list_name_2'],
                    "list_description_2":list_names['list_description_2'],
                    "list_name_3":list_names['list_name_3'],
                    "list_description_3":list_names['list_description_3'],
                    "sublist_name":parapsy_sublist['sublist_name'],
                    "list_name":parapsy_list['list_name'],
                    "sublist_description":parapsy_sublist['sublist_description']
                }

                for item_index, item in enumerate(parapsy_sublist['items']):
                    prompt_terms[f'item_{item_index+1}'] = item['item_name']
                    prompt_terms[f'item_description_{item_index+1}'] = item['item_description']
                
                prompt_terms_iterator.append(prompt_terms)

            yield iter(prompt_terms_iterator)


if __name__ == "__main__":

    prompts = promptGenerator(
        parapsy_mode=parapsyMode.TELEPATHY,
        ability_input="Détection de tous les humains conscients dans un rayon de 100 mètres"
    )

    for prompt_list in prompts.lazy_prompt_generator():
        for prompt_sublist in prompt_list:
            print(prompt_sublist)