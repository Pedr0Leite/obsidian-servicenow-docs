<!-- Tracking note, not a source. Not meant for wiki ingestion — delete once fully resolved. -->

# URL fetch batch — 2026-07-23 (updated after browser retry)

Original batch of 27 URLs. First pass (CLI-only, `defuddle`/WebFetch, no browser) got 4. Second pass (`claude-in-chrome`, real logged-in-adjacent browser session, no login wall needed for any of them) resolved 18 more of the 22 that were CDN-blocked at the CLI level — confirming the block was tool-level (Akamai bot detection on non-browser HTTP clients), not a genuine login requirement.

## Resolved on retry (18) — now in raw/inbox/ as individual notes

- `in-product-experience-for-agentic-workflows` → `now-assist-in-product-experience-agentic-workflows.md` *(the original article that started this whole batch)*
- `ai-agents-hands-on-demo-setup-walkthrough` → `ai-agents-hands-on-demo-setup-walkthrough.md`
- `get-familiar-with-agentic-workflows-amp-ai-agent` → `get-familiar-with-agentic-workflows-ai-agents-lab.md`
- `bring-ai-agents-on-the-forms` → `bring-ai-agents-on-the-forms.md`
- `ai-agents-faq-and-troubleshooting` → `ai-agents-faq-and-troubleshooting.md`
- `limit-assist-consumption-by-designing-ai-agents-which-avoid` → `limit-assist-consumption-avoiding-loops.md`
- `ai-agent-tools-getting-the-most-out-of-your-agentic-workflows` → `ai-agent-tools-getting-most-out-of-agentic-workflows.md`
- `a-field-guide-to-evaluating-analyzing-and-debugging-ai-agents-on` → `field-guide-evaluating-debugging-ai-agents.md`
- `now-assist-for-csm-email-reply-recommendations` → `now-assist-for-csm-email-reply-recommendations.md`
- `now-assist-panel-error` → `now-assist-panel-error-plugin-sync.md`
- `accelerating-agent-responses-with-now-assist-s-activity-response` → `accelerating-agent-responses-activity-response-generation.md`
- `how-to-show-action-button-on-now-assist-chat-window` (+ the `now-assist-panel-get-help` URL, which redirected here) → `now-assist-forum-misc-threads.md`
- `now-assist-panel-not-functioning` → `now-assist-forum-misc-threads.md` (same file, second thread)
- `now-assist-context-menu-a-productivity-tool-within-servicenow` → `now-assist-context-menu-productivity-tool.md`
- `now-assist-faqs` → `now-assist-faqs-general.md`
- `ai-agents-and-3rd-party-integrations` → `ai-agents-3rd-party-integrations.md`
- `ai-agent-to-fetch-data-from-custom-table-and-return-couple` → `ai-agent-custom-table-fetch-va-forum.md`
- `ai-agents.html` (products page, was 403 via CLI) → `ai-agents-product-page.md`

## Genuinely dead / low-value — not captured, no note written

- `now-assist-panel-get-help/m-p/3524561` — redirected to the same content as `how-to-show-action-button-on-now-assist-chat-window` instead of loading distinct content. Broken/merged community link, not a separate source (noted inline in `now-assist-forum-misc-threads.md`).
- `now-assist/ct-p/now-assist` — category landing page, trivial content (just links out to an "AI Academy" teaser). Not worth a note.
- `docs/bundle/yokohama-intelligent-experiences/.../exploring-ai-agents.html` — dead link, ServiceNow's docs site silently redirects this old bundle URL to its own homepage (confirmed by full page render, not a fetch failure).
- `docs/r/intelligent-experiences/platform-approval-aia.html` — same dead-link pattern; loads only the site's global mega-menu nav, no article body.
- `docs/bundle/yokohama-conversational-interfaces/.../va-user-inputs.html` — different failure mode: page shell and sidebar navigation load correctly (correct title, correct doc-tree highlight), but the actual article content pane stays empty after 3 separate waits (up to ~13s). Possibly a genuine rendering bug on ServiceNow's docs site rather than a dead link — could be worth one more try later, but not chased further per the "don't loop on the same failure" rule.
- `slideshare.net/.../conversational-agents-building-intelligent-assistants...` — loaded fine, but it's a **UiPath Community** deck about UiPath's own Agentic Automation product, not ServiceNow. Out of scope for this vault; not captured.

## Summary

22 of 27 original URLs now captured (4 from the first CLI pass + 18 from the browser retry). 5 remain uncaptured: 3 genuinely dead ServiceNow docs pages, 1 broken/duplicate community link, 1 off-topic (UiPath) deck. Nothing further to chase automatically — the 3 dead docs pages would need their content found via search or an alternate URL if still wanted; the va-user-inputs rendering issue could be retried once, later, if that specific page's content becomes needed.
