from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings

model = ChatGoogleGenerativeAI(
    model=settings.LLM_MODEL,
    temperature=settings.LLM_TEMPERATURE,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key = settings.GOOGLE_API_KEY
)