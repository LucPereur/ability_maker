from app.core.prompts import PROMPT_TEMPLATE

import json
from pathlib import Path
from typing import Iterator
from operator import itemgetter

from langchain.chat_models.base import _ConfigurableModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSerializable



def get_chain(llm_model: _ConfigurableModel) -> RunnableSerializable:
    return ( PROMPT_TEMPLATE | llm_model | StrOutputParser() )


#if __name__ == "__main__":
