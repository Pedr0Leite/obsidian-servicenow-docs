---
title: Configure onboarding tasks in playbook
description: You can configure customer success onboarding tasks in a playbook using the Process Automation Designer.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/acct-lifecycle-events/account-lifecycle-configure-simple.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Account onboarding playbook, Configure, Customer Success Management]
tags:
  - acct-lifecycle-events
  - account-lifecycle
  - ale
  - blueprint
  - case-management
  - sub-flows
  - type-task
---

# Configure onboarding tasks in playbook

You can [[account-lifecycle-config-cust-success|configure customer success]] onboarding tasks in a playbook using the Process Automation Designer.

## Before you begin

Role required:

-   sn\_acct\_lc.agent
-   One or more Playbooks roles. See [Playbooks roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/process-automation-designer-roles.md) for details.

## About this task

You can add, modify, and delete any tasks for the [[account-lifecycle-events-customer-success-about|Customer success]] onboarding tasks in a playbook using the Process Automation Designer. For example, if you want to configure one of the tasks in the Development &amp; Automation lane, perform the following steps.

## Procedure

1.  Navigate to **All** &gt; **Process Automation Designer** &gt; **Playbook Designer**.

2.  Select the **Account lifecycle onboarding process**.

3.  Navigate to the Development &amp; Automation lane and select the Setup Account Relationships activity.

4.  In the Activity properties window, select **View all properties** and select **Advanced**.

5.  In the General tab, enter the label name and description.

6.  In the When to start field, select **With Previous**.

    This option enables you to execute all activities in the task in parallel.

7.  Select the Automation tab and select **Onboarding Task** table.

8.  Add all required fields and any other fields that must be populated for this task in the [[account-lifecycle-use-cust-success|Customer success]] onboarding in the [[account-lifecycle-onboard-playbook|onboarding playbook]].

9.  Select **Done** and then **Activate**.


**Parent Topic:**[[account-lifecycle-configure|Configure the account onboarding playbook]]

## Related

- [[account-lifecycle-configure|Configure the account onboarding playbook]]
- [[account-lifecycle-config-cust-success|Configure customer success]]
- [[account-lifecycle-onboard-playbook|Onboarding playbook]]
- [[account-lifecycle-events-customer-success-about|Customer success]]
- [[account-lifecycle-use-cust-success|Customer success]]
