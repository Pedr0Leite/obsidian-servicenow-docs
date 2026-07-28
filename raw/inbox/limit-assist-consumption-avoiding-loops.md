<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/ceg-ai-coe-articles/limit-assist-consumption-by-designing-ai-agents-which-avoid/ta-p/3450013 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# Limit Assist Consumption by Designing AI Agents which Avoid Loops

TJL, ServiceNow Employee (AI Center of Excellence) — 12-15-2025, edited 01-12-2026

Three complementary loop-prevention strategies: (1) trigger configuration, (2) filter condition patterns, (3) built-in recursive-check properties as safeguards.

## Part 1 — Trigger Configuration

Trigger types: Record-Based (On Created / On Updated / On Created and Updated), Time-Based (Scheduled: Daily/Weekly/Monthly), Application-Based (Inbound Email).

**A common loop scenario**: an AI Agent adds a resolution plan to an incident's work notes, using both "On Record Created" and "On Record Updated" triggers without proper filters:
1. New incident creation fires the AI Agent
2. Agent adds resolution plan to work notes
3. Updating work notes fires the "On Record Updated" trigger
4. Agent invoked again, adds another plan
5. Loop continues

**Legitimate multi-trigger use case**: refiring when the employee adds clarifying info, as long as filter conditions prevent loops (see Part 2).

**Inbound Email + Create/Update triggers**: avoid combining — an email creating/updating a record can fire both triggers, causing duplicate executions.

**Scheduled triggers**: use for agents analyzing data across multiple records (e.g. detecting a pattern of VPN incidents to flag as a major incident candidate). Do NOT loop within the Agentic Workflow itself — use a scheduled Flow/script (API Pathway) for looping, calling the workflow per record.

## Part 2 — Trigger Condition Filters

A filter like "Active is True AND State is Work in Progress" can loop forever if the agent's own action (logging to work notes) doesn't change `state` — the condition stays true, retriggering continuously. Ensure your AI Agent modifies a field that causes the "Record Updated" trigger's filter to resolve false.

**Recommended pattern — Assignment Group**: assign the record to a group with virtual workers → filter activates AI Agents only for that group → agent tool reassigns to a group with human fulfillers → agent adds recommendations to work notes → assignment-group change makes the trigger condition false, preventing retriggering.

Benefits: no custom fields required; ServiceNow auto-records assignment group changes (audit trail); existing AWA/Predictive Intelligence rules can be reused for reassigning to human fulfillers.

**Alternative — Custom True/False Flag**: a simple boolean field indicating the AI Agent already processed the record. Avoid modifying OOB State selections since other Now Assist skills leverage State.

## Part 3 — Built-in Recursive-Check Properties

Found in the `sn_aia_property` list.

- **Create Record check** (`recursive_check.query_for_create_record`) — batch/API pathway scenario, counts invocations to reach the same objective. Default max: **50 executions** (`recursive_check.create_max_executions`) within a **15-minute window** (`recursive_check.create_time_window`). Example: 60 records created yesterday via batch → 50 processed, 10 left unprocessed if invoked within the window.
- **Update Record check** (`recursive_check.query_for_update_record`) — identifies an "On Record Update" trigger whose filter still resolves true after the agent's own update, firing perpetually. Default max: **5 executions** (`recursive_check.update_max_executions`) within a **15-minute window** (`recursive_check.update_time_window`). Example: filter `Active=True AND State IN (New, Work in Progress)` on both Created and Updated triggers — adding a resolution plan on creation updates the record, second trigger resolves true, agent runs 5 times then is rate-limited.

Recursive loops occur for **autonomous** AI Agents only — supervised tools require human approval for certain steps (fulfiller/requester interaction in NAP or NA for VA), which breaks the loop.

**Quick reference**: Create Record Check — 50 executions / 15 min — scheduled triggers processing batches, Flows using AI Agents. Update Record Check — 5 executions / 15 min — On Record Update triggers, On Record Created-and-Updated (monitors the update portion).

**Version requirement**: if these properties aren't visible, upgrade `sn_aia` to v4.0.38+ (Xanadu Patch 9+, Yokohama Patch 3+, Zurich releases).

## Monitoring for Loops

AI Agent Studio > Status tab (Realtime Monitoring: execution plans/executions and status over time) and Assist Consumption tab (graphical Assist trend, top 10 workflows by Assist consumption, per-workflow/agent counts).

**Warning signs**: a single-agent test showing multiple invocations via Status dashboard; sudden Assist consumption spike; one workflow/agent consuming unusually high Assists.

## Production Checklist

- AI Agent modifies the loop-breaking field (Assignment Group or custom flag) early in execution
- Tested with 5–10 records in sub-production
- Verified recursive properties exist (`sn_aia` v4.0.38+)
- Quantified expected Assist consumption rate

## What if I already have a loop in production? (emergency steps)

1. **Deactivate the trigger immediately** — AI Agent Studio > Create and Manage > find agent/workflow > Trigger tab > set Inactive or delete
2. **Check for active executions** — `sn_aia_execution_plan` table, sort Created newest→oldest, filter State = In Progress, cancel stuck executions
3. **Analyze the cause** — which fields does the agent update; do those updates satisfy trigger conditions; why didn't conditions resolve FALSE
4. **Redesign and test** — add a loop-breaking filter condition (Part 2), test with 5–10 records in sub-production, verify resolved before re-enabling

## Notable comment (governor/alerting)

- **lomo1014** asked for a governor/monitor sending alerts on a consumption threshold. TJL replied: in Zurich there's an OOB email notification "[AIA] AI Agent assist spike" that fires when Assist consumption exceeds **5,000 assists in a 3-hour window** with **>50% growth vs. the prior equivalent window** — enable the notification for these defaults out of the box.
- **vasavisasap** asked about limiting per-human-agent token consumption. TJL: not quite the same lever, but `sys_one_extend_rate_limit_rules` can limit request counts per capability/LLM provider, instance-wide or per-user — an *approximation* of Assist consumption, not a direct 1:1 cap.

7 Helpfuls · 6,992 Views

## Why this might matter to this vault

Directly extends [[Proactive Customer Case Communicator]]'s known risk "No batching in Stale Case Scheduled Job — every qualifying case fires a subflow in one while loop. No cap, pacing, or backpressure" — the **Create Record check (50/15min)** default limit is exactly the kind of platform-level backstop that risk note should be checked against (does PCCC's scheduled job actually hit this ceiling on a large batch, and if so what happens to the un-processed remainder?). Also gives a concrete emergency runbook (deactivate trigger → check `sn_aia_execution_plan` → analyze → redesign) that's more actionable than what PCCC's own docs currently capture for its "stuck execution / silent exclusion" open risk.
