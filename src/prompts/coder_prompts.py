"""
Module containing prompts for the Coder Agent.
"""

from src.prompts.strategy_rules import get_default_profile_photo, get_strategy_rules


def get_coder_prompt(
    filtered_content: str,
    document_type: str,
    strategy: str = "targeted_resume",
    profile_photo_filename: str | None = None,
) -> str:
    """
    Returns the prompt used for the Coder agent to generate LaTeX.
    """
    doc_type_clean = document_type.replace("_", " ")
    strategy_text = get_strategy_rules(strategy, document_type)

    if profile_photo_filename is None:
        profile_photo_filename = get_default_profile_photo(strategy)

    return f"""You are an expert LaTeX programmer.
Based on the following experience points and the Reasoner's blueprint, generate a COMPLETE,
professional, and compilable LaTeX {doc_type_clean}.
You must include the document class (e.g., \\documentclass{{article}}),
preamble, and \\begin{{document}} ... \\end{{document}}.
Generate ONLY valid LaTeX code without any markdown formatting or explanations.

Profile Photo Asset (use ONLY when the active strategy requires a photo): {profile_photo_filename}

{strategy_text}

Reasoner's Blueprint & Experience points:
{filtered_content}"""
