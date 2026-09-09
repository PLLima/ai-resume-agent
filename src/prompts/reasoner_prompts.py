"""
Module containing prompts for the Reasoner Agent.
"""


def get_reasoner_prompt(job_description: str, professional_data: dict) -> str:
    """
    Returns the prompt used for the Reasoner agent.
    """
    return f"""
    You are an HR Specialist.
    Here is the job description: '{job_description}'.
    
    Here is the candidate's professional data (JSON format):
    {professional_data}
    
    Which of these experiences should I focus on for the resume? (Summarize in plain text).
    """
