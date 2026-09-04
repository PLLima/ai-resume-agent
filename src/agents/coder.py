import ollama
from src.config import Config

class CoderAgent:
    def __init__(self, model_name: str = Config.CODER_MODEL):
        self.model_name = model_name
        self.client = ollama.Client(host=Config.OLLAMA_HOST, timeout=Config.OLLAMA_TIMEOUT)

    def generate_latex(self, filtered_content: str, document_type: str = "resume") -> str:
        print("-" * 50)
        print(f"💻 STARTING STAGE 2: {self.model_name} (LaTeX {document_type.capitalize()} Generation)")
        print(f"Loading {self.model_name} into RAM (This might take a bit longer)...")
        
        doc_type_clean = document_type.replace('_', ' ')
        latex_prompt = f"""
        You are an expert LaTeX programmer.
        Based on the following experience points, generate a COMPLETE, professional, and compilable LaTeX {doc_type_clean}.
        You must include the document class (e.g., \\documentclass{{article}}), preamble, and \\begin{{document}} ... \\end{{document}}.
        Generate ONLY valid LaTeX code without any markdown formatting or explanations.
        
        Experience points:
        {filtered_content}
        """

        response = self.client.generate(
            model=self.model_name,
            prompt=latex_prompt,
            keep_alive=0  # Unload model from RAM at the end
        )

        final_latex = response['response']
        print(f"\n✅ LaTeX code generated:\n", final_latex)
        print(f"\n🧹 {self.model_name} removed from RAM. Process Finished.")
        
        return final_latex
