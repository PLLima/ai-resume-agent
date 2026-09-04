from src.config import Config
from src.agents.base import AgentFactory
from src.prompts.coder_prompts import get_coder_prompt

class CoderAgent:
    def __init__(self, model_name: str = Config.CODER_MODEL):
        self.model_name = model_name
        self.llm = AgentFactory.create_agent()

    def generate_latex(self, filtered_content: str, document_type: str = "resume") -> str:
        print("-" * 50)
        print(f"💻 STARTING STAGE 2: {self.model_name} (LaTeX {document_type.capitalize()} Generation)")
        print(f"Loading {self.model_name} into RAM (This might take a bit longer)...")
        
        prompt = get_coder_prompt(filtered_content, document_type)

        final_latex = self.llm.generate(prompt=prompt, model_name=self.model_name)

        print(f"\n✅ LaTeX code generated:\n", final_latex)
        print(f"\n🧹 {self.model_name} removed from RAM. Process Finished.")
        
        return final_latex
