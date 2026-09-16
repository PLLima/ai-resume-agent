"""
Module containing strategy rules for different types of resumes.
"""

COURSEWORK_END_DATE_RULE = """
For any education entry that has a coursework end date separate from the official degree end date (e.g., if you are currently in your penultimate year and have finished coursework), render the dates explicitly using both fields like so: 'Expected [Coursework Month/Year] (Coursework) / [End Year] (Official Degree)'.
"""

IN_PERSON_RULES = """
Strategy Rules for In-Person Resumes:
1. Professional Summary (Objective): Keep it modular with placeholders for role and duration if needed (e.g., [SEEKING INTERNSHIP: TARGET ROLE / DOMAIN] -- [DURATION: 5 MONTHS | START: AUG 2027]).
2. Narrative Theme: Bridge algorithmic problem-solving with scalable system architecture.
3. Projects/Experiences: Limit to exactly 3 top experiences (IDE Jr., BasiCS Tutor, LASCAR) and 3 top projects (EI Climat, Voice CRM, 3D Tower Defense) to fit on one page with the photo header.
4. Formatting Rules: Must fit strictly on one page. Use \\pagestyle{empty}, 10pt font, 0.75in side margins, 0.5in top/bottom margins, circular profile picture (Profile Photo.jpg, 2.4cm), and fontawesome5 icons. Reduce \\titlespacing and \\resumeItem paddings to 1mm.
5. Additional Sections: Include 'Interests' tailored to soft skills (Travel, Culinary, Pop Culture). Do NOT include 'Achievements' to save space.
"""

ONLINE_ATS_RULES = """
Strategy Rules for Online/ATS Resumes:
1. Professional Summary: Focus on low-level programming (C/C++), embedded systems, firmware, and hardware-software integration.
2. Projects: Include exactly 4 technical projects emphasizing C, STM32, Hardware SPI, and hardware prototyping. Add a GitHub link note at the end of the section.
3. Experience: Include ALL experiences, but sort them by descending relevance to Embedded Systems/Hardware.
4. Additional Sections: Include 'Achievements' to signal strong mathematical and analytical problem-solving skills.
5. Formatting: Strategically use \\textbf{} inside bullet points to highlight key technologies (e.g., C++, STM32) and metrics. Always leave a blank line between consecutive \\resumeItem or \\resumeExperience commands to prevent LaTeX overlapping.
"""

def get_strategy_rules(strategy: str) -> str:
    """
    Returns the combined string of strategy rules based on the strategy type.
    """
    rules = COURSEWORK_END_DATE_RULE + "\n"
    if strategy == "in_person":
        rules += IN_PERSON_RULES
    elif strategy == "online_ats":
        rules += ONLINE_ATS_RULES

    return rules.strip()
