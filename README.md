**AI Resume & Cover Letter Architect** is a privacy-first, automated career document generator. Instead of manually editing CVs, this system treats a professional's career history as a centralized NoSQL database (MongoDB). It uses a sequential dual-LLM architecture running entirely locally via Ollama:
- **The Reasoner (Llama 3.1):** Analyzes the target Job Description and cross-references it with the database to select the most relevant experiences, skills, and projects.
- **The Coder (Qwen 2.5 Coder):** Takes the filtered data and safely generates syntax-perfect LaTeX code.
- 
*The result is a hyper-targeted, ATS-friendly PDF resume and cover letter generated in minutes, with zero data sent to external cloud AI providers.*
