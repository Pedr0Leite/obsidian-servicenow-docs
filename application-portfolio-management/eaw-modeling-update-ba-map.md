---
title: Update a business application hierarchy map
description: Modify an existing business application hierarchy map by adding or removing shapes and relationships.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-update-ba-map.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Working with business hierarchy map, Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Update a business application hierarchy map

Modify an existing business application hierarchy map by adding or removing shapes and relationships.

## Before you begin

Role required: sn\_apm.apm\_user

**Note:** You must have the Owner or Editor access to the artifact or diagram.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization icon\).

3.  Open an existing business hierarchy map artifact from the **Diagrams** page.

4.  Select the newly added shape and select the Open the side panel icon \(\[Omitted image "icon-open-side-panel.png"\] Alt text: Open side panel\) to open the details panel for the selected shape in the canvas.

5.  Select a shape in the diagram to see the following options:

    -   Side panel icon \(\[Omitted image "icon-open-side-panel.png"\] Alt text: Open side panel\) to update the details of a record.
    -   Add related records icon \( \[Omitted image "icon-add-related-records.png"\] Alt text: Add related records\) to add entities and relationship.
    -   More Actions context menu \(\[Omitted image "eaw-icon-menu.png"\] Alt text: More actions menu\) to see options for adding relationship or deleting a shape from the canvas.
6.  Select **Commit changes** to synchronize the diagram to the database.

    This option is available only when the diagram is approved. For more information, see [[eaw-modeling-sync-shape|Synchronize a shape to the database]].

7.  Select **Share** to share the diagram with individuals or groups.

    For more information, see [[eaw-modeling-share-diagram|Share a modeling diagram]].

8.  Select the More Actions menu \(\[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.\) to perform the following actions:

    -   **Save as new version**: Select this option to create a version for the selected diagram. The version number is automatically added in the Version number field, and it isn’t editable. For more information, see [[eaw-modeling-save-as-new|Save as a version]].
    -   **Duplicate**: Select this option to duplicate the diagram. For more information, see [[eaw-modeling-duplicate|Duplicate a modeling diagram]].
    -   **Submit for approval**: Select this option to submit the diagram for approval. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group. For more information, see [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]].

**Parent Topic:**[[eaw-work-with-ba-map|Working with business hierarchy map]]

**Related topics**  


[[eaw-modeling-bc-map|Create a diagram for a business capability map]]

[[eaw-modeling-update-bc-map|Update a business capability map]]

[[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]

[[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]

## Related

- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-work-with-ba-map|Working with business hierarchy map]]
- [[eaw-modeling-bc-map|Create a diagram for a business capability map]]
- [[eaw-modeling-update-bc-map|Update a business capability map]]
- [[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]
- [[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]
- [[ea-workspace|Enterprise Architecture Workspace]]
