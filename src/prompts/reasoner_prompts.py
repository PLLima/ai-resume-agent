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

    Analyze the data against the job description. Output a structured blueprint detailing:
    1. Which `educations`, `experiences`, `projects`, `volunteering`, and `achievements` entries to include. By default, include the highest level of completed education and ongoing ones. Limit to 2-3 educations maximum, prioritizing the two best ones.
    2. For EACH included entry, you MUST explicitly tag it with either:
       - [TARGET MATCH]: If the entry directly addresses core technical/business requirements of the job description.
       - [SECONDARY ENTRY]: If the entry is included for background, timeline continuity, or supplementary soft skills.
    """
