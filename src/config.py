import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "pllima_com")
    
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "600.0")) # 10 minutes default
    
    # Model Configurations
    REASONER_MODEL = "llama3.1"
    CODER_MODEL = "qwen2.5-coder:14b"
