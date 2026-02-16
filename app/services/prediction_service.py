from langchain.chat_models.base import _ConfigurableModel
from app.api.models import parapsyMode, abilityDescription, modeEnum, abilityComposition


class predictionService:
    def __init__(self, chat_model: _ConfigurableModel, ability_input: abilityDescription, parapsy_mode: parapsyMode):
        self.chat_model = chat_model
        self.ability_input = ability_input
        self.parapsy_mode = parapsy_mode
    
    def predict(self) -> abilityComposition:
        composition = abilityComposition(parapsy_mode=self.parapsy_mode)
        return composition