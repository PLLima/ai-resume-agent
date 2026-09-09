"""
Reasoner Agent module for selecting relevant professional data.
"""

from src.agents.base import AgentFactory
from src.config import Config
from src.prompts.reasoner_prompts import get_reasoner_prompt


class ReasonerAgent:
    """
    Agent responsible for reasoning and filtering professional data based on a job description.
    """

    def __init__(self, model_name: str = Config.REASONER_MODEL):
        self.model_name = model_name
        self.llm = AgentFactory.create_agent()

    def analyze_and_filter(self, job_description: str, professional_data: dict) -> str:
        """
        Analyzes the job description and professional data to filter relevant experiences.
        """
        print(f"🧠 STARTING STAGE 1: {self.model_name} (Reasoning and Selection)")
        print(f"Loading {self.model_name} into RAM (This might take a few seconds)...")

        prompt = get_reasoner_prompt(job_description, professional_data)

        filtered_content = self.llm.generate(prompt=prompt, model_name=self.model_name)

        print(f"\n✅ {self.model_name} summary completed:\n", filtered_content)
        print(f"\n🧹 {self.model_name} removed from RAM.\n")

        return filtered_content
