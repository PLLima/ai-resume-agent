"""
Module containing strategy rules for different types of resumes and cover letters.
"""

MASTER_CV_STRATEGY = r"""Strategy Rules for Master CV:
1. Length Constraint: There is NO page limit. This document serves as a comprehensive reference containing everything about the professional.
2. Section Ordering & Titling: The order MUST be: Summary -> Skills & Languages -> Education -> Projects -> Experience -> Volunteering -> Achievements -> Interests. Standardize the skills title to 'Skills & Languages' (localized).
3. Data Mapping: Include EVERYTHING as detailed as possible. Render the 'detailedDescription' for all `projects`, `experiences`, and `volunteering`. Nothing is omitted.
4. Content Selection: Include ALL achievements, ALL hard skills, and ALL interests.
5. Geographical Formatting & Photo Customization: Always include the circular profile photo using `\includegraphics[width=2.4cm, keepaspectratio]{{profile_photo_filename}}`. Support customizable selection between `ProfilePhoto.jpg` (default for archival Master CV) and `ProfilePhoto_light.jpg` (compressed variant for smaller PDF memory footprint).
6. Formatting & Margins: Always leave a blank line between consecutive entries. To prevent text from overflowing the right margin, ALWAYS include `\setlength{\emergencystretch}{2em}` in the preamble.
7. Page Break Prevention (Orphan Control): Always use `\usepackage{needspace}` in the preamble. Prepend `\needspace{8em}` exactly before every `\section{...}` command, and `\needspace{5em}` exactly before every `\resumeExperience`, project, or achievement entry to ensure the title, role, and at least one bullet point stay together.
8. Sorting Rule: Sort all `education`, `projects`, `experiences`, and `volunteering` entries in strict anti-chronological order (newest `endDate` first). If entries share the exact same `endDate`, sort them alphabetically by their localized title/name.

LINGUISTIC & FORMATTING DIRECTIVES:

1. Data Mapping & The Match Rule: Strictly render the `detailedDescription` array as multiple bullet points for all entries. For `education`: Always strictly render the `highlights` array as bullet points, followed immediately by the `detailedDescription` array. Do NOT render the `resumeDescription` string.

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like ' : ' and ' ; '). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Skills & Languages' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt] (or topsep=2pt based on template).
- Macros & Projects: Format projects directly (e.g., \par\vspace{1.5mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Date}). Format achievements directly extracting DB fields: \par\vspace{1.5mm}\noindent\textbf{event} \textbar{} \textit{eventType / awardOrRole} \hfill \textcolor{darkgray}{Formatted Date}\par

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks."""

