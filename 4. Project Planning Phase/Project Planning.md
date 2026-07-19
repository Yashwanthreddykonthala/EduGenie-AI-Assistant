# Phase 4: Comprehensive Project Planning, Gantt Scheduling, and Team WBS Matrix

## 1. Project Execution Methodology (Agile/Sprint Framework)
The EduGenie AI Assistant project was executed utilizing a tailored Agile-Scrum framework. The timeline was divided into distinct execution sprints spanning February 2026 to April 2026. This framework enabled the engineering team to iterate rapidly on core components, balance computing loads across local and cloud environments, and continuously deploy frontend changes without interrupting the core API router architecture.

---

## 2. Granular Work Breakdown Structure (WBS) Matrix

To ensure absolute system stability and optimize individual developer output, the project architecture was decomposed into discrete modular assignments. Every component was tracked under formal milestones:

| Milestone ID | Software Engineering Task Segment | Primary Assigned Developer | Operational Scope & Metrics | Current Status |
| :--- | :--- | :--- | :--- | :--- |
| **M1: Architecture Baseline** | Environment Configuration & Secure Sandbox Architecture | **Velamala Preetham** (Lead) | • Isolated runtime generation via Python `venv`. <br>• Strict packaging configurations inside `requirements.txt`. <br>• Abstract configurations mapping variable objects dynamically from `.env`. | **Completed** |
| **M2: Edge Core Model** | Local Transformer Architecture & Storage Cache Engineering | **Konathala Divyateja** | • Formulating pipeline routines utilizing `transformers`. <br>• Resolving first-run cache verification hooks for `LaMini-Flan-T5-783M`. <br>• Hardening model execution pipelines to run local text on CPU loops. | **Completed** |
| **M3: Intelligence Layer** | Cloud Reasoning Module Engineering & Schema Binding | **Pavan Kumar Reddy Yerram** | • Orchestrating `qna.py` functional connections. <br>• Designing robust prompt wrappers to structure cloud data output layers. <br>• Formatting JSON matrix configurations within the quiz builder pipeline. | **Completed** |
| **M4: Core Backend Assembly** | API Routing Infrastructure & Controller Layer Construction | **Gandepalli Radha Krishna** | • Mapping text processing arrays into unified operational pathways in `main.py`. <br>• Organizing individual route controllers (`/qa`, `/explain`, `/summarize`). <br>• Configuring static asset directory pathways. | **Completed** |
| **M5: Interface Layer** | Frontend Workbook Workspace Architecture & Theme Styling | **Yashwanth Reddy Konthala** | • Designing a single-page application canvas using modern CSS tokens. <br>• Crafting the academic "Study Workbook" motif frame layout. <br>• Constructing asynchronous client-side Fetch API integration handlers. | **Completed** |
| **M6: Verification & Release** | Security Auditing, Markdown Optimization & Main Release | **All Hands Collaboration** | • Implementing client-side scripting validation routines (`escapeHTML`). <br>• Injecting live regex conversion pipelines (`renderMarkdownLite`). <br>• Compiling repository release documentation rules. | **Completed** |

---

## 3. Critical Path Timeline & Sprint Schedules

The software development lifecycle was precisely mapped across three key sprints to transition the project from raw ideation to a ready-to-deploy release asset:

### Sprint 1: Architecture Inception & Core Scoping (Feb 1, 2026 – Feb 28, 2026)
*   **Deliverables:** Requirement analysis validation, technology stack evaluation, initial configuration of local execution pipelines, and coordination of professional scripts for promotional outreach via club platforms.
*   **Milestone Target:** Successful verification of local machine capability to host and load deep transformer model weights (LaMini-Flan) into working hardware memory.

### Sprint 2: Core Engineering & Algorithmic Design (Mar 1, 2026 – Mar 31, 2026)
*   **Deliverables:** Functional implementation of all AI modules (`qna.py`, `quiz_module.py`, `summary_module.py`), establishing secret parameters configurations, and establishing text extraction logic loops inside backend files.
*   **Milestone Target:** Zero exceptions generated during internal integration tests between individual Python script processes and external cloud processing frameworks.

### Sprint 3: UI Polishing, Testing, and Repo Freezing (Apr 1, 2026 – Apr 30, 2026)
*   **Deliverables:** Full execution of UI style guidelines, deploying asynchronous frontend loop mechanics, fixing directory path mismatches, adding regex filters to display clean HTML blocks, and compiling final release assets.
*   **Milestone Target:** Seamless execution of the local web app on a public browser interface with no formatting breakages or unhandled errors.

---

## 4. Risk Management, Technical Debt, and Live Sprint Pivots

During active integration sprints, the project encountered critical technical bottlenecks. The table below documents the engineering challenges faced and the programmatic adjustments implemented to preserve system stability:

### Risk 1: Cloud Service 404 Endpoint Failure Matrix
*   **Root Cause Analysis:** Initial implementation calls targeting the baseline `gemini-1.5-pro` identifier threw persistent `404 Not Found` errors due to recent endpoint restriction modifications on the public developer v1beta gateway.
*   **Engineering Resolution:** Executed a comprehensive backend refactoring cycle across all core modules (`qna.py`, `quiz_module.py`, `summary_module.py`, `learning_path.py`), replacing the target configuration string with the stable, high-performance `gemini-1.5-flash` model instance.

### Risk 2: File System Directory Pathing Resolution Crash
*   **Root Cause Analysis:** The application router experienced immediate application crashes at execution runtime, surfacing a critical `jinja2.exceptions.TemplateNotFound: 'index.html'` error. The asset tree layout structure mapped a singular `template/` path, while internal FastAPI directory conventions strictly require a pluralized configuration layout structure.
*   **Engineering Resolution:** Restructured the local layout file tree, renaming the folder to `templates/` and re-indexing the stylesheet path context to reside safely under a dedicated `static/` structural asset layer.

### Risk 3: Raw Markdown Syntax DOM Rendering Defects
*   **Root Cause Analysis:** Dynamic model outputs containing standard markdown markers (e.g., `## Header Content` or `**Bold Text**`) were injected directly into the DOM container as unparsed literal text blocks, diminishing visual quality and creating potential Cross-Site Scripting (XSS) script entry points.
*   **Engineering Resolution:** Engineered a custom, lightweight rendering script (`renderMarkdownLite`) on the frontend to parse raw data streams line-by-line using regular expressions, while nesting every output variable securely behind an automated `escapeHTML()` verification layer to sanitize user code inputs.
