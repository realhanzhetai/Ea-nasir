import numpy as np
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
# import settings
from settings import LLM_MODEL, EMBEDDING_MODEL, BASE_URL, API_KEY

# Model Initialization
# Embedding function
async def embedding_func(texts: list[str]) -> np.ndarray:
    return await openai_embed(
        texts=texts,
        model=EMBEDDING_MODEL,
        base_url=BASE_URL,
        api_key=API_KEY,
    )

# Get Embedding Dim through test sentence
async def get_embedding_dim():
    test_text = ["This is a test sentence."]
    embedding = await embedding_func(test_text)
    embedding_dim = embedding.shape[1]
    print(f"{embedding_dim=}")
    return embedding_dim

# Initialize LLM model
async def llm_model_func(
    prompt, system_prompt=None, history_messages=[], keyword_extraction=False, **kwargs
) -> str:
    return await openai_complete_if_cache(
        model=LLM_MODEL,
        prompt=prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        base_url=BASE_URL,
        api_key=API_KEY,
        **kwargs,
    )
