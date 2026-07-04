---
title: "Transfer Order Lines Remain in Draft State and TOL Tasks Are Not Generated After Catalog Order"
aliases:
  - KB2987181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2987181
kb_number: KB2987181
last_modified: 2026-05-04
---

## Transfer Order Lines Remain in Draft State and TOL Tasks Are Not Generated After Catalog Order

  

### Issue

When ordering hardware via the Service Catalog, Transfer Orders (TO) and Transfer Order Lines (TOL) are created successfully but remain in Draft state indefinitely. No Transfer Order Line Tasks (TOL Tasks) are generated, and no error messages are displayed.

### Symptoms

-   A catalog request for a hardware item creates a TO and TOL, but both records stay in Draft state
-   The TOL's related list for TOL Tasks is empty — no tasks are created at any stage (Ready for Fulfillment, Ship, Receive, etc.)
-   The "Request" UI action does not appear on the Transfer Order
-   No error messages or log entries are visible at the default log level
-   Manually adding a Delivery Date to the TO does not trigger task creation

### Facts

-   The system property `com.sn_itam.enable_flow_designer.transfer_order_line` controls which task-creation path is used: the Flow Designer path (new) or the legacy Workflow Engine path
-   The Business Rule Transfer Order Line Flow Trigger fires on TOL insert but is wrapped in a condition that checks this property — if the property is `false`, the rule exits silently with no error
-   A fix script called TOL Workflow Deactivation is intended to set this property to `true` during upgrade or fresh install, but will intentionally leave it `false` if a customized legacy TOL workflow is detected
-   If the fix script never ran AND no legacy workflow is active, both task-creation paths are simultaneously inactive
-   The property's default value is `false`

### Release

Hardware Asset Management (BAM/HAM) — applicable to instances where the asset management plugin was activated or upgraded and the fix script `TOL Workflow Deactivation` did not execute

### Cause

The system property `com.sn_itam.enable_flow_designer.transfer_order_line` is set to `false` (its default value), and no active legacy TOL workflow exists to serve as a fallback. This leaves both task-creation paths inactive simultaneously.

This state occurs when the fix script TOL Workflow Deactivation — which is responsible for enabling the Flow Designer path and disabling the legacy workflow — did not execute during plugin installation or upgrade. The fix script may not run if the plugin was activated after its eligibility window, or if the upgrade sequence was interrupted.

### Resolution

Step 1 — Confirm the root cause

Run the following in Scripts - Background:

javascript

```
gs.print(gs.getProperty('com.sn_itam.enable_flow_designer.transfer_order_line'));
```

If the output is `false` or `null`, the property is not enabled. Proceed to Step 2.

_(Suggested screenshot placement: Scripts - Background showing the `false` output — include in this section)_

Step 2 — Enable the Flow Designer path

Before enabling, confirm no active customized legacy TOL workflow exists:

javascript

```
var gr = new GlideRecord('wf_workflow_version');
gr.addQuery('table', 'alm_transfer_order_line');
gr.addQuery('published', true);
gr.query();
while (gr.next()) {
    gs.print('Version SysID: ' + gr.getUniqueValue() + ' | Name: ' + gr.getDisplayValue('name'));
}
gs.print('Total active TOL workflow versions: ' + gr.getRowCount());
```

-   0 results — No legacy workflow active. Safe to proceed.
-   1 result — If the sys\_id matches `f1bf2a05e7c133009a610558d2f6a94b`, this is the stock workflow. Proceed.
-   1 result with a different sys\_id — A customized legacy workflow exists. Do not change the property; investigate why the legacy workflow is not generating tasks separately.

If safe to proceed, set the property:

Navigate to System Properties and set `com.sn_itam.enable_flow_designer.transfer_order_line` to `true`.

Or via Scripts - Background:

javascript

```
gs.setProperty('com.sn_itam.enable_flow_designer.transfer_order_line', 'true');
gs.print('Property set: ' + gs.getProperty('com.sn_itam.enable_flow_designer.transfer_order_line'));
```

Step 3 — Backfill TOL Tasks for existing stuck TOLs

Run the following in Scripts - Background to generate missing tasks for all non-cancelled TOLs currently in Draft:

javascript

```
new TransferOrderLineTemplateTaskAPI().createTasksForInflightTOLs();
```

To target a specific TOL only:

javascript

```
var tolSysId = '<TOL_SYS_ID>'; // Replace with the actual TOL sys_id
new TransferOrderLineHandler().triggerAction(tolSysId, 'draft');
```

Step 4 — Verify

Submit a new catalog order for a hardware item and confirm that a TOL Task appears in the TOL's related list immediately after the TOL is created.
