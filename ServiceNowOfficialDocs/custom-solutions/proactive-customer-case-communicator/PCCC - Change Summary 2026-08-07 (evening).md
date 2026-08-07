---
aliases:
  - "PCCC Change Summary 2026-08-07 evening"
area: "custom-solutions/proactive-customer-case-communicator"
tags:
  - servicenow
  - ai-agent
  - csm
  - unit4
  - changelog
---

# PCCC — Change Summary, 2026-08-07 (evening)

Triage session driven by one live case: **`CS0991191`** — Vinje kommune, P3, **no linked Problem**, state In Progress, `u_last_comment_from_unit4 = 2026-07-07` (31 days quiet).

Starting question: *"should the No Update in 7 Days scenario trigger template 7.10.2?"*
Ending answer: **no — and three separate defects were blocking any message at all.**

---

## 1. What was wrong

### Defect A — the morning's Gate 1/3 fixes were never live

The Script Include `caseRoutingPCCCUtil` was deployed and correct. The AI Agent Tool still held its **own pre-refactor inline script**, so `resolve()` was dead code.

NAP returned, on a case with no Problem linked:

```
stop_reason: Template could not be determined for problem_state: ,
             resolution_code: , routing_decision: 6B
```

Character-identical to the pre-fix incident — a stop the hardened Gate 1 cannot produce.

Two tells confirmed the tool was running the old copy: no `_boolish()` in its script, and the workaround-only-change override still present (a block the Script Include never carried).

**Impact:** every case with no linked Problem silently received nothing, where the design specifies 7.1 or 7.2.

### Defect B — skill-generated bodies posted wrapped in quotes

```
Dear Vicky,
Thank you for your patience regarding your case CS0991191, …

"We wanted to reach out with a brief update on your case regarding the CB05 (XML)
bank reconciliation import behavior. …"
```

Greeting unquoted, skill block quoted — the boundary was exactly where the skill output entered the template.

Cause: `_getStaleCaseSum()` ended in `return JSON.stringify(skillResponse);`. JSON-encoding a string adds its own delimiters (`Hello` → `"Hello"`). Not an LLM problem — the skill prompt already forbids wrappers.

### Defect C — no-Problem stale cases got static filler

Even once routing worked, `7.1` was canned "we are actively reviewing" text, repeated identically every stale cycle. `7.10.2`'s case-specific, skill-generated quality was unavailable to any case without a linked Problem.

---

## 2. What changed

| # | Component | Change |
|---|---|---|
| 1 | AI Agent Tool — *Resolve routing decision and template selection* | Inline script replaced with a delegating wrapper (below) |
| 2 | `caseUpdateAgentUtil._getStaleCaseSum()` | `return JSON.stringify(skillResponse);` → `return skillResponse;` |
| 3 | `caseUpdateAgentUtil._buildTemplates()` | `7.1`'s body now calls `this._getStaleCaseSum(cs)` — "Option A" |
| 4 | `caseRoutingPCCCUtil.resolve()` | `is_first_linkage`, `workaround_pending`, `new_worknote_available` now normalised through `_boolish()` |
| 5 | `caseRoutingPCCCUtil.resolve()` | `6B` branch gains `Assess` → `7.3`, mirroring `6A` |
| 6 | `caseRoutingPCCCUtil.resolve()` | New `6B_DEGRADED` fallback: linked Problem + blank `problem_state` → `7.10.2` + `gs.warn` |

**Change 1:**

```javascript
(function(inputs) {
    return new caseRoutingPCCCUtil().resolve(inputs);
})(inputs);
```

Add the scope prefix (`sn_csm_ai_agents.caseRoutingPCCCUtil`) only if the tool runs outside the Script Include's scope.

The Stale Case Summarization skill itself needed **no change** — it takes only `case_number`, and its prompt's status buckets already cover non-Problem cases ("Waiting for customer information or action", "Waiting for CSS or another internal support team", and the "No clear recent progress found" fallback).

**Changes 4–6 — routing hardening.** Once the tool was actually executing `resolve()`, three latent issues became worth closing in the same pass:

