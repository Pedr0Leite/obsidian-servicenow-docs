---
title: Create a Lucidchart diagram for a business capability in the Enterprise Architecture Workspace
description: Create a diagram in Lucidchart for your business capability maps and associate it with an architectural artifact.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-create-lucid-diagram-cap.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Manage business capabilities, Using business architecture, Working with Portfolio list view, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Create a Lucidchart diagram for a business capability in the Enterprise Architecture Workspace

Create a diagram in Lucidchart for your business capability maps and associate it with an architectural artifact.

## Before you begin

Ensure the following ServiceNow Store applications are installed:

-   Lucidchart Diagramming Spoke \[sn\_lucdchart\_spoke\] \(v 1.1.1 or later\)
-   Lucidchart Integration \[sn\_lcdchart\_int\] \(v 2.3.0 or later\)
-   Personal Authentication \[sn\_ihub\_personal\_auth\] \(v 27.0.0 or later\)

Ensure a connection is established with Lucid. For details, see [Create OAuth 2.0 Client in Lucidchart](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/set-up-lucidchart.md) and [Create a connection and credential alias for the Lucidchart diagramming spoke](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/create-conn-cred-lucidchart.md).

Role required: Member of the Enterprise Architect group

## Procedure

1.  Navigate to **Workspace** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Portfolio List view by selecting the Portfolio icon \[Omitted image "eaw-portfolio-icon-polaris.png"\] Alt text:.

3.  Select the expand row icon \(\[Omitted image "ExpandIcon.png"\] Alt text: Expand Row icon\) next to **Business Architecture**.

4.  Select **Business Capabilities**.

5.  Select a business capability to open it.

6.  Select the more actions menu \[Omitted image "icon-three-dot-menu-eaw.png"\] Alt text: More actions menu and select **Create Diagram**.

7.  On the Create Diagram form, fill in the fields.

    **Note:** Use the authorization link on the Create Diagram window, to generate an authentication token and fetch your Lucid folders to save the diagram. Ensure that you have at least one folder created in the My documents folder of your computer.

    For field information, see [[eaw-create-diagram-bc|Create diagram for a business capability form]].

8.  Select **Create Diagram**.


## Result

After a successful submission, a link to the newly created Lucid diagram appears on top of the screen. You can select the link to navigate to the diagram. The Architectural Artifacts page shows the link to the Lucidchart diagram and an artifact name associated with it. You can select the respective link to access the artifact or diagram.

**Parent Topic:**[[eaw-manage-business-capabilities|Manage business capabilities]]

**Related topics**  


[Create diagram for a business capability form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-create-diagram-bc.md)

[[eaw-view-all-capabilities-on-the-portfolio-page|View all business capabilities on the Portfolio page]]

[[eaw-add-capability|Add or edit a business capability from the Portfolio page]]

[[eaw-assoicate-artifact-bc|Manage architectural artifacts of a business capability in EA Workspace]]

[[eaw-create-a-sub-capability-from-the-portfolio-page|Create a sub-capability from the Portfolio page]]

[[add-a-capability|Add a business capability]]

[[eaw-create-a-demand-towards-achievement-of-capability|Create a demand towards achievement of a capability]]

[[update-hierarchy|Update the hierarchy of a business capability]]

[[eaw-create-sub-capability|Create a sub-capability]]

[[assign-a-business-application|Assign a business application]]

[[unassign-a-business-application-from-a-capability|Unassign a business application from a capability]]

[[delete-a-capability|Delete a capability from the hierarchy]]

[[eaw-view-roadmap-bc|View a roadmap of a business capability]]

## Related

- [[eaw-create-diagram-bc|Create diagram for a business capability form]]
- [[eaw-manage-business-capabilities|Manage business capabilities]]
- [[eaw-view-all-capabilities-on-the-portfolio-page|View all business capabilities on the Portfolio page]]
- [[eaw-add-capability|Add or edit a business capability from the Portfolio page]]
- [[eaw-assoicate-artifact-bc|Manage architectural artifacts of a business capability in EA Workspace]]
- [[eaw-create-a-sub-capability-from-the-portfolio-page|Create a sub-capability from the Portfolio page]]
- [[add-a-capability|Add a business capability]]
- [[eaw-create-a-demand-towards-achievement-of-capability|Create a demand towards achievement of a capability]]
- [[update-hierarchy|Update the hierarchy of a business capability]]
- [[eaw-create-sub-capability|Create a sub-capability]]
- [[assign-a-business-application|Assign a business application]]
- [[unassign-a-business-application-from-a-capability|Unassign a business application from a capability]]
- [[delete-a-capability|Delete a capability from the hierarchy]]
- [[eaw-view-roadmap-bc|View a roadmap of a business capability]]
- [[ea-workspace|Enterprise Architecture Workspace]]
