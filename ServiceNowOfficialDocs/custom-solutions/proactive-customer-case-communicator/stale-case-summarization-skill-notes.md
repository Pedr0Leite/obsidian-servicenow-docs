---
aliases:
  - "Stale Case Summarization"
  - "Stale Case Summarization Skill"
area: "custom-solutions/proactive-customer-case-communicator"
tags:
  - servicenow
  - now-assist
  - ai-skill
  - csm
  - unit4
---

# Now Assist Skill: Stale Case Summarization

**Source:** ServiceNow Now Assist Skill Kit (`unit4dev1.service-now.com`), part of the **Proactive Customer Case Communicator** solution.

## Overview

| Field | Value |
|---|---|
| Skill name | Stale Case Summarization |
| Status | Published |
| Skill type | Custom skill |
| Created by | Pedro Leite |
| Created on | 2026-08-06 |
| Last modified by | Pedro Leite |
| Last modified on | 2026-08-06 |

**Description:** Generates a customer-safe status update for stale support cases. Reviews case details, comments, work notes, and linked incident/problem data to detect current status and draft a professional follow-up message — without exposing internal team names, ticket IDs, or escalation details.

**Short description:** *(empty)*

---

## 1. Inputs (1)

| Name | Type |
|---|---|
| Case number | String |

---

## 2. Outputs (5)

| Name | Type |
|---|---|
| provider | String |
| response | String |
| error | String |
| errorCode | String |
| status | String |

---

## 3. Tools

The skill uses a single **Script** tool, `GetRecordInfo`, which runs before the LLM prompt in the flow:

```
Start → Script: GetRecordInfo → Skill prompt: Stale Case Summarization prompt → End
```

### Tool: GetRecordInfo (Script)

> ⚠️ Editor warning shown in the tool: *"Script uses GlideRecord. If directly processing input or returning information to the caller, use GlideRecordSecure instead."*

```javascript
(function runScript(context) {
    /* @param {Object} context - Execution context, which may include:*/
    /*                 - Previous tool outputs/inputs (e.g., context['ToolName.attributeName'] or context.getValue('ToolName.attributeName')).*/
    /*                 - Additional context information (e.g., context.getAllValues()).*/
    /* @returns {Object} - The computed value for the attribute.*/
    var utils = new global.U4NowAssistSkillUtils();
    var tableName = 'sn_customerservice_case';
    var caseObj = {};

    var caseGR = new GlideRecord(tableName);
    caseGR.addQuery('number', context['case_number']);
    caseGR.setLimit(1);
    caseGR.query();

    if(caseGR.next()){
        caseObj.short_description = caseGR.short_description+'';
        caseObj.description = caseGR.description+'';
    }

    caseObj.case_comments = utils.getAllCommentsFromRec(caseGR.sys_id+'', tableName);
    caseObj.case_work_notes = utils.getAllWorkNotesFromRec(caseGR.sys_id+'',tableName);
    var case_rel_rec = utils.getCaseRelatedRecs(caseGR.sys_id+'');
    caseObj.case_rel_rec_activities = utils.getRecActivitiesPerPeriod(case_rel_rec, 'last30Days');

    return caseObj;
})(context);
```

This tool looks up the case (`sn_customerservice_case`) by number and assembles a payload with the short description, description, all customer comments, all work notes, and related-record (linked incident/problem) activity from the last 30 days, using a custom script include: `global.U4NowAssistSkillUtils`.

---

## 4. Prompt — "Stale Case Summarization prompt"

- **Provider / Prompt target:** AWS Claude (Amazon Bedrock Chat Completions)
- **Status:** Default prompt, Published
- **Length:** 670 words

Full prompt text (transcribed as authored):

```
You are a customer support communications assistant helping a support agent draft a
status update for a case that has gone stale (no recent customer-facing update).

=== TOP 3 RULES (Non-Negotiable) ===

1. Before doing anything else, replace all abbreviations in the input using below lookup table:
CSS  → Customer Success Services
CSM  → Customer Success Manager
CX → Customer Experience
P&E → Product & Engineering
Edu → Education
(University4U / Customer Success Education) → Education

Use these names whenever a department is mentioned or implicated, regardless of the wording in comments.

2. Department Naming Rule: Always use these exact department names whenever a
department is mentioned, implied, commented on, or not addressed:
- Customer Support
- Customer Success Services
- Customer Success Manager
- Customer Experience
- Product & Engineering
- Education

3. Maintain a professional, neutral, and evidence-based tone.
- No adjectives implying judgment (e.g., "serious," "severe," "unjust").
- Keep language concise, factual, and executive-appropriate.

INPUT
- Case short description: {{GetRecordInfo.output.short_description}}
- Case description: {{GetRecordInfo.output.description}}
- Case customer comments: {{GetRecordInfo.output.case_comments}}
- Case work notes: {{GetRecordInfo.output.case_work_notes}}
- Linked records activities: {{GetRecordInfo.output.case_rel_rec_activities}}

GOAL
Return one customer-ready follow-up message. Nothing else.

INTERNAL REASONING — do not output any of this
Work through these silently. They shape the message; they never appear in it.

1. Identify the issue originally reported, the most recent activity, and
   whether active work is ongoing.
2. Classify the current status as exactly one of:
   - Waiting for customer information or action
   - Waiting for Cloud Operations
   - Waiting for CSS or another internal support team
   - Linked incident is being reviewed
   - Linked problem investigation is ongoing
   - Workaround is being tested or validated
   - Product or Engineering review is in progress
   - Escalation or internal review is in progress
   - Monitoring after a change, fix, or workaround
   - No clear recent progress found
   If several apply, choose the one best supported by the most recent activity.
   If none is clearly supported, use "No clear recent progress found".
3. List privately (i.e. never surface to the customer): internal team
   or individual names, internal ticket/incident/problem IDs, escalation
   mechanics, vendor names, and internal-only technical detail. Exclude every
   one of them from the message.

EXPECTATIONS — the message
MUST:
- Rest only on the input above. Never invent facts, dates, names, or next steps.
- Rest only on the input above. Never invent facts, dates, names, or next steps.
- Reassure the customer the case is still being actively followed.
- State the status in plain, customer-friendly language.
- Name the next step only where the input clearly evidences one.
- Run 3-6 sentences, professional, calm, helpful.
- Read as specific to this case. Vary the phrasing; do not reuse a template.

MUST NOT:
- Name internal teams, internal record IDs.
- Never refer to the "Cloud Team" (or Cloud Operations) in the message. If the
  case is waiting on that team, describe the status in neutral customer-facing
  terms without naming them.
- Describe escalation mechanical detail.
- State or imply a resolution date unless that date appears in
  customer-shareable input
- Blame any team, vendor, or the customer.
- Quote work notes verbatim unless the text is plainly customer-safe as-is.

FALLBACK
If the status is "No clear recent progress found", write a neutral holding
message: the case remains confirming the latest
status before sharing further detail. Do not guess at a cause or a next step.

OUTPUT FORMAT
Return the message text only. No headings, no labels, no preamble, no sign-off
block, no explanation of character of your response
is the first character o[text as displayed cuts off here in the source editor]

Example of the expected shape and tone (do not reuse this wording):

Thank you for your continued patience while we work through this. Our team is
currently validating a potential fix in a test environment to make sure it
fully resolves the behaviour you reported before we apply it more widely. This
verification step is underway now, and we are monitoring the results closely.
We will come back to you as soon as we have confirmed the outcome.
```

