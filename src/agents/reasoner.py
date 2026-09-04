import ollama
from src.config import Config

class ReasonerAgent:
    def __init__(self, model_name: str = Config.REASONER_MODEL):
        self.model_name = model_name

    def analyze_and_filter(self, job_description: str, professional_data: dict) -> str:
        print(f"🧠 STARTING STAGE 1: {self.model_name} (Reasoning and Selection)")
        print(f"Loading {self.model_name} into RAM (This might take a few seconds)...")
        
        reasoning_prompt = f"""
        You are an HR Specialist.
        Here is the job description: '{job_description}'.
        
        Here is the candidate's professional data (JSON format):
        {professional_data}
        
        Which of these experiences should I focus on for the resume? (Summarize in plain text).
        """

        response = ollama.generate(
            model=self.model_name,
            prompt=reasoning_prompt,
            keep_alive=0  # FUNDAMENTAL: Unload model from RAM as soon as it finishes!
        )
        
        filtered_content = response['response']
        print(f"\n✅ {self.model_name} summary completed:\n", filtered_content)
        print(f"\n🧹 {self.model_name} removed from RAM.\n")
        
        return filtered_content
