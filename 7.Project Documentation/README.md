# EduGenie Learning Assistant

> A premium, hybrid AI-powered educational assistant structured to streamline learning workflows. EduGenie provides dynamic question answering, long-form concept explanations, document summarization, interactive quiz validation, and personalized adaptive learning path recommendations—all delivered via a stunning dark/light glassmorphic single-page workspace.

---

## 1. Project Summary

EduGenie integrates cloud intelligence (**Gemini 2.5 Flash**) and local edge processing (**LaMini-Flan-T5-783M**) to deliver high-performance study tools while maintaining absolute data security, zero-cost scaling, and complete cross-device accessibility:

| # | Tool | Engine Used | Execution Layer | Endpoint |
|---|---|---|---|---|
| **1** | Factual Q&A | Gemini 2.5 Flash | Cloud (Generative AI SDK) | `GET /qa` |
| **2** | Concept Explanation | LaMini-Flan-T5-783M | Local CPU (Hugging Face) | `POST /explain/` |
| **3** | Text Summarization | Gemini 2.5 Flash | Cloud (Generative AI SDK) | `POST /summarize/` |
| **4** | MCQ Quiz Builder | Gemini 2.5 Flash | Cloud (Dynamic JSON Schema) | `POST /quiz` |
| **5** | Adaptive Roadmaps | Gemini 2.5 Flash | Cloud (Generative AI SDK) | `GET /learn/recommendations` |

The project uses a structured, modular FastAPI package layout configured inside the **`5. Project Development Phase`** directory.

---

## 2. Directory Layout & Repository Structure

Following the track template guidelines, the repository is organized into distinct project lifecycle phases:

```
EduGenie-AI-Assistant/
├── 1. Brainstorming & Ideation/     # Detailed project proposal
├── 2. Requirement Analysis/         # Software Requirements Specification (SRS)
├── 3. Project Design Phase/         # Architecture models, wireframes & schemas
├── 4. Project Planning Phase/       # Milestones scheduling & team WBS matrices
│
├── 5. Project Development Phase/    # CENTRAL CODEBASE
│   ├── app/                         # Modular application packages
│   │   ├── api/                     # Controller routes routers
│   │   │   ├── auth.py              # OTP Sign Up, Login, and Guest handlers
│   │   │   └── study.py             # Q&A, Summaries, Quizzes, roadmaps endpoints
│   │   ├── core/                    # Specialized AI logic wrappers
│   │   │   ├── explanation.py       # Local transformer setup
│   │   │   ├── qna.py               # Cloud Q&A driver
│   │   │   ├── quiz.py              # Quiz prompt engineering
│   │   │   ├── learning.py          # Roadmap generator
│   │   │   └── summary.py           # Summarizer driver
│   │   ├── database.py              # SQLite session connection provider
│   │   └── models.py                # Database entity schemas (Users, Queries, Quizzes)
│   │
│   ├── static/                      # Custom dark/light mode stylesheets
│   │   └── style.css
│   ├── templates/                   # Client-side workbook workspaces
│   │   └── index.html
│   │
│   ├── main.py                      # FastAPI startup entry point
│   ├── requirements.txt             # Python dependencies
│   └── .env                         # API & Mail credentials (git-ignored)
│
├── 6.Project Testing/               # QA test suite cases and bug reports
├── 7.Project Documentation/         # API guides and user manuals
├── 8.Project Demonstration/         # Slides, presentation assets & demo links
│
├── .gitignore                       # Structured Git ignore file
└── README.md                        # Project documentation (this file)
```

---

## 3. Technology Stack

*   **Backend Core Engine:** Python 3.9+ / FastAPI / Uvicorn
*   **Database ORM:** SQLAlchemy (SQLite Engine)
*   **Security & Auth:** Secure SHA-256 Hashing / SMTP-based 6-digit OTP delivery with a 10-minute expiry
*   **Client Viewport:** Single Page HTML5 / CSS3 Dark-Light Glassmorphic theme / Vanilla JS Asynchronous Fetch
*   **Cloud Processing:** Google Generative AI SDK (`gemini-2.5-flash` model)
*   **Local Processing:** Hugging Face `transformers` library (`LaMini-Flan-T5-783M` text-to-text token model)

---

## 4. Local Execution & Set Up

### Step 1: Open the Development Directory
All runnable source code assets reside inside the Phase 5 directory. Open your terminal and navigate to it:
```bash
cd "5. Project Development Phase"
```

### Step 2: Create a Virtual Environment
Initialize a clean Python virtual environment to manage dependencies safely:
```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Package Dependencies
Install the required packages listed in the requirements file:
```bash
pip install -r requirements.txt
```
*(First-time runs of the local explanation tool will automatically fetch the ~3GB model weights for `MBZUAI/LaMini-Flan-T5-783M` from Hugging Face Hub).*

### Step 4: Configure the Environment Secrets
Create a file named `.env` in the `5. Project Development Phase/` directory. Specify your access credentials:
```env
# Gemini API Key (obtain from Google AI Studio)
GEMINI_API_KEY=your_gemini_api_key_here

# SMTP configuration for email verification OTPs
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_gmail_address@gmail.com
SMTP_PASSWORD=your_gmail_app_password
```

### Step 5: Boot the Server
Start the Uvicorn hot-reload server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Open **`http://127.0.0.1:8000`** in your browser. You can also view it on mobile devices connected to your local network by opening `http://your-local-ip:8000`.

---

## 5. Team & Engineering Credits

| Phase Milestone Module | Lead Assigned Engineer |
|---|---|
| **Architecture Sandbox & Environments** | Velamala Preetham |
| **Local Inference Optimization** | Konathala Divyateja |
| **Cloud Reasoning Prompting & Quizzes** | Pavan Kumar Reddy Yerram |
| **FastAPI Core Routing & Databases** | Gandepalli Radha Krishna |
| **UI Design, Glassmorphism & Themes** | Yashwanth Reddy Konthala |
