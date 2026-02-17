from datetime import datetime
from typing import Self
from enum import Enum
from langchain_core.documents import Document
from pydantic import BaseModel

class parapsyMode(Enum):
    TELEPATHY = "telepathy"
    TELEKINSIS = "telekinesis"

class abilityDescription(BaseModel):
    ability_description: str

class itemDetails(BaseModel):
    from_sublist: str
    item_value: int
    item_name: str
    item_description: str
    item_description_alt: str

class abilityComposition(BaseModel):
    parapsy_mode: parapsyMode
    composition: dict[str, itemDetails]