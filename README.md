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

- **Privacy-First:** 100% local execution using Ollama. Zero data is sent to external cloud AI providers.
- **Database-Driven:** Your career is a database. Update your MongoDB documents once, and generate infinite permutations of resumes.
- **Hyper-Targeted:** Every resume and cover letter is uniquely tailored to the specific job description provided.
- **ATS-Friendly:** Outputs high-quality, ATS-optimized PDF documents compiled via LaTeX.
- **Multilingual Support (i18n):** Native support for generating documents in multiple languages using localized fields in the database.

*The result is a hyper-targeted, ATS-friendly PDF resume and cover letter generated in minutes, with zero data sent to external cloud AI providers.*
