---
title: "Now Assist Readiness Evaluation: Architecture Deep Dive"
aliases:
  - Now Assist Readiness Evaluation Architecture
  - NARE Architecture
  - sn_assess Architecture
tags:
  - now-assist-ai
  - now-assist
  - readiness-evaluation
  - sn_assess
  - architecture
  - store-app
---

# Now Assist Readiness Evaluation: Architecture Deep Dive

*Reverse-engineered from a live ServiceNow instance via progressively deeper static code inspection (metadata counts → representative full-script reads). Not official ServiceNow documentation — see [[now-assist-readiness-evaluation-landing-page|Now Assist Readiness Evaluation]] and the rest of the official `intelligent-experiences/now-assist-readiness-evaluation/` docs for the user-facing conceptual/how-to material this note complements.*

**App:** "Now Assist Readiness Evaluation" — ServiceNow store app, scope `sn_assess`, v1.4.2, vendor ServiceNow.

---

## 1. What it does

Scans a customer instance to score its readiness to adopt Now Assist Generative AI / Agentic AI skills across ITSM (Incident, Change), CSM (Case, Triage), HRSD (HR Case), Virtual Agent/NLU, and AI Search/Knowledge Management. It detects customizations that could block skill applicability, scores each domain against a configurable threshold, estimates remediation effort ("t-shirt sizing"), and presents results in a UI Builder dashboard plus Performance Analytics dashboards, with a downloadable report.

---

## 2. Data model — rides the platform Assessment engine

No bespoke tables. Everything sits on the generic Assessment framework:

| Table | Role |
|---|---|
| `sn_assess_assessment` | Assessment definitions |
| `sn_assess_assessment_run` | One record per execution of one domain's assessment |
| `sn_assess_question` | Question bank (86 rows, shared across all 8 assessment definitions) |
| `sn_assess_answer` | Rendered answers, linked back to a run |

**Eight assessment definitions:** CSM, HRSD, ITSM, VA, AI Search (the "classic" generation) plus **Agentic AI – CSM**, **Agentic AI – HRSD**, **Agentic AI – ITSM** (a newer, parallel generation focused specifically on agentic/GenAI skill fit — confirms classic and agentic tracks run independently, not as variants of one pipeline).

### Question records are small programs, not static text

Each of the 86 question rows carries:
- A question label
- **Issue Categorization**: `Configuration Needed` / `Now Support Recommended` / `Data Readiness`
- An ordering value (display sequence)
- An optional numeric **weight** (values seen: 0.1, 0.2, 0.5) used when rolling scores up
- A **Visibility on Summary Page** flag
- An **Answer Template** — JSON with placeholder tokens, e.g. `{{conversationalStoppers}}`, `{{badKB}}`
- A **Script** field containing an actual JS function, e.g. `fetchCustomizations(assessmentResults)`, `languageUsed(assessmentResults)`, `countConversationalStoppers(assessmentResults)`, `isVALive(assessmentResults)`, `fetchTopTenItems(assessmentResults)`, `isNextExperience(assessmentResults)`, `badArticles(assessmentResults)`, `groupRestrictions`, `fieldCompletion`, `aiExperiences`, `scNames`, `kbToTarget`, `fetchOpportunityConv`, `countActiveTopics`, `automationFound`, `isAISearchLive`, `fetchHrCaseVolume`, `fetchSummary` (roll-up questions per domain, e.g. "Overall Findings" / "Virtual Agent:")

**Two full question scripts read verbatim, confirming the pattern:**

```javascript
// CSM: "Is Create Knowledge UI Action custom both in UI16 and Workspace UIs?"
function fetchCustomizations(assessmentResults) {
  var result = {
    answer: JSON.stringify(assessmentResults["kbUIActionCustomizations"]),
    effort: assessmentResults["kbUIActionCustomizations"].uiActionCustomizationDays
  };
  return result;
}
fetchCustomizations(assessmentResults);
```

```javascript
// HRSD: "What language is used in instance?"
function languageUsed(assessmentResults) {
  var languageObject = assessmentResults["HrCaseCustomization"];
  var result = { answer: JSON.stringify(languageObject.queryLanguageUsed()), effort: null };
  return result;
}
```