TARGETED_RESUME_STRATEGY = r"""Strategy Rules for Targeted Resumes (ATS/Online):
1. Length Constraint (STRICTLY 1-PAGE CEILING): STRICTLY enforce a 1-page limit for all early-career or internship roles using `\pagestyle{empty}`. Page 2 overflow is a critical failure.
2. Professional Summary: Keep it concise (2–3 lines max). State the target role, availability/duration if specified, and apply Markdown emphasis ('*bold*') to highlight 3 to 5 core competencies directly matching the job posting.
3. Projects & Experiences Selection & 1-Page Content Budget (CRITICAL): Sort by descending relevance to the target job description. Add a 1-line GitHub link note at the end of the Projects section. Strictly enforce the following density budgets by Geographical Standard:
 - **Continental Standard (1-Flagship Budget):** Because the circular photo and mandatory `Interests` / `Centres d'intérêt` section consume ~110–120 pt of vertical height, you MUST select **EXACTLY 3 projects and 3 experiences** (6 entries total), 2 educations, and at most 2 achievements. The Reasoner MUST tag **AT MOST 1 flagship entry** (either 1 project OR 1 experience, max 3 bullets) as `[TARGET MATCH]` (`detailedDescription`), and tag ALL remaining 5 entries as `[SECONDARY ENTRY]` (`briefDescription`, 1 bullet each). NEVER tag 2 or more entries as `[TARGET MATCH]` on a Continental Standard targeted resume.
 - **Anglo-Saxon Standard:** Select **3 projects and 3 experiences** (6 entries total), 2 educations, and 2–3 achievements. Tag AT MOST 2 entries as `[TARGET MATCH]` (`detailedDescription`) and the remaining 4 as `[SECONDARY ENTRY]` (`briefDescription`), OR render all 6 using `briefDescription` if total bullet lines would threaten the 1-page ceiling.
4. Geographical Formatting, Layout Scaling & Photo Customization (CRITICAL): Evaluate the target firm's location and corporate standard:
 - **Anglo-Saxon Standard** (US, UK, Canada, Australia, Quant Hedge Funds, and Top-tier Multinationals in the EU): Strictly EXCLUDE the candidate's photo, personal details, and the 'Interests' section. Use `left=0.5in, top=0.4in, right=0.5in, bottom=0.4in`, `\titlespacing{\section}{0pt}{1ex}{0.8ex}`, and inject `\small` immediately after `\pagestyle{empty}`. Aggressively highlight quantitative metrics.
 - **Continental Standard** (Local DACH, France, European corporate/banking/tech firms): Strictly INCLUDE the circular profile photo and the 'Interests' / 'Centres d'intérêt' section at the bottom of Page 1. To guarantee a strict 1-page fit, you MUST use `left=0.45in, top=0.35in, right=0.45in, bottom=0.35in`, `\titlespacing{\section}{0pt}{0.7ex}{0.5ex}`, `\resumeExperience` top spacing of `0.6mm`, a `2.1cm` circular photo (`0.78\textwidth` / `0.22\textwidth` header split), and inject `\footnotesize` immediately after `\pagestyle{empty}`.
 - **Customizable Profile Photo Asset:** For Continental Standard resumes, render the circular photo via `\includegraphics[width=2.1cm, keepaspectratio]{{profile_photo_filename}}`, supporting either `ProfilePhoto.jpg` (standard high-res) or `ProfilePhoto_light.jpg` (recommended default for online/ATS portals to minimize PDF file size).
5. Formatting & Macros: Always leave a blank line between consecutive entries to prevent LaTeX overlapping. Bypass the heavy tabular `\resumeItem` macro for projects and achievements; instead use lightweight paragraph breaks (`\par\vspace{0.6mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Date}` for Continental, `1mm` for Anglo-Saxon) to conserve vertical space and maximize ATS parsability.

LINGUISTIC & FORMATTING DIRECTIVES:

1. Data Mapping & The Match Rule: Strictly follow the Reasoner's blueprint for `educations`, `experiences`, `projects`, `volunteering`, and `achievements`:
 - If tagged [TARGET MATCH]: Render the `detailedDescription` array as multiple bullet points (strictly capped at 1 entry total on Continental Standard resumes).
 - If tagged [SECONDARY ENTRY]: Render the `briefDescription` string as a single, high-impact STAR-method bullet point.
 - For `education`: Always strictly render the `resumeDescription` string.

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: Strictly OMIT soft skills from the 'Technical & Language Skills' section to maximize technical density and preserve vertical space; render only Hard Skills and Spoken Languages. When rendering 'techStackRefs', alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting: First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is non-existent, ALWAYS display the 'timeline.endDate'. NEVER omit concurrent degree graduation dates. Output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR).
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like '~:' and '~;'). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt].
- Achievements Formatting: Format achievements directly extracting DB fields using compact spacing: \par\vspace{0.6mm}\noindent\textbf{event} \textbar{} \textit{eventType / awardOrRole} \hfill \textcolor{darkgray}{Formatted Date}\par (use `1mm` on Anglo-Saxon).

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks."""

