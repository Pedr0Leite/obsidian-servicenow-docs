---
title: Create a Lucidchart diagram for a business application in the EA Workspace
description: Create a diagram Lucidchart for your business application hierarchy and associate it with an architectural artifact.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-create-lucid-diagram-ba.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Working with an application portfolio, Working with Portfolio list view, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Create a Lucidchart diagram for a business application in the EA Workspace

Create a diagram Lucidchart for your business application hierarchy and associate it with an architectural artifact.

## Before you begin

Ensure the following ServiceNow Store apps are installed:

-   Lucidchart Diagramming Spoke \[sn\_lucdchart\_spoke\] \(v 1.1.1 or later\)
-   Lucidchart Integration \[sn\_lcdchart\_int\] \(v 2.3.0 or later\)
-   Personal Authentication \[sn\_ihub\_personal\_auth\] \(v 27.0.0 or later\)

Ensure a connection is established with Lucid. For details, see [Create OAuth 2.0 Client in Lucidchart](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/set-up-lucidchart.md) and [Create a connection and credential alias for the Lucidchart diagramming spoke](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/create-conn-cred-lucidchart.md).

Role required: Member of the Enterprise Architect group

## Procedure

1.  Navigate to **Workspace** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Portfolio List view by selecting the Portfolio icon \[Omitted image "portfolio-icon.png"\] Alt text: Portfolio icon.

3.  Select the expand row icon \(\[Omitted image "ExpandIcon.png"\] Alt text: Expand Row icon\) next to **Business Applications**.

4.  Select a business application to open it.

5.  Select the more actions menu \(\[Omitted image "icon-three-dot-menu.png"\] Alt text: More Actions menu\) and select **Create Diagram**.

6.  On the Create Diagram form, fill in the fields.

    For field information, see [[eaw-create-diagram-ba|Create a diagram for a business application in the EA Workspace]].

    **Note:** For Lucidchart, use the authorization link on the Create Diagram window, to generate an authentication token and fetch your Lucid folders to save the diagram. Ensure that you have at least one folder created in the My documents folder of your computer.

7.  Select **Create Diagram**.


## Result

After a successful submission, a link to the newly created Lucid diagram appears on top of the screen. You can select the link to navigate to the diagram. The Architectural Artifacts page shows the link to the Lucidchart diagram and an artifact name associated with it. You can select the respective link to access the artifact or diagram.

**Parent Topic:**[[eaw-work-with-application-portfolio|Working with an application portfolio]]

**Related topics**  


[Create a diagram for a business application in the EA Workspace](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-create-diagram-ba.md)

[[eaw-view-roadmap-ba|View roadmap of a business application]]

[[eaw-view-business-capabilities-assoc-with-ba|View business capabilities associated with a business application]]

[[eaw-create-business-app|Add or edit a business application]]

[[eaw-associate-info-obj-ba|Manage information objects of a business application in EA Workspace]]

[[eaw-unassign-archi-artfct-assoc-ba|Remove architectural artifacts associated with a business application]]

[[eaw-assoicate-artifact-ba|Create an architectural artifact and associate it with a business application]]

[[eaw-view-archi-artfct-assoc-with-ba|View architectural artifacts associated with a business application]]

[[eaw-unassign-business-capabilities-from-ba|Remove business capabilities associated with a business application]]

[[view-ba-form-in-coreui|Open business application form in Core UI from EA Workspace]]

[[view-all-business-apps|View all business applications]]

[[eaw-open-map-ba|View a unified map for a business application]]

[[eaw-add--existing-archi-artfct-to-a-ba|Add an existing architectural artifact to a business application]]

[[eaw-add-existing-business-capability-to-ba|Add an existing business capability to a business application]]

## Related

- [[eaw-create-diagram-ba|Create a diagram for a business application in the EA Workspace]]
- [[eaw-work-with-application-portfolio|Working with an application portfolio]]
- [[eaw-view-roadmap-ba|View roadmap of a business application]]
- [[eaw-view-business-capabilities-assoc-with-ba|View business capabilities associated with a business application]]
- [[eaw-create-business-app|Add or edit a business application]]
- [[eaw-associate-info-obj-ba|Manage information objects of a business application in EA Workspace]]
- [[eaw-unassign-archi-artfct-assoc-ba|Remove architectural artifacts associated with a business application]]
- [[eaw-assoicate-artifact-ba|Create an architectural artifact and associate it with a business application]]
- [[eaw-view-archi-artfct-assoc-with-ba|View architectural artifacts associated with a business application]]
- [[eaw-unassign-business-capabilities-from-ba|Remove business capabilities associated with a business application]]
- [[view-ba-form-in-coreui|Open business application form in Core UI from EA Workspace]]
- [[view-all-business-apps|View all business applications]]
- [[eaw-open-map-ba|View a unified map for a business application]]
- [[eaw-add--existing-archi-artfct-to-a-ba|Add an existing architectural artifact to a business application]]
- [[eaw-add-existing-business-capability-to-ba|Add an existing business capability to a business application]]
- [[ea-workspace|Enterprise Architecture Workspace]]
