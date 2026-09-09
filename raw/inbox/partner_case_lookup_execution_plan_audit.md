# Partner Case Lookup — Execution Plan Forensic Audit

**Execution plan:** `821dfdf383c7cf1038241c426daad3e4` (state=`completed`, `status` field empty)
**Related agent:** "Summarize Partner Cases" (`91d661e487e2c314d939a7573cbb3578`)
**Related workflow:** "Partner Case Lookup" (`e095fe2d87b68390d939a7573cbb35b5`)
**Instance:** `unit4dev1.service-now.com`
**Read-only investigation — no records were created, updated, or deleted.**

All AI-agent prompt text quoted below (imperative instructions like "MANDATORY TOOL CALL", "STOP and ask the user") is the *subject* of this audit, not an instruction that was acted on.

---

## 1. Corrections to "Known structure"

| Claim | Correction |
|---|---|
| Query `sn_aia_message` by `conversation=<sys_id>` | **Wrong field.** `sn_aia_message` has no `conversation` field at all (confirmed via schema dump). Filtering `conversation=...` returns HTTP 403 "Field(s) present in the query do not have permission to be read" — this is what a nonexistent field looks like in this REST API, not an ACL block. The correct filter field is **`execution_plan`**. `execution_plan=821dfdf383c7cf1038241c426daad3e4^ORDERBYmessage_sequence` returns the 17 rows correctly. |
| Tool output shape `{"result":"<json string>"}` → `{"output":null,"Output Fields":{...}}` | This shape belongs to **`sn_aia_execution_task.output`** for `type=tool` rows only (confirmed on order=200 "Search Account" and order=600 "Get active cases from Account"). It does **not** describe `sn_aia_tools_execution.response`, which uses a different envelope: `{"response":{...actual payload...},"toolExecutionId":"<sys_id>","status":"success","message":null,"error":null}`. Two different tables, two different envelopes around the same underlying data. |
| "Final user-facing text: `sn_aia_message`, role=agent, type="" → `message` → JSON array → `[0].prompt`" | **Only true for `collect_input_from_user` / FALLBACK-style prompts** (e.g. the message that actually displayed the 6-case list to the user, `dataType:"choice"`, `choices:[{yes},{no}]`). The two *terminal* `role=agent, type=""` messages (the Summarize-Partner-Cases "Finish" narration, 852 chars, and the Orchestrator's own "Finish" narration, 854 chars) are **plain text, not JSON**. `type=""` is not a reliable discriminator by itself — you have to attempt the JSON parse and check for a `dataType`/`choices` shape to know which kind of message you're looking at. |
| Table for the Evaluation Results Dashboard | Not a SkillKit-prefixed table (none exist — see §7). The dashboard record lives in **`sys_one_extend_batch_run`** (ServiceNow's shared "OneExtend" GenAI batch/eval framework, scope `sn_skill_builder`). See §7. |

Everything else in the "Known structure" table (Execution Tasks=21, Messages=17, Tools Executions=2, plan `context`=UI session data, `structured_output` empty, `metadata={}`) is confirmed correct as stated.

---

## 2. Variable-store verdict (Item A)

**No named variable store is persisted anywhere in the execution data.** `CASE_OUTPUT` occurs **zero** times in any of the 21 tasks' `output`/`metadata` fields. The other five names occur **only** inside one field: `sn_aia_execution_task.metadata` of the order=200 "Summarize Partner Cases" task — and every single occurrence is inside a `${...}` template placeholder in free-text prose, never as a real, quoted JSON key (`"CASES_FOUND":` never appears; `${CASES_FOUND}` does, 7 times).

That metadata field's `background` property is headed literally `# Memory Variables` and documents a full scheme of **eight** placeholder names used only inside the prompt text: `${REQUEST_TYPE}`, `${CASE_NUMBER}`, `${ACCOUNT_NAME_INPUT}`, `${ACCOUNT_CANDIDATES}`, `${SELECTED_ACCOUNT_NAME}`, `${SELECTED_ACCOUNT_SYS_ID}`, `${CASES_FOUND}`, `${RETURNED_CASE_COUNT}` — 38 occurrences total, all as `${...}`. So:

- `ACCOUNT_SYS_ID` alone never appears — only as the tail of the compound name `SELECTED_ACCOUNT_SYS_ID`.
- `SELECTED_ACCOUNT` alone never appears — only as the head of `SELECTED_ACCOUNT_NAME` / `SELECTED_ACCOUNT_SYS_ID`.
- `CASE_OUTPUT` doesn't appear at all, in this task or any other.

This is a **prompt-level convention telling the LLM to treat these as its own working memory within one ReAct pass** — it is not a ServiceNow field, not a script variable, and not a structured object anywhere in `sn_aia_execution_task`, `sn_aia_tools_execution`, or `sn_aia_message`. The LLM appears to honor it only informally, through its own `Thought` text and `Action Inputs` (e.g. it does carry the real account sys_id `dece780a87aa89d044d4a9740cbb3532` forward correctly from the Search Account observation into the next tool call), never through a literal named slot.

The closest **real, persisted** analogs to the conceptual names, found by exhaustively grepping every task:

| Conceptual name | Real field, where it actually lives |
|---|---|
| `${REQUEST_TYPE}` | `lookup_request_type` — a `dataType:"choice"` field name inside the order=100/order=200 communicator tasks' `metadata.task`/`message` (value observed: `"all_active_cases_for_client_account"`) |
| `${SELECTED_ACCOUNT_SYS_ID}` | The literal string `account_sys_id` inside the `Action Inputs` of the "Get active cases from Account" tool call, and inside `sn_aia_tools_execution.request.payload.account_sys_id` |
| `${SELECTED_ACCOUNT_NAME}` | Never captured under a consistent field name — the confirmation step's user response used field name `account_selection` (value `"1"`), not an account name |
| `${CASES_FOUND}` | `Output Fields.casesFound` in the tool task's `output.result`, and `response.casesFound` in `sn_aia_tools_execution.response` |
| `${RETURNED_CASE_COUNT}` | Not materialized anywhere as a count field — it is only ever the array length of `casesFound`, computed implicitly |

**Bottom line for your metric:** you cannot read a named variable. You have to reconstruct everything from tool output (`sn_aia_tools_execution.response` or the `type=tool` task's `output`) plus the calling agent's own scratchpad `Action Inputs`/`Observation` pairs, exactly as the prompt says was assumed impossible.

---

## 3. Task dump (Item B) — all 21 rows, `execution_plan=821dfdf383c7cf1038241c426daad3e4`

| order | type | description | status | out len | meta len |
|---|---|---|---|---|---|
| 50 | access_verification | Partner Case Lookup | success | 975 | 2 |
| 100 | gen_ai | AIA ReAct Engine | success | 267 | 2 |
| 100 | gen_ai | AIA ReAct Engine | success | 723 | 2 |
| 100 | agent | Orchestrator | success | 2825 | 331 |
| 200 | agent | Summarize Partner Cases | success | 22024 | 19334 |
| 200 | communicator | Get user input unrefined | success | 216 | 736 |
| 200 | tool | Search Account | success | 159 | 234 |
| 300 | gen_ai | AIA ReAct Engine | success | 1132 | 2 |
| 300 | gen_ai | AIA ReAct Engine | success | 262 | 2 |
| 300 | agent | Orchestrator | success | 5926 | 278 |
| 400 | communicator | Get user input unrefined | success | 180 | 602 |
| 400 | communicator | Get user input unrefined | success | 185 | 194 |
| 500 | gen_ai | AIA ReAct Engine | success | 250 | 2 |
| 500 | gen_ai | AIA ReAct Engine | success | 775 | 2 |
| 600 | gen_ai | AIA ReAct Engine | success | 167 | 2 |
| 600 | tool | Get active cases from Account | success | 5362 | 276 |
| 700 | gen_ai | AIA ReAct Engine | success | 4624 | 2 |
| 800 | tool | organize_general_knowledge | success | 3529 | 534 |
| 900 | gen_ai | AIA ReAct Engine | success | 7612 | 2 |
| 1000 | communicator | Get user input unrefined | success | 178 | 6932 |
| 1100 | gen_ai | AIA ReAct Engine | success | 1473 | 2 |

Every `output`/`metadata` value on this list was fetched and parsed in full (not just the head). Narrative below groups them by what they actually do, since most are duplicate views of the same six ReAct cycles at increasing levels of the call stack (Orchestrator → gen_ai log → Summarize Partner Cases agent → tool).

**order=50 (access_verification)** — the declared, access-checked resource tree for this run. This is the authoritative *declared tool list*:
```
Partner Case Lookup (workflow)
 └─ Summarize Partner Cases (agent, 91d661e487e2c314d939a7573cbb3578)
     ├─ Search Account (tool, c31f6da08766c314d939a7573cbb35a1)
     ├─ Get active cases from Account (tool, 171fa1e48766c314d939a7573cbb35f0)
     └─ Get single Case resume (tool, c7dfe9b6834b431038241c426daad306) — never invoked this run
```
`organize_general_knowledge` is **not** in this tree at all — see §4.

**order=100 (gen_ai ×2 + agent "Orchestrator")** — the very first turn. Orchestrator's own 3-cycle scratchpad: (1) FALLBACK asking "specific case number, or all active cases for a client account?" → user answered `{"lookup_request_type":"all_active_cases_for_client_account"}`; (2) FALLBACK asking "Please provide the client account name" → user answered `{"question":"Gemeente Deurne"}`; (3) delegates via `Action.Name="Summarize Partner Cases"`, `Action Inputs={"task":"Retrieve partner case summaries for Gemeente Deurne."}`. `result`: `"Retrieve partner case summaries for Gemeente Deurne."` `plannerCooldown: 4`.

**order=200 (agent "Summarize Partner Cases", the 22024/19334-char task)** — see §2 for the metadata (its full spec/prompt). Its `output` is a 6-cycle ReAct scratchpad:
- Cycle 0: `Search Account({"account_name_or_number":"Gemeente Deurne"})` → `{"accFound":[{"name":"Gemeente Deurne","sys_id":"dece780a87aa89d044d4a9740cbb3532"}],"error":""}`
- Cycle 1: FALLBACK "I found the following accounts. Which one do you mean?\n\n1) Gemeente Deurne" → user answered `{"account_selection":"1"}`
- Cycle 2: `Get active cases from Account({"account_sys_id":"dece780a87aa89d044d4a9740cbb3532","account_name":""})` → 6 cases (full data in §4/§5)
- Cycle 3: `organize_general_knowledge({"problem":"...sort by case number, check duplicate summaries, prepare four-part entries..."})` → produces the sorted, formatted 6-entry text
- Cycle 4: FALLBACK presenting the formatted case list + "another_lookup?" question → user answered `{"another_lookup":"no"}`
- Cycle 5: `Finish`, `last_objective:true`
- `result` (852 chars): "Completed operations: Summarize Partner Cases classified the request as an account-based lookup for Gemeente Deurne..." (matches the persisted `role=agent,type="conversation"` message verbatim)

**order=200 (communicator, 872d3537...)** and **order=100 gen_ai #1 (e21d3137...)** are the same "specific case number or account?" FALLBACK step, logged at two levels (raw `Task` string and the communicator record's own `metadata.task`/`message`).

**order=200 (tool "Search Account", 3f5d3d37...)** — task-level record of the same call as tool cycle 0 above. `metadata`: `{"memory_scope":"global_memory_scope","outputTransformation":"none","inputs":{"account_name_or_number":"Gemeente Deurne"},"name":"Search Account","id":"c31f6da08766c314d939a7573cbb35a1","type":"tool","toolSummarizationStatus":"ready"}`.

**order=300 (gen_ai ×2 + agent "Orchestrator")** — Orchestrator's *second* invocation. Its scratchpad **replays the full history from order=100** (cycles 0–1 are byte-for-byte the same Thought/Action/Observation as order=100's cycles 0–1), then adds: cycle 2 = re-delegates to "Summarize Partner Cases" and receives the full 852-char completion Observation; cycle 3 = `Finish`. `result`: the same "Summary of all completed operations..." 854-char narration that is the very last message in the conversation. `getMoreContextSubtasks: ["165d3d3783c7cf1038241c426daad302"]` (points at order=200's own sys_id). This confirms **the ReAct engine resends the entire scratchpad on every planning round** rather than diffing — a real cost/design detail, not a bug signature by itself.

**order=400 (communicator ×2)** — "I found the following accounts. Which one do you mean?" (field name `account_selection`) and "Please provide the client account name for which you want all active cases." (plain string, no `dataType`).

**order=500 (gen_ai ×2)** — the delegation-dispatch log and the "confirmed account, ready to retrieve cases" reasoning log; mirror cycle 2 of order=200 exactly.

**order=600 (gen_ai + tool "Get active cases from Account")** — the gen_ai row here is the reasoning that decides `Action=Finish` **with no `Task`/`Thought`/candidate-action field at all** — see the anomaly flagged in §8. The tool row (b5ddf9f7...) is the task-level twin of `sn_aia_tools_execution` response `fdddf9f783c7cf1038241c426daad316`; both hold the identical 6 `casesFound` entries in the identical order, cross-verified case-number-for-case-number.

**order=700 (gen_ai)** — the reasoning that decides to call `organize_general_knowledge`, Thought text identical to cycle 3 of order=200.

**order=800 (tool "organize_general_knowledge")** — see §4 for the rogue-tool analysis. `output.result` (3529 chars) is the fully sorted, four-part-formatted case text; identical byte-for-byte to the Observation embedded in order=200's cycle 3.

**order=900 (gen_ai)** — the reasoning that decides to FALLBACK-present the formatted list with an "another_lookup" yes/no question; `Datatypes[0].prompt` is the exact 3215-char case list shown to the user (see §4/§5 for redaction note).

**order=1000 (communicator)** — the "another_lookup" prompt/answer round; its `metadata` (6932 chars) is large only because it re-embeds the entire formatted case-list text as `metadata.task`/`message` — not new content.

**order=1100 (gen_ai)** — the `Finish` reasoning, Thought identical to cycle 5 of order=200.

### Item A deep-dive: does `CASE_OUTPUT` / `CASES_FOUND` / `REQUEST_TYPE` / `RETURNED_CASE_COUNT` / `ACCOUNT_SYS_ID` / `SELECTED_ACCOUNT` appear as keys anywhere?

Grepped all 21 rows × 2 fields (42 fields total):

| key | hits | location | as real JSON key? |
|---|---|---|---|
| `CASE_OUTPUT` | 0 | — | no |
| `CASES_FOUND` | 7 | order=200 `metadata` only | no — always `${CASES_FOUND}` |
| `REQUEST_TYPE` | 6 | order=200 `metadata` only | no — always `${REQUEST_TYPE}` |
| `RETURNED_CASE_COUNT` | 7 | order=200 `metadata` only | no — always `${RETURNED_CASE_COUNT}` |
| `ACCOUNT_SYS_ID` | 4 | order=200 `metadata` only | no — always the tail of `${SELECTED_ACCOUNT_SYS_ID}` |
| `SELECTED_ACCOUNT` | 8 | order=200 `metadata` only | no — always the head of `${SELECTED_ACCOUNT_NAME}` / `${SELECTED_ACCOUNT_SYS_ID}` |

200 characters of context for a representative hit of each (order=200 metadata):

- `CASES_FOUND`: `...l output or the request stops.\n  Display:     Never.\n  Used by:     account_cases path only.\n\n${CASES_FOUND}\n  Set in:      2.2.c (single_case) / 3.7.c (account_cases)\n  Contents:    casesFound array, verb...`
- `REQUEST_TYPE`: `...# Memory Variables\n${REQUEST_TYPE}\n  Set in:      1.1 (single_case) / 1.2 (account_cases)\n  Contents:    "single_case" or "account_cases"\n  Read in:     2 (gate), 3 (gate)...`
- `RETURNED_CASE_COUNT`: `...VER display sys_id.\n\n${RETURNED_CASE_COUNT}\n  Set in:      2.2.c (always 1) / 3.7.c (length of ${CASES_FOUND})\n  Contents:    Number of cases to be presented...`
- `ACCOUNT_SYS_ID` (as part of `SELECTED_ACCOUNT_SYS_ID`): appears in step "3.5. Do NOT proceed to step 3.6 until ${SELECTED_ACCOUNT_SYS_ID} is locked" and in the Memory Variables glossary entry for that name.
- `SELECTED_ACCOUNT`: appears as `${SELECTED_ACCOUNT_NAME}` / `${SELECTED_ACCOUNT_SYS_ID}` throughout section 3 (account resolution) and section 4 (formatting gate — "the account presented is the one the user selected in step 3.4").

The full "Memory Variables" glossary in the `background` sub-field documents 8 conceptual variables total: `REQUEST_TYPE`, `CASE_NUMBER`, `ACCOUNT_NAME_INPUT`, `ACCOUNT_CANDIDATES`, `SELECTED_ACCOUNT_NAME`, `SELECTED_ACCOUNT_SYS_ID`, `CASES_FOUND`, `RETURNED_CASE_COUNT` — all of them template placeholders in prose, none of them real data-store keys.

---

## 4. `organize_general_knowledge` (order=800) and Orchestrator `agentDetails`

**Confirmed: `organize_general_knowledge` is not in the agent's declared tool list.** The order=50 access-verification tree (§3) lists exactly three tools for "Summarize Partner Cases": Search Account, Get active cases from Account, Get single Case resume. A direct query of `sn_aia_tool` for `nameLIKEorganize_general_knowledge` returns **zero rows** — it is not a registered/configured tool record at all.

Its `sn_aia_execution_task.metadata` (order=800) explains where it comes from:
```json
{"type":"tool","id":"organize_general_knowledge","name":"organize_general_knowledge",
 "inputs":{"problem":"From the retrieved active cases for the selected account, sort the cases by case number ascending, check whether any non-exempt case summaries are identical, and prepare one final display entry per case using number, state, last-comment line, and a cleaned or shortened summary that follows the stated formatting rules."},
 "preRun":false,"toolSummarizationStatus":"ready","abstractTool":true,"memory_scope":"global_memory_scope"}
```
The key field is **`"abstractTool":true`**. This is a platform-level generic reasoning capability (an "abstract tool") that the AIA ReAct engine can invoke on its own initiative for reasoning/formatting sub-steps, distinct from — and not subject to — the per-agent declared tool list and its access-verification gate. It is invoked identically and produces byte-identical output whether looked at from the order=800 standalone task or embedded as cycle 3's Action/Observation inside order=200's own scratchpad. This is expected platform behavior, not evidence of a misconfigured or leaked tool, but it does mean **any path-conformance check that only counts calls to the 3 declared tools will silently miss this step** — which is exactly where the duplicate-summary check and the 4-line-cap enforcement (the part of the spec you're trying to make numerically checkable) actually happens.

**Orchestrator `agentDetails` (order=100 and order=300):**
```json
{"agentDetails":{"name":"Orchestrator","role":"You are an expert at planning ahead for solving a given task.","background":"","sys_id":"orchestrator_team_id","strategy":"orchestrator_strategy_id"},"task":"Partner Case Lookup","strategyTopic":"AIA-ReAct","additional_context":""}
```
Identical between the two invocations — `background` is empty, `sys_id`/`strategy` are literal placeholder strings (`"orchestrator_team_id"`, `"orchestrator_strategy_id"`), not real sys_ids. The order=100 record additionally carries `"originalSubtask":"161d313783c7cf1038241c426daad38f"` — a forward reference to the sys_id of the order=300 Orchestrator task record that hadn't been created yet at order=100's own creation time (or was created in the same transaction). Nothing agent-specific or case-specific is carried in `agentDetails` — it's generic Orchestrator boilerplate both times.

---

## 5. Resume metrics (Item C)

Source: `sn_aia_tools_execution` response for "Get active cases from Account" (`fdddf9f783c7cf1038241c426daad316`), cross-verified against the identical `casesFound` array embedded in order=200's scratchpad cycle 2 and the order=600 standalone tool task — all three sources match exactly, case-number for case-number, character-for-character.

| number | chars | words | sentence-ending marks (`.`/`!`/`?`) |
|---|---|---|---|
| CS0987859 | 486 | 72 | 4 |
| CS0973587 | 767 | 108 | 6 |
| CS0974494 | 840 | 116 | 8 |
| CS0985286 | 718 | 110 | 5 |
| CS0977930 | 683 | 104 | 6 |
| CS0990080 | 746 | 100 | 6 |

**This contradicts a premise in the prompt.** Rule 4.2.d/4.2.e is not a pure line-count rule: the actual text reads *"4.2.d. Otherwise, if the resume is 4 lines or fewer, **or roughly 80 words or fewer**, output it VERBATIM... 4.2.e. Otherwise, shorten it to a maximum of 4 lines..."* There is already a word-count escape hatch (~80 words) baked into the spec alongside the line-count one — the spec's author anticipated exactly the "single unwrapped line" problem you're describing. All 6 of these resumes are well above 80 words (100–116 words for 5 of the 6; the shortest, CS0987859, is 72 words and would pass verbatim under the existing 80-word rule). So the real gap isn't "no numeric threshold exists" — it's that **4.2.d's 80-word threshold was apparently not what actually gated verbatim-vs-shortened behavior for these 6 cases**: the organize_general_knowledge step's own output for CS0987859 doesn't show whether it was passed verbatim or trimmed (I did not diff its specific entry text against the raw resume word-for-word — worth doing before picking a number, since CS0987859 is your one real test case for the boundary). If you want a defensible standalone number independent of the word-based 4.2.d exception, sentence-count is the tightest of the three signals here (4–8 across the sample, versus 486–840 chars and 72–116 words) and least prone to the single-unwrapped-line failure mode you flagged, since it doesn't depend on line breaks at all.

---

## 6. Duplicate-resume findings (Item D)

**No exact duplicate resumes** among the 6 cases. Longest common prefix between any pair: **14 characters**, between CS0985286 and CS0977930 (`"The support a`), i.e. two resumes that both happen to open the same way and then diverge immediately — not a near-duplicate in any meaningful sense. Every other pair shares 0–13 characters of prefix.

Based on this one sample, an exact-match test would have caught the case the spec is written to protect against (identical resumes = tool defect), and near-duplicates were not observed. That's a single data point, though — I did not have a second account/run with a genuine near-duplicate to test against, so I can't rule out near-duplicates occurring in practice elsewhere; I'd treat "exact match is sufficient" as provisional rather than proven.

The spec's actual duplicate rule (quoted in full, from the self-check bullet list in order=200 `metadata`): *"If two or more cases carry an identical resume, treat that as a tool defect: do NOT present the duplicated text. State that summaries could not be reliably generated for this account and stop. Cases handled under 4.2.b or 4.2.c are exempt from this check."* — exact-match only, no fuzzy-match language anywhere in the spec.

**Side finding, not asked for but relevant:** the raw `resume` field returned by the "Get active cases from Account" tool already contains the literal placeholder text `"[REDACTED]"` in place of individual names in some cases (confirmed in CS0973587's resume — "The user [REDACTED] confirmed...", "Support analyst [REDACTED] suggested..."), and this same `[REDACTED]` text passes through verbatim into the organize_general_knowledge output and the final user-facing message. Five of the six resumes do **not** contain `[REDACTED]` at all — so redaction is not applied uniformly by whatever generates `resume`, it's present only where the source text apparently named someone. This is upstream tool behavior, not anything the agent or this audit did.

---

## 7. Double-cycle plan analysis (Item E)

**Plan:** `6e6def1ec38b0b10bf79bc3ed4013158` — this is a **different execution plan** from the one audited above.

**The 4 tool executions**, in order, with request payloads:

| # | tool | request payload | timestamp (epoch ms) |
|---|---|---|---|
| 1 | Search Account | `{"account_name_or_number":"Superdry"}` | 1788427488740 |
| 2 | Get active cases from Account | `{"account_sys_id":"520b3636db4b50505d62571cd3961991"}` | 1788427519186 |
| 3 | Search Account | `{"account_name_or_number":"Gemeente Deurne"}` | 1788427579860 |
| 4 | Get active cases from Account | `{"account_sys_id":"dece780a87aa89d044d4a9740cbb3532"}` | 1788427604313 |

**This was two separate, sequential lookups in one conversation — not a re-selection.** The two `Search Account` calls used two entirely different account name strings ("Superdry" vs. "Gemeente Deurne"), not the same name with a different candidate picked from one result set. The message trail confirms the shape explicitly:

1. Orchestrator delegates: *"Retrieve the partner case summaries for the client account name Superdry."*
2. Search Account → account confirmed → **"SUPERDRY PLC has no active cases at present."** (zero cases — the first lookup came back empty)
3. Agent offers another lookup; user says yes and gives a new name.
4. Orchestrator delegates: *"Retrieve the partner case summaries for the client account name Gemeente Deurne."*
5. Search Account → account confirmed → **"Active cases for Gemeente Deurne (6)"** — the same 6 cases seen in the audited plan.

**Ordered task list** (26 rows total, more than the single-lookup plan's 21 because of this second cycle):
```
50  access_verification  Partner Case Lookup            success
100 gen_ai ×3                                            success
100 agent   Orchestrator                                 success
200 tool    Search Account                               success   (Superdry)
200 communicator Get user input unrefined                success
200 agent   Summarize Partner Cases                      success
300 gen_ai                                                success
300 agent   Orchestrator                                 success
300 gen_ai                                                success
400 communicator Get user input unrefined                success
400 agent   Summarize Partner Cases                      CANCELLED  ← anomaly, see below
400 gen_ai                                                success
500 agent   Orchestrator                                  CANCELLED  ← anomaly, see below
500 gen_ai                                                success
600 tool    Get active cases from Account                success   (Superdry → 0 cases)
700 gen_ai                                                success
800 communicator Get user input unrefined                success
900 gen_ai                                                success
1000 tool   Search Account                                success   (Gemeente Deurne)
1100 gen_ai                                                success
1200 communicator Get user input unrefined                success
1300 gen_ai                                                success
1400 tool   Get active cases from Account                success   (Gemeente Deurne → 6 cases)
1500 gen_ai                                                success
```

**Anomaly worth flagging separately from your question:** there are two `status=cancelled` task rows sandwiched between the two account cycles — order=400 "Summarize Partner Cases" (`output={}`, so it never produced any scratchpad — cancelled essentially at/before starting) and order=500 "Orchestrator" (`output` has a partial 1-cycle scratchpad, so it had started reasoning before being cancelled). Both sit chronologically *after* the Superdry Search Account/Get-cases tool calls succeeded and *before* the "SUPERDRY PLC has no active cases" message was shown. This looks like the platform started a run, cancelled/restarted it mid-flight, and the already-dispatched tool calls' results survived the restart — consistent with the user editing or re-sending something the platform then interrupted and resumed, but I did not have enough information (no error reason field was populated on the cancelled rows) to confirm the actual cause. Flagging it because it directly bears on your path-check design: **a real conversation can contain in-flight cancellation/retry of the Orchestrator/agent layer even while individual tool calls still complete and get recorded**, so a naive "count tool-execution rows" check could over-count if it doesn't also account for cancelled agent/orchestrator wrapper tasks.

**Design implication for your path check:** count/detect invocations of the Search-Account→Get-cases pair, don't assume a single-shot pattern. A user asking about two different accounts in one conversation is legitimate and produces exactly this shape (two full tool-pair cycles, two different account names, two different final case lists). Your check needs to distinguish that from a true re-selection (same account name, one Search Account call, a picked candidate) and from the cancellation/retry noise illustrated above.

---

## 8. Parser tool / eval backing (Item F)

**No `sn_aia_tool` record matches `nameLIKEparser`.** Confirmed — zero rows.

**No SkillKit-prefixed tables exist.** Confirmed — `sn_nask*`, `sn_skillkit*`, and `labelLIKE'Skill Kit'` all return zero rows against `sys_db_object`. The actual scoped app is named **"AI Skill Kit"** but its technical **scope is `sn_skill_builder`**, not `sn_skillkit` or `sn_nask` — that's almost certainly why those searches came up empty; the naming convention doesn't match the product name.

**Evaluation Results Dashboard** (`/now/now-assist-skillkit/evaluation-results-dashboard/cbbf3561c38b0b50bf79bc3ed401317d`) — confirmed: "Evaluated records 0/9", Agentic workflow/Version/Dataset/Description all blank in the UI.

- **Backing table: `sys_one_extend_batch_run`** (scope `sn_skill_builder`, label "OneExtend Batch Run" — part of ServiceNow's shared cross-product GenAI batch/evaluation framework, not something specific to Now Assist Skill Kit). The dashboard's URL sys_id is that table's primary key; the record exists and reads:
  ```json
  {"name":"Clone1 of AutoEval-[REDACTED]-2026-08-31-17:29:38","status":"completed",
   "evaluation_type":"agentic_ai","run_type":"eval_run",
   "usecase_version_table":"sn_aia_version",
   "test_dataset":"cfbf3561c38b0b50bf79bc3ed401317a",
   "query_override":"auto_chat_task.configuration=c3bf3561c38b0b50bf79bc3ed4013195^status=complete",
   "parent":"3212a1e9c3830b50bf79bc3ed40131b7"}
  ```
  (`[REDACTED]` above stands for a username embedded in the auto-generated record name — the record's `sys_updated_by` is the account currently running this audit, i.e. this batch run was created by you, not a third party, but I've redacted the literal string per your instruction.)
- **The 9 records**: `query_override` is the literal answer — it's an encoded ServiceNow query against **`auto_chat_task`**: `configuration=c3bf3561c38b0b50bf79bc3ed4013195^status=complete`. Running that exact query returns **exactly 9 rows**. That's your "9".
- **The "0" is contradicted by the data.** The batch run record's own `status` field is `"completed"`, and I found **60** rows in `sys_one_extend_eval_metric_result` and at least 10 (capped by my query, likely more) in `sys_one_extend_batch_result` that reference `batch_run=cbbf3561c38b0b50bf79bc3ed401317d`. That is real, populated evaluation-result data tied to this exact batch run — the dashboard's "0/9" figure does not match what's actually stored. Whatever the "Evaluated records" column is counting, it is not counting rows in either of those two result tables, or the count logic is stale/broken relative to a `status="completed"` run. I'd treat "0/9" as a UI display bug rather than ground truth that nothing was evaluated — plan your metric against the underlying `sys_one_extend_eval_metric_result`/`sys_one_extend_batch_result` data, not the dashboard number.

**`AgenticExecutionParserTool` search — this is the most important correction in this whole audit.** No script include, UI page, or other record named exactly `AgenticExecutionParserTool` exists anywhere (confirmed via name search on `sys_script_include` and `sys_ui_page`; a `sys_metadata` name search wasn't usable — that table's `name` field doesn't correspond to a meaningful per-record filter the way it does on concrete tables, so I'm not treating that particular check as conclusive either way). But a **very close cousin exists and is directly relevant**: `sys_script_include` **`AgenticEvalParserTool`** (`sys_id cbae77c0ff35221086adffffffffff1a`, `api_name sn_skill_builder.AgenticEvalParserTool`, scope `sn_skill_builder`). Its own source code contains this comment, which is the one and only hit for the literal string "AgenticExecutionParserTool" anywhere I searched:

> `// matching input param name: 'executionplansysid' with 'AgenticExecutionParserTool' definition attribute name as that pattern is followed for tools in general and to avoid unnecessary issues.`

So "AgenticExecutionParserTool" is a real, intentional naming reference inside this system — just not the name of *this* script include. It's most plausibly the name of a tool/attribute definition elsewhere (e.g., a tool record consumed by an evaluator, matching this script's `executionplansysid` input parameter name) rather than a script include or UI page. I did not find that second record under any of the table types checked; if it exists it may be under a table type outside `sys_script_include`/`sys_ui_page`/`sys_metadata` (e.g. a `sys_aia_tool`-style definition record, or a REST/scripted-endpoint definition), which is out of scope for what was asked but worth a follow-up query if you need it.

**The payload shape** (full, verbatim, since this is exactly what you asked for): `AgenticEvalParserTool.getExecutionEval(executionplansysid)` calls `sn_skill_builder.AIAAPIService.getCompleteExecutionEval(executionplansysid)`, flattens it via its own `_getFlattenedExecutionEval()`, and returns (wrapped via `aiaAPIService.wrapSuccessObject()`):
```
{
  executionInputs: {
    agenticWorkflow,      // usecase.use_case_name
    description,          // usecase.description
    instructions,         // usecase.instructions
    utterance,             // usecase.utterance
    agents: [{
      name,                // agent.agent_name
      instructions,        // agent.details.instructions
      tools: [{ name, description, ... }]   // agent.details.tools
    }]
  },
  executionOutputs: {
    agents: [{
      name,                // agent.agent_name
      subTask,             // agent.agent_subtask
      tools: [{ name, inputs, output }]   // from agent.execution_state, filtered to event_type==="tool", sorted by tool_order
    }]
  },
  executionMessages: <sn_skill_builder.AIAAPIService.getConversationChatDetails(executionplansysid) || []>,
  executionPlanDetails: <sn_skill_builder.AIAAPIService.executionPlanDetails(executionplansysid) || {}>
}
```
On error it returns `aiaAPIService.wrapErrorObject({}, "Error in retrieving execution plan for execution plan - ${executionplansysid}: ${e.toString()}")`.

None of these field names (`tool_name`/`tool_inputs`/`tool_output`/`agent_name`/`agent_subtask`/`execution_order`/`tool_order`) match `CASE_OUTPUT`/`CASES_FOUND`/etc. either — this reinforces §2's conclusion from a completely independent angle: the platform's own evaluation-payload builder has no concept of your named variables, so any metric built on top of this parser tool will face exactly the same "reconstruct from tool output + scratchpad" problem as reading the raw execution_task table directly.

---

## Summary of things that contradict an assumption in the original brief

1. **4.2.e's line cap is not the only threshold in the spec** — 4.2.d already has a ~80-word verbatim exception. Your "a line-based check can never trip" framing is right about lines, but the spec anticipated the unwrapped-line problem with a word-count fallback you may not have accounted for.
2. **The "Known structure" table's message-shape row is only half-true** — it describes FALLBACK/choice messages, not the terminal Finish narration messages, both of which are `role=agent, type=""`.
3. **`sn_aia_message` has no `conversation` field** — the working conversation-scoping field is `execution_plan`, and the 403 you'd get querying `conversation=` is a "field doesn't exist" error dressed up as a permissions error, not an actual ACL restriction.
4. **The double-cycle plan has two genuinely cancelled task rows** mid-sequence that aren't mentioned anywhere in the brief — real in-flight cancellation/retry noise that any path-conformance check needs to tolerate.
5. **The Evaluation Results Dashboard's "0/9" doesn't match the underlying data** — the batch run is `status=completed` and has 60+ metric-result rows against it. Whatever "Evaluated records" counts, it isn't counting from `sys_one_extend_eval_metric_result` or `sys_one_extend_batch_result` correctly (or at all).
6. **"AgenticExecutionParserTool" doesn't exist as a record name, but is a deliberate naming reference inside `AgenticEvalParserTool`'s source** — the two are related but not the same object, and the real payload shape came from the *existing* script, not the literally-named one you searched for.
