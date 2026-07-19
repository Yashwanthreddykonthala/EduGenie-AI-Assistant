# Phase 3: Detailed System Design, Data Flows, and UI/UX Engineering Architecture

## 1. Monolithic Modular Architecture Blueprint
EduGenie executes on a decoupled Single Page Application (SPA) system design philosophy. The execution architecture safely distinguishes between Local Inference pipelines (minimizing overhead and zeroing API costs) and Cloud Inference systems (for heavy natural language reasoning). 

```text
       ┌────────────────────────────────────────────────────────┐
       │             Web Browser UI ("Study Workbook")          │
       │        (HTML5 DOM Context / Asynchronous Fetch API)    │
       └───────────────────────────┬────────────────────────────┘
                                   │
                    HTTP Asynchronous Payloads (JSON Engine)
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │             FastAPI Application Core Router            │
       │                (Uvicorn Context Gateway)               │
       └─────┬────────────────────────────────────────────┬─────┘
             │                                            │
             │ Condition: Local Route                     │ Condition: Cloud Route
             ▼                                            ▼
┌───────────────────────────┐              ┌───────────────────────────┐
│    Local Inference Engine │              │   Cloud Inference Engine  │
├───────────────────────────┤              ├───────────────────────────┤
│ • Module: explanation.py  │              │ • Module: qna.py          │
│ • Model: LaMini-Flan-T5   │              │ • Module: summary_module  │
│ • Backend: Transformers   │              │ • Module: quiz_module     │
│ • Execution: Local CPU    │              │ • Module: learning_path   │
│ • Weights Cache: 3.13 GB  │              │ • Model: gemini-1.5-flash │
└───────────────────────────┘              └───────────────────────────┘

---

## 2. Module Decomposition & Technical Specification

The core execution engine is programmatically modularized into independent operational layers to ensure strict separation of concerns. Every logical file acts as an isolated subsystem driver:

### A. Local Edge Processing Layer
*   **`explanation_module.py`**: Interacts directly with the local Python `transformers` framework execution thread. It binds the initialization of the `LaMini-Flan-T5-783M` model weights directly to the host CPU/hardware memory pipeline on boot. It completely isolates text generation tasks from external internet interfaces, executing heavy topic breakdowns locally with zero token consumption.

### B. Cloud Reasoning Layer
*   **`qna.py`**: Controls active query streams directed to the remote cloud server endpoint. It manages immediate contextual factual validation pipelines utilizing the Google Generative AI platform instance.
*   **`summary_module.py`**: Processes heavy inbound paragraph sequences, parsing structural text segments down into optimized, low-density content summary strings.
*   **`quiz_module.py`**: Enforces advanced programmatic response shapes. It overrides standard LLM text loops, forcing the remote engine to return exact machine-parsable JSON string structures. It processes raw strings through a regex utility function (`clean_json_block`) before outputting lists to ensure the user interface never crashes.
*   **`learning_path.py`**: Generates multi-tier progressive learning paths by transforming complex target text properties into highly organized course outlines.

---

## 3. Asynchronous Data Flow Matrix (API Endpoint Contract)

The system communication pipeline relies entirely on strict, modern JSON payloads and explicit query parameter paths exchanging data over asynchronous HTTP networks:

| API Interface Route | HTTP Method Verb | Inbound Data Structure | Outbound Payload Shape | Internal Engine Dependency |
| :--- | :--- | :--- | :--- | :--- |
| `/qa` | `GET` | Query String: `?question=...` | Plain Text Output Block | Cloud `gemini-1.5-flash` Engine |
| `/explain` | `POST` | JSON Object: `{"topic": "..."}` | Formatted Explanatory Paragraph | Local `LaMini-Flan-T5-783M` Cache |
| `/summarize` | `POST` | JSON Object: `{"text": "..."}` | Bulleted Structural Text Points | Cloud `gemini-1.5-flash` Engine |
| `/quiz` | `POST` | JSON Object: `{"text": "..."}` | Deserialized Custom JSON Array | Cloud Engine via Strict RegEx Filter |
| `/learn/recommendations` | `GET` | Query String: `?topic=...` | Raw Title Markdown Document Stream | Cloud `gemini-1.5-flash` Engine |

---

## 4. UI/UX "Study Workbook" Design System Matrix

The presentation canvas models an accessible, high-contrast digital notebook layout, running entirely as a Single Page Application (SPA) driven by state transitions instead of browser page reloads.

### A. Style and Typography Architecture Tokens
*   **Canvas Grid Wallpaper (`--color-bg`):** Deep Navy Indigo Shade (`#16213E`) representing a focus-driven night-desk environment.
*   **Workbook Chapter Cards (`--color-paper`):** Warm parchment text-sheet layer (`#F7F1E3`) optimized for high readability.
*   **Typographic Highlighter Accent (`--color-gold`):** Vibrant gold tone (`#D9A441`) applied directly to interactive triggers and active header underlines.
*   **Core Font Interface Framework:** Dynamic Google Web Fonts bindings featuring `Lora` for elegant book-like title components, `Inter` for clean form input contexts, and `IBM Plex Mono` for raw data streaming blocks.

---

## 5. Security Filtering & Client-Side Formatting Engine

To guarantee complete execution safety and maintain presentation fidelity without installing heavy third-party parsing modules, raw data strings pass through a two-step transformation framework before being rendered into the browser DOM:

### Step 1: Security Hardening (XSS Prevention)
The script executes a dedicated `escapeHTML()` functional pass immediately on every raw incoming text parameter string. By converting characters like `<` and `>` into safe character entity references (`&lt;` and `&gt;`), it neutralizes malicious code injection risks.

### Step 2: Markdown Real-Time Translation Pipeline
The lightweight client-side parser (`renderMarkdownLite()`) dynamically scans the protected string layout array line-by-line using regular expression matching logic to swap text tokens on the fly:
*   Converts standard triple hash markers (`### Title Line`) directly into semantic HTML5 `<h5>` tags.
*   Converts standard double hash markers (`## Title Line`) directly into semantic HTML5 `<h4>` tags.
*   Detects bold notation structures (`**Target Text**`) and transforms them into standard typographic bold spans (`<strong>Target Text</strong>`).
*   Applies a final structural line join framework utilizing HTML `<br>` breaks to preserve paragraph formatting across parchment view sections.
