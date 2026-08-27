---
title: Add or edit a data domain from the Portfolio page
description: Create or edit a data domain to relate an information object to the database catalog of a database instance to collect the physical data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-add-or-edit-a-data-domain-from-the-portfolio-page.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Manage data domains, Working with information portfolio, Working with Portfolio list view, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Add or edit a data domain from the Portfolio page

Create or edit a data domain to relate an information object to the database catalog of a database instance to collect the physical data.

## Before you begin

Although an [[application-portfolio-management-landing-page|Enterprise Architecture]] user \(sn\_apm.apm\_user\) can view a data domain, the access control on the Data Domain \[sn\_apm\_data\_domain\] table is limited to its different users.

-   -   The Enterprise Architecture analyst and Enterprise Architecture administrator with sn\_apm.apm\_admin role have create, write, and delete privileges.
-   The Enterprise Architecture user with the sn\_apm.apm\_user role has read access only.

Role required: sn\_apm.apm\_admin

## Procedure

1.  Navigate to **Workspace** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Portfolio List view by selecting the Portfolio icon \[Omitted image "portfolio-icon.png"\] Alt text: Portfolio icon.

3.  Select the expand row icon \(\[Omitted image "ExpandIcon.png"\] Alt text: Expand Row icon\) next to **Information Portfolio**.

4.  Select **Data Domains**.

5.  Add or edit a data domain.

    -   To add a data domain, select **New**.
    -   To update details of an existing data domain, select the data domain.
6.  On the form, fill in the fields.

    For field information, see [[eaw-data-domain-form|Data Domain form]].

7.  Select **Save**.

    You can also create data domains from the Setup page of Enterprise Architecture Workspace. For information, see [[eaw-add-edit-info-data-domain|Add or edit an information data domain]].


**Parent Topic:**[[eaw-manage-data-domains|Manage data domains]]

**Related topics**  


[[eaw-view-all-data-domains|View all data domains]]

## Related

- [[eaw-data-domain-form|Data Domain form]]
- [[eaw-add-edit-info-data-domain|Add or edit an information data domain]]
- [[eaw-manage-data-domains|Manage data domains]]
- [[eaw-view-all-data-domains|View all data domains]]
- [[application-portfolio-management-landing-page|Enterprise Architecture]]
- [[ea-workspace|Enterprise Architecture Workspace]]
