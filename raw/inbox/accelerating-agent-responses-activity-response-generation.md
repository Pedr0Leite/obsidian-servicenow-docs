<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/accelerating-agent-responses-with-now-assist-s-activity-response/ta-p/3489063 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Accelerating Agent Responses with Now Assist's Activity Response Generation

Dexter Chan, ServiceNow Employee — 02-13-2026, edited 02-25-2026

**Problem**: customer service/IT tier agents facing complex cases with dozens of updates spend valuable time scrolling activity streams before crafting responses — context switching delays responses, creates inconsistent handoffs.

**Solution**: Activity Response Generation analyzes the entire case history via the activity stream and suggests contextually appropriate responses at that specific moment.

## Common Use Cases

- **Agent handoff** — summarize all actions taken when transferring a ticket, so the receiving agent has full context without reading the whole history
- **Customer acknowledgement** — professional acknowledgments when a customer submits info
- **Proactive follow-ups** — reminder messages when waiting on info/action items
- **Ticket communications** — respond to multiple customers quickly with full context, without sacrificing professionalism

## Prerequisites

- ServiceNow release: Zurich patch 4 or higher
- Now Assist Admin Console: store app v7.0.8+ (as of Feb 2026)
- Now Assist for Platform: store app v10.0.3+
- Platform AI Agents and Skills: store app v10.9.7+

(Always install the latest version.)

2 Helpfuls · 943 Views

## Why this might matter to this vault

Directly relevant to [[Proactive Customer Case Communicator]]'s "worknote summarization" and dedup logic (§4–5 of that architecture note) — this is the OOB skill version of the same "read the whole activity/journal history and produce a contextual summary" capability PCCC re-implements custom via `caseUpdateAgentUtil`'s journal-mining. Worth checking whether PCCC could have used this OOB skill as a tool instead of reimplementing worknote-history parsing from scratch — though PCCC's need (deterministic dedup against prior AI comments, not just "summarize the thread") likely still requires the custom logic.
