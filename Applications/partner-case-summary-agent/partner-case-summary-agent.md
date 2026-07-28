---
title: Partner Case Summary Agent (Story)
tags:
  - servicenow
  - now-assist
  - ai-agent
  - csm
  - virtual-agent
  - internal-tool
  - proposed
aliases:
  - Partner Case Summary Agent
  - AI Agent for Customer Active Case Summaries
status: proposed
date: 2026-07-22
---

# Partner Case Summary Agent (Story)

> [!info] Status
> **Proposed** — no build has started. This note captures the refined story only. Nothing in ServiceNow (AI Agent, tools, roles) exists yet for this.

## Origin

Originally requested as a Microsoft Copilot Studio agent connected to ServiceNow via its native connector (Partner Manager org wanted case connection details to configure that connector). Refined to drop Copilot Studio entirely and rebuild the same capability as a ServiceNow-native [[na-ai-agents|Now Assist AI Agent]] instead — no external Microsoft-side dependency, no connector credentials to manage.

## Story

**As a** Partner Manager
**I want** to look up a specific ServiceNow case or all active cases for a client account and get a short AI-generated summary of each (status, next steps, blockers) — entirely inside ServiceNow
**So that** I can walk into partner engagements with quick, accurate visibility into ongoing issues, without needing deep ServiceNow navigation skills or a separate Microsoft Copilot Studio agent

## Description

Replaces the original Copilot Studio connector request. Business need is unchanged, but everything now runs inside ServiceNow — no external Microsoft-side agent, no connector config. A Now Assist AI Agent ([[na-ai-agents|ReAct framework]]) performs the retrieval and summarization; the Partner Manager interacts with it conversationally rather than through a table/list view.

## Acceptance Criteria

- [ ] Given a case number, the agent retrieves that case from `sn_customerservice_case` and returns a 2–3 line summary (current status, next steps, blockers)
- [ ] Given a client/account name, the agent retrieves all active cases for that account and returns a 2–3 line summary for each, presented as one consolidated list
- [ ] "Active" = standard active/open state field on `sn_customerservice_case`, excluding closed/cancelled/resolved
- [ ] Summaries are generated from real case data (short description, work notes/activity, state, assignment) — not fabricated content
- [ ] No list/filter navigation is required — a natural-language ask (e.g. "show me open cases for Acme Corp") triggers both flows
- [ ] Only the 5 named users (or their assigned role) can invoke the agent, and only see cases they're already authorized to view under existing case ACLs
- [ ] No Microsoft Copilot Studio connector, connection details, or external agent configuration is created or exposed as part of this work
- [ ] Test user (`andreea.ionescu@unit4.com`) validates both flows end-to-end in sub-prod or scoped prod

## Business Justification

Supports Partner Managers during partner engagements by providing quick access to case information, improving visibility of ongoing issues, and enabling more informed discussions — delivered without introducing an external Microsoft-side dependency or additional connector/security surface.

## Users

- andreea.ionescu@unit4.com — **test user**, already has ServiceNow access
- andy.christenson@unit4.com
- elsa.granzow@unit4.com
- eva.beltowska@unit4.com
- henric.ceder@unit4.com

All confirmed active Unit4 employees.

## ServiceNow Implementation Notes

- **AI Agent (ReAct), two tools:**
  - **"Get Case Summary"** — case number → `GlideRecord` lookup on `sn_customerservice_case` → 2–3 line summary (status, next steps, blockers)
  - **"Get Active Cases for Account"** — account → query `sn_customerservice_case` filtered by `account` reference field + `active=true` (excluding closed/cancelled/resolved) → invokes Tool 1's summarization per matching case → consolidated list
- **Table:** `sn_customerservice_case` (CSM) — **locked**, confirmed as the target table
- **Surfacing:** [[virtual-agent|Virtual Agent]] / [[Now Assist Panel]] conversational entry point — fits the "low navigation skill" requirement better than requiring a list/filter. An Agent Workspace UI action could exist as a secondary path for power users, but the primary entry point should stay conversational.
- **Security:**
  - Dedicated role scoped to the 5 named users (e.g. a custom role assigned only to them), rather than opening the agent broadly
  - Agent must respect existing `sn_customerservice_case` ACLs — no privilege escalation via the agent; it only summarizes cases the invoking user is already authorized to see
  - Standard ServiceNow login only — no external OAuth/connector credentials to manage or rotate (a direct security simplification vs. the original Copilot Studio approach)
  - Log/audit AI Agent tool invocations (which cases were summarized, by whom) for traceability, consistent with standard Now Assist governance practice
- **Removed from scope:** all Copilot Studio connector/config details (client ID/secret, OAuth endpoint, connector setup) — no longer applicable

**Story points:** 8
**Priority:** High

## Open Questions

- ~~Role vs. group-based access design for the 5 named users~~ — resolved in [[partner-case-summary-agent-architecture|Architecture §6]]: dedicated role, direct assignment to the 5 named users (not a group), role gates agent invocation only (not table-level ACLs).
- ~~Virtual Agent / Now Assist Panel licensing availability in the target instance (Agent Workspace UI action as fallback if not)~~ — resolved in [[partner-case-summary-agent-architecture|Architecture §7]]: NAP conversational entry as primary (VA topic as equivalent alternative), Agent Workspace UI action as documented fallback; licensing confirmation is a pre-build verification step since PCCC already runs NAP on this instance.

## Related

- [[partner-case-summary-agent-architecture]] — full technical design: tools, Script Include, ACL/role, surfacing decision, dev build order
- [[partner-case-summary-agent-test-plan]] — test plan traced to these acceptance criteria
- [[Proactive Customer Case Communicator]] — sibling Now Assist AI Agent solution on the same `sn_customerservice_case` table, similar human-in-the-loop / case-summarization pattern, worth comparing tool design against
- [[na-ai-agents|Now Assist AI agents]]
- [[Now Assist Panel]]

#servicenow #now-assist #ai-agent #csm #proposed
