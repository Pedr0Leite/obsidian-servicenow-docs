---
title: Partner Case Lookup — Custom Evaluation Metric
type: evaluation-metric
platform: ServiceNow
scope: sn_aia
instance: unit4dev1
workflow: Partner Case Lookup
agent: Summarize Partner Cases
framework: Now Assist SkillKit
status: draft
mode: read-only
last_updated: 2026-09-07
tags:
  - servicenow
  - now-assist
  - sn_aia
  - agentic-workflow
  - evaluation
  - skillkit
  - custom-metric
---

# Partner Case Lookup — Custom Evaluation Metric

> [!abstract] Purpose
> Deterministic output-contract compliance metric for the **Partner Case Lookup** agentic workflow (AWF) and its **Summarize Partner Cases** AI Agent (AIA). Answers one question: *did the agent present exactly the case data its tools returned, in exactly the format its instructions mandate?*

---

## Description (metric record field)

Evaluates output-contract compliance for the Partner Case Lookup agentic workflow and its Summarize Partner Cases agent. Scores the agent's final response against the case data its tools actually returned — not against semantic similarity.

Deterministic checks, each mapped to a numbered rule in the agent prompt:

- **Path exclusivity** (post-exec validation) — a single-case request called only `Get single Case resume`; an account request called only `Search Account` then `Get active cases from Account`. Weight 20.
- **Case completeness** (4.1) — every case number in `${CASES_FOUND}` appears exactly once in the output. Weight 25.
- **State fidelity** (4.2.g / 4.2.i) — `state` reproduced verbatim, not re-labelled or derived from resume text. Weight 15.
- **Last-comment line** (4.2.h) — `lastCommentFromU4` output as returned, or "none recorded" when empty. Weight 15.
- **Four-part structure** (4.3) — number, state, last-comment, resume present for every case. Weight 15.
- **Resume line limit** (4.2.e) — no resume exceeds four lines. Weight 10.

Two guardrail violations force a score of 0 regardless of other checks: a `sys_id` reaching the user (4.6) and the `NO_TECHNICAL_ACTIVITY` sentinel appearing in the output (4.2.b).

Score is normalised over *applicable* weight only. A check that cannot be evaluated against the payload is skipped and its weight leaves the denominator, so an unexposed variable is never scored as a behavioural failure. Bands: ≥80 Compliant, ≥50 Partially compliant, ≥20 Largely non-compliant, below that Non-compliant. Returns `status: "error"` with the payload key list when the parser output is unusable.

Read-only. Requires the parser tool to expose `CASE_OUTPUT` and `CASES_FOUND`; `tool_calls` and `REQUEST_TYPE` are optional and improve coverage when present.

### Short form (length-capped field)

```text
Scores Partner Case Lookup output-contract compliance against tool-returned
case data: path exclusivity, case completeness, state and last-comment
fidelity, four-part structure, resume length. Hard-fails on sys_id or
NO_TECHNICAL_ACTIVITY leakage. Normalised over applicable checks only.
```

> [!tip] Keep the description stable
> The long description above documents the weights, so it goes stale the moment the `W` block changes. If you'd rather it stay stable, drop the per-check weights and keep them only in the script.

---

## What is the evaluation metric?

A deterministic output-contract compliance metric.

It does **not** assess whether the retrieved cases were the right ones, whether a summary is well written, or whether the Partner Manager found the answer useful. Those are relevance and quality judgements requiring an LLM-as-judge. This metric measures fidelity and format only — the classes of failure that are objectively verifiable from tool output.

Its value comes from the agent's unusually rigid prompt:

- `state`, `lastCommentFromU4`, and case numbers are verbatim-passthrough fields
- `sys_id` is absolutely prohibited from output
- the presented case count must equal `${RETURNED_CASE_COUNT}` exactly

Every one of those is checkable by string comparison — no fuzzy matching, no false positives from paraphrase.

> [!info] Design contrast
> The Similar Records metric scored *semantic relevance* with bag-of-words Jaccard and collapsed into a two-state step function. This metric deliberately scores nothing that requires semantic judgement.

---

## How does the metric work?

### 1. Input resolution

Reads `context['AgenticExecutionParserTool.output']`, coercing from string to object if needed, and gates on `status === 'completed'`. Logs the full payload key list plus a type/preview line per key, so a misconfigured parser is diagnosable from the syslog without a re-run.

### 2. Variable extraction

Resolves four workflow variables through `pick()`, which tries known spellings then falls back to a separator- and case-insensitive scan, logging which key matched.

| Variable | Required | Used for |
| --- | --- | --- |
| `CASE_OUTPUT` | yes | the text the user saw |
| `CASES_FOUND` | no | ground truth: `number`, `sys_id`, `resume`, `state`, `lastCommentFromU4` |
| `tool_calls` | no | path exclusivity |
| `REQUEST_TYPE` | no | justification context |

`CASES_FOUND` is normalised through `normaliseCases()`, which accepts an array, a JSON string, or an object wrapping `casesFound`, and coerces `resume: false` to the string `'false'` so the 4.2.c failure case stays detectable.

### 3. Hard gates

Evaluated first; either one forces a final score of 0.

| Gate | Rule | Method |
| --- | --- | --- |
| `sys_id` leakage | 4.6 + Guardrails | each case `sys_id` searched in output, plus a `\b[0-9a-f]{32}\b` sweep to catch an account sys_id from `Search Account` that never appears in `CASES_FOUND` |
| Sentinel leakage | 4.2.b | literal `NO_TECHNICAL_ACTIVITY` present in output |

