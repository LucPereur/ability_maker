from app.core.prompts import DESCRIPTION_PROMPT_TEMPLATE

from langchain.chat_models.base import _ConfigurableModel
from langchain_core.runnables import RunnableSerializable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException

def get_chain(llm_model: _ConfigurableModel) -> RunnableSerializable:
    return ( DESCRIPTION_PROMPT_TEMPLATE | llm_model | StrOutputParser() )



#if __name__ == "__main__":
