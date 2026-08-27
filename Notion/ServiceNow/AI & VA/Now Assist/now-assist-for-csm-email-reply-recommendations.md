---
aliases:
  - "Now Assist for CSM - Email Reply Recommendations"
area: "AI & VA"
source: raw-inbox
tags:
  - now-assist
  - csm
  - email
  - generative-ai
---

<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/csm-articles/now-assist-for-csm-email-reply-recommendations/ta-p/3345499 (redirected to "servicenow-otto-for-csm-email-reply-recommendations" — rebranding) -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# ServiceNow Otto for CSM - Email reply recommendations

FernandoCastro, ServiceNow Employee — 08-06-2025, edited "Wednesday" (recent)

Note: title/URL shows the "Now Assist" → "ServiceNow Otto" rebrand mid-flight (URL slug still says now-assist, page title already says Otto).

**Email Reply Recommendations** is a generative AI skill providing suggested responses during customer email interactions — analyzes case context, email thread, and customer history to draft reply suggestions. Agents review, edit, and send.

## Key Capabilities

- **Context-Aware Email Suggestions** — draft replies from email thread + related customer info. Actions: review/choose KB article snippets highlighted on generated responses; refine (elaborate/shorten/change tone); leverage email template recommendations.
- **Editable Reply Drafts** — suggestions are editable before sending.
- **Integration with Workspace Email panel** — appears in CSM Configurable Workspace email interface, via the Now Assist Context Menu icon.
- **Controlled Activation and Permissions** — admins configure access by role/case criteria via Now Assist Admin Console.

## Implementation

Prerequisites: Enable Now Assist for CSM; AI Search; Email Recommendation skill; use CSM Configurable Workspace (email interaction view); configure the Email reply recommendations skill (customize similar to Case Summarization).

## Best Practices

- Agents review and personalize each suggestion before sending
- Set up email templates beforehand
- Use keyboard shortcut `/r` for adoption
- Train agents to check tone, accuracy, policy compliance
- Role-based access: trusted agents free use, restrict newer agents
- Monitor suggestion acceptance/feedback/fallback via Now Assist Admin Console

## Measured Success

| Outcome | Benefit | Key Metric |
|---|---|---|
| Shorter email response time | Pre-drafted content | Average time to send email |
| Consistent email quality | Templates/tone maintain standards | % replies using suggestion drafts |
| Reduced agent fatigue | Less repeated writing | Hours saved per agent per week |
| Better customer feedback | Faster/accurate responses | CSAT / customer feedback |
| Agent confidence increase | Comfortable replying to unfamiliar issues | Agent satisfaction survey |

## FAQ

- **Where do suggestions appear?** Email tab/modal of CSM Configurable Workspace, via Now Assist icon.
- **Can agents modify and use templates?** Yes, all recommendations are editable drafts using pre-set templates.
- **What information generates the reply?** Email thread history, case details, customer info, relevant knowledge.
- **Portal/customer-facing availability?** No — agent-facing CSM Configurable Workspace only.
- **Can admins control when shown?** Yes — skill visibility, trigger points, role/context access via Now Assist Admin Console.

0 Helpfuls · 3,871 Views

## Why this might matter to this vault

Same "draft → agent reviews/edits/sends" pattern as [[Proactive Customer Case Communicator]]'s Approve/Modify/Reject loop, but for **inbound** email replies rather than **outbound** proactive updates — worth comparing if PCCC's draft-review UX is ever redesigned. Confirms the "Now Assist" → "ServiceNow Otto" rebrand is actively in progress on the ServiceNow Community site itself (title/URL mismatch), consistent with the branding note already captured in `servicenow-sdk-building-ai-agents-guide.md`.