This is the key architectural insight: **the orchestrator/domain script include does the real `GlideRecord` work** and stashes rich sub-objects (`kbUIActionCustomizations`, `HrCaseCustomization`) into a shared `assessmentResults` context object — some of which expose their own query-style helper methods (`queryLanguageUsed()`). **Each question's own script is a thin accessor** that pulls one property or calls one method off that shared context and returns `{answer, effort}`. All 86 questions (visually reviewed) follow this exact two-tier shape — no question script does its own `GlideRecord` querying.

---

## 3. Scoring, thresholds, and effort estimation (system properties)

14 system properties total; the four that drive the actual math:

| Property | Shape | Purpose |
|---|---|---|
| `sn_assess.Threshold` | JSON map | Per-domain pass bar, percent. Current values: `itsm`, `ai_search`, `csm`, `virtual_agent`, `hrsd` all `75` |
| `sn_assess.TShirtMetric` | JSON weighting table | Assigns an estimated remediation-effort-in-days value per detectable customization type |
| `sn_assess.TShirtSize` | JSON bucket map | Buckets the summed day total into a label |
| `sn_assess.effort_visibility` | boolean | Toggles whether the effort "pill" is shown in the UI |

**`TShirtMetric` values seen** (days): `using_OOB_widgets` 2, `enable_AI_search` 6, `group_restriction` 6, `enable_virtualAgent` 1, `enable_nlu` 0.5, `unsupportedreason_remediation` 3, per-line script customization 0.0005, `table_customization` 0.0005, `resolve_workflow` 0.05, plus per-domain factors: `itsm_cat_custom_fields`, `itsm_cat_conflicting_triggers`, `itsm_cr_custom_acls`, `csm_custom_fields_effort`, `csm_business_rule_effort`, `csm_email_handling_effort`, `hrsd_cat_custom_fields`, `hrsd_cr_custom_acls`, `hrsd_cat_conflicting_triggers`.

**`TShirtSize` buckets:** small ≤5 days, medium ≤10, large ≤30, xl ≤90, xxl ≤180.

**Confirmed at runtime** (from the full `AgenticHRAssessment` read): every check computes `result.effort = totalIssues * AgenticHRAssessment.constants.TSHIRT_METRIC['hrsd_cat_custom_fields']` (or the matching key) — this is the exact runtime link back to the `TShirtMetric` property JSON, proving the weights are consumed by name, per check, at scan time. Scoring itself is **a traffic-light tally, not a percentage average**: `initialize()` on the domain evaluator just zeroes three counters (`tickCountHrsd`, `crossCountHrsd`, `warningCountHrsd`), and each check sets `result.icon = {tick:0, cross:1, warning:0}` (issue found) or `{tick:1, cross:0, warning:0}` (clean).

**Two more properties bound the scan itself:** `sn_assess.task_limit` (50) caps records sampled per table per check; `sn_assess.assessment_limit` (10000) caps overall record volume considered.

**Legacy/WIP schema property:** `sn_assess.assessment.config` stores a JSON `ASSESSMENT_SCHEMA` block, explicitly marked **"work in progress / POC"** in its own description, mapping per-domain question/answer/run table names plus the sys_ids of representative questions and a UI Action used to resolve/propose a fix. This confirms at least ITSM and CSM were originally wired through an earlier, more rigid schema-driven approach before the current script-per-question model matured — the property is a leftover of that earlier design, not the live scoring path.

**Go/No-Go display logic** (from the official docs, ties the two data models together): >75% ready → green **Ready**; ≤75% → yellow **Action Required**. Findings are auto-tagged product/data/configuration issue. Re-running the scheduled job after fixes is how the percentage moves — see [[assessing-go-no-go|Assessing readiness status]].

---

## 4. Server-side logic — Script Includes (14 total)

### 4.1 Orchestrator: `AgenticAIAssessmentRun` (full script read, ~317 lines)

The single class every scheduled job calls. Defines plugin-id constants (`PLUGIN_VA = 'com.glide.cs.chatbot'`, `PLUGIN_HRSD = 'com.sn_hr_core'`, `PLUGIN_CSM = 'com.sn_customerservice'`) and `TABLE_ASSESSMENT_RUN = 'sn_assess_assessment_run'`.

Exposes **one `executeXJob` method per domain** — more methods than domains, because classic and Agentic-AI generations run independently: `executeVAJob`, `executeItsmJob`, `executeCsmJob`, `executeHrsdJob` (classic, delegates to `HrCaseCustomizationFinder`), `executeAiSearchJob`, `executeHrsdAgenticAiJob` (newer, delegates to `AgenticHRAssessment`).

