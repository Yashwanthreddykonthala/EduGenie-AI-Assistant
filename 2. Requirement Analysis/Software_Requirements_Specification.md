# Phase 2: Software Requirements Specification (SRS) Document

## 1. Introduction & Project Scope
This SRS document outlines the structural framework, functional modules, and hardware constraints governing the EduGenie AI Assistant application. The system delivers lightweight, secure, and resilient artificial intelligence modules via a clean FastAPI server structure.

## 2. System Users & Target Audience
* **Students & Self-Learners:** Users seeking fast automated notes extraction, immediate academic question-answering, and direct concept cross-examination.
* **Educators:** Teachers requiring immediate creation of clean multi-option evaluation quizzes (MCQs) mapped out from baseline reading passages.

## 3. Detailed Functional Requirements
* **FR-1 (Q&A Framework):** The system must expose an asynchronous asynchronous GET route (`/qa`) that passes string parameters directly into the cloud processing layer and returns rapid factual text.
* **FR-2 (Local Compute Execution):** The system must dynamically bind local hardware configurations (CPU or Mac Silicon Apple GPU acceleration via `device="mps"`) at initialization time to run offline text explanations smoothly.
* **FR-3 (Strict Schema Quiz Extraction):** The quiz component must filter input streams, query the cloud model under strict schema templates, apply regular expression boundary stripping (`clean_json_block`) via `re.sub`, and successfully deserialize string matrices into local Python list dictionaries using `json.loads()`.
* **FR-4 (Secure Environment Isolation):** The application framework must reject manual API credential tracking. It must crash loudly at startup (`raise EnvironmentError`) if an isolated `.env` configuration mapping for the target `GEMINI_API_KEY` properties is missing.

## 4. Non-Functional Requirements
* **Performance:** Local model text response generation must begin rendering within 5 seconds on machines equipped with at least 4GB of RAM. Cloud interactions must feature timeout boundaries maxing out at 3000ms.
* **Security:** Complete input sanitization layer (`escapeHTML()`) applied to raw model string injections on the client-side browser to neutralize Cross-Site Scripting (XSS) vectors.
* **Maintainability:** Pure modular design principles where every AI processing stream operates independently (`qna.py`, `explanation_module.py`, `quiz_module.py`, `summary_module.py`, `learning_path.py`).