NETWORKING_RESUME_STRATEGY = r"""Strategy Rules for Networking Resumes (In-Person):
1. Length Constraint: STRICTLY fit on 1-page for all early-career or internship roles.
2. Data Mapping: Strictly render the 'briefDescription' string (a 1-bullet STAR summary) for ALL `experiences`, `projects`, and `volunteering` to save vertical space. Ignore the Reasoner's Match Rule tags for description length.
3. Professional Summary (Objective): Keep it modular with role, duration, and start date separated strictly by en-dashes `--` (e.g., `SEEKING CÉSURE / OFF-CYCLE INTERNSHIP: [TARGET ROLE] -- 5--6 MONTHS -- START: JUL/AUG 2027`). NEVER use em-dashes (`---`) in the headline, project titles, or date/duration ranges.
4. Selection & Page-Fill Density (CRITICAL):
 - Anglo-Saxon Standard (`\small` global font, no photo, no interests): Select **8 entries total** — either **5 projects and 3 experiences** OR **4 projects and 4 experiences**, depending on which combination best matches the specific target role.
 - Continental Standard (`\footnotesize` global font, circular photo + FontAwesome5 icons, mandatory `Interests` / `Centres d'intérêt` section at the end of the document): Select **7 entries total** — either **4 projects and 3 experiences** OR **3 projects and 4 experiences**, depending on which combination best matches the specific target role. Never use 4 projects + 4 experiences on Continental Standard resumes, as the 8th entry pushes the mandatory `Interests` / `Centres d'intérêt` section off Page 1.
5. Formatting & Global Scaling Rules: Use `\pagestyle{empty}`, 10pt base font, 0.75in side margins, 0.5in top/bottom margins (tighten to 0.5in/0.4in if Continental text nears the bottom margin), and `\titlespacing{\section}{0pt}{0.8ex}{0.6ex}`. Immediately after `\pagestyle{empty}`, inject `\small` for Anglo-Saxon Standard resumes and `\footnotesize` for Continental Standard resumes (regardless of whether the Continental resume is written in French, English, or Portuguese).
6. Geographical Formatting Rules & Photo Customization (CRITICAL): Evaluate the target firm's cultural standard (NOT the document language):
 - Anglo-Saxon Standard (US, UK, Canada, Australia, Quant Hedge Funds, and US/UK Tier-1 Investment Banks): DO NOT include a photo. Strictly EXCLUDE the 'Interests' section.
 - Continental Standard (Local DACH, France, and European corporate/tech/banking firms, even when the resume is written in English): MUST include the circular profile picture (`2.1cm`–`2.4cm`) and FontAwesome5 icons in the header, and MUST INCLUDE the 'Interests' / 'Centres d'intérêt' section at the very bottom of Page 1 to signal cultural fit. Render the photo using `\includegraphics[width=2.4cm, keepaspectratio]{{profile_photo_filename}}`, supporting customizable selection between `ProfilePhoto.jpg` (default for high-DPI in-person print) and `ProfilePhoto_light.jpg` (lightweight PDF option for digital sharing/QR codes).
7. Additional Sections: Do NOT include 'Achievements' to save vertical space.

LINGUISTIC & FORMATTING DIRECTIVES:

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: When rendering 'techStackRefs', ALWAYS output Hard Skills first, followed by Soft Skills. Alphabetize them within their respective groups based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

5. Education Dates Formatting (Full Academic Integrity): First, check 'metadata.ongoing' for each entry.
- Past Degrees ('ongoing: false'): Always output 'Completed: [Month] [Year]' (EN) | 'Concluído: [Mês] de [Ano]' (PT-BR) | 'Diplôme obtenu : [Mois] [Année]' (FR).
- Active Entries ('ongoing: true'): Identify the earliest approaching milestone between 'timeline.courseworkEndDate' and 'timeline.endDate'. If 'timeline.courseworkEndDate' is null or non-existent, ALWAYS display 'timeline.endDate'. NEVER omit or replace the graduation date of a concurrent degree (such as UFRGS) with 'Double Degree'. Always output 'Expected: [Month] [Year]' (EN) | 'Previsão: [Mês] de [Ano]' (PT-BR) | 'Diplôme attendu : [Mois] [Année]' (FR) for every ongoing degree.
- Education Description Mapping: Render the localized 'resumeDescription' string directly below the \resumeExperience{} command as a single itemized bullet point with `\footnotesize`.

6. Advanced Linguistic, Stylistic & Typographical Mastery: Ensure native-level fluency and absolute structural integrity in the target language. Strictly avoid the following:
- Morphological Errors: Prevent overregularization, incorrect pluralization, and wrong verb forms.
- Lexical Errors, Calques & Collocations: Avoid literal translations, false friends, and confused word pairs. Strictly use native-level professional collocations and precise industry terminology.
- Syntactic Errors: Ensure flawless subject-verb agreement, natural idiomatic word order, and correct preposition usage. Strictly avoid comma splices and dangling modifiers.
- Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
- Coherence & Cohesion: Maintain logical flow and cause-and-effect coherence within bullet points (Action -> Result). Ensure accurate use of relative pronouns and transitional phrasing to bind clauses naturally. Ensure absolute grammatical parallelism. End every single bullet point with a period.
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like '~:' and '~;'). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&). Strictly use `--` (en-dash) for all ranges and headline separators; never use `---` (em-dash).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt].
- Networking Macros & Projects: For Networking templates, bypass \resumeItem entirely for projects, instead using manual paragraph breaks without skills (e.g., \par\vspace{0.8mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Formatted Date}).

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks."""

