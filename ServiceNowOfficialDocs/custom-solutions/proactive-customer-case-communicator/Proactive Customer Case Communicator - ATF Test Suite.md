---
title: PCCC — ATF Test Suite
tags:
  - servicenow
  - atf
  - testing
  - now-assist
  - csm
  - proactive-customer-case-communicator
  - custom-solutions
scope: sn_csm_ai_agents
suite: PCCC – Deterministic Regression
created: 2026-07-16
---

# PCCC — ATF Test Suite

Automated regression for the **deterministic layer** of [[Proactive Customer Case Communicator]]: [[caseUpdateAgentUtil]], [[Resolve routing decision and template selection]], [[AIPF_Flag Cases on Problem State or Work]], and the counter/cooloff logic. This is the regression net for future template edits.

> [!info] Scope boundary
> ATF asserts on deterministic output only. The LLM drafting (worknote synthesis, semantic dedup, title, 7.8 option pick) and the [[Now Assist Panel]] approval flow are **not** covered here — those are manual. See [[PCCC - Testing - ATF Build & Manual Runbook]] Part B.

---

## 0. One-time prerequisites

1. **Enable ATF execution** (non-production only): *All → Automated Test Framework → Administration → Properties* → set **"Enable test execution"** (`sn_atf.runner.enabled`) = **true**. Never enable on PROD.
2. **Roles:** `atf_test_designer` (build) + `atf_test_admin` (manage/suites). `admin` covers both.
3. **Scope:** set every test's **Application** field to **`sn_csm_ai_agents`** so it can instantiate `caseUpdateAgentUtil` and read the scoped tool. Cross-scope reads of `problem` / `sn_customerservice_case` are fine.
4. **Test data hygiene:** ATF Record Insert steps auto-roll-back after the run, so test-created Problems/Cases/Work Items are cleaned up. Never point write-tests at real records.

---

## 1. Suite structure

Create one **Test Suite**: `PCCC – Deterministic Regression`, containing:

