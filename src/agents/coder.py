import ollama
from src.config import Config

class CoderAgent:
    def __init__(self, model_name: str = Config.CODER_MODEL):
        self.model_name = model_name

    def generate_latex(self, filtered_content: str) -> str:
        print("-" * 50)
        print(f"💻 STARTING STAGE 2: {self.model_name} (LaTeX Generation)")
        print(f"Loading {self.model_name} into RAM (This might take a bit longer)...")
        
        latex_prompt = f"""
        You are a LaTeX programmer.
        Transform the following experience points into a LaTeX list format (using \\begin{{itemize}}).
        Generate ONLY valid code, without any explanations.
        
        Experience points:
        {filtered_content}
        """

        response = ollama.generate(
            model=self.model_name,
            prompt=latex_prompt,
            keep_alive=0  # Unload model from RAM at the end
        )

        final_latex = response['response']
        print(f"\n✅ LaTeX code generated:\n", final_latex)
        print(f"\n🧹 {self.model_name} removed from RAM. Process Finished.")
        
        return final_latex
