"""
Module containing strategy rules for different types of resumes and cover letters.
"""

MASTER_CV_STRATEGY = r"""
Strategy Rules for Master CV:
1. Length Constraint: There is NO page limit. This document serves as a comprehensive reference containing everything about the professional.
2. Data Mapping: Include EVERYTHING as detailed as possible. Render the 'detailedDescription' for all `educations`, `projects`, `experiences`, and `volunteering`. Nothing is omitted.
3. Content Selection: Include ALL achievements, ALL hard skills, and ALL interests.
4. Geographical Formatting: Always include the profile photo (using \includegraphics with `metadata.profilePicturePath`).
5. Formatting: Always leave a blank line between consecutive \resumeItem or \resumeExperience commands to prevent LaTeX overlapping.

LINGUISTIC & FORMATTING DIRECTIVES:

1. Data Mapping & The Match Rule: Strictly render the `detailedDescription` array as multiple bullet points for all entries. For `education`: Always strictly render the `resumeDescription` string.

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
- ATS Macros: Leave the second parameter of \resumeItem empty for projects (e.g., \resumeItem{Project Name}{}{Date}) to prevent ATS overflow. Format achievements directly extracting DB fields: \par\vspace{1.5mm}\noindent\textbf{event} \textbar{} \textit{eventType / awardOrRole} \hfill \textcolor{darkgray}{Formatted Date}\par

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks.
"""

TARGETED_RESUME_STRATEGY = r"""
Strategy Rules for Targeted Resumes (ATS/Online):
1. Length Constraint: STRICTLY enforce a 1-page limit for all early-career or internship roles.
2. Professional Summary: Focus on what the job requires and how you can help the company. Keep it short and concise. Highlight technical skills and experiences relevant to the job posting. Apply Markdown emphasis ('*bold*') to highlight 3 to 5 core competencies.
3. Projects & Experiences: Sort by descending relevance to the target job description. Add a GitHub link note at the end of the Projects section.
4. Geographical Formatting Rules (CRITICAL): Evaluate the target firm's location and type:
   - Anglo-Saxon Standard (US, UK, Canada, Australia AND Top-tier Multinationals in the EU): Strictly EXCLUDE the candidate's photo, personal details, and the 'Interests' section. Aggressively highlight quantitative metrics.
   - Continental Standard (Local DACH, France, European firms): Strictly INCLUDE the candidate's photo (using \includegraphics with `metadata.profilePicturePath`) and INCLUDE the 'Interests' section to signal cultural fit.
5. Formatting: Always leave a blank line between consecutive \resumeItem or \resumeExperience commands to prevent LaTeX overlapping.

LINGUISTIC & FORMATTING DIRECTIVES:

1. Data Mapping & The Match Rule: Strictly follow the Reasoner's blueprint for `educations`, `experiences`, `projects`, `volunteering`, and `achievements`:
   - If tagged [TARGET MATCH]: Render the `detailedDescription` array as multiple bullet points.
   - If tagged [SECONDARY ENTRY]: Render the `briefDescription` string as a single, high-impact STAR-method bullet point.
   - For `education`: Always strictly render the `resumeDescription` string.

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
- ATS Macros: Leave the second parameter of \resumeItem empty for projects (e.g., \resumeItem{Project Name}{}{Date}) to prevent ATS overflow. Format achievements directly extracting DB fields: \par\vspace{1.5mm}\noindent\textbf{event} \textbar{} \textit{eventType / awardOrRole} \hfill \textcolor{darkgray}{Formatted Date}\par

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks.
"""

