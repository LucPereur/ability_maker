from langchain.chat_models.base import _ConfigurableModel

from app.api.models import parapsyMode, abilityDescription, abilityComposition
from app.core.schema_loader import schemaLoader
from app.chains.description_chain import get_chain
from app.chat_model.get_model import model

class descriptionGenerationService:
    def __init__(self, chat_model: _ConfigurableModel, parapsy_mode: parapsyMode):
        self.chat_model = chat_model
        self.parapsy_mode = parapsy_mode
        self.schema_loader = schemaLoader()
    
    def generate(self, ability_composition: abilityComposition) -> str :
        chain = get_chain(llm_model=chat_model)
        ability_description = chain.invoke({
            "composition_summary": ability_composition.composition_summary(),
            "ability_description": ability_composition.ablity_description
        })
        return ability_description

if __name__ == "__main__":
    from app.services.composition_prediction_service import compositionPredictionService
    chat_model = model
    ability_input=abilityDescription(
        ability_description="décupler la confiance en soi d'un ami en le touchant"
    )
    prediction_service = compositionPredictionService(
        chat_model=chat_model,
        parapsy_mode=parapsyMode.TELEPATHY
    )
    description_generation_service = descriptionGenerationService(
        chat_model=chat_model,
        parapsy_mode=parapsyMode.TELEPATHY
    )
    composition_prediction = prediction_service.predict(ability_input=ability_input)
    print(composition_prediction.composition_summary())
    ability_description = description_generation_service.generate(ability_composition=composition_prediction)
    print(ability_description)
    