*Normalisation completed (4).* The three content flags previously used bare-literal `=== true || === 'true'`, so `'True'`, `' true '`, `'Yes'` and `'1'` all read as *not set*. For `workaround_pending` that failed twice in one pass — `6C` skipped the `7.4` branch **and** `append_workaround` stayed `false`, dropping the workaround in both directions. All six boolean-ish inputs now normalise at the top of `resolve()`.

*`6B` + `Assess` (5).* Open since 2026-07-16. `6A` had `New || Assess`; `6B` had neither an `Assess` branch nor a generic fallback, so an `Assess` Problem routing through `6B` sent the customer nothing. `6B` now mirrors `6A`.

*`6B_DEGRADED` (6).* Past Gate 1, `problem_linked` is confirmed `'true'` — so a blank `problem_state` is a data-population fault, not a state. These now route to `7.10.2` under a distinct label with a `gs.warn`, rather than sending nothing. Safe content-wise: `7.10.2`'s body comes from the skill reading case comments and work notes, and asserts nothing about the Problem.

Two limits are deliberate. A state that is **present but unrecognised** still `STOP`s — that is a new or unmapped Problem state and must surface rather than quietly receiving "no significant change". And `6A` keeps its plain `STOP`, since first linkage with a blank state is a much stronger signal of upstream breakage.

> **Treat a rising `6B_DEGRADED` count as an input-pipeline alarm, not an acceptable routing outcome.** The label exists so these stay countable instead of blending into normal `6B`.

---

## 3. Why `7.10.2` was the wrong target

`7.10.2` exists **only** in the `6C` branch. `6C` is reachable only after Gate 1 passes, and Gate 1 fires on any case with no linked Problem. `7.10.2` is therefore structurally unreachable for `CS0991191` — no configuration change short of a routing rewrite alters that.

Two options were evaluated:

| | **Option A** — reuse `7.1` (chosen) | **Option B** — route `7.10.2` without a Problem |
|---|---|---|
| Routing change | none | new Gate 1 third branch + a "prior outreach" input |
| Counter impact | none — `reset_count = skip` preserved | `7.10.2` is `reset_count = false`; no-Problem cases enter the counter with **no reset path** (full reset requires the Problem Update Path) → permanent cooloff-restamp loop |
| Agent prompt | none | Step 7.2's hardcoded ID→`reset_count` map must read `templates[SELECTED_TEMPLATE].reset_count` instead |
| Doc churn | one registry row | gates, matrix, decision table, registry |
| Effort | one line | five changes |

Customer-visible outcome is identical. Only the template **ID** differs — reporting that counts stale no-change messages will see these as `7.1`.

---

## 4. Behaviour changes to expect

| Change | Effect | Who notices |
|---|---|---|
| Gate 1 now fires | Unlinked cases produce 7.1 / 7.2 instead of a bogus `6B` stop | Consultants — new drafts appear on cases that were silent |
| **Gate 3 now fails closed** | `has_work_item` blank or uninterpretable now STOPs rather than releasing a message | Consultants — **visible rise in NAP stops**. Correct, but reads as a regression unless announced. |
| Workaround-only override gone | `7.4` reachable only via the ordinary `6C` + `workaround_pending` path | Anyone relying on workaround-only Problem edits firing 7.4 |
| `7.1` body skill-generated | Case-specific stale messages on no-Problem cases | Customers |
| `6B` + `Assess` now sends `7.3` | Cases that were silently stopping now produce drafts | Consultants — new drafts on previously silent Problems |
| `6B_DEGRADED` appears in routing output | New `routing_decision` value in NAP and reporting | Anyone filtering or counting by `routing_decision` |
| Content flags normalised | Workarounds and worknotes that were silently dropped now reach the customer | Customers — possibly a backlog of never-communicated workarounds |

> ⚠️ **Tell the support team about the Gate 3 change before they see it.** More stops is the intended outcome — the gate exists to stop a message going out on a Problem with no Work Item — but without warning it looks like the agent broke.

---

## 5. Verification performed