Every method follows the identical guard-then-run shape:
1. Check `GlidePluginManager.isActive(...)` for the relevant plugin
2. Check the matching `sn_assess.<domain>` property
3. On either failure → log a **failed** run with a plain-English reason (e.g. *"Virtual Agent plugins not installed"*, *"sn_assess.va property not enabled"*) — never crashes, never runs
4. On success → instantiate the domain's assessment class → `logAssessmentRun(startTime, null, "success")` opens a run record → `getAnswerDetails(sysId)` populates answers → `logAssessmentRun` again with an end time closes it out
5. Whole thing wrapped in try/catch; failures logged with `error.toString()`

Ends with `getNextRunCount` / `updateRunCountAssessmentRun`, which query the most recent `sn_assess_assessment_run` for that assessment ordered by `sys_created_on`, read its `run_count` field, and increment it — how the app knows "this is your 3rd Agentic AI CSM scan" for trend purposes.

### 4.2 A full domain evaluator: `AgenticHRAssessment` (full script read, ~700+ lines)

Constants block hardcodes: `HRSD_TABLE: 'sn_hr_core_case'`, `WORKFLOW_TABLE: 'wf_workflow'`, `FLOW_TRIGGER_TABLE: 'sys_flow_record_trigger'`, `METADATA_CUSTOMIZATION_TABLE: 'sys_metadata_customization'`, `SCRIPT_TABLE: 'sys_script'`, `SYS_ACL_SECURITY_TABLE: 'sys_security_acl'`, `DICTIONARY: 'sys_dictionary'`, `JOURNAL: 'sys_journal_field'`; pulls `INSTANCE_URL` from `glide.servlet.uri` and a parsed copy of `sn_assess.TShirtMetric`.

`initialize()` zeroes `tickCountHrsd`/`crossCountHrsd`/`warningCountHrsd`. Each question maps to one prototype method, commented with the exact question text (`/* Q1. Are there any custom fields... */`, `/* Q2. Are there custom Business Rules... */`, `/* Q6. Are there custom triggers... */`).

- **`checkHrsdTriggerConflicts` (Q6)** — `GlideRecordSecure` on `wf_workflow` filtered to the HRSD table, counts matches; same against `sys_flow_record_trigger`; either non-zero → issue icon.
- **`checkHrsdFieldDependencies` (Q1)** — hardcodes the exact field set the out-of-box Agentic AI skill depends on: `opened_for`, `opened_by`, `assignment_group`, `assigned_to`, `short_description`, `description`, `priority`, `state`, `hr_service`, plus journal fields `work_notes`, `comments` — checks each for customization.
- Volume/completion checks open `GlideRecordSecure` on `sn_hr_core_case` with `addQuery('active', true)` and `setLimit(ASSESSMENT_LIMIT)` (from `sn_assess.assessment_limit`), iterating records to build per-field fill-rate statistics.

### 4.3 Shared engine: `TableCustomizationFinder`

Marked **`Accessible from: All application scopes | public`** — unlike every other script include here (scope-private). Deliberately the one reusable class the domain-specific finders build on.

Constants block is a directory of every metadata table the app inspects: `sys_metadata_customization`, `sys_choice`, `sys_journal_field`, `sys_dictionary`, `sys_hub_flow`, `sys_ui_action`, `kb_knowledge`, `kb_knowledge_base`, `sys_security_acl`, `sys_declarative_action_assignment`, plus `INSTANCE_CLONE: 'clone_instance'`, `KBTASK_TABLE: 'm2m_kb_task'`, `MID_VERSION_PROPERTY: gs.getProperty('mid.version')`.

Pre-builds clickable base URLs (`DICTIONARY_BASE_QUERY`, `HUB_FLOW_BASE_QUERY`, `CLIENT_SCRIPT_BASE_QUERY`, `UIACTION_BASE_QUERY`, `SCRIPTS_BASE_QUERY`, `UI_POLICIES_BASE_QUERY`, `ACL_SECURITY_BASE_QUERY`, etc.), each literally `"<a href='" + INSTANCE_URL + "sys_dictionary_list.do?sysparm_query=..."` — these are what get dropped into answer templates so a customer can click straight through to "here are the 12 custom fields we found."

