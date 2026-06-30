---
title: Corrective actions
description: Corrective action enables you to address the asset issue, either by eliminating or replacing the asset.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-corrective-actions.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a campaign, Recall management, Agent management, Use, Manufacturing Commercial Operations]
---

# Corrective actions

Corrective action enables you to address the asset issue, either by eliminating or replacing the asset.

## Before you begin

Role required: sn\_rcl\_claim\_mgmt.recall\_manager

## Procedure

1.  Navigate to **Workspaces** &gt; **CSM/FSM Configurable Workspace** &gt; **Lists** &gt; **[[mco-recall-management|Recall Management]]** &gt; **My Campaigns**.

2.  Select the corresponding campaign record in which you want to [[mco-corrective-action|create a corrective action]].

3.  Select **Corrective Actions**.

4.  Select **New**.

5.  On the corrective action form, fill in the fields.

    For a description of the field values, see [[mco-corrective-action-form|Corrective action form]].

6.  Select **Save**.

    **Ready to use** option is displayed.

    **Note:** At least one "In use" corrective action is required to initiate the [[mco-rcl-clms|recall campaign]] to In-progress.

    Corrective action must contain at least one action charge line to move it to In use.


-   **[[mco_corrective_action_charges|Corrective action charges]]**  
Create correction action charges to enable the expenses incurred to address a non-conformance and implement measures to help prevent its recurrence.
-   **[[mco-part-requirements|Generate a part requirement]]**  
Capture all the part requirements at the campaign level.

**Parent Topic:**[[mco-rc-my-campaigns|Create a campaign]]

## Related

- [[mco-corrective-action-form|Corrective action form]]
- [[mco_corrective_action_charges|Corrective action charges]]
- [[mco-part-requirements|Generate a part requirement]]
- [[mco-rc-my-campaigns|Create a campaign]]
- [[mco-recall-management|Recall management]]
- [[mco-corrective-action|Create a corrective action]]
- [[mco-rcl-clms|Recall campaign]]
