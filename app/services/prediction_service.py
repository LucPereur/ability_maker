from langchain.chat_models.base import _ConfigurableModel
from tqdm import tqdm

from app.api.models import parapsyMode, abilityDescription, abilityComposition, itemDetails
from app.utils.prompt_generation import promptGenerator
from app.chains.composition_chain import get_chain
from app.chat_model.get_model import model
from app.utils.print_composition import print_composition

class predictionService:
    def __init__(self, chat_model: _ConfigurableModel, parapsy_mode: parapsyMode):
        self.chat_model = chat_model
        self.parapsy_mode = parapsy_mode
    
    def predict(self) -> abilityComposition:
        prompt_generator = promptGenerator(parapsy_mode=self.parapsy_mode, ability_input=abilityDescription)
        ability_composition = abilityComposition(parapsy_mode=self.parapsy_mode, composition = {})
        for prompt_terms_list in tqdm(prompt_generator.lazy_prompt_generator(), desc="lists study"):
            for prompt_terms in tqdm(prompt_terms_list, desc="sublists study"):
                list_name = prompt_terms['list_name']
                sublist_name = prompt_terms['sublist_name']
                chain = get_chain(llm_model=self.chat_model)
                score = chain.invoke(prompt_terms)
                item_name = prompt_terms[f'item_{score}']
                item_description = prompt_terms[f'item_description_{score}']
                item_details = itemDetails(
                    from_sublist=sublist_name,
                    item_value=score,
                    item_name=item_name,
                    item_description=item_description,
                    item_description_alt=""
                )
            ability_composition.composition[list_name] = item_details
        return ability_composition

if __name__ == "__main__":
    chat_model = model
    ability_input=abilityDescription(
        ability_description="supprimer les souvenirs d'un individu"
    )
    prediction_service = predictionService(
        chat_model=chat_model,
        parapsy_mode=parapsyMode.TELEPATHY
    )
    decomposition_prediction = prediction_service.predict()
    print_composition(decomposition_prediction)
    