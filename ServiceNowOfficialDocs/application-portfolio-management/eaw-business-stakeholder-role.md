---
title: Business stakeholder role for Enterprise Architecture Workspace
description: The Business Stakeholder \(com.snc.business\_stakeholder\) plugin contains the business stakeholder role for Enterprise Architecture Workspace application. Users with this role can view or read records in the Enterprise Architecture Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-business-stakeholder-role.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-reference
---

# Business stakeholder role for Enterprise Architecture Workspace

The Business Stakeholder \(com.snc.business\_stakeholder\) plugin contains the business stakeholder role for Enterprise Architecture Workspace application. Users with this role can view or read records in the [[ea-workspace|Enterprise Architecture Workspace]].

## Upgrade information

-   **Upgrade customer**

    If you are upgrading to Australia, the business stakeholder role for Enterprise Architecture Workspace is available only when you activate Read only roles for [[application-portfolio-management-landing-page|Enterprise Architecture]] \(com.snc.apm\_read\_roles\) plugin.

-   **New customer**

    If you are a new customer, the Read only roles for Enterprise Architecture \(com.snc.apm\_read\_roles\) plugin is activated on zBoot. However, the business stakeholder role for Enterprise Architecture Workspace is available only when you [[install-ea-workspace|install Enterprise Architecture Workspace]] plugin.


## Why business stakeholder read-only role

The Business Stakeholder role is designed to give users read-only access to all the tables within the Enterprise Architecture Workspace application. This role is ideal for business stakeholders, such as business owners or managers, who need to view data but should not have the ability to modify it. By assigning this role, you ensure that these users can stay informed and monitor the data without making any changes.

## Business stakeholder read-only access limitations in Enterprise Architecture Workspace

Enterprise Architecture Workspace users with Business stakeholder role for Enterprise Architecture Workspace \(sn\_apm.apm\_read\) role have only view access to all the pages and they can't create or update any data in the Enterprise Architecture Workspace.

**Parent Topic:**[[explore-eaw|Exploring Enterprise Architecture Workspace]]

## Related

- [[explore-eaw|Exploring Enterprise Architecture Workspace]]
- [[ea-workspace|Enterprise Architecture Workspace]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
- [[install-ea-workspace|Install Enterprise Architecture Workspace]]
