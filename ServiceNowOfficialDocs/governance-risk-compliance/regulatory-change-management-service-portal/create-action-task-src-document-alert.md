---
title: Complete the action task associated with the alert
description: Complete the action tasks that are related to the regulatory event alerts and source document alerts. The compliance and risk users complete the action tasks that are assigned to them. The compliance and risk managers track the progress on the action tasks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/regulatory-change-management-service-portal/create-action-task-src-document-alert.html
release: australia
product: Regulatory Change Management Service Portal
classification: regulatory-change-management-service-portal
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Manage regulatory tasks, Regulatory Change Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - regulatory-change
  - grc
  - impact
  - tracking
  - type-task
---

# Complete the action task associated with the alert

Complete the action tasks that are related to the regulatory event alerts and source document alerts. The compliance and risk users complete the action tasks that are assigned to them. The compliance and risk managers track the progress on the action tasks.

## Before you begin

Role required: sn\_compliance.manager, sn\_risk.manager, sn\_compliance.user, sn\_risk.user, sn\_grc\_reg\_change.manager

## About this task

The action tasks are created as a follow-up to complete the changes that have been identified as part of the [[reg-change-task|regulatory change tasks]] and [[source-doc-import-task|source document import tasks]].

The actions described in the following steps are performed by the users with the sn\_compliance.manager, sn\_risk.manager, sn\_compliance.user, sn\_risk.user, and sn\_grc\_reg\_change.manager roles.

## Procedure

1.  Log in with the sn\_compliance.manager or the sn\_risk.manager user role.

2.  Navigate to **All** &gt; **[[reg-change-mgmt-landing-page|Regulatory Change Management]]** &gt; **Compliance Workspace**.

    The Regulatory Change Management application in the Compliance Workspace is displayed.

3.  In the [[list-view-uib-ws|List view]], navigate to **Lists** &gt; **[[list-view-of-reg-alerts|Regulatory Alerts]]** &gt; **Assigned Alerts** view.

4.  Navigate to the action task that is marked for you.

5.  Assign the action task as described in the table.

    |Role|Description|
    |----|-----------|
    |**sn\_compliance.manager**|Log in with the sn\_compliance.manager user role. Assign the action task associated with the regulatory event alert or the source document alert to the user with the sn\_compliance.user role.|
    |**sn\_risk.manager**|Log in with the sn\_risk.manager user role. Assign the action task associated with the regulatory event alert or the source document alert to the user with the sn\_risk.user role.|

6.  Complete the action task as described in the table.

    |Role|Description|
    |----|-----------|
    |**sn\_compliance.user**|Log in with the sn\_compliance.manager user role. Complete the action tasks that are assigned to you and mark the state of the action task as **Completed**.|
    |**sn\_risk.user**|Log in with the sn\_risk.manager user role. Complete the action tasks that are assigned to you and mark the state of the action task as **Completed**.|

7.  Verify the status of the action task as described in the table.

    |Role|Description|
    |----|-----------|
    |**sn\_compliance.manager**|Log in with the sn\_compliance.manager user role. Verify that the action task associated with the regulatory event alert or the source document alert has been completed by the user with the sn\_compliance.user role.|
    |**sn\_risk.manager**|Log in with the sn\_risk.manager user role. Verify that the action task associated with the regulatory event alert or the source document alert has been completed by the user with the sn\_risk.user role.|


## Result

Once the user with the sn\_compliance.user or the sn\_risk.user role completes the action task, the regulatory event alert and the parent regulatory change task are closed automatically. Similarly, the source document alert and the parent source document import task are closed when the associated action tasks are completed. This is the final step of the regulatory tasks workflow.

## Related

- [[reg-change-task|Regulatory change tasks]]
- [[source-doc-import-task|Source document import tasks]]
- [[reg-change-mgmt-landing-page|Regulatory Change Management]]
- [[list-view-uib-ws|List view]]
- [[list-view-of-reg-alerts|Regulatory alerts]]
