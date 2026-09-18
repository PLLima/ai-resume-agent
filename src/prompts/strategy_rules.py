"""
Module containing strategy rules for different types of resumes.
"""

COURSEWORK_END_DATE_RULE = """
Education Dates Formatting (Strategic ATS Anchoring & Multi-Anchor): Your goal is to bypass rigid ATS graduation-year filters while maximizing keyword relevance based on the target job description. First, check 'metadata.ongoing' and 'metadata.type' for each entry.

- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).

- Active Entries ('ongoing: true'): Group active entries by 'metadata.type'. For EACH type, identify the earliest approaching milestone (evaluating 'courseworkEndDate' then 'endDate').

- Multi-Anchor Selection: ALL active entries within a type that share this exact earliest date are designated as "ATS Anchors". For THESE entries, output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).

- Omission Rule (Concurrent Programs): For any concurrent active entries in that type with later dates, you must OMIT the date to prevent ATS miscalculation. Instead of a date, output 'Double Degree' (EN) | 'Duplo Diploma' (PT-BR) | 'Double diplôme' (FR) if the type is "degree". For other types, output 'Concurrent Course' (EN) | 'Curso Simultâneo' (PT-BR) | 'Formation simultanée' (FR).
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
4. Casing, Post-Colon Formatting & Terminology:
   - Skill Lists: For comma-separated lists (e.g., Technical Skills), enforce Title Case for all items in English and Portuguese (e.g., '\\textbf{Core Competencies:} System Architecture, Machine Learning'). In French, enforce strict lowercase for all items (e.g., 'architecture système, apprentissage automatique') except for proper nouns like 'Python'.
   - Interests/Focus Areas: Enforce Sentence Casing. After a colon, capitalize the first letter in English/PT-BR. In French, the first letter after a colon must be lowercase unless it is a proper noun.
   - Terminology: Accurately translate terms (e.g., use 'Apprentissage automatique' in FR, not 'Machine Learning'). Never capitalize generic nouns like 'anime' or 'manga' in any language.
5. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
   - Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms (ensure exact gender/number agreement for all nouns and adjectives).
   - Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
   - Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
   - Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
   - Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action $\\rightarrow$ Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally.
   - Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4,000').
"""

SECTION_TITLES_AND_ALIGNMENT_RULES = """
Section Titles & Alignment Constraints:
1. Standardize the skills section title to exactly 'Technical & Language Skills' (localized to the target language).
2. NEVER use bare \\begin{itemize} commands, as default LaTeX margins will break the document's spatial grid. You MUST apply these exact enumitem parameters:
   - For Flat Lists (Skills & Interests): Use exactly \\begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] to snap the text perfectly flush-left with the section headers.
   - For Nested Bullets (Experience & Projects): Use exactly \\begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt depending on the template) to perfectly align the bullets with the text block.
"""

MARKDOWN_TO_LATEX_RULES = """
Markdown to LaTeX Emphasis:
Translate Markdown emphasis syntax into LaTeX: use *word* for bold (e.g., \\textbf{word}) and **word** for italic (e.g., \\textit{word}). This ensures dynamic emphasis of key metrics and technologies. Never print the raw asterisks in the final LaTeX output.
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
    rules += "\n" + SECTION_TITLES_AND_ALIGNMENT_RULES

    return rules.strip()
