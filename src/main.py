"""
Main CLI orchestration script for generating professional documents.
"""

# pylint: disable=wrong-import-position,import-error

import argparse
import os
import sys

# Ensure the root project directory is in the PYTHONPATH so we can import src.* modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.coder import CoderAgent
from src.agents.reasoner import ReasonerAgent
from src.db.client import DatabaseClient
from src.utils.pdf_compiler import PDFCompiler


def main():
    """
    Orchestrates the resume/cover letter generation pipeline.
    """
    # pylint: disable=too-many-locals
    print("🚀 Initializing AI Resume & Cover Letter Architect CLI...\n")

    parser = argparse.ArgumentParser(description="AI Resume & Cover Letter Architect")
    parser.add_argument(
        "document_type",
        nargs="?",
        default="resume",
        choices=["resume", "cover_letter"],
        help="The type of document to generate (resume or cover_letter)",
    )
    parser.add_argument(
        "language",
        nargs="?",
        default="en",
        help="The target language code (e.g., en, fr, pt)",
    )

    # Target-specific parameters
    parser.add_argument(
        "--role", default="software-engineer", help="Target role for the document"
    )
    parser.add_argument("--company", default="unknown-company", help="Target company")
    parser.add_argument("--country", default="unknown-country", help="Target country")

    args = parser.parse_args()
    document_type = args.document_type
    language = args.language
    role = args.role
    company = args.company
    country = args.country

    print(f"📄 Target Document Type: {document_type.replace('_', ' ').title()}")
    print(f"🌍 Target Language: {language.upper()}")
    print(f"👔 Target Role: {role.replace('-', ' ').title()}")
    print(f"🏢 Target Company: {company.title()}")
    print(f"🗺️  Target Country: {country.title()}")

    db_client = DatabaseClient()
    professional_data = db_client.get_professional_data()

    target_role = (
        f"{role.replace('-', ' ').title()} at {company.title()} in {country.title()}"
    )

    reasoner = ReasonerAgent()
    filtered_content = reasoner.analyze_and_filter(
        job_description=target_role, professional_data=professional_data
    )

    coder = CoderAgent()
    latex_output = coder.generate_latex(filtered_content, document_type=document_type)

    compiler = PDFCompiler()
    pdf_path = compiler.compile(
        latex_output,
        document_type=document_type,
        language=language,
        role=role,
        company=company,
        country=country,
    )

    if pdf_path:
        print(f"\n🎉 Pipeline execution successful! Document saved at: {pdf_path}")
    else:
        print("\n⚠️ Pipeline executed, but PDF compilation encountered errors.")


if __name__ == "__main__":
    main()
