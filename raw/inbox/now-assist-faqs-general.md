<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/now-assist-faqs/ta-p/2685122 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->
<!-- Long-running FAQ, originally 09-2023, last edited 12-2025. General Now Assist product FAQ (not AI-Agent-specific — see the separate "ai-agents-faq-and-troubleshooting.md" for that). -->

# Now Assist FAQs

Eliza, ServiceNow Employee — originally 09-29-2023, updated to 12-13-2025 (by Victor Chen)

## What is Now Assist?
Generative-AI-driven solutions/workflows ServiceNow delivers to drive productivity and intelligent work/employee experience.

## Product list (as of Yokohama)
Now Assist for Creator, ITSM, HRSD, CSM, FSM, ITOM, SPM, IRM, and more — full list in the ServiceNow store.

## Own LLM subscription (Azure OpenAI etc.)?
Most customers rely on ServiceNow's NowLLM Service. OEM models (Claude, Azure OpenAI, Gemini) also available via the model provider flexibility framework. Custom skills via Skill Kit / Generative AI Controller can use your own LLM provider subscription (separate charges may apply).

## Commercial model
Contact account rep for Now Assist + Pro Plus/Enterprise Plus licensing. Consumption measured in **assists** — different skills/uses consume different numbers. Rate card: ServiceNow Assist Overview.

## More LLM providers planned?
Two vehicles: (1) OOTB skills (Now LLM + OEM: Gemini, Azure OpenAI, Claude as of Yokohama Patch 6/July 2025); (2) custom workflows via Generative AI Controller/Skill Kit, connectable to external LLMs via spoke or generic LLM connector.

## Countries/languages
All Now Platform countries. Natively supported by Now LLM: English, Spanish, Japanese, French, German, Italian, Brazilian Portuguese, Dutch, Canadian French. Other languages via Dynamic Translation (OOB translation service provided free when used only for Now Assist). Custom Skill Kit/Generative AI Controller use cases connecting external LLMs may support other languages per that LLM's own support.

## FedRAMP/GCC
Yes, since June 2024 — subset of features unavailable, check with account rep.

## On-premises/self-hosting
Yes — AWS, GCP, or Azure infra required. Whitelisting for image/model file download: log a Support Case assigned to 'Generative AI Operationalization' team (KB1647748).

## Domain separation
Yes for most Now Assist features — see the dedicated Domain Separation FAQ, plus product-specific guidance for Now Assist Admin, Generative AI Controller, AI Search.

## PDI availability
No, Now Assist apps not enabled on PDIs.

## Performance metrics/SLAs
None currently published — varies by use/customer.

## "Can't install a Now Assist plugin"
Ensure Pro Plus/Enterprise Plus entitlement + latest instance version. Only install/update the "Now Assist for X (BU)" store app — don't install Generative AI Controller/Skills/Spokes individually. Use Now Assist admin console to activate skills first; if Plugins manager is missing plugins, click "Sync" (top right) or use Classic App Manager view.

## Now LLM model card
Available in ServiceNow documentation.

## Single-product licensing (only ITSM or only HRSD) + shared VA/AI Search
Recommendation: maintain separate requestor experiences. Create a custom role for licensed agents, assign fulfiller seats only to licensed number. On requestor/portal side: use Now Assist in Search/VA on a department portal with relevant filters (Category/Org), use "Exclude in Now Assist Genius Results" for sources belonging to the unlicensed org; limit summaries/catalog to licensed content ("Turn off Now Assist conversation for this item" field on catalog items).

## Assist charging on provider error
OOTB NowLLM skills: no assist charged on error (including Guardian-triggered blocks). 3rd-party OEM calls (e.g. Skill Kit evaluation): no assist charged on error. Custom Skill Kit/Generative AI Controller skills using 3rd-party LLMs: no assist charged on error, but 3rd-party LLM may still bill per their own licensing.

## Different results: NA in VA vs. NA in Search (portal)
Ensure plugins up to date; re-index AI Search sources; ensure the VA search profile matches the portal search profile (Portals > Search Application); or use "Copy existing configuration" on the NA in VA setup page (Assistants > Information Sources) to copy the portal's profile over.

## Notable comment thread highlights

- **Language support clarified (Victor Chen)**: officially completely limited to English for the interface; the LLM *may* summarize non-English content but quality is unverified.
- **Assists and Integration Hub "double dipping"**: NA products use a separate Assists pool from Integration Hub transactions (not double-charged).
- **Azure OpenAI GenAI Controller model deployment naming**: a user (Tomas14) reported the controller was hardcoded to the `gpt-35-turbo` deployment name — no resolution shown in-thread.
- **Assist token overage**: 1 assist per call; calls exceeding 1,000 output tokens consume additional assists (Victor Chen: e.g. a 3,000-token cap still charges exactly 3 assists, not a different ratio).
- **Finding underlying assist-consumption data (Marc54)**: `sn_entitlement_genai_assist_counts` gives an aggregate view; no answer given for the underlying per-call table (this is answered more precisely in `field-guide-evaluating-debugging-ai-agents.md`'s Usage layer section: `sys_gen_ai_usage_log`).
- **Testing/sub-prod assist charges (cajimenezps)**: confirmed — yes, charged for actions in lower environments too.
- **SPM Pro Plus requirement**: confirmed yes, required for Now Assist for SPM.
- **Token limit increase beyond 15,000 (vishokmohan)**: some flexibility exists for input vs. response token split on custom skills; otherwise recommended to switch to a higher-context LLM. Points to support KB2038552 for details.

40 Helpfuls · 89,514 Views

## Why this might matter to this vault

General product-level FAQ, mostly licensing/commercial/language scope rather than technical architecture — lower direct relevance to [[Proactive Customer Case Communicator]] or [[partner-case-summary-agent]] than the other articles in this batch, but useful background: confirms assists aren't charged on errors (relevant when estimating Partner Case Summary Agent's cost footprint for "not found"/ACL-denied lookups), and that PDIs can't be used for Now Assist testing at all (only sub-prod/scoped-prod, consistent with what both agents' test plans already assume).
