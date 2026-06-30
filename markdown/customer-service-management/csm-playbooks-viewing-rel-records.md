---
title: Viewing dynamic related records in the contextual side panel
description: Customer service agents can view dynamic related records in the contextual side panel in CSM Configurable Workspace. This feature displays related records that dynamically change based on the context of the current record or playbook activity.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-playbooks-viewing-rel-records.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Using playbooks, Automate and optimize, Use, Customer Service Management]
---

# Viewing dynamic related records in the contextual side panel

Customer service agents can view [[csm-contextual-related-records|dynamic related records]] in the contextual side panel in [[csm-workspaces-configure|CSM Configurable Workspace]]. This feature displays related records that dynamically change based on the context of the current record or playbook activity.

Agents can view, search, and sort the records in the Related Records tab in the contextual side panel. These records appear in the Related Records tab as read-only cards.

The Related Records tab displays related records that dynamically change based on the context of the current record or playbook activity. The records that are displayed in the Related Records tab depend on the following settings:

-   The related record contexts and definitions that have been configured for a record or playbook activity.
-   The agent's access permissions to data.

Depending on the related record configuration for the source record or playbook activity, agents can see the following types of related records:

-   SLAs
-   Emails
-   Escalations for the case or customer \(account and contact or consumer\).
-   Blocked By
-   [[sold-product|Sold Products]]
-   [[install-base-item|Install Base Items]]
-   Active Contracts
-   Active Entitlements
-   [[c_OnScreenAlerts|Special Handling Notes]]
-   Tasks

<table id="table_dyn_rel_records_in_side_panel"><thead><tr><th>

Task

</th><th>

Steps

</th></tr></thead><tbody><tr><td>

View related records in the contextual side panel

</td><td>

Select the Related Records tab \(\[Omitted image "contextual-side-panel-related-records.jpg"\] Alt text: Related Records icon.\) to view the Related Records list.

 Related records appear in the list in a card format. The initial set of records displayed in the list is determined by the record type selected. The displayed records can be changed using the filter located at the top of the list.

</td></tr><tr><td>

Select the type of related record to view

</td><td>

Use the filter at the top of the Related Records list to select the type of related records to view. Agents can also use the filter to see the current selection.

1.  Click the Filter icon \(\[Omitted image "dynamic-related-records-filter-icon.png"\] Alt text: Filter icon.\).
2.  Select a record type from the drop-down menu.

 The drop-down menu includes the related [[migration-lists|lists]] that have been configured for the parent record.

</td></tr><tr><td>

Search the related records list

</td><td>

Use the search field at the top of the Related Records list to perform a text search. Records that match the search text are highlighted.

1.  Enter the search text in the search field at the top of the Related Records list.
2.  Select the search icon.

 If the search field is grayed out, search is not available for the selected type of related records.

</td></tr><tr><td>

Open a related record in a subtab

</td><td>

Select a card in the Related Records list to open the record in a subtab under the parent record. In the subtab, the agent can view the record details and perform available actions.

</td></tr><tr><td>

Open the related record list in a list view in a subtab

</td><td>

Select the list view icon \(\[Omitted image "dynamic-related-records-list-view-icon.png"\] Alt text: List view icon.\) to display the related records in a list view in a subtab under the parent record.

</td></tr><tr><td>

Create a new record for the selected related list

</td><td>

Create a new record for the record type currently selected in the Related Records list. This action opens a new record form in a subtab under the parent record.

1.  Select the Create record icon \(\[Omitted image "dynamic-related-records-create-record-icon.png"\] Alt text: Create record icon.\) at the top of the Related Records list.
2.  Fill in the fields on the record form and select **Save**.

</td></tr></tbody>
</table>**Related topics**  


[[csm-playbook-filter-activities|Filter playbook activities]]

[[csm-playbooks-using-activity-stream|Using the activity stream in the contextual side panel]]

[[csm-playbooks-viewing-ribbon-info|Viewing ribbon information in the contextual side panel]]

[[using-customized-playbook-experience-for-customer-service-management|Add an optional activity]]

[[case-summarization-in-process-page|Summarize a case]]

[[csm-playbook-create-record|Create a record using a playbook]]

## Related

- [[csm-playbook-filter-activities|Filter playbook activities]]
- [[csm-playbooks-using-activity-stream|Using the activity stream in the contextual side panel]]
- [[csm-playbooks-viewing-ribbon-info|Viewing ribbon information in the contextual side panel]]
- [[using-customized-playbook-experience-for-customer-service-management|Add an optional activity]]
- [[case-summarization-in-process-page|Summarize a case]]
- [[csm-playbook-create-record|Create a record using a playbook]]
- [[csm-contextual-related-records|Dynamic related records]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[sold-product|Sold products]]
- [[install-base-item|Install base items]]
- [[c_OnScreenAlerts|Special handling notes]]
- [[migration-lists|Lists]]
