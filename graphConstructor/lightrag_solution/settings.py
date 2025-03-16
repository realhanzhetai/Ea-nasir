import os
from dotenv import load_dotenv

load_dotenv()

# Configure working directory
DEFAULT_RAG_DIR = "index_default"
WORKING_DIR = os.environ.get("RAG_DIR", f"{DEFAULT_RAG_DIR}")
print(f"WORKING_DIR: {WORKING_DIR}")
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# Model Settings
# Define LLM model
qwen_model = "Qwen/QwQ-32B-Preview"
qwen_70b_model = "Qwen/Qwen2-VL-72B-Instruct"
llama_model = "meta-llama/Llama-3.3-70B-Instruct"
deepseek_model = "Pro/deepseek-ai/DeepSeek-R1"
LLM_MODEL = os.environ.get("LLM_MODEL", deepseek_model)
print(f"LLM_MODEL: {LLM_MODEL}")

# Define Embedding model
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "BAAI/bge-m3")
print(f"EMBEDDING_MODEL: {EMBEDDING_MODEL}")
# Define Embedding Model Size
EMBEDDING_MAX_TOKEN_SIZE = int(os.environ.get("EMBEDDING_MAX_TOKEN_SIZE", 8192))
print(f"EMBEDDING_MAX_TOKEN_SIZE: {EMBEDDING_MAX_TOKEN_SIZE}")

# Get Base URL of model provider
BASE_URL = os.environ.get("BASE_URL", "https://api.siliconflow.cn/v1")
print(f"BASE_URL: {BASE_URL}")

# Get API
API_KEY = os.getenv("Siliconflow_api_key")
print(f"API_KEY: {API_KEY}")