---
title: Import certification schedules in to Data Manager
description: Import the certification schedules into Data Manager to convert the existing certification schedules to certification policies.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-convert-cert-schedules-to-cert-policies.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure certification policies, Configure EA Workspace using the Setup page, Configuring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-task
---

# Import certification schedules in to Data Manager

Import the certification schedules into Data Manager to convert the existing certification schedules to certification policies.

## Before you begin

Role required: system admin

## About this task

This process converts the certification schedules into draft certification policies and you can then publish these policies to activate them.

**Note:** If you upgraded your EA Workspace from a previous version to the 4.0.0 version, you might see that your certification data is still fetched from the Certification Schedules \(cert\_schedule\) table. Follow these instructions to import your data certification schedules to certification policies.

## Procedure

1.  Navigate to **All** &gt; **Workspaces** &gt; **CMDB Workspace**.

2.  Select **Management** in the CMDB Workspace menu bar.

3.  Select the Data Manager link in Management tools, in the Manage section.

    \[Omitted image "cmdb-datamangement.png"\] Alt text: Management tools page

4.  On the Data Manager overview page, select **Import** on the banner at the top of the page.

    **Note:** If all the certification schedules are already imported, the Import banner doesn’t appear. You can see the imported policies in the Draft policies tab \(refer to step 6\).

5.  In the Confirm import of certification schedule into draft policies, select **Import into draft policies**.

    \[Omitted image "cmdb-import-cert-schedules.png"\] Alt text: Confirmation message for importing Data Certification schedules as Data Manager draft policies

6.  In the Import summary modal, select **View draft policies**.

    The converted policies appear in the Data Manager policies page, under the Draft policies tab.\[Omitted image "cmdb-draft-policies.png"\] Alt text: Draft policies list

7.  Publish the draft policies to activate them.

    For more information, see [[eaw-publish-a-draft-policy|Publish a draft Data Manager policy]].


**Parent Topic:**[[eaw-setup-cert-policies|Configure certification policies]]

**Related topics**  


[Publish a draft Data Manager policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-publish-a-draft-policy.md)

[[eaw-manage-cert-schedules|Add or edit a certification policy]]

[[eaw-view-all-cert-schedules|View all certification policies]]

## Related

- [[eaw-publish-a-draft-policy|Publish a draft Data Manager policy]]
- [[eaw-setup-cert-policies|Configure certification policies]]
- [[eaw-manage-cert-schedules|Add or edit a certification policy]]
- [[eaw-view-all-cert-schedules|View all certification policies]]
