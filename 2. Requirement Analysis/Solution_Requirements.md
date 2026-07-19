# Solution Requirements — EduGenie AI Assistant

## Step 1: Functional Requirements (FR)

| S.No | Requirement Category | Requirement Description | Priority |
|---|---|---|---|
| 1 | Authentication | Users register with email + password; identity is verified via a 6-digit OTP sent by SMTP, expiring after 10 minutes | High |
| 2 | Authorization | Two roles: registered user (full history/persistence) and guest (session-only, no saved history) | Medium |
| 3 | External Interfaces | Integrates with Google Generative AI SDK (Gemini 2.5 Flash) for cloud reasoning and Hugging Face `transformers` for local inference | High |
| 4 | Transactions | Each study interaction (Q&A, explanation, summary, quiz, roadmap) is processed synchronously and logged to the database | High |
| 5 | Reporting | Quiz results are scored and displayed immediately; users can view a history of past queries | Medium |
| 6 | Business rules | Local model is used only for `/explain`; all JSON-structured outputs (quizzes) must pass schema validation before reaching the UI | High |
| 7 | Compliance to laws/regulations | No personal data beyond email is stored; API keys are isolated via `.env` and never committed to source control | Medium |
| 8 | Other | Client-side markdown rendering (`renderMarkdownLite`) converts model output into readable HTML safely | Low |

## Step 2: Non-Functional Requirements (NFR)

| S.No | NFR Category | Requirement Description | Target Metric / Acceptance Criteria |
|---|---|---|---|
| 1 | Performance & Speed | Cloud responses should return quickly; local responses should begin rendering promptly on modest hardware | Cloud call ≤ 3000ms timeout; local response starts within 5s on 4GB RAM |
| 2 | Scalability | System should tolerate growth in concurrent study sessions without major refactor | Stateless API routes; DB layer swappable from SQLite to PostgreSQL |
| 3 | Security & Data Privacy | Credentials and API keys must never be hardcoded or exposed to the client | Passwords hashed (SHA-256); secrets loaded only from `.env`; XSS input escaped |
| 4 | Reliability & Availability | Core study features should remain usable even if the cloud API is temporarily unavailable | `/explain` (local) works fully offline; graceful error messages for cloud failures |
| 5 | Usability & Accessibility | Interface should be readable and comfortable for extended study sessions | Dark/Light theme toggle; high-contrast "Study Workbook" typography |
| 6 | Other (Maintainability) | Each AI capability should be isolated so it can be modified independently | Modular file-per-feature structure (`qna.py`, `quiz.py`, `summary.py`, `learning.py`, `explanation.py`) |
