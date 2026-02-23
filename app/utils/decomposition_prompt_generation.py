from app.core.config import settings
from app.api.models import parapsyMode, abilityDescription, parapsyMode, SchemaModeDefinition, compositionItem
from app.core.prompts import PROMPT_TEMPLATE
from app.core.schema_loader import schemaLoader
import json
from pathlib import Path
from typing import Iterator

class decompositionPromptGenerator():
    def __init__(
        self,
        parapsy_mode: parapsyMode,
        ability_input: abilityDescription,
        schema: SchemaModeDefinition
    ):
        self.parapsy_mode = parapsy_mode
        self.ability_input = ability_input
        self.schema = schema

    def lazy_prompt_generator(self) -> Iterator[Iterator[compositionItem]]:

        list_names = {}
        for index, parapsy_list in enumerate(self.schema.lists):
            list_names[f'list_name_{index+1}'] = parapsy_list.list_name
            list_names[f'list_description_{index+1}'] = parapsy_list.list_description

        for parapsy_list in self.schema.lists:

            prompt_terms_iterator = []

            for parapsy_sublist in parapsy_list.sublists:
                
                prompt_terms = {
                    "ability_description":self.ability_input,
                    "mode_adjective":self.schema.adjective,
                    "mode_noun":self.schema.noun,
                    "mode_general_description":self.schema.general_description,
                    "list_name_1":list_names['list_name_1'],
                    "list_description_1":list_names['list_description_1'],
                    "list_name_2":list_names['list_name_2'],
                    "list_description_2":list_names['list_description_2'],
                    "list_name_3":list_names['list_name_3'],
                    "list_description_3":list_names['list_description_3'],
                    "sublist_name":parapsy_sublist.sublist_name,
                    "list_name":parapsy_list.list_name,
                    "sublist_description":parapsy_sublist.sublist_description
                }

                for item_index, item in enumerate(parapsy_sublist.items):
                    prompt_terms[f'item_{item_index}'] = item.item_name
                    prompt_terms[f'item_description_{item_index}'] = item.item_description
                
                composition_item = compositionItem()
                composition_item.update(schema_sublist=parapsy_sublist)
                composition_item.list_name = parapsy_list.list_name
                composition_item.prompt_terms = prompt_terms

                prompt_terms_iterator.append(composition_item)

            yield iter(prompt_terms_iterator)


if __name__ == "__main__":

    prompts = decompositionPromptGenerator(
        parapsy_mode=parapsyMode.TELEPATHY,
        ability_input="Détection de tous les humains conscients dans un rayon de 100 mètres"
    )

    for prompt_list in prompts.lazy_prompt_generator():
        for prompt_sublist in prompt_list:
            print(prompt_sublist)