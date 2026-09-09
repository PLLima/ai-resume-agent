"""
Configuration module for the AI Resume Agent.
"""

import os

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """
    Configuration variables for the application.
    """

    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "pllima_com")

    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "600.0"))  # 10 minutes default
    OLLAMA_NUM_CTX = int(
        os.getenv("OLLAMA_NUM_CTX", "8192")
    )  # Context limit to balance memory and capability

    # Model Configurations
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()
    REASONER_MODEL = os.getenv("REASONER_MODEL", "llama3.1")
    CODER_MODEL = os.getenv("CODER_MODEL", "qwen2.5-coder:14b")
