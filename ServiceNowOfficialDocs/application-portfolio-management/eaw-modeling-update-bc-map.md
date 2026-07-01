---
title: Update a business capability map
description: Modify an existing business capability map by adding new capabilities, business applications, or changing the hierarchy of the existing capabilities.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-modeling-update-bc-map.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Working with business capability map, Working with Enterprise Modeling and Visualization, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Update a business capability map

Modify an existing business capability map by adding new capabilities, business applications, or changing the hierarchy of the existing capabilities.

## Before you begin

Role required: sn\_apm.apm\_user

**Note:** You must have the Owner or Editor access to the artifact or diagram.

## Procedure

1.  Navigate to **Workspaces** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Modeling page by selecting the Enterprise Modeling and Visualization icon \(\[Omitted image "icon-modeling-logo.png"\] Alt text: Enterprise Modeling and Visualization icon\).

3.  Open an existing capability map artifact from the **Diagrams** page.

    By default, two levels of hierarchy are displayed. Use the down arrow in a capability box to expand and see the next level capabilities.

4.  Update the map as required.

    -   Move the capabilities from one capability to another capability. Use the **Update hierarchies** button on the Business Portfolio page to refresh the IDs of all the capabilities according to the changes in the committed diagram.
    -   To add a new business capability or a business application to the hierarchy map, select the **Add** drop-down menu and then select **Business Capability** or **Business Application**. Drag on the new capability or business application on to a business capability to add the relationship.
    -   To apply a color to a capability, select the capability box and select the color that you want to apply from the color pallet.
    All the updates are auto-saved.

5.  Select **Commit changes** to synchronize the diagram to the database.

    This option is available only when the diagram is approved. For more information, see [[eaw-modeling-sync-shape|Synchronize a shape to the database]].

6.  Select **Share** to share the diagram with individuals or groups.

    For more information, see [[eaw-modeling-share-diagram|Share a modeling diagram]].

7.  Select the More Actions menu \(\[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu.\) to perform the following actions:

    -   **Save as new version**: Select this option to create a version for the selected diagram. The version number is automatically added in the Version number field, and it isn’t editable. For more information, see [[eaw-modeling-save-as-new|Save as a version]].
    -   **Duplicate**: Select this option to duplicate the diagram. For more information, see [[eaw-modeling-duplicate|Duplicate a modeling diagram]].
    -   **Submit for approval**: Select this option to submit the diagram for approval. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group. For more information, see [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]].

**Parent Topic:**[[eaw-work-with-bc-map|Working with business capability map]]

**Related topics**  


[[eaw-modeling-bc-map|Create a diagram for a business capability map]]

[[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]

[[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]

[[eaw-modeling-update-ba-map|Update a business application hierarchy map]]

## Related

- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-work-with-bc-map|Working with business capability map]]
- [[eaw-modeling-bc-map|Create a diagram for a business capability map]]
- [[eaw-modeling-bcmap-add-bc-ba|Add a business capability or business application to the capability map]]
- [[eaw-modeling-ba-map|Create diagram for a business hierarchy map]]
- [[eaw-modeling-update-ba-map|Update a business application hierarchy map]]
- [[ea-workspace|Enterprise Architecture Workspace]]
