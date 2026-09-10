"""
PDF Compiler Module

This module provides the PDFCompiler class to clean and compile LaTeX code into PDFs.
"""

import datetime
import os
import subprocess


class PDFCompiler:
    """
    Handles cleaning of LLM-generated LaTeX code and compiling it into a PDF using pdflatex.
    """

    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def clean_latex_code(self, raw_code: str) -> str:
        """Removes markdown code blocks if the LLM output wrapped the LaTeX code."""
        code = raw_code.strip()
        if code.startswith("```latex"):
            code = code[len("```latex") :]
        elif code.startswith("```"):
            code = code[len("```") :]

        code = code.removesuffix("```")

        return code.strip()

    def compile(
        self,
        latex_code: str,
        document_type: str = "resume",
        language: str = "en",
        role: str = "role",
        company: str = "company",
        country: str = "country",
    ) -> str:
        """
        Saves the LaTeX code to a .tex file and compiles it into a PDF.
        Returns the path to the generated PDF on success, or an empty string on failure.
        """
        clean_code = self.clean_latex_code(latex_code)

        # Determine folder and file names based on Cloudinary spec
        folder_type = "resumes" if document_type == "resume" else "cover-letters"
        file_doc_type = "resume" if document_type == "resume" else "cover-letter"

        # Create output directory structure (e.g., output/resumes/en)
        project_dir = os.path.join(self.output_dir, folder_type, language)
        os.makedirs(project_dir, exist_ok=True)

        # Format filename: yyyy-mm-dd_hh-min-ss_role_company_country_language_documentType
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d_%H-%M-%S"
        )
        filename_base = (
            f"{timestamp}_{role}_{company}_{country}_{language}_{file_doc_type}"
        )

        tex_filepath = os.path.join(project_dir, f"{filename_base}.tex")

        with open(tex_filepath, "w", encoding="utf-8") as f:
            f.write(clean_code)

        print(f"📄 LaTeX saved to {tex_filepath}")
        print("🔨 Compiling PDF with pdflatex...")

        try:
            # Run pdflatex
            result = subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    f"-output-directory={project_dir}",
                    tex_filepath,
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            pdf_path = os.path.join(project_dir, f"{filename_base}.pdf")
            if result.returncode == 0:
                print(f"✅ PDF successfully compiled: {pdf_path}")
                return pdf_path

            print(
                "❌ LaTeX compilation finished with errors. "
                "The PDF might still be generated but could have issues."
            )
            print("Check the logs or the generated .log file in the output directory.")
            if os.path.exists(pdf_path):
                return pdf_path
            return ""
        except FileNotFoundError:
            print(
                "❌ pdflatex not found. Please ensure LaTeX is installed on your system."
            )
            return ""
