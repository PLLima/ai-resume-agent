"""
Module containing strategy rules for different types of resumes and cover letters.
"""

ONLINE_ATS_STRATEGY = r"""
Strategy Rules for Online/ATS Resumes:
1. Professional Summary: Focus on what the job requires and how you can help the company. Keep it short and concise. Highlight your technical skills and experiences that are relevant to the job posting.
2. Projects: Highlight your technical skills and experiences that are relevant to the job posting. Add a GitHub link note at the end of the section.
3. Experience: Include ALL experiences, but sort them by descending relevance to the job posting.
4. Additional Sections: Include 'Achievements' to signal strong mathematical and analytical problem-solving skills.
5. Formatting: Always leave a blank line between consecutive \resumeItem or \resumeExperience commands to prevent LaTeX overlapping.
6. Professional Summary Emphasis: Strategically apply Markdown emphasis ('*bold*') to highlight 3 to 5 core competencies, academic milestones, or domain-specific keywords (e.g., *scalable system architecture* or *Master of Engineering*). These must translate directly into \textbf{} in the final LaTeX output to immediately draw the recruiter's eye to your most critical qualifications.
"""

IN_PERSON_STRATEGY = r"""
Strategy Rules for In-Person Resumes:
1. Data Mapping: Strictly render the 'briefDescription' string (a 1-bullet STAR summary) for projects and experiences.
2. Professional Summary (Objective): Keep it modular with placeholders for role and duration if needed (e.g., [SEEKING INTERNSHIP: TARGET ROLE / DOMAIN] -- [DURATION: 5 MONTHS | START: AUG 2027]).
3. Narrative Theme: Bridge algorithmic problem-solving with scalable system architecture, but also depending on the job posting.
4. Projects/Experiences: Limit to exactly 3 top experiences (choose them depending on what is more relevant for the job posting) and 3 top projects (choose them depending on what is more relevant for the job posting) to fit on one page with the photo header.
5. Formatting Rules: Must fit strictly on one page. Use \pagestyle{empty}, 10pt font, 0.75in side margins, 0.5in top/bottom margins, circular profile picture (Profile Photo.jpg, 2.4cm), and fontawesome5 icons. Reduce \titlespacing and \resumeItem paddings to 1mm. Inject the \small command immediately after \pagestyle{empty} to globally scale the document and ensure it fits perfectly on a single page.
6. Additional Sections: Include 'Interests' tailored to soft skills (Travel, Culinary, Pop Culture). Do NOT include 'Achievements' to save space.
"""

SHARED_DATA_MAPPING_1 = r"""
1. Data Mapping: Strictly render the 'detailedDescription' array for projects and experiences.
"""

SHARED_LINGUISTIC_2_TO_4 = r"""
2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Apprentissage'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.
"""

SHARED_EDUCATION_DATES_5 = r"""
5. Education Dates Formatting (Strategic ATS Anchoring & Multi-Anchor): Your goal is to bypass rigid ATS graduation-year filters while maximizing keyword relevance based on the target job description. First, check 'metadata.ongoing' and 'metadata.type' for each entry.

- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).

- Active Entries ('ongoing: true'): Group active entries by 'metadata.type'. For EACH type, identify the earliest approaching milestone (evaluating 'courseworkEndDate' then 'endDate').

- Multi-Anchor Selection: ALL active entries within a type that share this exact earliest date are designated as "ATS Anchors". For THESE entries, output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).

- Omission Rule (Concurrent Programs): For any concurrent active entries in that type with later dates, you must OMIT the date to prevent ATS miscalculation. Instead of a date, output 'Double Degree' (EN) | 'Duplo Diploma' (PT-BR) | 'Double diplôme' (FR) if the type is "degree". For other types, output 'Concurrent Course' (EN) | 'Curso Simultâneo' (PT-BR) | 'Formation simultanée' (FR).
"""

SHARED_ADVANCED_LINGUISTIC_6 = r"""
6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:

- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.

- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.

- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.

- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').

- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.

- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).
"""

