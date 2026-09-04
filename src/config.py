import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "pllima_com")
    
    # Model Configurations
    REASONER_MODEL = "llama3.1"
    CODER_MODEL = "qwen2.5-coder:14b"
