---
title: Duplicate a modeling diagram
description: You can make a copy of an existing diagram that you created and modify the duplicate diagram according to your requirement.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-duplicate.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Duplicate a modeling diagram

You can make a copy of an existing diagram that you created and modify the duplicate diagram according to your requirement.

## Before you begin

Role required: Role required: sn\_apm.apm\_user and Owner or Editor access to the artifact or diagram

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization icon.\).

3.  Select an existing diagram from the Diagrams page.

4.  Select the More actions menu \[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.

5.  Select **Duplicate**.

6.  Enter a name for the diagram.

    On duplicating a business process map, the value in the **Link to business process** field in the **Duplicate** pop-up window is selected by default, based on the status of the business process associated with the original business process map.

    -   If the original business process isn’t committed to the database:
        -   The default selection in the **Link to business process** field is **New**.
        -   You can rename the business process in the **Name of new business process** field.
    -   If the original business process exists in the database:
        -   The default selection in the **Link to business process** field is **Existing**.
        -   You can choose a different business process using the **Select existing business process** field.
    You can change the default values in the **Link to business process** field according to your requirement.

7.  Select **Duplicate**.


## Result

A duplicate diagram is created.

**Parent Topic:**[[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]

**Related topics**  


[[eaw-modeling-bc-map|Create a diagram for a business capability map]]

[[eaw-modeling-update-bc-map|Update a business capability map]]

[[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]

[[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]

[[eaw-modeling-update-ba-map|Update a business application hierarchy map]]

[[eaw-modeling-add-related-records|Add related records in the modeling diagram]]

[[eaw-modeling-share-diagram|Share a modeling diagram]]

[[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]

[[eaw-modeling-save-as-new|Save as a version]]

[[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]

[[eaw-modeling-sync-shape|Synchronize a shape to the database]]

[[eaw-modeling-delete-shape|Delete a shape]]

## Related

- [[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]
- [[eaw-modeling-bc-map|Create a diagram for a business capability map]]
- [[eaw-modeling-update-bc-map|Update a business capability map]]
- [[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]
- [[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]
- [[eaw-modeling-update-ba-map|Update a business application hierarchy map]]
- [[eaw-modeling-add-related-records|Add related records in the modeling diagram]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-delete-shape|Delete a shape]]
- [[ea-workspace|Enterprise Architecture Workspace]]
