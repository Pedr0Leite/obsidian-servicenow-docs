---
title: Create a campaign
description: Create a recall campaign and also view the list of campaigns claims assigned to the person who has logged in to the workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-rc-my-campaigns.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Recall management, Agent management, Use, Manufacturing Commercial Operations]
---

# Create a campaign

Create a [[mco-rcl-clms|recall campaign]] and also view the list of campaigns claims assigned to the person who has logged in to the workspace.

## Before you begin

Role required: sn\_rcl\_claim\_mgmt.recall\_manager

## Procedure

1.  Navigate to **Workspaces** &gt; **CSM/FSM Configurable Workspace** &gt; **Lists** &gt; **Recall Management** &gt; **My Campaigns**.

2.  Select **New**.

3.  On the Recall campaign form, fill in the fields.

    For a description of the field values, see [[mco-recall-campaign-form|Recall campaign form]].

4.  Select **Save**.

    The recall campaign record is created.

    The following actions are displayed:

    -   Import Impacted Assets: To import impacted assets, refer [[mco_importing_impacted_assets|Importing impacted assets]]
    -   Initiate Recall Campaign: To change the recall campaign state from draft to in-progress, you must have at least one corrective action marked as In use. Only then can the campaign progress beyond the draft stage.
    -   Cancel Campaign: To cancel the recall campaign.

## What to do next

1.  Create [[mco-corrective-actions|Corrective actions]].
2.  Create [[mco_corrective_action_charges|Corrective action charges]].
3.  Select **Initiate Recall Campaign** to enable Recall Campaign Phases and Phase &amp; Sub-phases.

-   **[Importing impacted assets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/manufacturing/mco_importing_impacted_assets.md)**  
Recall campaign management enables you to import the impacted assets.
-   **[[mco-campaign-tasks|Campaign tasks]]**  
As an OEM, plan, manage, and execute a promotional effort.
-   **[Corrective actions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/manufacturing/mco-corrective-actions.md)**  
Corrective action enables you to address the asset issue, either by eliminating or replacing the asset.
-   **[[mco-impacted-asset|Create an impacted asset]]**  
Identify an impacted asset that must be replaced or recalled.
-   **[[mco-recall-campaign-phases|Recall a campaign phase]]**  
Create a recall campaign for a specific geography or a dealership.

**Parent Topic:**[[mco-recall-management|Recall management]]

## Related

- [[mco-recall-campaign-form|Recall campaign form]]
- [[mco_importing_impacted_assets|Importing impacted assets]]
- [[mco-corrective-actions|Corrective actions]]
- [[mco_corrective_action_charges|Corrective action charges]]
- [[mco-campaign-tasks|Campaign tasks]]
- [[mco-impacted-asset|Create an impacted asset]]
- [[mco-recall-campaign-phases|Recall a campaign phase]]
- [[mco-recall-management|Recall management]]
- [[mco-rcl-clms|Recall campaign]]
