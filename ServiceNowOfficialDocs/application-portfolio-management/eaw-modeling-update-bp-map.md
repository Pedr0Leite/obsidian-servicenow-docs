---
title: Update a business process map
description: Modify an existing business process map by adding new events, activities, or gateways.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-update-bp-map.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Working with business process map, Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Update a business process map

Modify an existing business process map by adding new events, activities, or gateways.

## Before you begin

Role required: sn\_apm.apm\_user

**Note:** To update a diagram, you must have Owner or Editor access to the artifact or diagram.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization icon\).

3.  Open an existing business process map from the Diagrams page.

4.  Add the required shapes and connections.

    Drag shapes from the **Shapes** palette to the canvas. BPMN shapes are organized into sub-categories — **Gateway**, **Event**, **Activity**, and **General**. For a full list of available shapes, see [[eaw-modeling-bpmn-shapes|Business Process Modeling Notation \(BPMN\) shapes]].

    For activity shapes such as user task or service task, select the Open the side panel icon \(\[Omitted image "icon-open-side-panel.png"\] Alt text: Open side panel\) to update the details of the associated record.

    To change the style of a connector, select the relationship line and choose a line type from the list that appears directly on the line. BPMN shapes and [[eaw-modeling-general-shapes|general shapes]] have their own sets of line types.

5.  Select the More Actions context menu \(\[Omitted image "eaw-icon-menu.png"\] Alt text: More actions menu\) to [[eaw-modeling-delete-shape|delete a shape]] from the canvas.

6.  Select **Share** to share the diagram with individuals or groups.

    For more information, see [[eaw-modeling-share-diagram|Share a modeling diagram]].

7.  Select the More Actions menu \(\[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.\) to perform the following actions:

    -   **Save as new version**: Select this option to create a version for the selected diagram. The version number is automatically added in the Version number field, and it is read-only. For more information, see [[eaw-modeling-save-as-new|Save as a version]].
    -   **Duplicate**: Select this option to duplicate the diagram. For more information, see [[eaw-modeling-duplicate|Duplicate a modeling diagram]].
    -   **Submit for approval**: Select this option to submit the diagram for approval. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group. For more information, see [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]].
8.  Select **Commit changes** to synchronize the diagram to the database.

    This option is available only when the diagram is approved. For more information, see [[eaw-modeling-sync-shape|Synchronize a shape to the database]].


**Parent Topic:**[[eaw-work-with-bp-map|Working with business process map]]

**Related topics**  


[[eaw-modeling-bp-map|Create a diagram for a business process map]]

[[eaw-view-shape-libraries|View all shape libraries]]

[Business Process Modeling Notation \(BPMN\) shapes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-modeling-bpmn-shapes.md)

[[business-process-modeling|Business process modeling]]

[[eaw-bpm-diagram-from-image|Business process map diagrams from images]]

[[eaw-create-bpm-diag-from-image|Create a business process map diagram from an image]]

[[eaw-review-ai-generated-bpm-diag|Review and accept a Now Assist-generated business process map diagram]]

## Related

- [[eaw-modeling-bpmn-shapes|Business Process Modeling Notation \(BPMN\) shapes]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-work-with-bp-map|Working with business process map]]
- [[eaw-modeling-bp-map|Create a diagram for a business process map]]
- [[eaw-view-shape-libraries|View all shape libraries]]
- [[business-process-modeling|Business process modeling]]
- [[eaw-bpm-diagram-from-image|Business process map diagrams from images]]
- [[eaw-create-bpm-diag-from-image|Create a business process map diagram from an image]]
- [[eaw-review-ai-generated-bpm-diag|Review and accept a Now Assist-generated business process map diagram]]
- [[ea-workspace|Enterprise Architecture Workspace]]
- [[eaw-modeling-general-shapes|General shapes]]
- [[eaw-modeling-delete-shape|Delete a shape]]
