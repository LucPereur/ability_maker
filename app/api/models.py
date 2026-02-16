from datetime import datetime
from typing import Self
from enum import Enum
from langchain_core.documents import Document
from pydantic import BaseModel

class modeEnum(str, Enum):
    TELEPATHY = "telepathy"
    TELEKINSIS = "telekinesis"

class parapsyMode(BaseModel):
    parapsy_mode = modeEnum

class abilityDescription(BaseModel):
    ability_description = str
