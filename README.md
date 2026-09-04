# AI Resume & Cover Letter Architect

**AI Resume & Cover Letter Architect** is a privacy-first, automated career document generator. Instead of manually editing CVs, this system treats a professional's career history as a centralized NoSQL database (MongoDB). 

By leveraging a sequential dual-LLM architecture running entirely locally via Ollama, it ensures that your professional data never leaves your machine. 

## 🧠 Architecture

The system utilizes two specialized local models working in tandem:

1. **The Reasoner (Llama 3.1):** 
   Analyzes the target Job Description and cross-references it with your MongoDB career database to intelligently select the most relevant experiences, skills, and projects.
   
2. **The Coder (Qwen 2.5 Coder):** 
   Takes the filtered, hyper-relevant data and safely generates syntax-perfect LaTeX code.

## ✨ Features

- **Privacy-First:** 100% local execution using Ollama by default. Zero data is sent to external cloud AI providers.
- **Config-Driven Strategy:** AI models are decoupled from the agent logic. You can easily upgrade or swap providers (e.g., from Ollama to Gemini) by modifying the `.env` file and leveraging the `BaseAgent` interface.
- **Database-Driven:** Your career is a database. Update your MongoDB documents once, and generate infinite permutations of resumes.
- **Hyper-Targeted:** Every resume and cover letter is uniquely tailored to the specific job description provided.
- **ATS-Friendly:** Outputs high-quality, ATS-optimized PDF documents compiled via LaTeX.
- **Multilingual Support (i18n):** Native support for generating documents in multiple languages using localized fields in the database.

## 🛠️ Installation & Usage

### Prerequisites
- [Ollama](https://ollama.com/) installed and running locally.
- Models downloaded: `llama3.1` and `qwen2.5-coder:14b` (or `7b`).
- Python 3.10+
- MongoDB instance running (local or cloud).

### Setup
```bash
# Clone the repository and setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements (if any)
pip install ollama pymongo python-dotenv

# Set up your environment variables
cp .env.example .env
# Edit .env to add your MongoDB URI and set your preferred AI models.
# You can also configure OLLAMA_NUM_CTX in .env to balance memory usage 
# with context limits (e.g., set to 8192 or 4096).
```

### Run the CLI
You can generate either a resume or a cover letter, and optionally specify the language (defaults to `en`):
```bash
python src/main.py [document_type] [language]

# Examples:
python src/main.py resume en
python src/main.py cover_letter fr
```

The generated LaTeX and the compiled PDF will be saved in a timestamped, localized folder inside the `output/` directory (e.g., `output/2026-09-04_14-30-00_en_resume/`).

*The result is a hyper-targeted, ATS-friendly PDF resume and cover letter generated in minutes, with zero data sent to external cloud AI providers.*
