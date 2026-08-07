---
title: Security Operations Integration - Email Search and Delete flow
description: The Security Operations Integration - Email Search and Delete flow returns the number of threat emails from an email server search and, optionally, return details for each email found. After the email search is completed, you can delete the emails.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integ-email-search-delete.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Email Search and Delete capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Integration - Email Search and Delete flow

The Security Operations Integration - Email Search and Delete flow returns the number of threat emails from an email server search and, optionally, return details for each email found. After the email search is completed, you can delete the emails.

## Before you begin

Role required: sn\_si.analyst

## About this task

The search query can take some time to complete. After the count is received, approval is required to delete emails from an email server.

This flow is triggered by the **Delete from Email Server\(s\)** and **Search on Email Server\(s\)** buttons on the **Email Search** form in a security incident. For more information, see [Search for and delete phishing emails](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/search-delete-exchange-emails.md).

\[Omitted image "email-search-and-delete-flow.png"\] Alt text: Security Operations integration - Email Search and Delete flow

Activities specific to this flow are described here. For more information on other activities, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

The flow process activities include:

-   **[[execution-tracking-begins-mail-search-activity|Execution Tracking Begin \(Mail Search\) action]]**  
The Execution Tracking - Begin \(Mail Search\) capability execution action creates an execution tracking record and marks the record state as Started. This action is used by all capability and implementation flows to keep track of their state.

**Parent Topic:**[[email-search-capability|Security Operations Integration- Email Search and Delete capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[execution-tracking-begins-mail-search-activity|Execution Tracking Begin \(Mail Search\) action]]
- [[email-search-capability|Security Operations Integration- Email Search and Delete capability]]
