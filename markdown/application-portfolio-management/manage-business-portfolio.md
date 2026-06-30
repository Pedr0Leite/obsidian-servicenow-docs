---
title: Exploring a business portfolio
description: As an Enterprise Architect, view the capability hierarchy, manage capabilities, and assign business applications to the capabilities.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/manage-business-portfolio.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Exploring a business portfolio

As an Enterprise Architect, view the capability hierarchy, manage capabilities, and assign business applications to the capabilities.

The Business Portfolio page displays the hierarchy map for your business capabilities. You can view the number of defined business capabilities and the number of business applications that support these capabilities.

Business applications marked as **Retired** or in **End of Life** lifecycle stage aren’t displayed on the Business Portfolio page. However, you can view those business applications by updating the **sn\_apm\_ws.business\_application\_default\_filter** system property. Contact your ServiceNow® account service manager to update the system property.

A business capability is the ability of an organization to do its business activities successfully and fulfill its business goals. Use the business capability mapping to establish a CI relationship between the business capability and the business applications. The Business Capabilities Hierarchy page contains the following items:

-   Capabilities: Total number of business capabilities.
-   Leaf Capabilities: Total number of capabilities at the leaf level \(that have no child capabilities of its own\) in all the hierarchies of the business capabilities listed.
-   Assessed: Total number of assessed business capabilities.
-   Not Assessed: Total number of capabilities that haven’t been assessed.
-   Major Gap: Total number of capabilities with a score in the range of 1-4.
-   Medium Gap: Total number of capabilities with a score in the range of 4-7.
-   No Gap: Total number of capabilities with a score in the range of 7-10.

You can create a capability or subcapability, and then assign a business application to the capability.

Business capabilities are assessed by indicators to provide indicator scores used to make strategic decisions on the business applications that support the business capability. You can sort the business capabilities by their scores.

**Note:** The business capability scores of the current fiscal year are displayed by default. You can change the fiscal year value using the Fiscal year filter.

By default, the first business capability in the hierarchy at level 0 expands to display its immediate child capabilities at level 1. For subsequent business capabilities and child capabilities, select the expand icon \(\[Omitted image "9328d408edd1abfc208eefc89af4b5dca79df0ee.png"\] Alt text: Expand icon.\) to expand and view its subcapabilities at each level. You can see the total count of the subcapabilities below each parent capability, the total number of business applications directly related to each capability, and their capability score. Similarly, on expanding a parent capability, you can see the number of subcapabilities and the total count of business applications that are directly related to the subcapability at that level.

**Note:** You can zoom on this page or any of the child pages to 200% or 400% through your browser settings without the loss of content or functionality. Page layouts are transformed into a vertical, stacked view automatically.

You can associate business capabilities with value stream stages to map your organizational capabilities to specific steps in your value streams. Value stream stages represent the discrete steps that make up a value stream, and each stage can be associated with multiple business capabilities.

To view the value stream stages associated with a business capability, open a business capability record and select the **Value Stream Stages** tab. The tab displays a read-only list of associated value stream stages, showing the name, display name, and description of each stage.

**Parent Topic:**[[explore-eaw|Exploring Enterprise Architecture Workspace]]

**Related topics**  


[[add-a-capability|Add a business capability]]

[[eaw-create-a-demand-towards-achievement-of-capability|Create a demand towards achievement of a capability]]

[[update-hierarchy|Update the hierarchy of a business capability]]

[[eaw-create-sub-capability|Create a sub-capability]]

[[assign-a-business-application|Assign a business application]]

[[delete-a-capability|Delete a capability from the hierarchy]]

[[unassign-a-business-application-from-a-capability|Unassign a business application from a capability]]

[[eaw-view-roadmap-bc|View a roadmap of a business capability]]

[[generate-insights-into-ba|Generate insights into business applications]]

## Related

- [[explore-eaw|Exploring Enterprise Architecture Workspace]]
- [[add-a-capability|Add a business capability]]
- [[eaw-create-a-demand-towards-achievement-of-capability|Create a demand towards achievement of a capability]]
- [[update-hierarchy|Update the hierarchy of a business capability]]
- [[eaw-create-sub-capability|Create a sub-capability]]
- [[assign-a-business-application|Assign a business application]]
- [[delete-a-capability|Delete a capability from the hierarchy]]
- [[unassign-a-business-application-from-a-capability|Unassign a business application from a capability]]
- [[eaw-view-roadmap-bc|View a roadmap of a business capability]]
- [[generate-insights-into-ba|Generate insights into business applications]]