> **Note on transcription:** The "OUTPUT FORMAT" section's final sentence appears truncated/garbled in the source editor itself ("...no explanation of character of your response is the first character o"), and step 3 of the internal reasoning block ("List privately...") was lightly clarified in brackets where the on-screen wording was ambiguous. Everything else above is verbatim from the published prompt.

**Notable prompt design points:**
- Uses a strict abbreviation/department-name normalization table (CSS, CSM, CX, P&E, Edu, University4U → their full names) so raw internal shorthand from comments/work notes never leaks into a customer message.
- Forces the model to silently classify the case into one of 10 fixed "current status" buckets before writing anything.
- Has a dedicated redaction step: internal team/individual names, ticket/incident/problem IDs, escalation mechanics, and vendor names must be identified and then excluded.
- Hard constraints against naming the "Cloud Team"/"Cloud Operations," implying dates not present in the input, or assigning blame.
- Includes a fallback holding-message template for when no clear recent progress can be found.
- Output must be the raw customer message only — no headings/labels/preamble/sign-off.

---

## 5. Optimize and evaluate

- **Dashboard → Automated evaluations:** *Nothing to show* — no automated evaluations have been set up/run yet.
- **Evaluation metrics configured (available, not yet run):**
  - Faithfulness Metric (Amazon Bedrock)
  - Correctness Metric with Golden Response (Amazon Bedrock)
  - Correctness Metric (Amazon Bedrock)
- **Optimization runs:** none set up.

---

## 6. Deployment and skill settings

### Deployment settings
- **Workflow:** Other
- **Product:** *(not set)*
- **Feature:** *(not set)*
- **Activation surfaces** (admin can enable the skill to be triggered via) — all currently **unchecked**:
  - Now Assist Panel
  - UI Action
  - Flow action
  - Now Assist Context Menu
  - Virtual assistants
  - UI Builder

### General information
- **Skill name:** Stale Case Summarization
- **Default provider:** AWS Claude
- **Provider API:** Amazon Bedrock Chat Completions
- **Providers (Provider API):** AWS Claude (Amazon Bedrock Chat Completions) — Preprocessors: 0, Postprocessors: 0, Published prompts: 1, set as default.

### Security controls
- **Role restrictions:** none configured — *"This skill doesn't have any role restrictions."*

### Provider detail — AWS Claude (Amazon Bedrock Chat Completions)
- Provider preprocessors: 0
- Provider postprocessors: 0

---

## Summary

Stale Case Summarization is a custom Now Assist skill (part of the Proactive Customer Case Communicator solution) that takes a case number, pulls the case's description, comments, work notes, and last-30-days linked incident/problem activity via a `GetRecordInfo` script tool, and feeds that into an AWS Claude (Amazon Bedrock) prompt. The prompt is heavily engineered to normalize internal department abbreviations, silently classify the case's status, strip out anything internal (team names, ticket IDs, escalation/vendor detail), and return a single short, calm, customer-safe follow-up message with no internal jargon, blame, or invented facts. The skill is currently published but not yet activated on any surface (Now Assist Panel, UI Action, Flow action, etc.), has no role restrictions, and has no automated evaluations run yet.

---

## Related

- [[Proactive Customer Case Communicator]] — parent solution; `caseUpdateAgentUtil.script.js`'s `_getStaleCaseSum(caseNumber)` calls this skill to generate the `7.10.2` ("no significant change") template body on the [[Stale Case Path]], replacing what used to be static filler text. See that doc's [[Proactive Customer Case Communicator#5. `caseUpdateAgentUtil` (Script Include)|§5]] and [[Proactive Customer Case Communicator#8. Template Registry|§8]].
- [[caseUpdateAgentUtil]]
- [[Template Registry]]
- [[Now Assist]]
