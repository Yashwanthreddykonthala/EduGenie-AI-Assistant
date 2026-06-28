# EduGenie Learning Assistant

> A lightweight, AI-powered educational assistant that helps students, self-learners, and educators understand concepts, get quick answers, generate quizzes, summarize material, and receive personalized learning roadmaps — all from a single page, with no page reloads.

---

## 1. Project Summary

EduGenie combines a cloud LLM (**Gemini 1.5 Pro**) with a local, CPU-friendly model (**LaMini-Flan-T5-783M**) to deliver five focused study tools through one FastAPI backend and a single-page frontend:

| # | Tool | Model Used | Route |
|---|------|-----------|-------|
| 1 | Q&A | Gemini 1.5 Pro | `GET /qa` |
| 2 | Topic Explanation | LaMini-Flan-T5-783M (local) | `POST /explain` |
| 3 | Text Summarization | Gemini 1.5 Pro | `POST /summarize` |
| 4 | Quiz Generation | Gemini 1.5 Pro | `POST /quiz` |
| 5 | Learning Path / Roadmap | Gemini 1.5 Pro | `GET /learn/recommendations` |

The hybrid AI strategy keeps the app responsive and cost-efficient: routine explanation requests run locally and offline-capable, while tasks that benefit from stronger reasoning (Q&A, summarization, quiz generation, roadmap planning) call out to Gemini 1.5 Pro.

**Design goal:** make learning interactive, accessible, and efficient across academic levels, while running comfortably on resource-constrained hardware (Intel i3/i5+, 4GB+ RAM, Mac M1 included).

---

## 2. Tech Stack

| Layer | Technology |
|---|---|
| Backend Framework | Python 3.10+, FastAPI, Uvicorn (ASGI server) |
| Frontend | HTML5, CSS3 (animations), Jinja2 templating, vanilla JavaScript (Fetch API) |
| Cloud AI Model | Google Gemini 1.5 Pro (`google-generativeai` SDK) |
| Local AI Model | LaMini-Flan-T5-783M (Hugging Face `transformers` + CPU `torch`) |
| Database | SQL — PostgreSQL or SQLite (via SQLAlchemy) |
| Config Management | `python-dotenv` |
| Tooling | VS Code, Git, GitHub |

**Minimum hardware:** Intel i3/i5 or equivalent, 4GB RAM (8GB recommended), 10GB free storage (for local model weights + dependencies).

---

## 3. Modular Folder Architecture

```
edugenie/
├── main.py                    # FastAPI app: routes, static/template mounting
├── requirements.txt           # Python dependency list
├── .env                       # GEMINI_API_KEY (not committed to Git)
├── .gitignore
│
├── qna.py                     # Q&A module        -> Gemini 1.5 Pro
├── explanation_module.py      # Explanation module -> LaMini-Flan-T5-783M (local)
├── summary_module.py          # Summary module     -> Gemini 1.5 Pro
├── quiz_module.py             # Quiz module        -> Gemini 1.5 Pro + JSON parsing
├── learning_path.py           # Learning path module -> Gemini 1.5 Pro
│
├── templates/
│   └── index.html             # Single-page frontend (5 tool sections + JS)
│
└── static/
    └── style.css               # "Study Workbook" theme stylesheet
```

Each AI module is self-contained: it loads its own `.env` config, initializes its own model client, and exposes one public function (`explain_topic`, `answer_question_with_gemini`, `summarize_text`, `generate_quiz`, `get_learning_recommendations`). `main.py` imports these functions directly and never talks to the models itself — keeping routing and AI logic cleanly separated.

---

## 4. Installation (Virtual Environment, via VS Code)

### Step 1 — Clone / open the project folder in VS Code

```bash
cd path/to/edugenie
code .
```

### Step 2 — Create a virtual environment

Open the VS Code integrated terminal (`` Ctrl+` `` / `` Cmd+` ``) and run:

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Once active, your terminal prompt should be prefixed with `(venv)`.

> **VS Code tip:** After creating the venv, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) → **"Python: Select Interpreter"** → choose the interpreter inside `./venv` so linting, debugging, and the integrated terminal all use the same environment.

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

> **Apple Silicon (M1/M2) note:** `requirements.txt` pins a `+cpu` torch build intended for x86 machines. On Apple Silicon, instead run:
> ```bash
> pip install torch torchvision torchaudio
> ```
> then install the rest of `requirements.txt` as usual — the default PyPI torch build already runs on M1/M2 via the MPS backend.

### Step 4 — Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Each AI module (`qna.py`, `summary_module.py`, `quiz_module.py`, `learning_path.py`) reads this key independently via `python-dotenv`, and will raise a clear `EnvironmentError` at startup if it's missing.

### Step 5 — First-run note on the local model

The first time the app starts, `explanation_module.py` will download **MBZUAI/LaMini-Flan-T5-783M** (~3GB) from the Hugging Face Hub and cache it locally. This can take a few minutes depending on your connection; subsequent runs load instantly from cache.

---

## 5. Running the Server Locally

With the virtual environment active and dependencies installed:

```bash
uvicorn main:app --reload
```

- `--reload` enables hot-reloading on code changes (development only — omit it in production).
- The app will be available at: **http://127.0.0.1:8000**

Open that URL in your browser to use all five tools from the single-page interface. No page reloads occur during use — all forms submit asynchronously via the Fetch API.

### Quick sanity check

If the server starts without errors and the workbook-themed homepage renders with all five chapters (Q&A, Explanation, Summarization, Quiz, Learning Path), your setup is complete.

---

## 6. Project Stats

- **Epics:** 8
- **Tasks:** 11
- **Core Entities (ER Model):** USER, USER_QUERY, AI_RESPONSE, QUIZ, SUMMARY, LEARNING_PATH

---

## 7. Team & Credits

| Role | Name |
|---|---|
| **Team Lead** | Velamala Preetham |
| Member | Konathala Divyateja |
| Member | Pavan Kumar Reddy Yerram |
| Member | Gandepalli Radha Krishna |
| Member | Yashwanth Reddy Konthala |

Built with care by the EduGenie team as a modular, resource-conscious learning assistant — designed to run efficiently on everyday student hardware while still leveraging state-of-the-art generative AI where it matters most.

---

## 8. License

*Add your chosen license here (e.g. MIT, Apache 2.0) before publishing this repository publicly.*
