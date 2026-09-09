# CS9676678 — Related records search not indexed

**Priority:** 2 - High | **Status:** Work in Progress | **Last updated:** 2026-09-08

## Issue

The Related Records search contextual side panel shows "Search is unavailable for this list because it isn't indexed" and cannot be used to search related records on Cases. It affects SLA-related records, and separately, agents can no longer see Knowledge articles in related records either.

Related Record Definitions and Text Index configuration were already checked by Pedro and appeared fine. Regenerating the text index for the SLA table did not trigger any indexing activity.

**Business impact:** Agents cannot search SLA-related records or see Knowledge articles from the Related Records panel on Cases in production, reducing their ability to support cases effectively.

## Timeline

- **9/2 (7d ago)** — Case opened by Pedro Leite. Screenshot attached. Requested a call.
- **9/2** — Hal Motley (Support) acknowledged, confirmed understanding of the issue, and outlined next steps (call, review Related Record Definitions, text index config/health, indexing job logs, determine config vs. defect).
- **9/2** — Pedro requested a call the next day, 14:00–18:00 Lisbon time.
- **9/4 (5d ago)** — Pedro added: Knowledge articles also no longer show in related records.
- **9/8 (1d ago)** — Pedro flagged the case as urgent with no feedback yet.
- **9/8** — Tony Alldis (Sr. Technical Support Manager) apologized for inactivity and re-prioritized the case to P2 - High.
- **9/8** — Hal Motley confirmed he reproduced the issue in the CSM Configurable Workspace: SLA records display fine, but search on that list fails with the "not indexed" error. He compared the SLA related-records config against working searchable types and found differences. No production changes made. He is now engaging ServiceNow product specialists to determine if this is expected behavior or a defect.
- **Today (6h ago)** — Pedro asked Hal for an update.
- **Today (6h ago)** — Pedro clarified the main issue is that users no longer see Knowledge articles in related records at all.

## Current status

Awaiting response from ServiceNow product specialists on whether the SLA indexing behavior is expected or a defect. The Knowledge-articles-missing issue still needs to be addressed/reproduced by Support.