GENERALIST_ONLINE_RESUME_STRATEGY = r"""Strategy Rules for Generalist Online Resumes:
1. Length Constraint & Margins: STRICTLY enforce a 1-page limit by reducing document margins to 0.5in horizontally and 0.4in vertically (0.45in/0.35in if Continental Standard nears the bottom margin), and completely omitting page numbers using \pagestyle{empty}.
2. Data Mapping (Extreme Brevity): Select EXACTLY the 3 most impactful experiences and 3 most impactful projects. Strictly render ONLY the briefDescription string (a single-bullet STAR summary) for these entries. Render the resumeDescription string for education.
3. Global Scaling: Inject a global font scaling command immediately after \pagestyle{empty} and before the header. Use \small for the Anglo-Saxon Standard (English) and \footnotesize for the Continental Standard (French/Portuguese) to accommodate the circular photo and mandatory Interests section on Page 1.
4. Geographical Formatting & Photo Customization: Default to the Continental Standard (include circular photo and interests) unless the language dictates otherwise (e.g., if English, default to Anglo-Saxon Standard: no photo, no interests). When rendering the circular photo (2.1cm–2.4cm), use \includegraphics[width=2.1cm, keepaspectratio]{{profile_photo_filename}}, supporting customizable selection between ProfilePhoto_light.jpg (recommended default for fast web downloads and low PDF memory footprint) and ProfilePhoto.jpg.

LINGUISTIC & FORMATTING DIRECTIVES:

2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs (e.g., 'Projetei', 'Arquitetei', 'Dominei'). NEVER use 3rd person or literal translations. Localize degree names.

3. French (FR): Strictly start bullet points with strong Action Nouns (e.g., 'Conception', 'Présentation', 'Animation'). Never use conjugated verbs, past participles, or weak passive nouns (e.g., avoid 'Exposition', 'Acquisition'). Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").

4. Casing, Tech Stacks & Terminology: Strictly OMIT all soft skills from the "Technical & Language Skills" section to maximize technical density. Render only Hard Skills and Spoken Languages. When rendering 'techStackRefs', alphabetize them based on their English translation. French skills are stored capitalized in the DB; you MUST dynamically lowercase them in comma-separated lists except for proper nouns. For EN/PT-BR, enforce Title Case. Accurately translate 'Machine Learning' to 'Apprentissage automatique' (FR) / 'Aprendizado de Máquina' (PT-BR). Never capitalize generic nouns like 'anime' or 'manga'.

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
- Orthographic & Typographical Localization: Adhere strictly to target-language typography (e.g., French requires a non-breaking space before two-part punctuation like '~:' and '~;'). Properly localize all number and decimal formats (e.g., EN uses '4,000.00', PT-BR uses '4.000,00', FR uses '4 000,00' or LaTeX '4\,000'). Convert standard quotes ("word" and 'word') to LaTeX native quotes (``word'' and `word'). Ensure ampersands are safely escaped as \& but NEVER double-escaped (\\&).

7. Section Titles & Alignment Constraints: Standardize skills title to 'Technical & Language Skills' (localized). Enforce Sentence Case for French headers. NEVER use bare \begin{itemize}. Use exact enumitem parameters: Flat Lists: \begin{itemize}[leftmargin=0pt, label={}, itemsep=1pt, parsep=0pt] | Nested Bullets: \begin{itemize}[leftmargin=0.22in, topsep=1pt, itemsep=1pt, parsep=0pt]. Reduce \titlespacing vertical gaps to 1ex and 0.8ex.
- Macros & Projects: Bypass the \resumeItem tabular macro entirely for projects and achievements. Instead, use manual lightweight paragraph breaks to conserve vertical space (e.g., \par\vspace{1mm}\noindent\textbf{Project Name} \hfill \textcolor{darkgray}{Formatted Date}).

8. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks."""

