import asyncio
import os
from dotenv import load_dotenv
from lightrag import LightRAG
from lightrag.utils import EmbeddingFunc

from model_config import llm_model_func, get_embedding_dim, embedding_func
from settings import EMBEDDING_MAX_TOKEN_SIZE

load_dotenv()
WORKING_DIR = "./local_neo4jWorkDir"

# get neo4j config
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME= os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=llm_model_func,
    embedding_func=EmbeddingFunc(
        embedding_dim=asyncio.run(get_embedding_dim()),
        max_token_size=EMBEDDING_MAX_TOKEN_SIZE,
        func=embedding_func,
    ),
    graph_storage="Neo4JStorage",
    log_level="DEBUG",
)