Constructor `initialize(tableName, tableLabel, uiActionSysId)` is instantiated once per table by each domain finder — this is the exact mechanism tying back to the `RESOLVE_UI_ACTION` / `PROPOSE_SOLUTION_UI_ACTION` sys_ids in the legacy `sn_assess.assessment.config` property: that UI Action sys_id is passed straight into this constructor so the generated answer template can link to a "fix it" UI Action on the record.

### 4.4 Other script includes

- Domain evaluators: `AgenticHRAssessment`, `CSMTriageAssessment`, `VirtualAgentAssessment`, `AISearchKMAssessment`
- Table-specific finders (built on `TableCustomizationFinder`): `IncidentCustomizationFinder`, `ChangeCustomizationFinder`, `CaseCustomizationFinder`, `HrCaseCustomizationFinder`
- UI support: `AgenticAISummaryIcons`, `AnswerTemplateFetcher`
- Report export: `GenerateDownloadReportAgenticAI`, `GenerateDownloadURL`

---

## 5. Automation

**9 Scheduled Script Executions:** one overall "GenAI/AgenticAI Assessment" job, one per classic domain ("Now Assist Assessment – AI Search/CSM/HRSD/ITSM/Virtual Agent"), and separate newer jobs "AIAgentCSMAssessment", "AIAgentHRSDAssessment", "Agntic AI Assessment – ITSM – Change Request" [sic, typo in source]. Each domain job is individually switched on/off via its `sn_assess.<domain>` property (`ai_search`, `csm`, `hrsd`, `itsm`, `va`) — an admin can disable scanning for an unused module without touching the jobs themselves.

**Flow Designer footprint:** 1 Process Definition, 4 Activity Definitions, plus Playbook input/snapshot-input records — a small footprint, likely a guided/playbook-style walkthrough rather than doing heavy lifting itself.

---

## 6. Now Assist / licensing awareness

Beyond scanning for customizations, the app cross-checks whether Now Assist skills are actually turned on **and** entitled:

- **Generative AI Skill Applicability** and **Now Assist Skill Config Var Set UI** records — inspect live skill configuration
- **"One API" entitlement records** — 17 Features, 17 Feature Providers, 13 Service Plans, 17 Service Plan Features — the platform's subscription/entitlement metadata, letting the app reason about which Now Assist skills are actually *licensed*, not just technically configured
- **AI Search records** — a Search Dictionary plus 3 Search-Profile mapping records (dictionary, Genius Result configuration, search source) — let the AI Search evaluator judge whether Knowledge/Genius Results are properly set up

---

## 7. Presentation layer (Now Experience / UI Builder)

Single **UX App Configuration** named "GenAI Assessment" (icon `activity_fill`, landing path `agentic-ai-assessment-dashboard`).

Screen inventory (**46 UX Screens**) follows a clear pattern: a top-level "Now Assist Readiness Evaluation Dashboard" + "Now Assist Assessment" screen, a "Summary" / "Summary Now Assist" results screen, and a parallel pair of per-domain screens for each module — a classic variant ("Now Assist for AI Search", "Now Assist for HRSD", "Now Assist for ITSM", "Now Assist for VA") and a newer Agentic AI variant ("Agentic AI HRSD", "Agentic AI CSM"), all nested under shared "Workspace"/"Default" wrapper screens typical of Now Experience apps.

Built from **44 Macroponent Definitions**, wired by **31 App Routes** and **47 UX Events** (8 Add-on Event Mappings), themed by **3 App Themes**, driven by **~1,080 UX Client Scripts** — large but reflects per-component/per-field interactivity typical of a data-heavy UIB dashboard, not one mega-script.

**23 Data Broker Server Scripts** feed data server→screen:
- Percentage brokers per domain ("Agentic AI CSM/HRSD/ITSM Percentage")
- Answer-template fetchers per domain ("CSM-FetchAnswerTemplates", "Now Assist HRSD-FetchAnswerTemplates", "FetchTemplateForAISearch/HRSD/ITSM/VA")
- Summary-template fetchers ("FetchCSMsummary", "FetchHRSDSummaryTemplates", "FetchITSMSummaryTemplates", "FetchVAsummary")
- Effort/report helpers ("Effort visibility", "Fetch Report Download URL", "GetDownloadURL")
- "Get Dashboards Tab" broker
- T-shirt-size helpers ("parseTShirtMetric", "updateTshirtMetrics")
- One leftover dev broker ("TestSai")

