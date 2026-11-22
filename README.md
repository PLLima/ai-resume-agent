# AI Resume & Cover Letter Architect

**AI Resume & Cover Letter Architect** is a privacy-first, automated career document generator. Instead of manually editing CVs, this system treats a professional's career history as a centralized NoSQL database (MongoDB). 

By leveraging a sequential dual-LLM pipeline running locally via Ollama, professional data remains entirely within your local environment.

## 🧠 Architecture

The system utilizes two specialized models operating in sequence:

1. **The Reasoner (Llama 3.1):** 
   Analyzes the target Job Description and cross-references it with your MongoDB career database to select the relevant experiences, skills, and projects. It outputs a structured blueprint tagging each entry as either `[TARGET MATCH]` or `[SECONDARY ENTRY]`, enforcing strategy-specific cardinality limits (e.g., Continental 1-flagship budgets).
   
2. **The Coder (Qwen 2.5 Coder):** 
   Consumes the Reasoner's tagged blueprint and filtered JSON data to generate compilable LaTeX code based on dynamic strategy rules and configurable profile photo assets (`{profile_photo_filename}`).

## 📑 5-Tier Document Ecosystem

The architecture supports five distinct document strategies:

1. **Master CV (`master_cv`):** Comprehensive reference containing all career data without omissions. Unconstrained by page limits; uses anti-chronological sorting, page-break controls (`\needspace`), and `ProfilePhoto.jpg`.
2. **Targeted Resume (`targeted_resume`):** Strict 1-page ATS-optimized resume tailored to a job posting. Adheres to geographical standard budgets (Continental 1-flagship entry vs. Anglo-Saxon metric density) and defaults to `ProfilePhoto_light.jpg`.
3. **Networking Resume (`networking_resume`):** Strict 1-page condensed resume designed for in-person events and career fairs. Employs modular en-dash summaries, single-bullet STAR descriptions (`briefDescription`), and excludes achievements to preserve vertical space.
4. **Generalist Online Resume (`generalist_online_resume`):** Strict 1-page baseline for portfolio website downloads. Selects exactly 3 experiences and 3 projects with `briefDescription`, using `ProfilePhoto_light.jpg` for minimal payload.
5. **Cover Letter (`cover_letter`):** Tailored 1-page cover letter matching job requirements and company profile, with digital signature integration (`Signature.pdf`).

## ✨ Features

- **Privacy-First:** Local execution using Ollama by default. Zero data transmission to external cloud AI providers.
- **Config-Driven Strategy:** AI models are decoupled from agent logic via the `BaseAgent` interface, allowing provider transitions (e.g., Ollama, Gemini) via `.env`. The prompt engine dynamically applies linguistic, typographical, and structural rules per document type and strategy.
- **Configurable Photo Assets:** Strategy-aware profile image selection between high-resolution `ProfilePhoto.jpg` (archival/print) and lightweight `ProfilePhoto_light.jpg` (ATS portals and web downloads).
- **Geographical Standard Adaptation:** Dynamic switching between Anglo-Saxon Standard (no photograph, no personal details, no interests, aggressive metric focus) and Continental Standard (circular photo, FontAwesome icons, mandatory interests section, compact spacing).
- **Database-Driven:** Career records are stored as structured MongoDB documents. Update once, generate any resume permutation.
- **Multilingual Support (i18n):** Native support for generating documents in multiple languages (English, French, Portuguese) using localized fields from the database with strict grammatical and typographical enforcement.

## 🛠️ Installation & Usage

### Prerequisites
- [Ollama](https://ollama.com/) installed and running locally.
- Models downloaded: `llama3.1` and `qwen2.5-coder:14b` (or `7b`).
- Python 3.10+
- MongoDB instance running (local or cloud).
- `pdflatex` installed (e.g., TeX Live or MacTeX).

### Setup
```bash
# Clone the repository and setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Set up your environment variables
cp .env.example .env
# Edit .env to add your MongoDB URI and set your preferred AI models.
# You can also configure OLLAMA_NUM_CTX in .env to balance memory usage 
# with context limits (e.g., set to 8192 or 4096).
```

### Run the CLI
Generate resumes or cover letters with optional target parameters, strategies, and profile photo assets:
```bash
python src/main.py [document_type] [language] --role [role] --company [company] --country [country] --strategy [strategy] --profile-photo [asset]

# Examples:
# Targeted ATS Resume (Default strategy)
python src/main.py resume en --role software-engineer --company amazon --country germany --strategy targeted_resume

# Networking In-Person Resume
python src/main.py resume en --strategy networking_resume

# Master Reference CV
python src/main.py resume en --strategy master_cv --profile-photo ProfilePhoto.jpg

# Generalist Online Resume (Web Download)
python src/main.py resume en --strategy generalist_online_resume --profile-photo ProfilePhoto_light.jpg

# Tailored Cover Letter
python src/main.py cover_letter fr --role data-scientist --company google --country france
```

The generated LaTeX source and compiled PDF are saved in a Cloudinary-compatible, language-aware folder structure inside `output/` (e.g., `output/resumes/en/2026-09-04_14-30-00_software-engineer_amazon_germany_en_resume.pdf`).

## 🐛 Troubleshooting

### VS Code Pyrefly / Pylance Missing Imports
If VS Code displays import errors for `ollama`, `pymongo`, or `dotenv`, verify that the editor uses the virtual environment interpreter:
1. Ensure `.venv` exists in the repository root.
2. Open the Command Palette (`Ctrl+Shift+P`).
3. Select **Python: Select Interpreter** and point to `./.venv/bin/python`.
4. Reload the window (**Developer: Reload Window**).
