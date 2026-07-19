# No. of Functional Features Included in the Solution — EduGenie AI Assistant

## Functional Features Overview

| S.No | Feature Name | Feature Description | Module/Component | Status (Done/In Progress/Pending) | Marks Contribution |
|---|---|---|---|---|---|
| 1 | OTP Signup | Register with name/email/password, verify via emailed 6-digit OTP (10-min expiry) | `auth.py` | Done | High |
| 2 | Login / Guest Login | Log in with credentials, or continue as guest without an account | `auth.py` | Done | High |
| 3 | Factual Q&A | Ask a direct question, get a cloud-generated factual answer | `qna.py`, `/qa` | Done | High |
| 4 | Concept Explanation | Get a step-by-step topic explanation from a locally-run model (zero API cost) | `explanation.py`, `/explain/` | Done | High |
| 5 | Text Summarization | Paste long text, receive a structured concise summary | `summary.py`, `/summarize/` | Done | High |
| 6 | MCQ Quiz Generation | Auto-generate a schema-validated multiple-choice quiz from any text | `quiz.py`, `/quiz` | Done | High |
| 7 | Adaptive Learning Roadmap | Get a personalized study roadmap for any topic | `learning.py`, `/learn/recommendations` | Done | Medium |
| 8 | Dark/Light Theme UI | Toggle between glassmorphic dark and light interface themes | `style.css`, `index.html` | Done | Low |

## Feature Summary

| Metric | Count / Value |
|---|---|
| Total Features Planned | 8 |
| Total Features Implemented | 8 |
| Core / Must-Have Features | 6 (Signup, Login, Q&A, Explanation, Summary, Quiz) |
| Additional / Nice-to-Have Features | 2 (Roadmap, Theme toggle) |
| Features Tested & Verified | 8 (see `6.Project Testing/Testing_Report.md`) |

## Feature Category Breakdown

| S.No | Category | Features in Category | Example Features |
|---|---|---|---|
| 1 | User Interface (UI) | 2 | Study Workbook layout, dark/light theme toggle |
| 2 | Backend / Logic | 5 | Q&A, Explanation, Summary, Quiz, Roadmap generation |
| 3 | Database / Storage | 1 (cross-cutting) | User/Query/Response/Quiz/Summary/LearningPath persistence via SQLAlchemy |
| 4 | API / Integration | 2 | Google Generative AI SDK (Gemini), Hugging Face `transformers` (LaMini-Flan-T5) |
| 5 | Security / Authentication | 3 | OTP verification, password hashing, XSS input escaping |
