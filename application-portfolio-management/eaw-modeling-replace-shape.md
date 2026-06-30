---
title: Replace a shape in a diagram
description: Replace any shape on the diagram canvas with a different shape type. When you replace a shape, relationship lines update automatically to reflect the new shape type.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-replace-shape.html
release: australia
topic_type: task
last_updated: "2026-05-15"
reading_time_minutes: 2
breadcrumb: [Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Replace a shape in a diagram

Replace any shape on the diagram canvas with a different shape type. When you replace a shape, relationship lines update automatically to reflect the new shape type.

## Before you begin

You must have the Owner or Editor access to the artifact or diagram.

Role required: sn\_apm.apm\_user

## About this task

You can replace any shape on the canvas with a different shape type, including CI shapes, [[eaw-modeling-archimate-shapes|ArchiMate shapes]], and [[eaw-modeling-general-shapes|general shapes]]. When you replace a shape:

-   CI or reference relationship lines update to reflect the relationship between the new shape types.
-   ArchiMate relationship lines update based on the new shape type.
-   If both the original and replacement shapes are general shapes, relationship lines remain unchanged.
-   Labels on relationship lines are preserved after the replacement.

You can also update the entity associated with a shape without changing the shape type.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization\).

3.  Select an existing diagram from the Diagrams page.

4.  Select the shape you want to replace.

5.  Open the side panel for the selected shape by selecting the Open side panel icon \(\[Omitted image "icon-open-side-panel.png"\] Alt text: Open side panel\).

6.  In the **Shape Type** field, search for and select the shape type you want to use as the replacement.

    You can type in the field to filter the list of available shape types.

7.  Select and map an existing entity or create an entity for the replacement shape.

    -   To associate an existing entity, select **Choose Existing** and select an entity from the list.
    -   To create an entity, select **Create New** and enter the required details.
8.  Select **Update**.


## Result

The shape is replaced on the canvas. Relationship lines between the replaced shape and connected shapes update based on the new shape type, and labels on relationship lines are preserved. If the shape was part of a group, it remains in the group after the replacement.

**Parent Topic:**[[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]

**Related topics**  


[[eaw-modeling-shapes|Shapes to create a modeling diagram]]

[[eaw-modeling-sync-shape|Synchronize a shape to the database]]

[[eaw-modeling-delete-shape|Delete a shape]]

[[eaw-modeling-add-related-records|Add related records in the modeling diagram]]

[[eaw-modeling-archimate|ArchiMate shapes support in the Enterprise Modeling and Visualization]]

## Related

- [[eaw-work-with-ent-model-and-visual|Working with Enterprise Modeling and Visualization]]
- [[eaw-modeling-shapes|Shapes to create a modeling diagram]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-delete-shape|Delete a shape]]
- [[eaw-modeling-add-related-records|Add related records in the modeling diagram]]
- [[eaw-modeling-archimate|ArchiMate shapes support in the Enterprise Modeling and Visualization]]
- [[eaw-modeling-archimate-shapes|ArchiMate shapes]]
- [[eaw-modeling-general-shapes|General shapes]]
- [[ea-workspace|Enterprise Architecture Workspace]]
