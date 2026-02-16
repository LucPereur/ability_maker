import json
from pathlib import Path
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

class promptGenerator(ChatPromptTemplate):

    

    def make_prompts(path: Path, ability_description: str) -> list[dict[str,str]]:
        with open(path, "r") as f:
            details = json.load(f)
        details = details['telepathy']
        result = []

        list_names = {}
        for index, parapsy_list in enumerate(details['lists']):
            list_names[f'list_name_{index+1}'] = parapsy_list['list_name']
            list_names[f'list_description_{index+1}'] = parapsy_list['list_description']

        for parapsy_list in details['lists']:
            for parapsy_sublist in parapsy_list['sublists']:
                
                prompt_terms = {
                    "ability_description":ability_description,
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
                
            result.append(prompt_terms)
        
        return result