ATS_SECTION_TITLES_7 = r"""
7. Section Titles & Alignment Constraints:

- Standardize the skills section title to exactly 'Technical & Language Skills' (localized to the target language). Enforce Sentence Case for French section headers.

- NEVER use bare \begin{itemize} commands, as default LaTeX margins will break the document's spatial grid. You MUST apply these exact enumitem parameters: Flat Lists (Skills/Interests): \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets (Experience/Projects): \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template). Always leave a blank line between consecutive \resumeItem or \resumeExperience commands to prevent LaTeX overlapping.

- Macros & Projects: For ATS templates, leave the second parameter of \resumeItem empty for projects (e.g., \resumeItem{Project Name}{}{Date}) to prevent ATS overflow and tabular wrapping. Infer specific event details for achievements from the title/issuer.
"""

IN_PERSON_SECTION_TITLES_7 = r"""
7. Section Titles & Alignment Constraints:

- Standardize the skills section title to exactly 'Technical & Language Skills' (localized to the target language). Enforce Sentence Case for French section headers.

- NEVER use bare \begin{itemize} commands, as default LaTeX margins will break the document's spatial grid. You MUST apply these exact enumitem parameters: Flat Lists (Skills/Interests): \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets (Experience/Projects): \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template). Always leave a blank line between consecutive \resumeItem or \resumeExperience commands to prevent LaTeX overlapping.

- Macros & Projects: For In-Person templates, bypass \resumeItem entirely for projects and achievements, instead using manual paragraph breaks without skills (e.g., \par\vspace{1.5mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Formatted Date}).
"""

COVER_LETTER_SECTION_TITLES_7 = r"""
7. Section Titles & Alignment Constraints:

- Enforce Sentence Case for French section headers.
"""

MARKDOWN_RULE_8 = r"""
8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). This ensures dynamic emphasis of key metrics and technologies. Never print raw asterisks in the final LaTeX output.
"""


def get_strategy_rules(strategy: str, document_type: str = "resume") -> str:
    """
    Returns the combined string of strategy rules based on document type and strategy.
    """
    rules = ""

    if document_type == "resume":
        if strategy == "in_person":
            rules += IN_PERSON_STRATEGY.strip() + "\n\n"
            rules += "LINGUISTIC & FORMATTING DIRECTIVES:\n\n"
            rules += SHARED_LINGUISTIC_2_TO_4.strip() + "\n\n"
            rules += SHARED_EDUCATION_DATES_5.strip() + "\n\n"
            rules += SHARED_ADVANCED_LINGUISTIC_6.strip() + "\n\n"
            rules += IN_PERSON_SECTION_TITLES_7.strip() + "\n\n"
            rules += MARKDOWN_RULE_8.strip()
        else:  # online_ats or default resume
            rules += ONLINE_ATS_STRATEGY.strip() + "\n\n"
            rules += "LINGUISTIC & FORMATTING DIRECTIVES:\n\n"
            rules += SHARED_DATA_MAPPING_1.strip() + "\n\n"
            rules += SHARED_LINGUISTIC_2_TO_4.strip() + "\n\n"
            rules += SHARED_EDUCATION_DATES_5.strip() + "\n\n"
            rules += SHARED_ADVANCED_LINGUISTIC_6.strip() + "\n\n"
            rules += ATS_SECTION_TITLES_7.strip() + "\n\n"
            rules += MARKDOWN_RULE_8.strip()
    elif document_type == "cover_letter":
        # Cover letters inherit specific logic but omit Resume macro/ATS logic (like rule 5).
        rules += "LINGUISTIC & FORMATTING DIRECTIVES:\n\n"
        rules += SHARED_LINGUISTIC_2_TO_4.strip() + "\n\n"
        rules += SHARED_ADVANCED_LINGUISTIC_6.strip() + "\n\n"
        rules += COVER_LETTER_SECTION_TITLES_7.strip() + "\n\n"
        rules += MARKDOWN_RULE_8.strip()

    return rules.strip()
