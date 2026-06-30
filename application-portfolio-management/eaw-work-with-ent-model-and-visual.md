---
title: Working with Enterprise Modeling and Visualization
description: Enterprise Modeling and Visualization provides a structured, visual framework for managing the complex relationships between IT systems, business processes, and organizational goals.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-work-with-ent-model-and-visual.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Working with Enterprise Modeling and Visualization

Enterprise Modeling and Visualization provides a structured, visual framework for managing the complex relationships between IT systems, business processes, and organizational goals.

With Enterprise Modeling and Visualization, you can create and maintain architecture diagrams using built‑in shape libraries such as General, Common Service Data Model, Amazon Web Services, [[application-portfolio-management-landing-page|Enterprise Architecture]] Extended, ArchiMate, and Business Process Model and Notation. You can connect shapes with relationship lines and label connectors to represent architectural relationships.

Associate shapes with existing records, such as business applications, capabilities, and application services, and use the side panel to view or update record details directly from the canvas.

**Note:** The width of the side panel is saved to your user preferences. If you resize the panel, it opens at the same width the next time you open a diagram.

You can manage diagram evolution by saving changes as new versions. Versioning enables you to maintain a history of architecture decisions and switch between versions using the version selector. You can also compare different versions of a diagram and generate a summary of the changes.

The workspace supports collaboration and governance by enabling you to share diagrams with stakeholders and submit them for review and approval using the built‑in approval workflow. After approval, you can synchronize the diagram with your repository to update the underlying records.

**Note:**

After upgrading from Q2 2025 or Q3 2025 releases to the Q4 2025 release of [[ea-workspace|Enterprise Architecture Workspace]], you might observe that newly created shapes display color, while existing shapes for the same entity don’t.

The Q4 2025 release of Enterprise Architecture Workspace release introduced color styling to the shape library. Consequently, diagrams created in Q3 don’t display color. Following the upgrade, new shapes added to these older diagrams display color, but the previously existing shapes remain uncolored.

To update the shapes in the previously created diagrams, do the following:

-   For upgrades from Q3 to Q4- You must explicitly run the relevant fix script \(script name: Clean edges and synchronize shape names and met", sys\_id: "2a63972eff22621076fdffffffffffbe\). This is because the script was present in the Q3 release and has been modified for Q4.
-   The script runs automatically as part of the upgrade process.

