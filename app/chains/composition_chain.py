from app.core.prompts import PROMPT_TEMPLATE

import json
from pathlib import Path
from typing import Iterator
from operator import itemgetter

from langchain.chat_models.base import _ConfigurableModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSerializable
from langchain_core.output_parsers import StrOutputParser, BaseOutputParser
from langchain_core.exceptions import OutputParserException

class IntegerOutputParser(BaseOutputParser[int]):

    def parse(self, text: str) -> int:
        cleaned_text = text.strip()
        if not cleaned_text.isdigit():
            raise OutputParserException(
                f"IntegerOutputParser expected output value to either be an integer"
                f"Received {cleaned_text}."
            )
        elif int(cleaned_text) not in list(range(6)):
            raise OutputParserException(
                f"IntegerOutputParser expected output value to either be between 0 and 5"
                f"Received {cleaned_text}."
            )
        return int(cleaned_text)

    @property
    def _type(self) -> str:
        return "integer_output_parser"

def get_chain(llm_model: _ConfigurableModel) -> RunnableSerializable:
    return ( PROMPT_TEMPLATE | llm_model | IntegerOutputParser() )



#if __name__ == "__main__":
