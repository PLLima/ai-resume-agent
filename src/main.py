import sys
import os

# Ensure the root project directory is in the PYTHONPATH so we can import src.* modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db.client import DatabaseClient
from src.agents.reasoner import ReasonerAgent
from src.agents.coder import CoderAgent

def main():
    print("🚀 Initializing AI Resume & Cover Letter Architect CLI...\n")
    
    # 1. Database Connection Skeleton
    db_client = DatabaseClient()
    professional_data = db_client.get_professional_data()
    
    target_role = "Software Engineer focusing on C++ and Machine Learning"
    
    # 2. Reasoner Agent (Llama 3.1)
    reasoner = ReasonerAgent()
    filtered_content = reasoner.analyze_and_filter(
        job_description=target_role,
        professional_data=professional_data
    )
    
    # 3. Coder Agent (Qwen 2.5 Coder)
    coder = CoderAgent()
    latex_output = coder.generate_latex(filtered_content)
    
    print("\n🎉 Pipeline execution successful!")

if __name__ == "__main__":
    main()