**Representative broker read in full:** "Agentic AI CSM Percentage" hardcodes the CSM Agentic AI assessment's sys_id, opens `GlideRecord('sn_assess_answer')` filtered by `assessment_run.assessment = <that sys_id>`, and sums an `effort` field across the answer rows to compute a current-vs-maximum-possible effort ratio — this is the exact number that becomes the readiness percentage shown on the dashboard tile. **Confirms data brokers never re-run assessment logic — they only read back what the script includes already wrote to `sn_assess_answer`.**

A classic UI Page/List/Form-section set (UI Policy, Filter, Choice Set) supports fallback classic views of the 4 tables.

---

## 8. Reporting layer

**7 Performance Analytics (PAR) Dashboards**, each with tabs (6 total), page canvases (7), widgets (16), and visibility rules (2) — visualize aggregated readiness scores per domain, separate from the live UI Builder screens. Useful for trend/historical reporting rather than point-in-time interactive scan results.

---

## 9. Security model

- One custom role: **`sn_assess.admin`** gates the entire app
- **56 Access Controls**: 28 record-level ACLs (standard CRUD on the 4 Assessment tables), 26 `ux_data_broker` ACLs (one per data broker — every server-side data feed individually secured), 1 `ux_route` ACL, 1 `ui_page` ACL
- **58 Access Role assignments** tie these ACLs to the admin role
- **108 Cross-Scope Privilege records** grant broad read (and a couple of execute/insert/setValue/delete) access into other scopes: `sys_dictionary`, `sys_script`, `sys_script_client`, `sys_ui_policy`, `sys_choice`, `sys_ui_page`, `sys_ui_script`, `sys_update_xml`, `sys_user`, scripting primitives (`ScriptableGlideEvaluator.putVariable`, `ScriptableRESTMessageClient.execute`, `ScopedGlideRecordSecure`, `GlideRecord.insert`/`setValue`), `kb_knowledge_base` (both globally and specifically scoped to **Human Resources: Core** — matches a pending "Restricted Caller Access" approval seen on the app record), an AI Search Genius Result configuration table, a Catalog Conversational Coverage table, and even a delete privilege on the legacy Guided Setup change log table
- One auto-generated **OAuth Entity Profile** (named after its own sys_id, Authorization Code grant type, no provider configured) — standard platform scaffolding, not a deliberate external integration

---

## 10. End-to-end flow

```text
Scheduled job (per domain, if plugin active + property enabled)
        │
Script Include scans relevant tables for customizations/config
 (TableCustomizationFinder + domain-specific finder,
  sampling up to task_limit records per check)
        │
Each question's tiny script pulls one value off the shared
 assessmentResults context → {answer, effort}
        │
Effort summed and t-shirt-sized; tick/cross/warning tallied
 against the domain's Threshold
        │
Results written to sn_assess_assessment_run / sn_assess_answer
        │
        ├──> UI Builder dashboard's Data Brokers read the answer
        │     rows live (sum effort, no re-scan) → interactive dashboard
        ├──> PAR dashboards render the same data as classic
        │     reporting widgets (trend/historical view)
        └──> Report Script Include assembles a downloadable summary
```

---

## 11. Build prompt (scaffold an equivalent app)

*This is the fully detailed version — supersedes the shorter early-pass prompts from initial metadata-count-only inspection.*

