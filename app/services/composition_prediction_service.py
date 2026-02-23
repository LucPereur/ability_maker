from langchain.chat_models.base import _ConfigurableModel
from tqdm import tqdm

from app.api.models import parapsyMode, abilityDescription, abilityComposition, SchemaItem
from app.core.schema_loader import schemaLoader
from app.utils.decomposition_prompt_generation import decompositionPromptGenerator
from app.chains.composition_chain import get_chain
from app.chat_model.get_model import model
from app.utils.print_composition import print_composition

class compositionPredictionService:
    def __init__(self, chat_model: _ConfigurableModel, parapsy_mode: parapsyMode):
        self.chat_model = chat_model
        self.parapsy_mode = parapsy_mode
        self.schema_loader = schemaLoader()
    
    def predict(self, ability_input: abilityDescription) -> abilityComposition:
        schema = self.schema_loader.load_schema(self.parapsy_mode)
        prompt_generator = decompositionPromptGenerator(parapsy_mode=self.parapsy_mode, ability_input=ability_input, schema=schema)
        ability_composition = abilityComposition(parapsy_mode=self.parapsy_mode, composition = [])
        for composition_list in tqdm(prompt_generator.lazy_prompt_generator(), desc="lists study"):
            for composition_item in tqdm(composition_list, desc="sublists study"):
                chain = get_chain(llm_model=self.chat_model)
                score = chain.invoke(composition_item.prompt_terms)
                item = next((item for item in composition_item.sublist_items if item.item_value == score), None)
                composition_item.sublist_selection = item
                ability_composition.composition.append(composition_item)

        return ability_composition

if __name__ == "__main__":
    chat_model = model
    ability_input=abilityDescription(
        ability_description="supprimer les souvenirs d'un individu"
    )
    prediction_service = compositionPredictionService(
        chat_model=chat_model,
        parapsy_mode=parapsyMode.TELEPATHY
    )
    decomposition_prediction = prediction_service.predict(ability_input=ability_input)
    print_composition(decomposition_prediction)
    