NETWORKING_RESUME_STRATEGY = r"""
Strategy Rules for Networking Resumes (In-Person):
1. Length Constraint: STRICTLY fit on 1-page for all early-career or internship roles.
2. Data Mapping: Strictly render the 'briefDescription' string (a 1-bullet STAR summary) for ALL `experiences`, `projects`, and `volunteering` to save vertical space. Ignore the Reasoner's Match Rule tags for description length.
3. Professional Summary (Objective): Keep it modular with placeholders for role and duration if needed (e.g., [SEEKING INTERNSHIP: TARGET ROLE / DOMAIN] -- [DURATION: 5 MONTHS | START: AUG 2027]).
4. Selection: Limit to exactly 3 top experiences and 3 top projects to fit on one page with the photo header.
5. Formatting Rules: Use \pagestyle{empty}, 10pt font, 0.75in side margins, 0.5in top/bottom margins. Inject the \small command immediately after \pagestyle{empty} to globally scale the document.
6. Geographical Formatting Rules (CRITICAL): Evaluate the target firm's location and type:
   - Anglo-Saxon Standard (US, UK, Canada, Australia AND Top-tier Multinationals in the EU): DO NOT include a photo. Exclude 'Interests'. 
   - Continental Standard (Local DACH, France, European firms): MUST include the circular profile picture (`Profile Photo.jpg`, 2.4cm) using fontawesome5 icons in the header. INCLUDE 'Interests' tailored to soft skills.
7. Additional Sections: Do NOT include 'Achievements' to save space.

LINGUISTIC & FORMATTING DIRECTIVES:

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
- Networking Macros & Projects: For Networking templates, bypass \resumeItem entirely for projects and achievements, instead using manual paragraph breaks without skills (e.g., \par\vspace{1.5mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Formatted Date}).

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks.
"""

GENERALIST_ONLINE_RESUME_STRATEGY = r"""
Strategy Rules for Generalist Online Resumes:
1. Length Constraint: STRICTLY enforce a 1-page limit for early-career or internship stages.
2. Data Mapping: As there is no specific Job Description, assume the role of an HR Specialist curating a strong Generalist SWE profile. Use `detailedDescription` for the 2-3 most recent or globally impactful `experiences` and `projects`. Fall back to `briefDescription` for all other `experiences`, `projects`, and `volunteering` to guarantee the document fits exactly on 1 page. 
3. Geographical Formatting: Default to the Continental Standard (include photo and interests) unless the language dictates otherwise (e.g., if English, default to Anglo-Saxon Standard: no photo, no interests).

LINGUISTIC & FORMATTING DIRECTIVES:

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
- ATS Macros: Leave the second parameter of \resumeItem empty for projects (e.g., \resumeItem{Project Name}{}{Date}) to prevent ATS overflow. Format achievements directly extracting DB fields: \par\vspace{1.5mm}\noindent\textbf{event} \textbar{} \textit{eventType / awardOrRole} \hfill \textcolor{darkgray}{Formatted Date}\par

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks.
"""

COVER_LETTER_STRATEGY = r"""
LINGUISTIC & FORMATTING DIRECTIVES:
1. Length Constraint: STRICTLY fit on 1-page.
2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs.
3. French (FR): Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage"). 
4. Casing & Terminology: Accurately translate 'Machine Learning'. Never capitalize generic nouns.
5. Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
6. Orthographic & Typographical Localization: Adhere strictly to target-language typography. Convert standard quotes to LaTeX native quotes (``word'' and `word'). Escape ampersands safely (\&).
7. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks.
"""

def get_strategy_rules(strategy: str, document_type: str = "resume") -> str:
    """
    Returns the combined string of strategy rules based on document type and strategy.
    """
    if document_type == "cover_letter":
        return COVER_LETTER_STRATEGY.strip()
    
    if strategy == "master_cv":
        return MASTER_CV_STRATEGY.strip()
    elif strategy == "networking_resume":
        return NETWORKING_RESUME_STRATEGY.strip()
    elif strategy == "generalist_online_resume":
        return GENERALIST_ONLINE_RESUME_STRATEGY.strip()
    else: # Default to targeted_resume
        return TARGETED_RESUME_STRATEGY.strip()
