# Phase 1: Brainstorming & Ideation - Detailed Project Proposal

## 1. Project Overview & Motivation
EduGenie is an advanced, single-page hybrid AI educational assistant designed to streamline the learning workflow for students, professionals, and educators. In the modern learning environment, users constantly switch between disparate tools to ask questions, summarize long research text, generate assessment quizzes, and create structured learning paths. EduGenie unifies these fragmented workflows into a high-performance "Study Workbook" conceptual framework.

## 2. Problem Statement
* **Information Overload:** Students spend excessive time manually parsing dense textbooks and online documentation to extract core concepts.
* **Prohibitive Cloud Costs & Latency:** Relying entirely on heavy cloud-based LLM APIs for minor tasks (like generating long text explanations) drastically increases token expenditure and introduces network latency bottlenecks.
* **Lack of Local Resilience:** Complete reliance on internet-dependent cloud endpoints leaves users stranded during network outages.

## 3. The Proposed Solution (Hybrid Architecture)
EduGenie solves these issues by partitioning computing tasks across two distinct artificial intelligence boundaries:
1. **Cloud Intelligence Layer (High Reasoning):** Utilizes Google's `gemini-1.5-flash` model via the official Google Generative AI SDK to handle advanced analytical workflows—such as dynamic JSON array parsing for interactive quizzes, algorithmic roadmap planning, and instant factual Q&A handling.
2. **Local Edge Computing Layer (Privacy & Cost-Free):** Deploys the lightweight `LaMini-Flan-T5-783M` text-to-text transformer model locally on the user's system machine. It runs completely offline on local CPU/MPS hardware to process heavy conceptual definitions and step-by-step topic breakdowns with zero API operational costs.

## 4. Competitive Advantage & Market Value
Unlike generic chatbots, EduGenie features zero-configuration structured markdown rendering directly in the browser, multi-token fallback error tracking systems, and direct structural output constraints that guarantee valid data shapes (like pure JSON arrays for quizzes) without frontend crashes.