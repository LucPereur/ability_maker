
import logging
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOGGING_LEVEL: Literal[10] = logging.DEBUG
    API_V1_STR: str = "/api/v1"

    PATH_TO_JSON: str = "/Users/frengineer/Documents/Other/ability_maker/parapsy_lists.json"

    # API Keys
    GOOGLE_API_KEY: str

    # LLM Configuration
    LLM_MODEL: str = "gemini-2.5-flash"
    LLM_TEMPERATURE: float = 0.0

    RETRIEVAL_COUNT: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
