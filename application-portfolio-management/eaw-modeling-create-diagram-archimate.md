---
title: Create diagram using ArchiMate shapes and add relationships
description: Use the industry standard ArchiMate shapes to create modeling diagrams for your enterprise in the Enterprise Architecture Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-create-diagram-archimate.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Working with ArchiMate Shapes, Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Create diagram using ArchiMate shapes and add relationships

Use the industry standard ArchiMate shapes to create modeling diagrams for your enterprise in the [[ea-workspace|Enterprise Architecture Workspace]].

## Before you begin

Role required: sn\_apm.apm\_user

## About this task

You can create a diagram with the combination of CSDM and ArchiMate shapes or you can use only the ArchiMate shapes. If you want to create the diagram with only ArchiMate shapes, you can skip including the name of the Business Application in the Create a business hierarchy map form. It creates a empty canvas.

## Procedure

1.  Navigate to **Workspaces** &gt; **Enterprise Architecture Workspace**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Modeling\).

3.  Select **New** drop-down menu.

4.  Select **Business hierarchy map**.

5.  On the [[eaw-modeling-create-bc-map-form|Create a business capability map form]], fill in the details.

    For field information, see [[eaw-modeling-create-ba-map-form|Create a business hierarchy map form]].

6.  Select **Create diagram**.

    A empty canvas gets created for the artifact.

7.  Add ArchiMate shapes to the canvas.

    **Note:**

    You can add a shape to the canvas by either selecting the shape or by dragging the shape from the **Shapes** palette to the canvas.

8.  Associate a CI to the shape by selecting a radio button.

    -   **Choose existing**- Select this radio button to associate the shape with an existing CI.
    -   **Create new**- Select this radio button to create a new CI for the selected shape.
9.  Select a connector line to update the relationship type.

    The Relationship side panel opens. Select a **Relationship** and **Value**. For information on the ArchiMate shapes and relationships, see [[eaw-modeling-archimate|ArchiMate shapes support in the Enterprise Modeling and Visualization]].

    **Note:** Connector ports on ArchiMate shapes are bi-directional. You can use any connector port—top, bottom, left, or right—as either an input or an output.

10. Select a shape and add related records for the shape by selecting the \[Omitted image "icon-add-related-records.png"\] Alt text: Add related records icon.

    Th Add related records window opens. It lists the Entities with the number and Relationship type \(CI relationship or a Reference\).

11. Select the **Entities** that you want to include and then select **Add**.

    The selected entities are added to the diagram with the relationship showing in ArchiMate format. In the diagram, the dotted lines represent the Reference links and the solid lines represent the CI relationships.

12. Select **Commit changes** to synchronize the diagram to the database.

    This option is available only when the diagram is approved. For more information, see [[eaw-modeling-sync-shape|Synchronize a shape to the database]].

13. Select **Share** to share the diagram with individuals or groups.

    For more information, see [[eaw-modeling-share-diagram|Share a modeling diagram]].

14. Select the More Actions menu \(\[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.\) to perform the following actions:

    -   **Save as new version**: Select this option to create a version for the selected diagram. The version number is automatically added in the Version number field, and it isn’t editable. For more information, see [[eaw-modeling-save-as-new|Save as a version]].
    -   **Duplicate**: Select this option to duplicate the diagram. For more information, see [[eaw-modeling-duplicate|Duplicate a modeling diagram]].
    -   **Submit for approval**: Select this option to submit the diagram for approval. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group. For more information, see [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]].

**Parent Topic:**[[eaw-work-with-archimate-shapes|Working with ArchiMate Shapes]]

**Related topics**  


[ArchiMate shapes support in the Enterprise Modeling and Visualization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-modeling-archimate.md)

[[eaw-modeling-archimate-shapes|ArchiMate shapes]]

## Related

- [[eaw-modeling-create-ba-map-form|Create a business hierarchy map form]]
- [[eaw-modeling-archimate|ArchiMate shapes support in the Enterprise Modeling and Visualization]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-work-with-archimate-shapes|Working with ArchiMate Shapes]]
- [[eaw-modeling-archimate-shapes|ArchiMate shapes]]
- [[ea-workspace|Enterprise Architecture Workspace]]
- [[eaw-modeling-create-bc-map-form|Create a business capability map form]]