-   **[[eaw-view-shape-libraries|View all shape libraries]]**  
View all shape libraries available for the Enterprise Modeling and Visualization in the Enterprise Architecture Workspace.
-   **[[eaw-view-modeling-config|View configuration for Enterprise Architecture Workspace]]**  
View all the configuration details of Enterprise Architecture Workspace.
-   **[[eaw-view-entity-config|View all entities]]**  
View all entities available for the Enterprise Modeling and Visualization in the Enterprise Architecture Workspace.
-   **[[eaw-view-relationships|View relationships configurations]]**  
View all relationship configurations available for the Enterprise Modeling and Visualization in the Enterprise Architecture Workspace.
-   **[[eaw-show-shape-ports|Show shape controls without hovering]]**  
Enable an accessibility preference to keep all contextual buttons and controls on diagram shapes visible at all times, without requiring you to hover.
-   **[[eaw-modeling-create-diagram|Create a blank diagram using modeling in the EA Workspace]]**  
Create a diagram and synchronize it to the ServiceNow database.
-   **[[eaw-set-connector-properties|Set shape connector properties in Enterprise Modeling and Visualization]]**  
Configure the relationship type or visual style of a connector between shapes in an enterprise modeling diagram.
-   **[[eaw-modeling-add-labels-to-connector-lines|Add labels to connector lines between shapes in a diagram]]**  
You can enhance diagram clarity in Enterprise Modeling and Visualization by adding a descriptive text on the connector line between shapes. Connector line labels clarify the nature of the relationship between shapes, annotate the data flow direction, and provide contextual information.
-   **[[eaw-work-with-bc-map|Working with business capability map]]**  
Model your business capabilities map using the Enterprise Modeling and Visualization. Update existing capability maps by adding other business capabilities and business applications.
-   **[[eaw-work-with-ba-map|Working with business hierarchy map]]**  
Model your business application hierarchy using the Enterprise Modeling and Visualization. Update an existing business hierarchy map by adding more shapes and relationships.
-   **[[eaw-work-with-bp-map|Working with business process map]]**  
Use the Enterprise Modeling and Visualization to create, update, and manage business process diagrams that represent the current and future state of your business workflows.
-   **[[eaw-work-with-archimate-shapes|Working with ArchiMate Shapes]]**  
Use ArchiMate® shapes to build enterprise architecture diagrams that represent the relationships between business, application, and technology domains across your organization.
-   **[[eaw-work-with-aws-shapes|Working with Amazon Web Services \(AWS\) shapes]]**  
AWS is a cloud computing platform, used for cloud migration, application hosting, and digital transformation, making it critical for enterprise architecture planning. AWS shapes are part of the Cloud Architecture modeling capability. They enable architects to visualize AWS cloud components, model hybrid architectures, and support cloud migration planning and future-state architecture design.
-   **[[eaw-work-with-csdm-shapes|Working with CSDM shapes]]**  
Common Service Data Model \(CSDM\) is a standardized framework and CMDB data model provided by ServiceNow. It defines service-related terms, tables, and relationships across the Now Platform to ensure consistency in how services, applications, and infrastructure are represented. In Enterprise Architecture Workspace, CSDM shapes are visual elements that represent entities on diagrams for modeling and analysis.
-   **[[eaw-working-custom-shapes|Working with custom shapes]]**  
Custom shapes represent specific elements that are unique to your organization. Manage custom shapes, create diagram actions for the shapes in the Enterprise Architecture Workspace.
-   **[[eaw-modeling-group-ungroup-shape|Convert a shape to a group shape]]**  
Group shapes enable you to combine multiple related shapes into a single container for better organization and clarity in diagrams. It’s useful for representing logical groupings such as a set of applications under a business capability, related processes under a value stream stage.
-   **[[eaw-modeling-expand-collapse-shape|Expand or collapse a group shape]]**  
The expand and collapse functionality for a group shape helps in simplifying visualization, improves focus, and supports hierarchical modeling.
-   **[[eaw-modeling-download-diagram|Download a modeling diagram as an image]]**  
Download a diagram as an image to share it with other stakeholders with offline access or use it in the presentations.
-   **[[eaw-modeling-reorder-shapes-cat|Reorder shapes categories]]**  
Reordering shape categories helps architects customize the panel for faster access to frequently used shapes.
-   **[[eaw-align-distribute-shapes|Align and distribute shapes in a modeling diagram]]**  
Organize shapes on the diagram canvas by aligning them to a common edge or center, or by distributing them at equal spacing.
-   **[[eaw-modeling-replace-shape|Replace a shape in a diagram]]**  
Replace any shape on the diagram canvas with a different shape type. When you replace a shape, relationship lines update automatically to reflect the new shape type.
-   **[[eaw-modeling-show-hide-shapes-panel|Show or hide shapes panel]]**  
Show or hide the Shapes Panel to optimize your workspace for different tasks.
-   **[[eaw-modeling-shapes-grid-list-view|Switch to list or grid view of shapes panel]]**  
Switch between List View and Grid View in the shapes panel according to your modeling needs.
-   **[[eaw-filter-shapes|Search shapes in a diagram]]**  
Search for a shape in the Shapes palette of a diagram.
-   **[[eaw-modeling-add-related-records|Add related records in the modeling diagram]]**  
Fetch and add specific related records to the selected shape in a diagram.
-   **[[eaw-modeling-share-diagram|Share a modeling diagram]]**  
Share your draft diagrams with individuals and groups and define access levels for them to view and modify the diagram.
-   **[[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]**  
Synchronize an approved diagram and all its elements to the database.
-   **[[eaw-modeling-save-as-new|Save as a version]]**  
Copy an existing diagram and create a version for it within the selected architectural artifact. You can update the new version as required.
-   **[[eaw-add-or-edit-diagram-version-details|Add or edit diagram version details]]**  
You can add or edit version-specific details for a diagram to improve change management and compliance. Adding diagram version details ensures better clarity between all stakeholders in the context of the diagram and timelines.
-   **[[eaw-modeling-duplicate|Duplicate a modeling diagram]]**  
You can make a copy of an existing diagram that you created and modify the duplicate diagram according to your requirement.
-   **[[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]**  
Send your draft modeling diagrams for approval. After receiving the approval, you can commit the diagram to the database. The approval process can be done through a configured workflow. By default, the approval request is submitted to the Enterprise Architect group.
-   **[[eaw-modeling-sync-shape|Synchronize a shape to the database]]**  
Add a shape to a diagram. Synchronize the shape to the database by mapping the shape to an existing CI or adding a CI.
-   **[[eaw-approve-diagram-req|Approve or reject a modeling diagram request]]**  
As an Enterprise Architect, approve or reject a Enterprise Modeling and Visualization diagram requests submitted by other users.
-   **[[eaw-modeling-delete-shape|Delete a shape]]**  
Delete a shape and all of its relationships from a diagram.
-   **[[eaw-modeling-delete-diagram|Delete Enterprise Modeling and Visualization diagrams]]**  
You can delete diagrams from the Enterprise Modeling and Visualization All Diagrams page, confirming only the relevant and current diagrams are available.
-   **[[create-documents-for-diagrams|Generate a document from a diagram]]**  
Generate documents from the Enterprise Modeling and Visualization diagrams page.
-   **[[view-docs-for-diagram|View documents for a diagram]]**  
View documents that are generated for a diagram from the Enterprise Modeling and Visualization diagrams page.

**Parent Topic:**[[eaw-managing-ea-workspace|Managing Enterprise Architecture Workspace]]

**Related topics**  


[[eaw-modeling|Exploring Enterprise Modeling and Visualization in the EA Workspace]]

[[eaw-setup-modeling|Configure Enterprise Modeling and Visualization]]

[[compare-modeling-diagrams|Compare Enterprise Modeling and Visualization diagrams]]

## Related

- [[eaw-view-shape-libraries|View all shape libraries]]
- [[eaw-view-modeling-config|View configuration for Enterprise Architecture Workspace]]
- [[eaw-view-entity-config|View all entities]]
- [[eaw-view-relationships|View relationships configurations]]
- [[eaw-show-shape-ports|Show shape controls without hovering]]
- [[eaw-modeling-create-diagram|Create a blank diagram using modeling in the EA Workspace]]
- [[eaw-set-connector-properties|Set shape connector properties in Enterprise Modeling and Visualization]]
- [[eaw-modeling-add-labels-to-connector-lines|Add labels to connector lines between shapes in a diagram]]
- [[eaw-work-with-bc-map|Working with business capability map]]
- [[eaw-work-with-ba-map|Working with business hierarchy map]]
- [[eaw-work-with-bp-map|Working with business process map]]
- [[eaw-work-with-archimate-shapes|Working with ArchiMate Shapes]]
- [[eaw-work-with-aws-shapes|Working with Amazon Web Services \(AWS\) shapes]]
- [[eaw-work-with-csdm-shapes|Working with CSDM shapes]]
- [[eaw-working-custom-shapes|Working with custom shapes]]
- [[eaw-modeling-group-ungroup-shape|Convert a shape to a group shape]]
- [[eaw-modeling-expand-collapse-shape|Expand or collapse a group shape]]
- [[eaw-modeling-download-diagram|Download a modeling diagram as an image]]
- [[eaw-modeling-reorder-shapes-cat|Reorder shapes categories]]
- [[eaw-align-distribute-shapes|Align and distribute shapes in a modeling diagram]]
- [[eaw-modeling-replace-shape|Replace a shape in a diagram]]
- [[eaw-modeling-show-hide-shapes-panel|Show or hide shapes panel]]
- [[eaw-modeling-shapes-grid-list-view|Switch to list or grid view of shapes panel]]
- [[eaw-filter-shapes|Search shapes in a diagram]]
- [[eaw-modeling-add-related-records|Add related records in the modeling diagram]]
- [[eaw-modeling-share-diagram|Share a modeling diagram]]
- [[eaw-modeling-sync-diagram-servicenow|Commit diagram changes]]
- [[eaw-modeling-save-as-new|Save as a version]]
- [[eaw-add-or-edit-diagram-version-details|Add or edit diagram version details]]
- [[eaw-modeling-duplicate|Duplicate a modeling diagram]]
- [[eaw-modeling-submit-for-approval|Submit a modeling diagram for approval]]
- [[eaw-modeling-sync-shape|Synchronize a shape to the database]]
- [[eaw-approve-diagram-req|Approve or reject a modeling diagram request]]
- [[eaw-modeling-delete-shape|Delete a shape]]
- [[eaw-modeling-delete-diagram|Delete Enterprise Modeling and Visualization diagrams]]
- [[create-documents-for-diagrams|Generate a document from a diagram]]
- [[view-docs-for-diagram|View documents for a diagram]]
- [[eaw-managing-ea-workspace|Managing Enterprise Architecture Workspace]]
- [[eaw-modeling|Exploring Enterprise Modeling and Visualization in the EA Workspace]]
- [[eaw-setup-modeling|Configure Enterprise Modeling and Visualization]]
- [[compare-modeling-diagrams|Compare Enterprise Modeling and Visualization diagrams]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
- [[ea-workspace|Enterprise Architecture Workspace]]
