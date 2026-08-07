---
title: Create a pre-authorization request
description: Create a pre-authorization request to check if certain parts or charges are covered under warranty or service contracts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-agents-create-pre-auth-request.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Pre-authorization requests, Agent management, Use, Manufacturing Commercial Operations]
tags:
  - manufacturing
  - industry
  - solutions
  - ot
  - type-task
---

# Create a pre-authorization request

Create a pre-authorization request to check if certain parts or charges are covered under warranty or service contracts.

## Before you begin

Role required: sn\_claim\_cmn.warranty\_specialist

## Procedure

1.  Navigate to **Workspaces** &gt; **CSM/FSM Configurable Workspace** &gt; **Lists** &gt; **Pre-authorization requests** &gt; **All**.

2.  Select **New**.

3.  On the Create New Pre Authorized Repair Request form, fill in the fields.

    For a description of the field values, see [[mco-pre-auth-form|Pre-authorization form]].

4.  Select **Continue**.

5.  Select **Job details**.

6.  Select **Add claim jobs**.

7.  Set **Type** as one of the following:WarrantyGoodwill.

    -   Warranty: Repair, replacement, or service that is covered under the warranty.
    -   Goodwill: Repair services that may be free or discounted at the manufacturer's discretion.
8.  On the [[mco-use-repair-claim|Repair claim]] jobs form, fill in the fields.

    For a description of the field values, see [[mco-pre-auth-job-details-form|Pre-authorization job details form]].

9.  Select **Save**.

10. If you need to add additional claims, select **Add claim job**.

11. Select **Submit**.

    The [[mco-pre-auth-request|Pre-authorization]] in review window is displayed.

12. Select **Pre-authorization review**, and then either approve, reject, or return the request.

    For more information on pre-authorization review tasks, see [[mco-pre-auth-review|Review and approve a pre-authorization request]].

13. Select **Assign to me** to assign the case to yourself.


-   **[Review and approve a pre-authorization request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/manufacturing/mco-pre-auth-review.md)**  
Review and approve the [[mco-pre-auth-request-use|pre-authorization request]] submitted by a dealer.

**Parent Topic:**[[mco-agents-pre-auth-requests|Pre-authorization requests]]

## Related

- [[mco-pre-auth-form|Pre-authorization form]]
- [[mco-pre-auth-job-details-form|Pre-authorization job details form]]
- [[mco-pre-auth-review|Review and approve a pre-authorization request]]
- [[mco-agents-pre-auth-requests|Pre-authorization requests]]
- [[mco-use-repair-claim|Repair claim]]
- [[mco-pre-auth-request|Pre-authorization]]
- [[mco-pre-auth-request-use|Pre-authorization request]]
