def get_coder_prompt(filtered_content: str, document_type: str) -> str:
    """
    Returns the prompt used for the Coder agent to generate LaTeX.
    """
    doc_type_clean = document_type.replace('_', ' ')
    return f"""
    You are an expert LaTeX programmer.
    Based on the following experience points, generate a COMPLETE, professional, and compilable LaTeX {doc_type_clean}.
    You must include the document class (e.g., \\documentclass{{article}}), preamble, and \\begin{{document}} ... \\end{{document}}.
    Generate ONLY valid LaTeX code without any markdown formatting or explanations.
    
    Experience points:
    {filtered_content}
    """
