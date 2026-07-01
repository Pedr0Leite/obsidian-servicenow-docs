---
title: Exploring business applications
description: A business application is software used by business users to perform a business function. Classify the applications to maintain an inventory and consolidate the business applications. Analyze, assess, and evaluate the applications across various dimensions and determine the action that you can take for each application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-manage-business-applications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Exploring the application portfolio, Exploring Portfolio list view, Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-concept
---

# Exploring business applications

A business application is software used by business users to perform a business function. Classify the applications to maintain an inventory and consolidate the business applications. Analyze, assess, and evaluate the applications across various dimensions and determine the action that you can take for each application.

You can record the details of a business application manually or import the list of applications from a spreadsheet or a third-party tool. To [import data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/c_ImportDataUsingImportSets.md), define a data source and transform map, and run or schedule an import.

## Assessment of Business applications

In [[application-portfolio-management-landing-page|Enterprise Architecture]], add any business application that you want to assess and track for costs, usage, business value, functional fitment, and risks.

## Modeling platform applications and platforms

Use the [[eaw-apprat-business-application-form|Business Application form]] to create a record and capture the details of a platform application just as you create a record for a business application. Use the same form to create individual records of all business applications that run on the platform. This structure gives you a hierarchy of business applications associated with the platform host. The **Architecture type** field values help you to distinguish between the platform host and platform application data.

The architecture type values help in the following business cases:

-   Assess the performance of the platform as a whole as well as assess the performance of individual applications running on it.
-   Platform may be owned by a business owner who may not be the owner of the applications running on that platform. In such a scenario, the platform owner can assess the performance of the platform independent of the application owners, who assess the applications associated with the platform.

For example, you can create a business application record for the ServiceNow® platform. Then, create individual business application records such as Enterprise Architecture, Financial Management, and Project Portfolio Management and associate these applications to the ServiceNow® platform. The distinction between the records whether it’s a business application running on a host or a platform hosting the applications lies in the **Architecture type** values of platform application and platform host.

**Parent Topic:**[[eaw-app-portfolio|Exploring the application portfolio]]

**Related topics**  


[[view-all-business-apps|View all business applications]]

[[eaw-create-business-app|Add or edit a business application]]

[[eaw-view-business-capabilities-assoc-with-ba|View business capabilities associated with a business application]]

[[eaw-add-existing-business-capability-to-ba|Add an existing business capability to a business application]]

[[eaw-unassign-business-capabilities-from-ba|Remove business capabilities associated with a business application]]

[[eaw-create-lucid-diagram-ba|Create a Lucidchart diagram for a business application in the EA Workspace]]

[[view-ba-form-in-coreui|Open business application form in Core UI from EA Workspace]]

[[eaw-open-map-ba|View a unified map for a business application]]

[[eaw-view-roadmap-ba|View roadmap of a business application]]

[[eaw-associate-info-obj-ba|Manage information objects of a business application in EA Workspace]]

[[eaw-view-archi-artfct-assoc-with-ba|View architectural artifacts associated with a business application]]

[[eaw-assoicate-artifact-ba|Create an architectural artifact and associate it with a business application]]

[[eaw-add--existing-archi-artfct-to-a-ba|Add an existing architectural artifact to a business application]]

[[eaw-unassign-archi-artfct-assoc-ba|Remove architectural artifacts associated with a business application]]

## Related

- [[eaw-app-portfolio|Exploring the application portfolio]]
- [[view-all-business-apps|View all business applications]]
- [[eaw-create-business-app|Add or edit a business application]]
- [[eaw-view-business-capabilities-assoc-with-ba|View business capabilities associated with a business application]]
- [[eaw-add-existing-business-capability-to-ba|Add an existing business capability to a business application]]
- [[eaw-unassign-business-capabilities-from-ba|Remove business capabilities associated with a business application]]
- [[eaw-create-lucid-diagram-ba|Create a Lucidchart diagram for a business application in the EA Workspace]]
- [[view-ba-form-in-coreui|Open business application form in Core UI from EA Workspace]]
- [[eaw-open-map-ba|View a unified map for a business application]]
- [[eaw-view-roadmap-ba|View roadmap of a business application]]
- [[eaw-associate-info-obj-ba|Manage information objects of a business application in EA Workspace]]
- [[eaw-view-archi-artfct-assoc-with-ba|View architectural artifacts associated with a business application]]
- [[eaw-assoicate-artifact-ba|Create an architectural artifact and associate it with a business application]]
- [[eaw-add--existing-archi-artfct-to-a-ba|Add an existing architectural artifact to a business application]]
- [[eaw-unassign-archi-artfct-assoc-ba|Remove architectural artifacts associated with a business application]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
- [[eaw-apprat-business-application-form|Business application form]]
