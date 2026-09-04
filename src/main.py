import sys
import os
import argparse

# Ensure the root project directory is in the PYTHONPATH so we can import src.* modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db.client import DatabaseClient
from src.agents.reasoner import ReasonerAgent
from src.agents.coder import CoderAgent
from src.utils.pdf_compiler import PDFCompiler

def main():
    print("🚀 Initializing AI Resume & Cover Letter Architect CLI...\n")
    
    parser = argparse.ArgumentParser(description="AI Resume & Cover Letter Architect")
    parser.add_argument("document_type", nargs="?", default="resume", choices=["resume", "cover_letter"], 
                        help="The type of document to generate (resume or cover_letter)")
    parser.add_argument("language", nargs="?", default="en", 
                        help="The target language code (e.g., en, fr, pt)")
    
    args = parser.parse_args()
    document_type = args.document_type
    language = args.language
        
    print(f"📄 Target Document Type: {document_type.replace('_', ' ').title()}")
    print(f"🌍 Target Language: {language.upper()}")
    
    db_client = DatabaseClient()
    professional_data = db_client.get_professional_data()
    
    target_role = "Software Engineer focusing on C++ and Machine Learning"
    
    reasoner = ReasonerAgent()
    filtered_content = reasoner.analyze_and_filter(
        job_description=target_role,
        professional_data=professional_data
    )
    
    coder = CoderAgent()
    latex_output = coder.generate_latex(filtered_content, document_type=document_type)
    
    compiler = PDFCompiler()
    pdf_path = compiler.compile(latex_output, document_type=document_type, language=language, filename=f"generated_{document_type}")
    
    if pdf_path:
        print(f"\n🎉 Pipeline execution successful! Document saved at: {pdf_path}")
    else:
        print("\n⚠️ Pipeline executed, but PDF compilation encountered errors.")

if __name__ == "__main__":
    main()
