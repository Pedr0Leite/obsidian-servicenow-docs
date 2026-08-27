---
aliases:
  - "Bring AI Agents on the Forms"
area: "AI & VA"
source: raw-inbox
tags:
  - ai-agents
  - agentic-workflow
  - ui
  - forum
---

<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-forum/bring-ai-agents-on-the-forms/m-p/3405557 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Bring AI Agents on the Forms (forum thread)

ameybhaisar, Tera Contributor — 10-15-2025

**Question**: We have OOB Skills and Agentic Workflows enabled. Typing a prompt in Now Assist chat (e.g. "Generate Post Incident Review for INC000001") gives the right output. New requirement: instead of manually typing a prompt, can we give the user a button that triggers this automatically? (Referenced screenshot shows a button appearing for a "summarize incident" skill.) Is it possible for other Agentic Workflows/Agents like "Generate Post Incident Review"?

## Accepted-style answers

**Me Being Mustaq (Kilo Sage)**: Yes — possible via UI Actions (buttons), Script Includes, APIs, or Flow Designer actions, just like the OOB "Summarize" skill button.

- **UI Actions (Buttons)**: add a custom UI Action to the incident form/workspace, configured via server-side scripts or Flow Designer to call the Agentic Workflow for the current record. ServiceNow allows triggering AI Agent/Agentic Workflow programmatically via script or API with the right permissions.
- **Agentic Workflow Configuration**: in Agentic Workflow Studio, define custom triggers — record-based, schedule-based, or manual (e.g. from a button).
- **Workspace or Now Assist Panel**: in UI Builder, reconfigure the workspace to add/position the Agentic Workflow's trigger UI.

**rpriyadarshy**: points to a related thread "Trigger options for Agentic Workflow or AI Agent" and confirms triggering via a button.

**Paulsylo (Tera Sage)**: confirms enabling "get Post incident review" Agent gives this functionality via UI action — but raises a design question: "if you are doing this through button, are you defying the purpose of AI agent, losing the autonomous way of working and introducing tech debt?"

**Christian R**: reports triggering the agentic workflow from a UI button works in **Classic UI** but not from **Workspace** — asks for advice (unresolved as of fetch).

0 Helpfuls · 3,093 Views

## Why this might matter to this vault

Directly answers the surfacing question already resolved in [[partner-case-summary-agent-architecture]] §7 (NAP conversational primary + Agent Workspace UI action as secondary/fallback) — confirms UI actions triggering Agentic Workflows/AI Agents is a supported, real pattern, matching PCCC's own UI-action-based approach. **Flag**: the unresolved Classic-UI-works-but-Workspace-doesn't report from Christian R is worth checking if the Partner Case Summary Agent's UI action fallback ends up targeting Workspace specifically — this thread suggests that combination may have known issues.
