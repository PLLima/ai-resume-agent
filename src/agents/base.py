from abc import ABC, abstractmethod
# pyrefly: ignore [missing-import]
import ollama
from src.config import Config

class BaseAgent(ABC):
    """
    Abstract base class for LLM interactions. 
    Ensures that switching between Ollama, Gemini, etc. is frictionless.
    """
    @abstractmethod
    def generate(self, prompt: str, model_name: str) -> str:
        pass

class OllamaAgent(BaseAgent):
    def __init__(self):
        self.client = ollama.Client(host=Config.OLLAMA_HOST, timeout=Config.OLLAMA_TIMEOUT)
        
    def generate(self, prompt: str, model_name: str) -> str:
        try:
            response = self.client.generate(
                model=model_name,
                prompt=prompt,
                keep_alive=0, # Unload model from RAM
                options={"num_ctx": Config.OLLAMA_NUM_CTX} # Configurable context window
            )
            return response['response']
        except Exception as e:
            print(f"❌ OllamaAgent Error: {e}")
            raise

class AgentFactory:
    @staticmethod
    def create_agent(provider: str = Config.LLM_PROVIDER) -> BaseAgent:
        if provider == "ollama":
            return OllamaAgent()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