COVER_LETTER_STRATEGY = r"""LINGUISTIC & FORMATTING DIRECTIVES:
1. Length Constraint: STRICTLY fit on 1-page.
2. Portuguese (PT-BR): Strictly use 1st-person past tense active verbs.
3. French (FR): Enforce perfect elision (e.g., "d'apprentissage", never "de apprentissage").
4. Casing & Terminology: Accurately translate 'Machine Learning'. Never capitalize generic nouns.
5. Semantic, Pragmatic & Stylistic (Zero AI Fluff): Maintain a highly professional, academic, and technical register. Eliminate ambiguity, passive voice, unnecessary wordiness, and tonal inconsistencies. Absolutely eradicate hollow AI filler adverbs/adjectives (e.g., 'seamlessly', 'successfully', 'robust', 'cutting-edge').
6. Orthographic & Typographical Localization: Adhere strictly to target-language typography. Convert standard quotes to LaTeX native quotes (``word'' and `word'). Escape ampersands safely (\&).
7. Markdown to LaTeX Emphasis: Translate Markdown emphasis into LaTeX: use '*word*' for bold ('\textbf{word}') and '**word**' for italic ('\textit{word}'). Never print raw asterisks."""


def get_default_profile_photo(strategy: str) -> str:
    """
    Returns the recommended default profile photo asset filename based on strategy.

    ProfilePhoto.jpg: High-resolution asset for archival (master_cv) and
    high-DPI printed networking handouts (networking_resume).
    ProfilePhoto_light.jpg: Compressed lightweight asset for ATS portal
    uploads (targeted_resume) and web downloads (generalist_online_resume).
    """
    if strategy in ("master_cv", "networking_resume", "in_person"):
        return "ProfilePhoto.jpg"
    return "ProfilePhoto_light.jpg"


def get_strategy_rules(strategy: str, document_type: str = "resume") -> str:
    """
    Returns the combined string of strategy rules based on document type and strategy.
    """
    if document_type == "cover_letter":
        return COVER_LETTER_STRATEGY.strip()

    # Map legacy strategy aliases
    normalized_strategy = strategy
    if strategy == "online_ats":
        normalized_strategy = "targeted_resume"
    elif strategy == "in_person":
        normalized_strategy = "networking_resume"
    elif strategy == "general":
        normalized_strategy = "targeted_resume"

    if normalized_strategy == "master_cv":
        return MASTER_CV_STRATEGY.strip()
    if normalized_strategy == "networking_resume":
        return NETWORKING_RESUME_STRATEGY.strip()
    if normalized_strategy == "generalist_online_resume":
        return GENERALIST_ONLINE_RESUME_STRATEGY.strip()
    # Default to targeted_resume
    return TARGETED_RESUME_STRATEGY.strip()
