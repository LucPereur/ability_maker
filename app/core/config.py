
import logging
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOGGING_LEVEL: Literal[10] = logging.DEBUG
    API_V1_STR: str = "/api/v1"

    PATH_TO_JSON = "/Users/frengineer/Documents/Other/ability_maker/parapsy_lists.json"

    LLM_MODEL: str = "gcp:gemini-2.5-flash"
    LLM_TEMPERATURE: float = 0.0

    RETRIEVAL_COUNT: int = 10


settings = Settings()
