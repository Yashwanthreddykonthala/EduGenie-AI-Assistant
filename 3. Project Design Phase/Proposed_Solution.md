# Proposed Solution — EduGenie AI Assistant

## Project Overview
| Field | Details |
|---|---|
| **Objective** | Deliver a unified, low-cost, resilient AI study assistant that handles explanation, Q&A, summarization, quiz generation, and learning-path planning in one workspace |
| **Scope** | Covers account creation (OTP-secured), five core AI study tools, and a single-page dark/light "Study Workbook" interface, backed by SQLite for persistence |

## Problem Statement
| Field | Details |
|---|---|
| **Description** | Students juggle multiple disconnected tools to explain, summarize, and quiz themselves on study material, while fully cloud-dependent AI tools add cost and fail offline |
| **Impact** | Fragmented workflow increases study time and cognitive load; cloud-only architecture increases operating cost and creates a single point of failure during outages |

## Proposed Solution
| Field | Details |
|---|---|
| **Approach** | Hybrid architecture: route lightweight/offline-friendly tasks (concept explanation) to a local transformer model, and route high-reasoning tasks (Q&A, summarization, quiz generation, roadmap planning) to a cloud LLM (Gemini 2.5 Flash) |
| **Key Features** | - OTP-secured signup/login<br>- Instant factual Q&A<br>- Zero-cost local concept explanations<br>- Text summarization<br>- Auto-generated, schema-validated MCQ quizzes<br>- Personalized adaptive learning roadmaps<br>- Dark/light glassmorphic single-page UI |

## Resource Requirements
| Resource Type | Description | Specification / Allocation |
|---|---|---|
| **Hardware — Computing** | CPU/GPU for local model inference | Standard CPU (Apple Silicon MPS acceleration supported); no dedicated GPU required |
| **Hardware — Memory** | RAM for local transformer weights | Minimum 4GB, 8GB recommended |
| **Hardware — Storage** | Disk space for model cache + DB | ~5GB (LaMini-Flan-T5-783M weights) + SQLite file |
| **Software — Framework** | Backend web framework | FastAPI + Uvicorn |
| **Software — Libraries** | Core Python dependencies | `transformers`, `google-generativeai`, `sqlalchemy`, `python-dotenv`, `passlib`/`hashlib` |
| **Software — Dev Environment** | IDE | VS Code / PyCharm |
| **Data** | Model source | Hugging Face Hub (`MBZUAI/LaMini-Flan-T5-783M`); Google Generative AI API (`gemini-2.5-flash`) |
