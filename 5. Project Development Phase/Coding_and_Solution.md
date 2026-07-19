# Coding & Solution — EduGenie AI Assistant

## Solution Summary

| Field | Details |
|---|---|
| Repository Link / URL | *[Paste your GitHub repo URL here]* |
| Programming Language(s) | Python, JavaScript, HTML, CSS |
| Framework(s) Used | FastAPI, Uvicorn, SQLAlchemy, Jinja2 |
| Key Features Implemented | OTP-secured signup/login, guest login, cloud Q&A, local concept explanation, text summarization, MCQ quiz generation (schema-validated), adaptive learning roadmap, dark/light theme UI, XSS-safe markdown rendering |
| Pending / Incomplete Features | *[List anything not fully finished — e.g., password reset flow, quiz result history dashboard, if applicable]* |
| Setup / Run Instructions | See `README.md` → Section 4 ("Local Execution & Set Up"): create venv → `pip install -r requirements.txt` → configure `.env` → `uvicorn main:app --reload` |

## Code Quality Checklist

| S.No | Criteria | Status (Yes/No) |
|---|---|---|
| 1 | Code is modular and organized into functions/classes | Yes |
| 2 | Meaningful variable and function names are used | Yes |
| 3 | Code includes comments/documentation where necessary | Partial — see Code-Layout doc for detail |
| 4 | Error handling is implemented for critical operations | Yes — DB sessions, missing env vars, invalid OTP/login all handled |
| 5 | The application runs without critical errors | Yes (validated in Testing_Report.md) |
| 6 | Code is committed to a version control repository | Yes — Git repository present |

## Additional Notes / Comments
The application follows a hybrid inference design: cost-sensitive/offline-friendly tasks run on a local Hugging Face model, while reasoning-heavy tasks call Gemini 2.5 Flash. All user interactions are persisted to SQLite via SQLAlchemy for later retrieval/history features.
