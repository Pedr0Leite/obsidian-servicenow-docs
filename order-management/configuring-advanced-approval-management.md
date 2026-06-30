---
title: Configuring Advanced Approval Management
description: Install the Advanced Approval Management application to build workflows that automate the approval process for Sales Customer Relationship Management entities such as customer quotes.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/configuring-advanced-approval-management.html
release: australia
topic_type: concept
last_updated: "2026-03-23"
reading_time_minutes: 2
keywords: [configure]
breadcrumb: [Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Configuring Advanced Approval Management

Install the [[explore-advanced-approval-for-sales|Advanced Approval Management]] application to build workflows that automate the approval process for [[order-mgt-overview|Sales Customer Relationship Management]] entities such as customer quotes.

## Advanced Approval Management configuration overview

1.  [[install-advanced-approval-management|Install Advanced Approval Management]].

    You can install the Advanced Approval Management application \(sn\_adv\_appr\_mgmt\) if you have the admin role.

    **Note:** The plugin for the Sales Customer Relationship Management application for which you are creating workflows, such as [[quote-management|Quote Management]], must also be installed.

2.  [[create-approval-configuration|Create an approval configuration]].

    Create an approval configuration for a Sales Customer Relationship Management entity, such as quotes. An approval configuration contains the approval elements that you define to automate approval workflows: conditions that trigger approval workflows, approval [[rules_101|rules]], approval chains, and approval users and groups. Starting with the 1.0.1 release, you can enable certain features for the configuration, namely approval request consolidation, escalations, and email reminder features.

3.  [[set-approval-trigger-conditions|Create conditions that trigger approval workflows]].

    Define one or more conditions that apply company policies, such as legal or pricing guidelines, to trigger an approval workflow. Also enable the smart reapprovals feature, which allows previous approvals to be used for a resubmitted approval.

4.  [[create-approval-rules|Create approval rules]].

    Create approval rules that define the approval criteria and approvers for an approval step.

5.  [[create-approval-chain|Create approval chains]].

    Optionally create approval chains that control the sequence in which two or more approvals are run.

6.  [[create-approval-users|Define an approval user]].

    Define the approver and the associated approval rule that they review during the approval process.

7.  [[create-approval-groups|Define an approval group]].

    Define the group that can approve requests for a specified approval rule.


**Note:** System notifications are used to deliver approval status to requesters and inform approvers of approval rejections. You can use these notifications and customize them if needed. For more information on these notifications, see [[setting-up-approval-notifications|Notifications in Advanced Approval Management]].

## Related

- [[install-advanced-approval-management|Install Advanced Approval Management]]
- [[create-approval-configuration|Create an approval configuration]]
- [[set-approval-trigger-conditions|Create conditions that trigger approval workflows]]
- [[create-approval-rules|Create approval rules]]
- [[create-approval-chain|Create approval chains]]
- [[create-approval-users|Define an approval user]]
- [[create-approval-groups|Define an approval group]]
- [[setting-up-approval-notifications|Notifications in Advanced Approval Management]]
- [[explore-advanced-approval-for-sales|Advanced Approval Management]]
- [[order-mgt-overview|Sales Customer Relationship Management]]
- [[quote-management|Quote Management]]
- [[rules_101|Rules]]
