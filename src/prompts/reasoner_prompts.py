"""
Module containing prompts for the Reasoner Agent.
"""

from src.prompts.strategy_rules import get_strategy_rules


def get_reasoner_prompt(
    job_description: str,
    professional_data: dict,
    strategy: str = "general",
    document_type: str = "resume",
) -> str:
    """
    Returns the prompt used for the Reasoner agent.
    """
    doc_type_clean = document_type.replace("_", " ")
    strategy_text = get_strategy_rules(strategy, document_type)

    return f"""
    You are an HR Specialist.
    Here is the job description: '{job_description}'.

    {strategy_text}

    Here is the candidate's professional data (JSON format):
    {professional_data}
    
    Which of these experiences should I focus on for the {doc_type_clean}? (Summarize in plain text).
    """
