"""
Base Agent Module.
"""

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
        """Generate response from the model."""


class OllamaAgent(BaseAgent):
    """
    Agent implementation for Ollama models.
    """

    def __init__(self):
        self.client = ollama.Client(
            host=Config.OLLAMA_HOST, timeout=Config.OLLAMA_TIMEOUT
        )

    def generate(self, prompt: str, model_name: str) -> str:
        """Generate response from the Ollama model."""
        try:
            response = self.client.generate(
                model=model_name,
                prompt=prompt,
                keep_alive=0,  # Unload model from RAM
                options={
                    "num_ctx": Config.OLLAMA_NUM_CTX
                },  # Configurable context window
            )
            return response["response"]
        except Exception as e:
            print(f"❌ OllamaAgent Error: {e}")
            raise


class AgentFactory:
    """Factory to create the appropriate agent based on configuration."""

    @staticmethod
    def create_agent(provider: str = Config.LLM_PROVIDER) -> BaseAgent:
        """Create and return an agent instance."""
        if provider == "ollama":
            return OllamaAgent()

        raise ValueError(f"Unsupported LLM provider: {provider}")
