---
title: Activate Case Digests
description: Activate the Case Digests plugin to use the case digests feature.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/activate-case-digests.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure case digests, Configure case management, Case management, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Activate Case Digests

Activate the Case Digests plugin to use the case digests feature.

## Before you begin

Role required: admin

## About this task

The Case Digests plugin automatically activates the following plugins:

-   Customer Service \(com.sn\_customerservice\)
-   Customer Service Document Template \(com.sn\_csm\_doc\_template\)
-   ServiceNow Document Viewer \(com.snc.documentviewer\)
-   [[c_TargetedCommunications|Targeted Communications]] \(com.sn\_publications\)

The Case Digests feature uses the recipient [[migration-lists|lists]] feature from the Targeted Communications plugin \(sn\_publications\).

When creating a case action summary record, users with the sn\_esm\_agent role can select a recipient list of the type Internal Users. Selecting the **Publish to Case &amp; Notify** UI action on the Case Action Summary form sends an email notification to the users included in the selected recipient list.

**Note:** The **Publish to Case &amp; Notify** UI action is available when a list has been selected in the **Additional internal recipients** field.

For more information, see [[targeted-comm-dynamic-list|Recipient lists]].

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Plugins**.

2.  Search for the plugin com.sn\_csm\_case\_digest.

3.  Click **Activate**.

## Related

- [[targeted-comm-dynamic-list|Recipients lists]]
- [[c_TargetedCommunications|Targeted communications]]
- [[migration-lists|Lists]]