- Replayed the reported `CS0991191` payload against the tool after the swap → `STOP_GATE1` / `7.1`, no `stop_reason`.
- Re-ran the T2 ATF matrix. Any test asserting a message on a blank `has_work_item` moves to the fail-closed stop **by design** — update the assertion, do not revert the gate.
- Confirmed `typeof skillResponse === 'string'` before removing `JSON.stringify`. Had it been an object, `resp.capabilities[capabilityId].response` would have been needed instead; returning the object raw would have posted `[object Object]`.

**ATF changes required**

Two existing assertions move by design — update them, do not revert the code:

| Test | Was | Now |
|---|---|---|
| `6B` + `Assess` | `STOP` | **7.3** |
| `wi_required = true`, `has_work_item` blank | message released | `STOP` (fail-closed) |

New cases to add — the last four are regression guards without which `_boolish` can be reverted silently:

| Input | Expected |
|---|---|
| `6B` + blank `problem_state` | `6B_DEGRADED` / **7.10.2**, `gs.warn` emitted |
| `6B` + present-but-unrecognised `problem_state` | `STOP` |
| `6A` + blank `problem_state` | `STOP` (asymmetry is intentional) |
| `workaround_pending: 'True'` | **7.4**, `fill_workaround_token = true` |
| `new_worknote_available: 'Yes'` | **7.9**, `fill_worknote_token = true` |
| `is_first_linkage: '1'` | route `6A` |
| `problem_linked: ' FALSE '` | `STOP_GATE1` / **7.1** |
| `problem_linked: 'PRB0052356'` | `STOP`, named reason |

---

## 6. Open follow-ups

| Priority | Item |
|---|---|
| High | Tighten the agent prompt's Step 5 so tool inputs stop carrying literal `"null"` strings and mixed-case booleans. `_boolish` is a shield; this is the cure. |
| High | Sweep `sn_aia_execution_plan` for rows left in `ready`/`in_progress` by the pre-fix Gate 1 defect. The stale job skips any case with a live plan, so each orphan silently excludes its case from every future run — the "stuck execution / silent exclusion" risk, now with a population. |
| Medium | Decide the fate of the workaround-only-change override — restore the gate, or retire the dead `workaround_only_latest_change` input and variable |
| Medium | Run evals on the Stale Case Summarization skill. Its blast radius now covers *all* stale no-Problem cases; it has no automated evaluations, no role restrictions, and `GetRecordInfo` uses `GlideRecord` where the Skill Kit editor warns for `GlideRecordSecure`. |
| Medium | `u_last_comment_from_unit4` can predate case creation — `CS0991191` opened 2026-08-06 with a 2026-07-07 value, `comments` empty, `u_first_response = false`. Brand-new cases read as a month stale on day one. False-positive source for stale rules 1 and 4. |
| Low | `_getStaleCaseSum()` runs during `_buildTemplates()` for every execution, regardless of which template routing selects — two templates now depend on it. Candidate for lazy evaluation if run duration becomes a problem. |
| Low | Add a report or dashboard counter on `routing_decision = '6B_DEGRADED'` so the alarm is visible without reading logs |

---

## 7. Documentation updated

| File | Sections touched |
|---|---|
| `Proactive Customer Case Communicator.md` | §5 method table (`_buildTemplates`, `_getStaleCaseSum`), §7 Tool 2 (stale-tool bug callout, string-input warning, selection matrix, `Assess` resolved, `6B_DEGRADED` callout), §8 Template Registry (7.1 row + Option A/B comparison), §13 Risks (resolved + newly raised), §17 Changelog (full evening entry incl. routing hardening and ATF coverage) |
| `routing-decision-table.md` | Rewritten and expanded — `_boolish` states, all gate outcomes, 6A/6B/6C matrices incl. `Assess` and `6B_DEGRADED`, post-template flags, **both entry paths**, the five stale rules, counter/cooloff, body sources, 22 worked end-to-end scenarios, structurally unreachable combinations, and ATF coverage |

---

## Related

- [[Proactive Customer Case Communicator]]
- [[routing-decision-table]]
- [[stale-case-summarization-skill-notes|Stale Case Summarization]]
