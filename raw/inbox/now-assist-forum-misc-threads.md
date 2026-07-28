<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Two short forum threads bundled together — both low individual content but worth keeping. -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Now Assist forum — misc threads

## Thread 1: How to show action button on Now Assist chat window (unresolved)

Source: https://www.servicenow.com/community/now-assist-forum/how-to-show-action-button-on-now-assist-chat-window/m-p/3491042

prashantkulkarn, Tera Contributor — 02-17-2026

Has an Agentic Workflow calling multiple AI Agents, working fine when inputs are typed into Now Assist. Wants to instead show clickable action buttons in the chat window itself (not a form UI action) — e.g. for a custom work order table: "Summarize Work Order", "Add Labor Entry to Work Order", "Close Work Order" as buttons the user clicks rather than typing.

Reply (Tanushree Maiti, Tera Patron): pointed to the general "Now Assist panel | Overview" documentation link — no specific mechanism given.

Follow-up (rpriyadarshy): reports the suggested approach did not make the buttons appear.

**Status: unresolved as of fetch** — no working solution found in-thread for buttons *inside* the chat window (distinct from a form UI action button, which IS a documented pattern — see `bring-ai-agents-on-the-forms.md` in this same batch).

0 Helpfuls · 747 Views

---

Note: a second URL in the original batch (`now-assist-panel-get-help/m-p/3524561`) redirected back to this exact same thread rather than loading distinct content — likely a broken/merged community link, not a separate source.

## Thread 2: Now Assist Panel not functioning (solved)

Source: https://www.servicenow.com/community/now-assist-forum/now-assist-panel-not-functioning/m-p/3287877

Rami_Joulani, Tera Expert — 06-12-2025

**Problem**: Now Assist installed (many ITSM/HRSD/Creator/Platform plugins, skills activated, no issue), but activating the Now Assist Panel and following documented setup steps produces a "duplicate keys" error when activating skills in the panel — duplicate rows identified as empty, though they aren't.

**Accepted solution (anubhavkapoor76, ServiceNow Employee)**:
> Navigate to the `sn_nowassist_skill_config_status` table. Verify there are no duplicate records for NAVA-related skills (e.g., "Now Assist Topics"). If duplicates exist, delete the most recently created record.

Additional troubleshooting offered (Dexter Chan, ServiceNow Employee): double-check AI Search is installed; confirm NAP is activated in Now Assist Admin Console > Now Assist Experiences.

3 Helpfuls (on solution) · 4,884 Views

## Why this might matter to this vault

Thread 2 gives a second concrete, distinct root cause for "blank/malfunctioning NAP" beyond plugin-version drift (see `now-assist-panel-error-plugin-sync.md`): **duplicate records in `sn_nowassist_skill_config_status`**, fixable by deleting the most recent duplicate. Worth adding to a "NAP troubleshooting checklist" if one gets written for [[Proactive Customer Case Communicator]]. Thread 1 confirms in-chat action buttons (as opposed to form-level UI actions) aren't a solved/documented pattern yet — relevant if either PCCC or [[partner-case-summary-agent]] ever wants NAP-native buttons rather than a plain conversational or form-UI-action entry point.
