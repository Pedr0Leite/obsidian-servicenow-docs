---
title: Create a diagram using CSDM shapes
description: The CSDM shapes represent objects visually in diagrams, enabling architects to model business capabilities, applications, services, and technical components in alignment with the Now Platform.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-create-diagram-csdm.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Working with CSDM shapes, Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Create a diagram using CSDM shapes

The CSDM shapes represent objects visually in diagrams, enabling architects to model business capabilities, applications, services, and technical components in alignment with the Now Platform.

## Before you begin

Role required: sn\_apm.apm\_user

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Modeling\).

3.  Select the **New** drop-down menu.

4.  Select **Blank diagram**.

5.  On the Blank diagram modal, enter a name for the artifact.

    You can optionally choose an architectural category for the diagram.

6.  Select **Create diagram**.

    An empty canvas gets created for the artifact.

7.  From the Shapes panel, add CSDM shapes to the canvas.

    **Note:**

    You can add a shape to the canvas by either selecting the shape or by dragging the shape from the **Shapes** palette to the canvas.

8.  Select a shape on the canvas, and associate it with CMDB records.

    -   **Choose existing**- Select this radio button to associate the shape with an existing CMDB record.
    -   **Create new**- Select this radio button to create a CMDB record directly from the diagram.
9.  Define the relationship by selecting connector lines.

    The Relationship side panel opens. Select a **Relationship** and **Value**. For more information on the CSDM shapes and relationships, see [[align-with-csdm5|CSDM shapes support in the Enterprise Modeling and Visualization]].

    **Note:** Connector ports on CSDM shapes are bi-directional. You can use any connector port—top, bottom, left, or right—as either an input or an output.

10. Select a shape and add related records for the shape by selecting the \[Omitted image "icon-add-related-records.png"\] Alt text: Add related records icon.

    The **Add related records** icon appears only when the shape is linked to an existing CMDB record. When you select the icon, the **Add related records** window opens. This window displays the entities along with their names and relationship types \(CI relationship, M2M, or Reference\).

11. Select the **Entities** that you want to include and then select **Add**.

    The selected entities are added to the diagram with the relationship showing in CSDM format. In the diagram, the dotted lines represent the reference links and the solid lines represent the CI relationships.

12. Select **Commit changes** to synchronize the diagram to the database.

    This option is available only when the diagram is approved. For more information, see [[eaw-modeling-sync-shape|Synchronize a shape to the database]].

13. Select **Share** to share the diagram with individuals or groups.

    For more information, see [[eaw-modeling-share-diagram|Share a modeling diagram]].

14. Select the More Actions menu \(\[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.\) to perform the following actions:

    -   **Save as new version**: Select this option to create a version for the selected diagram. The version number is automatically added in the Version number field, and it isn’t editable. For more information, see [[eaw-modeling-save-as-new|Save as a version]].
    -   **Duplicate**: Select this option to duplicate the diagram. For more information, see [[eaw-modeling-duplicate|Duplicate a modeling diagram]].
    -   **Submit for approval**: Select this option to submit the diagram for approval. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group. For more information, see [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]].

**Parent Topic:**[[eaw-work-with-csdm-shapes|Working with CSDM shapes]]

## Related

- [[align-with-csdm5|CSDM shapes support in the Enterprise Modeling and Visualization]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-work-with-csdm-shapes|Working with CSDM shapes]]
- [[ea-workspace|Enterprise Architecture Workspace]]
