# Customer Journey Map — EduGenie AI Assistant

| Phase of Journey | Stage 1: Discovery & Sign-Up | Stage 2: Active Study Session | Stage 3: Review & Planning |
|---|---|---|---|
| **Actions** | • Finds EduGenie link/app<br>• Signs up via email<br>• Verifies account with OTP | • Pastes a topic/passage<br>• Requests explanation, summary, or quiz<br>• Answers the generated MCQs | • Reviews quiz score<br>• Requests a learning roadmap for a new skill<br>• Toggles dark/light theme for comfort |
| **Touchpoint** | Sign-up form → SMTP OTP email → Login screen | Study Workbook UI (`/explain`, `/summarize`, `/quiz` endpoints) | Roadmap panel (`/learn/recommendations`), quiz results panel |
| **Customer Thought** | "I hope this doesn't take long to set up." | "Is this actually going to save me time?" | "What should I study next to keep improving?" |
| **Customer Feeling** | Slightly cautious, hopeful | Focused, relieved once the answer/quiz appears quickly | Motivated, more in control of their study plan |
| **Process Ownership** | Auth module (`auth.py`) — OTP generation & verification | Core AI modules (`qna.py`, `explanation.py`, `quiz.py`, `summary.py`) | Learning roadmap module (`learning.py`) |
| **Opportunities** | • Add social/SSO login to reduce sign-up friction<br>• Shorten OTP delivery time | • Add response streaming so long answers don't feel like a wait<br>• Cache repeated local-model explanations | • Let users save/export their roadmap<br>• Add progress tracking across sessions |
