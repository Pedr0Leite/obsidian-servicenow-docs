<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/now-assist-context-menu-a-productivity-tool-within-servicenow/ta-p/3545940 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Now Assist Context Menu: A Productivity Tool Within ServiceNow

Juhi Poddar, Kilo Patron — 05-19-2026

Available since Yokohama, but many teams don't realize what it does. A Now Assist icon appears in text fields when composing content — click for AI-powered writing assistance that already understands case context (no copy-pasting to ChatGPT needed).

## Three capabilities

1. **Summarization** of complex cases — click "Summarize" at top of form → structured summary with 4 sections: Issue, Key Actions Taken, Resolution, Service Level Agreement. Includes feedback buttons and an accuracy reminder.
2. **Email drafting** based on case details — sparkle icon appears when typing in the email field. Popup shows page navigation (e.g. 1/6), Replace button, feedback, Copy, Refine dropdown — draggable/resizable so agents can review while keeping case info visible.
3. **Content refinement** — Refine → "Shorten" or "Elaborate" to adjust generated content.

## Common Questions

- **"Why not use ChatGPT?"** ChatGPT can't access ServiceNow data; Context Menu already has case context.
- **"What if it makes mistakes?"** Every output includes accuracy reminders; Replace button ensures review before use.
- **"Will it replace agents?"** No — it helps with writing, not judgment/problem-solving/customer relationships.

## Enable & Use

**Admins**: install plugin from ServiceNow Store; activate skills in Now Assist Admin → Skills; configure role-based access (which roles use which skills); enable analytics tracking.

**Users**: click Summarize at top of case; start typing in email field, click sparkle icon; use Refine to adjust; provide feedback.

Note: Context Menu appears automatically in standard ServiceNow workspaces. For custom workspaces, may need manual addition in UI Builder.

## Productivity Impact (author's figures)

Summarizing a complex case: 8-10 minutes → 30 seconds. Writing a professional email: 10-15 minutes → 2-3 minutes of review/personalization.

3 Helpfuls · 859 Views

## Why this might matter to this vault

This is the OOB, generic version of the same "summarize case + draft communication, human reviews before it goes out" pattern that [[Proactive Customer Case Communicator]] custom-builds with deterministic routing/templates instead of free-form Context Menu prompts. Also directly relevant background for [[partner-case-summary-agent]] — confirms case summarization inside a workspace is an established, already-adopted UX pattern (not a novel ask), which supports the story's "low navigation skill" design goal.