> Build a scoped ServiceNow application (scope `sn_assess`) called "Now Assist Readiness Evaluation." Reuse the platform Assessment tables only: `sn_assess_assessment`, `sn_assess_assessment_run`, `sn_assess_question`, `sn_assess_answer`. Create eight assessment definitions — CSM, HRSD, ITSM, VA, AI Search, and Agentic AI variants of CSM/HRSD/ITSM — each with its own bank of question records, where every question stores a JSON answer template with `{{placeholder}}` tokens, an issue-categorization choice (Configuration Needed / Now Support Recommended / Data Readiness), an ordering number, an optional weight, and a short JavaScript function of the shape `function checkX(assessmentResults) { return { answer: ..., effort: ... }; }` that reads one property or calls one method off a shared `assessmentResults` context object rather than doing its own querying.
>
> Build one reusable, publicly-accessible script include (`TableCustomizationFinder`) that centralizes every metadata table you're allowed to inspect (`sys_dictionary`, `sys_metadata_customization`, `sys_choice`, `sys_journal_field`, `sys_hub_flow`, `sys_ui_action`, `sys_security_acl`, `sys_declarative_action_assignment`, `sys_data_policy2`, `sys_script`, `sys_script_client`, `kb_knowledge`, `kb_knowledge_base`), pre-builds clickable drill-down URLs for each, reads its effort weights from a single JSON system property, and exposes a constructor taking `(tableName, tableLabel, uiActionSysId)` so any table-specific finder can wrap it.
>
> Build one table-specific customization-finder script include per domain (Incident, Change, Case, HR Case) on top of that engine, plus one richer domain-evaluator class per module (mirroring `AgenticHRAssessment`) whose constants block hardcodes that domain's key table and its dependent metadata tables, whose `initialize()` sets zeroed tick/cross/warning counters, and whose prototype has one commented method per question (`/* Q1... */ checkX: function() {...}`) that queries the relevant table with `GlideRecordSecure`, respects a record-sampling limit from a system property, computes `effort = issueCount * <namedWeight from the TShirtMetric property>`, and returns `result.icon = hasIssue ? {tick:0,cross:1,warning:0} : {tick:1,cross:0,warning:0}`.
>
> Build a single orchestrator script include (`AgenticAIAssessmentRun`) with plugin-id constants for each dependent plugin and one `executeXJob` method per domain (including separate methods for the classic and Agentic AI generations of the same domain), where every method: checks the domain plugin is active, checks a `sn_assess.<domain>` boolean property, on failure logs a failed assessment run with a plain-English reason, on success instantiates that domain's evaluator, calls `logAssessmentRun(start, null, "success")`, calls `getAnswerDetails(runSysId)` to populate answers, then closes the run with an end time, wrapped in try/catch that logs failures with the caught error's string. Add a run-count helper that reads the previous run's `run_count` field and increments it.
>
> Add system properties: a per-domain enable flag; a JSON per-domain pass-threshold percentage; a JSON effort-weighting table keyed by customization type (custom fields, custom ACLs, conflicting triggers/business rules, per-script-line cost, disabled OOB widgets, AI Search/Virtual Agent/NLU enablement, group restrictions, workflow resolution) expressed in days; a JSON day-to-t-shirt-size bucket map; a record-sampling limit; an overall record limit; and an effort-visibility toggle. Add one scheduled job per domain (plus per-generation variants) that simply calls the matching orchestrator method, gated by that domain's enable property.
>
> Build a Now Experience UI Builder app with a landing dashboard screen, a summary screen, and one detail screen per domain per generation, wired with routes/events, and back every percentage/answer/summary tile with a data-broker server script that opens `sn_assess_answer` filtered by `assessment_run.assessment = <assessment sys_id>` and sums the stored effort/answer values — never re-running the scan logic in the broker itself. Add a report-generation script include that assembles a downloadable summary and a URL-fetch helper for it. Secure the four Assessment tables, every data broker, and the app's route behind one custom admin role, and request cross-scope read access into every metadata table the finders touch, plus the specific foreign application (e.g., HR Core) whose tables you sample.

---

## 12. Methodology / how far this went

This is the result of static code inspection only, in increasing depth: metadata counts across all record types → full-script reads of the two most load-bearing script includes (`AgenticAIAssessmentRun`, `AgenticHRAssessment`) and the shared engine (`TableCustomizationFinder`) → one representative question script and one representative data broker script, fully read → all 86 question records visually scanned for the shared shape.

**Not yet done:** actually executing or stepping through a live assessment run (e.g., triggering `AgenticAIAssessmentRun.executeCsmJob()` in a background script and inspecting the resulting `sn_assess_answer` rows) — that's a "run code" action rather than "read code," and would be the next level of verification if this architecture understanding needs to be validated against real runtime behavior rather than inferred from source.

---

## Related

- [[now-assist-readiness-evaluation-landing-page|Now Assist Readiness Evaluation]] — official landing page
- [[exploring-now-assist-readiness-evaluation|Exploring Now Assist Readiness Evaluation]] — official product overview (agentic vs. generative AI assessment tracks, per-product benefit table)
- [[configuring-now-assist-readiness-evaluation|Configuring Now Assist Readiness Evaluation]] — official setup steps (plugin `sn_assess`, scheduled job, guided setup)
- [[assessing-go-no-go|Assessing readiness status]] — official go/no-go percentage logic (75% threshold, Ready/Action Required)
- [[platform-now-assist-landing|Now Assist]]
- [[na-ai-agents|Now Assist AI agents]]

#now-assist #readiness-evaluation #sn_assess #architecture #store-app
