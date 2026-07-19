# Communication — EduGenie AI Assistant

## Communication Plan

| S.No | Communication Type     | Frequency | Channel / Tool            | Participants                 | Purpose                                                                     |
| ---- | ---------------------- | --------- | ------------------------- | ---------------------------- | --------------------------------------------------------------------------- |
| 1    | Team Standup           | Daily     | WhatsApp / Discord        | All 5 team members           | Quick status check, blockers                                                |
| 2    | Progress Update        | Weekly    | Google Meet               | All 5 team members           | Review sprint progress against backlog                                      |
| 3    | Issue / Bug Discussion | As Needed | GitHub Issues + team chat | Relevant module owner(s)     | Diagnose and assign bug fixes (e.g., the Gemini 404 and template-path bugs) |
| 4    | Stakeholder Review     | Bi-Weekly | Google Meet               | Full team + mentor/evaluator | Demo progress, gather feedback                                              |
| 5    | Final Demo Rehearsal   | Once      | In-person / Google Meet   | All 5 team members           | Practice full demo flow before submission                                   |

## Communication Challenges & Resolutions

| S.No | Challenge Faced                                                                                          | Resolution / Action Taken                                                                                                    |
| ---- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1    | Coordinating across local (offline model) and cloud (API) module owners when the Gemini 404 bug appeared | Held an ad-hoc sync call; root-caused to a deprecated model string and standardized on `gemini-2.5-flash` across all modules |
| 2    | Frontend/backend mismatch on the `templates/` folder path caused confusion during integration            | Backend and frontend owners paired directly to resolve the Jinja2 path issue rather than debugging separately                |