1. [[#T1 — Template registry integrity]]
2. [[#T2 — Routing decision matrix]] (+ [[#T2a — caseRoutingUtil Script Include]] prerequisite)
3. [[#T3 — Business Rule case flagging]]
4. [[#T4 — Counter & cooloff mechanics]]

Keep the suite inside the PCCC update set so it travels with the app.

---

## T1 — Template registry integrity

**Purpose:** regression-check every future template edit in seconds — presence, no leftover tokens, first-name greeting + sign-off, greeting word, `reset_count` contract, no false active-work claim.

**Single step — Run Server Side Script:**

```javascript
(function(outputs, steps, params, stepResult) {
    var u = new caseUpdateAgentUtil();
    // fixed sample inputs — full names so we can prove first-name extraction
    var t = u._buildTemplates('Jane Doe', 'CS0012345', 'ERP Cloud', 'Pedro Silva', 'PRB0040001');

    var ids = ['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','7.10.1','7.10.2'];
    var expectReset = {
        '7.1':'skip','7.2':'skip','7.3':'true','7.4':'true','7.5':'true',
        '7.6':'true','7.7':'true','7.8':'true','7.9':'true',
        '7.10.1':'false','7.10.2':'false'
    };
    var hiTemplates = {'7.5': true};   // greeting is "Hi", not "Dear"

    var problems = [];

    ids.forEach(function(id) {
        var tpl = t[id];
        if (!tpl) { problems.push(id + ': MISSING'); return; }

        var full = String(tpl.greeting) + String(tpl.body) + String(tpl.sign_off);

        // (a) no unresolved Z-style {{ }} tokens
        if (/\{\{[^}]+\}\}/.test(full))
            problems.push(id + ': leftover {{token}}');

        // (b) first-name greeting (contains "Jane", NOT "Jane Doe")
        if (tpl.greeting.indexOf('Jane') === -1)
            problems.push(id + ': greeting missing first name');
        if (tpl.greeting.indexOf('Jane Doe') !== -1)
            problems.push(id + ': greeting used FULL name');

        // (c) sign-off first name (contains "Pedro", NOT "Pedro Silva")
        if (tpl.sign_off.indexOf('Pedro') === -1)
            problems.push(id + ': sign_off missing first name');
        if (tpl.sign_off.indexOf('Pedro Silva') !== -1)
            problems.push(id + ': sign_off used FULL name');

        // (d) correct greeting word (Hi vs Dear)
        var wantHi = !!hiTemplates[id];
        var isHi = tpl.greeting.indexOf('Hi ') === 0;
        if (wantHi !== isHi)
            problems.push(id + ': greeting word wrong (Hi/Dear)');

        // (e) reset_count contract
        if (String(tpl.reset_count) !== expectReset[id])
            problems.push(id + ': reset_count=' + tpl.reset_count + ' expected ' + expectReset[id]);

        // (f) no false active-work claim on 7.7 / 7.10.2 (Z rewrite requirement)
        if ((id === '7.7' || id === '7.10.2') && /actively working|working on it/i.test(tpl.body))
            problems.push(id + ': contains active-work claim (Z rewrite forbids)');
    });

    if (problems.length) {
        stepResult.setOutputMessage('FAIL (' + problems.length + '): ' + problems.join('  |  '));
        stepResult.setFailed();
    } else {
        stepResult.setOutputMessage('All 11 templates pass: tokens, first-name, greeting, reset_count, no active-work claim.');
        stepResult.setSuccess();
    }
})(outputs, steps, params, stepResult);
```

> [!tip] Maintenance
> New template (e.g. a future 7.11) → add its id to `ids` and `expectReset`. That's the whole cost.

> [!info] 2026-07-24 — first-name assertions now match a real code change, not just a naming convention
> This test's first-name checks (`(b)`/`(c)` above) were already asserting greeting/sign-off use first name only, before that was actually true in the live `_buildTemplates()` implementation. As of 2026-07-24, the live Script Include was updated with new `cnFirst`/`caFirst` helpers to actually match this test's assumption, and bodies `7.3`/`7.4`/`7.5`/`7.6`/`7.7`/`7.8`/`7.10.2` were rewritten verbatim per a canonical template sheet. Re-run T1 against the live instance to confirm the rewritten bodies still pass token/greeting/reset_count checks — this test wasn't changed, but what it's asserting against was. See [[Proactive Customer Case Communicator#17. Changelog]].

---

## T2 — Routing decision matrix

**Purpose:** prove the deterministic router picks the right `routing_decision` / `selected_template` / `append_*` per input combination.

> [!warning] Prerequisite — extract the router into a Script Include (done)
> `Resolve routing decision and template selection` is an AI Agent tool (`sn_aia_tool`) whose logic is an inline IIFE — ATF can't call it as-is. The logic has been moved verbatim into the scoped Script Include **[[caseRoutingUtil]]** (see [[#T2a — caseRoutingUtil Script Include]] below), and the tool now delegates to it, so tool + test share one code path.

> [!note] Real inputs & values
> The router reads **snake_case** keys off an `inputs` object — `problem_linked`, `case_state`, `is_first_linkage`, `implied_state`, `problem_state`, `resolution_code`, `workaround_pending`, `new_worknote_available`, `wi_required`, `has_work_item`, `last_template_style`. Note `has_work_item` (not `wi_exists`). Resolution values are **title-case strings**: `'Risk Accepted'`, `'Duplicate'`, `'Fix Applied'`, `'Canceled'`.

**Single step — Run Server Side Script:**

```javascript
(function(outputs, steps, params, stepResult) {
    var r = new caseRoutingUtil();
    var fails = [];

    function check(label, inputs, wantDecision, wantTemplate, wantAppendWA, wantAppendWN) {
        var o = r.resolve(inputs);
        if (o.routing_decision !== wantDecision)
            fails.push(label + ': decision=' + o.routing_decision + ' want ' + wantDecision);
        if (wantTemplate !== undefined && o.selected_template !== wantTemplate)
            fails.push(label + ': template=' + o.selected_template + ' want ' + wantTemplate);
        if (wantAppendWA !== undefined && o.append_workaround !== wantAppendWA)
            fails.push(label + ': append_workaround=' + o.append_workaround + ' want ' + wantAppendWA);
        if (wantAppendWN !== undefined && o.append_worknote !== wantAppendWN)
            fails.push(label + ': append_worknote=' + o.append_worknote + ' want ' + wantAppendWN);
    }

    // ---- Gate 1 — no problem linked ----
    check('G1 no problem / awaiting', {problem_linked:false, case_state:'Awaiting Customer Info'}, 'STOP_GATE1', '7.2');
    check('G1 no problem / other',    {problem_linked:false, case_state:'In Progress'},           'STOP_GATE1', '7.1');

    // ---- Resolution guard (title-case) ----
    check('res Risk Accepted', {problem_linked:true, resolution_code:'Risk Accepted'}, 'STOP', null);
    check('res Duplicate',     {problem_linked:true, resolution_code:'Duplicate'},     'STOP', null);

    // ---- Closed + Canceled special-case (BEFORE the WI gate) ----
    check('Closed+Canceled', {problem_linked:true, problem_state:'Closed', resolution_code:'Canceled'}, '6B', '7.8');

    // ---- Gate 3 — WI required, none linked ----
    check('FIP no WI', {problem_linked:true, problem_state:'Fix in Progress', wi_required:true, has_work_item:false}, 'STOP', null);

    // ---- 6A first linkage ----
    check('6A New',                 {problem_linked:true, is_first_linkage:true, problem_state:'New'},                 '6A', '7.3');
    check('6A Assess',              {problem_linked:true, is_first_linkage:true, problem_state:'Assess'},              '6A', '7.3');
    check('6A RCA',                 {problem_linked:true, is_first_linkage:true, problem_state:'Root Cause Analysis'}, '6A', '7.6');
    check('6A FIP + WI',            {problem_linked:true, is_first_linkage:true, problem_state:'Fix in Progress', wi_required:true, has_work_item:true}, '6A', '7.7');
    check('6A Resolved/FixApplied', {problem_linked:true, is_first_linkage:true, problem_state:'Resolved', resolution_code:'Fix Applied', wi_required:true, has_work_item:true}, '6A', '7.5');

    // ---- 6B state changed (implied_state present but != problem_state) ----
    check('6B -> RCA',                 {problem_linked:true, is_first_linkage:false, implied_state:'New',                 problem_state:'Root Cause Analysis'}, '6B', '7.6');
    check('6B -> FIP',                 {problem_linked:true, is_first_linkage:false, implied_state:'Root Cause Analysis', problem_state:'Fix in Progress', wi_required:true, has_work_item:true}, '6B', '7.7');
    check('6B -> Resolved/FixApplied', {problem_linked:true, is_first_linkage:false, implied_state:'Fix in Progress',     problem_state:'Resolved', resolution_code:'Fix Applied', wi_required:true, has_work_item:true}, '6B', '7.5');
    check('6B no implied_state',       {problem_linked:true, is_first_linkage:false, problem_state:'Fix in Progress', wi_required:true, has_work_item:true}, '6B', '7.7');

    // ---- 6C state unchanged (implied_state === problem_state) ----
    check('6C workaround',   {problem_linked:true, is_first_linkage:false, implied_state:'Fix in Progress', problem_state:'Fix in Progress', wi_required:true, has_work_item:true, workaround_pending:true},  '6C', '7.4', false, false);
    check('6C new worknote', {problem_linked:true, is_first_linkage:false, implied_state:'Fix in Progress', problem_state:'Fix in Progress', wi_required:true, has_work_item:true, workaround_pending:false, new_worknote_available:true}, '6C', '7.9', false, false);
    check('6C follow-up',    {problem_linked:true, is_first_linkage:false, implied_state:'Resolved', problem_state:'Resolved', resolution_code:'Fix Applied', wi_required:true, has_work_item:true, workaround_pending:false, new_worknote_available:false}, '6C', '7.10.1');
    check('6C nothing new',  {problem_linked:true, is_first_linkage:false, implied_state:'Fix in Progress', problem_state:'Fix in Progress', wi_required:true, has_work_item:true, workaround_pending:false, new_worknote_available:false}, '6C', '7.10.2');

    // ---- append/fill derivation (state template also carrying content) ----
    check('6B + append workaround', {problem_linked:true, is_first_linkage:false, implied_state:'New', problem_state:'Fix in Progress', wi_required:true, has_work_item:true, workaround_pending:true}, '6B', '7.7', true, false);
    check('6B + append worknote',   {problem_linked:true, is_first_linkage:false, implied_state:'New', problem_state:'Fix in Progress', wi_required:true, has_work_item:true, new_worknote_available:true}, '6B', '7.7', false, true);

    // ---- Safety fallback ----
    check('fallback undetermined', {problem_linked:true, is_first_linkage:false, implied_state:'New', problem_state:'SomethingUnmapped'}, 'STOP', null);

    if (fails.length) { stepResult.setOutputMessage('FAIL (' + fails.length + '): ' + fails.join('  |  ')); stepResult.setFailed(); }
    else { stepResult.setOutputMessage('Routing matrix OK (22 cases)'); stepResult.setSuccess(); }
})(outputs, steps, params, stepResult);
```

Each row is one branch of the routing tool — add rows as branches change.

> [!caution] Known asymmetry — do not "fix" in the test
> `6A` has a `New || Assess` branch, but **`6B` has no `Assess` branch** and no generic fallback, so a 6B routed with `problem_state='Assess'` hits the safety `STOP`. The matrix is written around this: `6A Assess` asserts `7.3`; there is deliberately no `6B Assess → 7.3` row. This mirrors the live tool exactly.
>
> **Status as of 2026-07-24**: re-confirmed still present in the live routing tool during a separate debugging session (see [[Proactive Customer Case Communicator#17. Changelog]]) — a Problem at `Assess` routed through `6B` still produces no customer message at all. Logged there as an open bug to fix, not a permanent design decision. This test matrix should keep matching live behavior (i.e. still no `6B Assess` row) until that fix actually ships — then this caution box and the T2 matrix both need updating together.

---

## T2a — caseRoutingUtil Script Include

The routing logic, lifted verbatim from the tool IIFE into a callable, scoped Script Include. **Create in scope `sn_csm_ai_agents`, Client callable = false.** Then point the tool at it (see the delegation snippet after the code).

> [!info] Behaviour-preserving
> Same gate order, same string comparisons, same return shape. Only structural change: `inputs` is a method argument instead of a closure variable.

> [!warning] Drift as of 2026-07-24 — this embedded script no longer matches the live routing tool
> On 2026-07-24 a new **workaround-only-change override gate** was added to the live [[Resolve routing decision and template selection]] tool: when `WORKAROUND_ONLY_LATEST_CHANGE` is true, template `7.4` fires directly, ahead of the `6A`/`6B`/`6C` decision block shown below (see [[Proactive Customer Case Communicator#7. Deterministic Routing]] and [[Proactive Customer Case Communicator#17. Changelog]]). The `resolve()` implementation embedded below does **not** yet include this gate — re-sync this Script Include (and add a T2 test row for the new gate) before trusting T2 as full coverage of live routing behavior.

```javascript
var caseRoutingUtil = Class.create();
caseRoutingUtil.prototype = {
    initialize: function() {},

    /**
     * Deterministic routing + template selection. Pure function — no reads/writes.
     * @param {Object} inputs  problem_linked, case_state, is_first_linkage,
     *   implied_state, problem_state, resolution_code, workaround_pending,
     *   new_worknote_available, wi_required, has_work_item, last_template_style
     * @return {Object} { success, routing_decision, selected_template,
     *   append_workaround, append_worknote, fill_worknote_token,
     *   fill_workaround_token, [stop_reason] }
     */
    resolve: function(inputs) {
        inputs = inputs || {};

        var isFirstLinkage = inputs.is_first_linkage;
        var impliedState = inputs.implied_state || null;
        var problemState = inputs.problem_state || '';
        var resolutionCode = inputs.resolution_code || '';
        var workaroundPending = inputs.workaround_pending;
        var newWorknoteAvailable = inputs.new_worknote_available;
        var lastTemplateStyle = inputs.last_template_style || null; // reserved

        // Gate 1 — No problem linked
        var problemLinked = inputs.problem_linked;
        if (problemLinked === false || problemLinked === 'false') {
            var caseState = inputs.case_state || '';
            if (caseState.indexOf('Awaiting') !== -1) {
                return this._out('STOP_GATE1', '7.2');
            }
            return this._out('STOP_GATE1', '7.1');
        }

        // Resolution guard — Risk Accepted / Duplicate
        if (resolutionCode === 'Risk Accepted' || resolutionCode === 'Duplicate' ||
            resolutionCode.toLowerCase() === 'risk accepted' ||
            resolutionCode.toLowerCase() === 'duplicate') {
            return this._stop('No communication required — Problem resolution code is ' +
                resolutionCode + '. Case update skipped.');
        }

        // Gate 2b — Closed + Canceled (before WI gate)
        if (problemState === 'Closed' && resolutionCode === 'Canceled') {
            return this._out('6B', '7.8');
        }

        // Gate 3 — Work Item required but not linked
        var wiRequired = inputs.wi_required;
        var hasWorkItem = inputs.has_work_item;
        if ((wiRequired === true || wiRequired === 'true') &&
            (hasWorkItem === false || hasWorkItem === 'false')) {
            return this._stop('No Work Item linked to Problem. Communication cannot be ' +
                'sent until a Work Item is linked. Please review.');
        }

        // Routing decision
        var routingDecision;
        if (isFirstLinkage === true || isFirstLinkage === 'true') {
            routingDecision = '6A';
        } else if (!impliedState || impliedState === 'null') {
            routingDecision = '6B';
        } else if (problemState === impliedState) {
            routingDecision = '6C';
        } else {
            routingDecision = '6B';
        }

        // Template selection
        var selectedTemplate;

        if (routingDecision === '6A') {
            if (problemState === 'New' || problemState === 'Assess') {
                selectedTemplate = '7.3';
            } else if (problemState === 'Root Cause Analysis') {
                selectedTemplate = '7.6';
            } else if (problemState === 'Fix in Progress') {
                selectedTemplate = '7.7';
            } else if ((problemState === 'Resolved' || problemState === 'Closed') &&
                resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            }
        } else if (routingDecision === '6B') {
            if (problemState === 'New') {
                selectedTemplate = '7.3';
            } else if (problemState === 'Root Cause Analysis') {
                selectedTemplate = '7.6';
            } else if (problemState === 'Fix in Progress') {
                selectedTemplate = '7.7';
            } else if (problemState === 'Resolved' && resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            } else if (problemState === 'Resolved' && resolutionCode === 'Canceled') {
                selectedTemplate = '7.8';
            } else if (problemState === 'Closed' && resolutionCode === 'Fix Applied') {
                selectedTemplate = '7.5';
            }
        } else if (routingDecision === '6C') {
            if (workaroundPending === true || workaroundPending === 'true') {
                selectedTemplate = '7.4';
            } else if (newWorknoteAvailable === true || newWorknoteAvailable === 'true') {
                selectedTemplate = '7.9';
            } else if (impliedState === 'Resolved' &&
                (resolutionCode === 'Canceled' || resolutionCode === 'Fix Applied')) {
                selectedTemplate = '7.10.1';
            } else {
                selectedTemplate = '7.10.2';
            }
        }

        // Safety fallback — never return undefined template
        if (!selectedTemplate) {
            return this._stop('Template could not be determined for problem_state: ' +
                problemState + ', resolution_code: ' + resolutionCode +
                ', routing_decision: ' + routingDecision);
        }

        var appendWorkaround = (workaroundPending === true || workaroundPending === 'true') &&
            selectedTemplate !== '7.4';
        var appendWorknote = (newWorknoteAvailable === true || newWorknoteAvailable === 'true') &&
            selectedTemplate !== '7.9';

        return {
            success: true,
            routing_decision: routingDecision,
            selected_template: selectedTemplate,
            append_workaround: appendWorkaround,
            append_worknote: appendWorknote,
            fill_worknote_token: selectedTemplate === '7.9',
            fill_workaround_token: selectedTemplate === '7.4'
        };
    },

    // ---- helpers (return shape identical to the original tool) ----
    _out: function(decision, template) {
        return {
            success: true,
            routing_decision: decision,
            selected_template: template,
            append_workaround: false,
            append_worknote: false,
            fill_worknote_token: false,
            fill_workaround_token: false
        };
    },

    _stop: function(reason) {
        return {
            success: true,
            routing_decision: 'STOP',
            selected_template: null,
            stop_reason: reason,
            append_workaround: false,
            append_worknote: false,
            fill_worknote_token: false,
            fill_workaround_token: false
        };
    },

    type: 'caseRoutingUtil'
};
```

**Tool delegation** — replace the tool's IIFE body with:

```javascript
(function(inputs) {
    return new caseRoutingUtil().resolve(inputs);
})(inputs);
```

> [!tip] Confirm the extraction before trusting T2
> Run a quick Background Script (scope `sn_csm_ai_agents`) calling `new caseRoutingUtil().resolve(...)` across a few known combinations and eyeball the output. Then draft one live NAP message through the tool — if it throws a cross-scope / `Illegal access` error, set the Script Include's **Accessible from** to *All application scopes* or add a cross-scope privilege record.

---

## T3 — Business Rule case flagging

**Purpose:** prove `AIPF_Flag Cases on Problem State or Work` flags/exits correctly. Uses native ATF record steps (auto-rolled-back).

**Per-scenario step pattern:**
1. **Record Insert — `problem`**: set `state`, `resolution_code`, `workaround` per scenario. (WI scenarios also: **Record Insert — `u_work_item`** with `parent` = the problem.)
2. **Record Insert — `sn_customerservice_case`**: `problem` = inserted problem, `active`=true, `category`=Issue (0), `state` ≠ 6, `assigned_to` = a valid active user.
3. **Record Update — `problem`**: make the triggering change so the BR fires.
4. **Record Query — `sn_customerservice_case`**: query the case; **assert** `u_problem_updated` = expected.

**Scenarios (assert `u_problem_updated`):**

| Scenario | Problem setup | WI | Expect |
|---|---|---|---|
| State → Fix in Progress, WI present | state=FIP | yes | **true** |
| State → Fix in Progress, no WI | state=FIP | no | **false** |
| State-only change → Assess | state=102 | – | **false** |
| Resolution = Risk Accepted | res=risk_accepted | – | **false** |
| Resolution = Duplicate | res=duplicate | – | **false** |
| Closed + Fix Applied | state=107, res=fix_applied | – | **false** |
| Workaround populated | workaround set, valid state | – | **true** |
| Category = Request (not 0/1) | valid state | yes | **false** |

Use the **Record Query** step's assertion tab (field `u_problem_updated`, operator `is`, value `true`/`false`).

---

## T4 — Counter & cooloff mechanics

**Purpose:** prove `_incrementAutoUpdateCount()` increments, stamps at threshold, and resets.

1. **Record Insert — `sn_customerservice_case`**: `u_auto_update_count`=0, `u_auto_update_threshold_reached` empty. Capture the number.
2. **Run Server Side Script** (threshold = 3; read from property if you want it config-driven):

```javascript
(function(outputs, steps, params, stepResult) {
    var caseNum = steps('<step1_sys_id>').record_number || params.caseNumber; // wire to your insert
    var u = new caseUpdateAgentUtil();
    var fails = [];

    u._incrementAutoUpdateCount(caseNum, false);   // -> 1
    u._incrementAutoUpdateCount(caseNum, false);   // -> 2
    u._incrementAutoUpdateCount(caseNum, false);   // -> 3, should STAMP

    var gr = new GlideRecord('sn_customerservice_case');
    gr.get('number', caseNum);
    if (gr.getValue('u_auto_update_count') != 3) fails.push('count != 3');
    if (!gr.getValue('u_auto_update_threshold_reached')) fails.push('threshold not stamped at 3');

    u._incrementAutoUpdateCount(caseNum, true);     // reset
    gr.get('number', caseNum);
    if (gr.getValue('u_auto_update_count') != 0) fails.push('reset did not zero count');
    if (gr.getValue('u_auto_update_threshold_reached')) fails.push('reset did not clear stamp');

    if (fails.length) { stepResult.setOutputMessage('FAIL: '+fails.join(' | ')); stepResult.setFailed(); }
    else { stepResult.setOutputMessage('Counter/threshold/reset OK'); stepResult.setSuccess(); }
})(outputs, steps, params, stepResult);
```

---

## 2. Run & wire into deployment

1. Run: *Automated Test Framework → Suites → PCCC – Deterministic Regression → Run*. All green before promoting.
2. **Optional:** add the suite to the AEMC/Pipelines **Application Deployment Test Suite** so it runs automatically on every deploy to TEST.
3. Keep the suite in the PCCC update set.

## Coverage

| Concern | Test |
|---|---|
| Template bodies / first-name / tokens / reset_count | T1 |
| Routing branch correctness (decision, template, append/fill) | T2 (via [[caseRoutingUtil]]) |
| BR flag/exit gates | T3 |
| Counter / threshold / reset | T4 |

Related: [[Proactive Customer Case Communicator]] · [[caseRoutingUtil]] · [[Resolve routing decision and template selection]] · [[PCCC - Template & Stale Rework - Task Plan]] · [[PCCC - Testing - ATF Build & Manual Runbook]]

#servicenow #atf #testing #now-assist #csm #custom-solutions
