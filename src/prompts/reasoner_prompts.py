"""
Module containing prompts for the Reasoner Agent.
"""

from src.prompts.strategy_rules import get_strategy_rules


def get_reasoner_prompt(
    job_description: str, professional_data: dict, strategy: str = "general"
) -> str:
    """
    Returns the prompt used for the Reasoner agent.
    """
    strategy_text = get_strategy_rules(strategy)

    return f"""
    You are an HR Specialist.
    Here is the job description: '{job_description}'.

    {strategy_text}

    Here is the candidate's professional data (JSON format):
    {professional_data}
    
    Which of these experiences should I focus on for the resume? (Summarize in plain text).
    """
