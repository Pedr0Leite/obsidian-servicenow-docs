---
title: Synchronize a shape to the database
description: Add a shape to a diagram. Synchronize the shape to the database by mapping the shape to an existing CI or adding a CI.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-sync-shape.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Synchronize a shape to the database

Add a shape to a diagram. Synchronize the shape to the database by mapping the shape to an existing CI or adding a CI.

## Before you begin

Role required: sn\_apm.apm\_user

**Note:** You must have the Owner or Editor access to the artifact or diagram and must have read access to the shape entity.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization\).

3.  Select an existing diagram from the Diagrams page.

4.  Add a shape to an existing or new diagram.

    You can observe that the unsynced icon \(\[Omitted image "icon-unsynced.png"\] Alt text: unsynced shape\) is displayed in the shape. It means, the shape hasn’t yet synced with the ServiceNow database.

5.  Open the side panel with details for the selected shape by selecting the Open the side panel icon \(\[Omitted image "icon-open-side-panel.png"\] Alt text: Open side panel\).

    **Note:** The width of the side panel is saved to your user preferences. If you resize the panel, it opens at the same width the next time you open a diagram.

6.  Select and map an existing CI or create a CI for the shape.

    -   To map an existing CI, select the **Choose Existing** button and select a CI from the drop-down list.
    -   To create a CI, select the **Create New** button and enter the details.
7.  Send the shape or diagram for approval.

    After receiving the approval, you can see the **Commit** button to synchronize a shape or diagram, or a relationship to the database.

8.  Select **Update**.

9.  Select **Commit** to synchronize the object to the database and save the diagram.


## Result

The shape gets synced to the database.

**Parent Topic:**[[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]

**Related topics**  


[[eaw-modeling-bc-map|Create a diagram for a business capability map]]

[[eaw-modeling-update-bc-map|Update a business capability map]]

[[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]

[[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]

[[eaw-modeling-update-ba-map|Update a business application hierarchy map]]

[[eaw-modeling-share-diagram|Share a modeling diagram]]

[[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]

[[eaw-modeling-save-as-new|Save as a version]]

[[eaw-modeling-duplicate|Duplicate a modeling diagram]]

[[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]

[[eaw-modeling-add-related-records|Add related records in the modeling diagram]]

[[eaw-modeling-delete-shape|Delete a shape]]

## Related

- [[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]
- [[eaw-modeling-bc-map|Create a diagram for a business capability map]]
- [[eaw-modeling-update-bc-map|Update a business capability map]]
- [[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]
- [[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]
- [[eaw-modeling-update-ba-map|Update a business application hierarchy map]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-modeling-add-related-records|Add related records in the modeling diagram]]
- [[eaw-modeling-delete-shape|Delete a shape]]
- [[ea-workspace|Enterprise Architecture Workspace]]
