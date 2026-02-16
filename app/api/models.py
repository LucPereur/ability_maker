from datetime import datetime
from typing import Self
from enum import Enum
from langchain_core.documents import Document
from pydantic import BaseModel

class modeEnum(Enum):
    TELEPATHY = "telepathy"
    TELEKINSIS = "telekinesis"

class parapsyMode(BaseModel):
    parapsy_mode: modeEnum

class abilityDescription(BaseModel):
    ability_description: str

class subListComposition(BaseModel):
    item_value: int
    item_name: str
    item_description: str
    item_description_alt: str

class abilityComposition(BaseModel):
    parapsy_mode: modeEnum
    composition: dict[str, subListComposition]