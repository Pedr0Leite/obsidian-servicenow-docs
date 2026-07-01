---
title: Quorum Control Policy
description: The Quorum Control Policy specifies the minimum number of approvals required among the total number of selected approvers to reach quorum for customer managed key withdrawal.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/cloud-encryption/quorum-ctrl-policy.html
release: australia
product: Cloud Encryption
classification: cloud-encryption
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Cloud Encryption with Key Management, Encryption]
tags:
  - platform-security
  - cloud-encryption
  - kms
  - keys
  - type-concept
---

# Quorum Control Policy

The Quorum Control Policy specifies the minimum number of approvals required among the total number of selected approvers to reach quorum for customer managed key withdrawal.

**Warning:** You must sign a legal addendum to activate the key withdrawal functionality. The Quorum Control Policy Settings option becomes available when the withdrawal feature is enabled, otherwise the module isn’t visible on the app menu. After key withdrawal, your instance is no longer available until the [[encryption-landing|encryption]] key is resupplied and is active again.

In certain circumstances, you may want to create a key withdrawal. You must first [[c_requestAPI|request]] the key withdrawal functionality from Customer Service and Support.

The Quorum Control Policy specifies the minimum number of approvals required among the total number of selected approvers to reach quorum for customer managed key withdrawal. For instance, there are a total of five approvers, but only four approvals are required to reach quorum. When four approvals are obtained, the withdrawal request is processed and the key withdrawn.

Whenever a withdrawal operation is performed in a group enabled for quorum approval, a workflow for quorum approval is triggered. An [[email|email]] notification is sent to all [[users|users]] who can grant approval. Tasks are also generated in the approvers’ accounts, which they see on the dashboard when they log in to their ServiceNow account.

The users can grant approvals from the Instance, the email, or the [[key-mgmt-operations-ce|Key Management Operations]] page. The key withdrawal operation is blocked until the quorum is met.

Once the minimum number of approvers is reached, quorum is reached and the key withdrawal will trigger. The withdrawal is performed and is logged, including the names of users who approved the request.

See [Configure Quorum Control Policy Settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/cloud-encryption/configure-quorum.md) for setup details.

-   **[Configure Quorum Control Policy Settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/cloud-encryption/configure-quorum.md)**  
Follow these steps to [[configure-quorum|configure Quorum Control Policy Settings]].
-   **[Manage Quorum Control](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/cloud-encryption/quorum-ctrl-mgmt.md)**  
After a withdrawal operation workflow is triggered, quorum actions can be managed from the Key Management Operations page. The key withdrawal operation is blocked until the quorum is met.

**Parent Topic:**[Cloud Encryption with Key Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/cloud-encryption/dare-overview.md)

## Related

- [[encryption-landing|Encryption]]
- [[c_requestAPI|request]]
- [[email|Email]]
- [[users|Users]]
- [[key-mgmt-operations-ce|Key management operations]]
- [[configure-quorum|Configure Quorum Control Policy Settings]]
