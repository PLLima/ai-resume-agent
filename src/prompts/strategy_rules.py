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
1. Data Mapping: Strictly render the 'briefDescription' string (a 1-bullet STAR summary) for projects and experiences.
2. Professional Summary (Objective): Keep it modular with placeholders for role and duration if needed (e.g., [SEEKING INTERNSHIP: TARGET ROLE / DOMAIN] -- [DURATION: 5 MONTHS | START: AUG 2027]).
3. Narrative Theme: Bridge algorithmic problem-solving with scalable system architecture, but also depending on the job posting.
4. Projects/Experiences: Limit to exactly 3 top experiences (choose them depending on what is more relevant for the job posting) and 3 top projects (choose them depending on what is more relevant for the job posting) to fit on one page with the photo header.
5. Formatting Rules: Must fit strictly on one page. Use \\pagestyle{empty}, 10pt font, 0.75in side margins, 0.5in top/bottom margins, circular profile picture (Profile Photo.jpg, 2.4cm), and fontawesome5 icons. Reduce \\titlespacing and \\resumeItem paddings to 1mm.
6. Additional Sections: Include 'Interests' tailored to soft skills (Travel, Culinary, Pop Culture). Do NOT include 'Achievements' to save space.
"""

ONLINE_ATS_RULES = """
Strategy Rules for Online/ATS Resumes:
1. Data Mapping: Strictly render the 'detailedDescription' array for projects and experiences.
2. Professional Summary: Focus on what the job requires and how you can help the company. Keep it short and concise. Highlight your technical skills and experiences that are relevant to the job posting.
3. Projects: Highlight your technical skills and experiences that are relevant to the job posting. Add a GitHub link note at the end of the section.
4. Experience: Include ALL experiences, but sort them by descending relevance to the job posting.
5. Additional Sections: Include 'Achievements' to signal strong mathematical and analytical problem-solving skills.
6. Formatting: Always leave a blank line between consecutive \\resumeItem or \\resumeExperience commands to prevent LaTeX overlapping.
7. Professional Summary Emphasis: Strategically apply Markdown emphasis ('*bold*') to highlight 3 to 5 core competencies, academic milestones, or domain-specific keywords (e.g., *scalable system architecture* or *Master of Engineering*). These must translate directly into \\textbf{} in the final LaTeX output to immediately draw the recruiter's eye to your most critical qualifications.
"""

LINGUISTIC_FORMATTING_RULES = """
Linguistic & Formatting Directives:
1. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei', 'Desenvolvi'). NEVER use 3rd person or literal translations (e.g., 'Engenhei'). Localize degree names (e.g., 'Mestrado em Engenharia').
2. French (FR): Strictly start all bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Apprentissage', 'Recherche', 'Enseignement', 'Inspection'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").
3. Parallelism & Punctuation: Ensure absolute grammatical parallelism within every list. End every single bullet point with a period.
4. Casing, Tech Stacks & Terminology:
   - Tech Stack Ordering: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation.
   - Skill Lists: French skills are stored capitalized in the DB. You MUST dynamically lowercase them in comma-separated lists (e.g., 'Architecture de systèmes' -> 'architecture de systèmes') except for proper nouns. For EN/PT-BR, enforce Title Case.
   - Interests/Focus Areas: Sentence casing. Post-colon: capitalize in EN/PT-BR, lowercase in FR. Never capitalize generic nouns ('anime', 'manga'). Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR).
5. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
   - Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms (ensure exact gender/number agreement for all nouns and adjectives).
   - Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
   - Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
   - Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
   - Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action $\rightarrow$ Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally.
   - Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4,000').
"""

SECTION_TITLES_AND_ALIGNMENT_RULES = """
Section Titles & Alignment Constraints:
1. Standardize the skills section title to exactly 'Technical & Language Skills' (localized to the target language).
2. NEVER use bare \\begin{itemize} commands, as default LaTeX margins will break the document's spatial grid. You MUST apply these exact enumitem parameters:
   - Flat Lists (Skills/Interests): \\begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt]
   - Nested Bullets (Experience/Projects): \\begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
"""

MARKDOWN_TO_LATEX_RULES = """
Markdown to LaTeX Emphasis:
Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\\textbf{word}') and '**word**' for italic ('\\textit{word}'). This ensures dynamic emphasis of key metrics and technologies. Never print raw asterisks in the final LaTeX output.
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
