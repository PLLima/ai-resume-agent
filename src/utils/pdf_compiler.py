import os
import subprocess

class PDFCompiler:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def clean_latex_code(self, raw_code: str) -> str:
        """Removes markdown code blocks if the LLM output wrapped the LaTeX code."""
        code = raw_code.strip()
        if code.startswith("```latex"):
            code = code[len("```latex"):]
        elif code.startswith("```"):
            code = code[len("```"):]
        
        if code.endswith("```"):
            code = code[:-3]
            
        return code.strip()

    def compile(self, latex_code: str, document_type: str = "resume", filename: str = "document") -> str:
        """
        Saves the LaTeX code to a .tex file and compiles it into a PDF.
        Returns the path to the generated PDF on success, or an empty string on failure.
        """
        import datetime
        clean_code = self.clean_latex_code(latex_code)
        
        # Create a unique project folder based on timestamp and document type
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        project_folder_name = f"{timestamp}_{document_type}"
        project_dir = os.path.join(self.output_dir, project_folder_name)
        os.makedirs(project_dir, exist_ok=True)
        
        tex_filepath = os.path.join(project_dir, f"{filename}.tex")
        
        with open(tex_filepath, "w", encoding="utf-8") as f:
            f.write(clean_code)
            
        print(f"📄 LaTeX saved to {tex_filepath}")
        print("🔨 Compiling PDF with pdflatex...")
        
        try:
            # Run pdflatex
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", f"-output-directory={project_dir}", tex_filepath],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                pdf_path = os.path.join(project_dir, f"{filename}.pdf")
                print(f"✅ PDF successfully compiled: {pdf_path}")
                return pdf_path
            else:
                print("❌ LaTeX compilation finished with errors. The PDF might still be generated but could have issues.")
                print("Check the logs or the generated .log file in the output directory.")
                pdf_path = os.path.join(project_dir, f"{filename}.pdf")
                if os.path.exists(pdf_path):
                    return pdf_path
                return ""
        except FileNotFoundError:
            print("❌ pdflatex not found. Please ensure LaTeX is installed on your system.")
            return ""
