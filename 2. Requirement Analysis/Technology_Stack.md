# Technology Stack — EduGenie AI Assistant

| S.No | Architecture Component / Layer | Technology Chosen | Justification / Purpose |
|---|---|---|---|
| 1 | Frontend / Client-Side | HTML5, CSS3, Vanilla JavaScript (Fetch API) | Single-page "Study Workbook" needed no heavy framework; keeps bundle size minimal and load time fast for a study tool |
| 2 | Backend / Server-Side | Python, FastAPI, Uvicorn | Async-native, auto-generates OpenAPI docs, and integrates cleanly with both the Google Generative AI SDK and Hugging Face `transformers` |
| 3 | Database / Data Storage | SQLite via SQLAlchemy ORM | Zero-config file-based DB is sufficient for user/query/quiz records at this scale; SQLAlchemy allows a future swap to PostgreSQL with minimal code change |
| 4 | Cloud / Hosting / Deployment | Local Uvicorn server (dev); deployable to Render/Railway/AWS | Keeps development friction low; FastAPI apps deploy easily to any ASGI-compatible host |
| 5 | Version Control & CI/CD | Git + GitHub | Standard team collaboration workflow; enables code review and rollback |
| 6 | Third-Party APIs / Other Tools | Google Generative AI SDK (`gemini-2.5-flash`), Hugging Face `transformers` (`LaMini-Flan-T5-783M`), SMTP (Gmail) | Gemini provides high-quality reasoning for Q&A/summary/quiz/roadmap; local LaMini model removes API cost + latency for simple explanations; SMTP delivers OTP for secure signup |