Both are absolute prohibitions in the prompt, so partial credit would misrepresent them.

### 4. Weighted checks

Six checks, each returning a ratio in 0–1 and an `applicable` flag.

| Check | Weight | Method |
| --- | --- | --- |
| Path exclusivity | 20 | tool-name presence in trace; single-case tool alongside account tools = 0; `Search Account` without active-cases = 0.5 (legitimate stop) |
| Case completeness | 25 | occurrence count per case number; exactly once = credit, zero = miss, duplicates flagged |
| State fidelity | 15 | case-insensitive `indexOf` of each `state` value |
| Last-comment line | 15 | date string present, or "none recorded" when the field is empty |
| Four-part structure | 15 | count of `State:` and `Last comment from U4:` lines against case count |
| Resume line limit | 10 | longest run of consecutive non-meta lines ≤ 4 |

### 5. Normalisation

The design decision that matters most:

```javascript
finalScore = Math.round((earned / applicableWeight) * 100);
```

The denominator is *applicable* weight, not total weight. A check that cannot be evaluated — no tool trace exposed, no case entries because the account had none — is marked `applicable: false` and its weight leaves the denominator entirely. It is never scored as a behavioural failure.

> [!warning] Why this exists
> In the Similar Records metric, an unparseable section silently cost 20 points, making a **parsing regression look like a quality regression**. Here, an unexposed variable produces a `Skipped checks` note in the justification and leaves the score untouched.

### 6. Finalisation

Hard gates applied, score clamped to 0–100, band label assigned, justification assembled.

### Verified spread

Nine smoke-test scenarios against mock payloads:

| Scenario | Score | Status |
| --- | --- | --- |
| Fully compliant, 2 cases | 100 | completed |
| No tool trace exposed | 100 | completed |
| Resume over 4 lines | 90 | completed |
| Path bleed | 80 | completed |
| State re-labelled | 78 | completed |
| One case dropped | 65 | completed |
| `sys_id` leak | 0 | completed |
| Sentinel leak | 0 | completed |
| Unusable payload | 0 | error |

Real spread across the bands — no step function.

---

## What is the output format of the metric?

Standard SkillKit indicator response. The script returns an object whose `response` property is a JSON string:

```javascript
{
  response: JSON.stringify({
    indicatorResponse: [{
      value:  "<justification text>",
      score:  <integer 0-100>,
      status: "completed" | "error"
    }]
  })
}
```

### `score`

Integer 0–100.

| Band | Label |
| --- | --- |
| ≥ 80 | Compliant |
| ≥ 50 | Partially compliant |
| ≥ 20 | Largely non-compliant |
| < 20 | Non-compliant |

### `status`

- `completed` — any evaluable run, **including hard-gated zeros**, because a guardrail breach is a real measurement rather than a metric malfunction.
- `error` — only when the payload itself is unusable: parser not completed, output unparseable, `CASE_OUTPUT` missing, or no check applicable.

### `value`

A single justification string, assembled from:

1. Band label and score
2. Any hard-gate notes, naming the leaked value
3. `REQUEST_TYPE` and case count
4. One clause per check: percentage, weight, and specific detail
5. Any skipped checks

Example on a dropped case:

```text
Partially compliant (65/100). REQUEST_TYPE=account_cases; cases in payload=2.
Only one path ran: 100% [w20] — Clean account_cases path (search then active
cases). Every case present exactly once: 50% [w25] — 1/2 case numbers present;
0 appear more than once; missing: CS0987860. ...
```

The detail strings name the offending case number and the expected value, so the justification alone tells you which rule broke and on which record.

On the error path, `value` includes the payload key list — the field that makes a parser misconfiguration fixable in one pass.

---

## Open items

> [!question] Unverified on `unit4dev1`
> - **Payload key casing.** `pick()` tries several spellings then falls back to a tolerant scan. That's a workaround, not a fix. Run once, read `payload keys (n): ...` in the syslog, then hard-code the real keys and delete the tolerant scan.
> - **Does `tool_calls` exist in the payload at all?** If the parser exposes no invocation trace, path exclusivity is unevaluable and 20 points leave the denominator. Getting that trace exposed is the highest-value parser change, since path bleed is the failure mode the prompt guards against hardest.
> - **Are `status: "error"` rows excluded from aggregation, or averaged in as zeros?** Determines whether error runs quietly depress the suite average. Same open question carried over from the Similar Records metric.

### Deferred decisions

| Decision | Rationale for deferring |
| --- | --- |
| Promote **path bleed** to a third hard gate | The prompt treats it as an absolute post-exec validation failure, but a noisy tool trace would produce false hard-zeros. A lenient score beats a false zero. |
| Raise **`stateFidelity`** weight 15 → 30 | `state` re-labelling currently scores 78 ("Partially compliant"), arguably generous for a verbatim-passthrough violation. |
| Tighten `resumeLineLimit` meta-line regex | Heuristic: a resume containing an internal blank line reads as two short blocks and passes. |

### Operational note

`gs.log()` writes to `syslog` unscoped. At 40+ lines per evaluation this bulks up the table fast on a suite run. Set `DEBUG = false` for bulk runs, or switch to `gs.debug()` gated on a `sys_properties` flag.

---

## Related

- [[Partner Case Lookup - Agentic Workflow]]
- [[Summarize Partner Cases - AI Agent]]
- [[AI Tool - Search Account]]
- [[AI Tool - Get active cases from Account]]
- [[AI Tool - Get single Case resume]]
- [[Similar Records - Agentic Workflow Eval Metric]]
- [[Now Assist SkillKit - Evaluation Framework]]
