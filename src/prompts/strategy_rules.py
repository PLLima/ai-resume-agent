"""
Module containing strategy rules for different types of resumes.
"""

COURSEWORK_END_DATE_RULE = """
Education Dates Formatting (Strategic ATS Anchoring): Your goal is to bypass rigid ATS graduation-year filters while maximizing keyword relevance based on the target job description. First, check 'metadata.ongoing' and 'metadata.type' for each entry.

- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).

- Active Degrees ('ongoing: true'): Group active degrees by 'metadata.type'. For EACH type, you must select ONE degree to act as the "ATS Anchor".

   - Selection Logic: Choose the anchor degree whose timeline ('courseworkEndDate' or 'endDate') and specialization best aligns with the target job's requirements (e.g., if the job requires a 2028 graduation, anchor to the 2028 degree. If the job strictly requires a specific "Computer Engineering" timeline, anchor to that degree).

   - Formatting: For the chosen Anchor Degree ONLY, output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).

- Omission Rule: You must OMIT the date entirely (leave the string completely blank: {}) for all other concurrent active degrees within that same 'metadata.type'. The ATS will still parse the keywords (e.g., Computer Engineering) without miscalculating the graduation year.
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

LINGUISTIC_FORMATTING_RULES = """
Linguistic & Formatting Directives:
1. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., use 'Projetei', 'Arquitetei', 'Desenvolvi'. NEVER use 3rd person like 'Desenvolveu', and NEVER use literal translations like 'Engenhei'). Ensure degree names are localized (e.g., 'Mestrado em Engenharia').
2. French (FR): Strictly start all bullet points with Action Nouns (e.g., 'Conception', 'Recherche', 'Enseignement', 'Inspection'). Never use conjugated verbs or past participles to start a bullet point.
3. Parallelism & Punctuation: Ensure absolute grammatical parallelism within every list. End every single bullet point with a period.
4. Casing: Enforce strict Sentence Casing for Skills, Focus Areas, and Interests (e.g., 'Aprendizado de máquina', 'Culture pop & jeux vidéo').
5. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
   - Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms (ensure exact gender/number agreement for all nouns and adjectives).
   - Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
   - Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
   - Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
   - Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action $\\rightarrow$ Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally.
   - Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4,000').
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

    rules += "\n" + LINGUISTIC_FORMATTING_RULES

    return rules.strip()
