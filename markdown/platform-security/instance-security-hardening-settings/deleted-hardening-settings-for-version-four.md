---
title: Deleted hardening settings for baseline version 4.0
description: Some hardening settings have been removed with the release of Security Center baseline version 4.0.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/instance-security-hardening-settings/deleted-hardening-settings-for-version-four.html
release: australia
product: Instance Security Hardening Settings
classification: instance-security-hardening-settings
topic_type: concept
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Deleted hardening settings, Baseline versions, Hardening settings, Platform Security]
---

# Deleted hardening settings for baseline version 4.0

Some [[security-hardening-settings|hardening settings]] have been removed with the release of [[sec-center-v2|Security Center]] baseline version 4.0.

-   LDAP Initial Password
-   Mobile Offline Roles
-   Restrict Access to Critical Data through Zero Trust Access [[ca-policies|Policies]] \(Plugin Applicability: [[adaptive-authentication|Adaptive Authentication]]\)
-   Read Only Tables Allowlist For Write
-   Allowed JDBC Probe Operations \(Plugin Applicability: MID Server\)
-   Set Allowed Domains which Create [[users|Users]] from Incoming Emails
-   Set Complex "Default" Password
-   Accessible Properties in GraphQL Allowlist
-   Cross Origin Messaging Allowlist
-   Limit Attachment Size in Training and Prediction Flows for GraphQL Enpoints \(Plugin Applicability: Platform Document Intelligence\)
-   Edit Content Roles Allowlist \(Plugin Applicability: Communities\)
-   Ensure Database Queries Do Not Trigger a OutofMemory Exception Due to Query Size
-   Role Allowlist for Script Execution
-   Downloadable File Type Allowlist
-   Read Only Tables Allowlist For Delete
-   Enforce [[c_Authentication|Authentication]] for Roleless ACL
-   Minimize LDAP One-Time Token Expiry Time
-   Allow Only Trusted IP Addresses for Authentication
-   Set Mobile [[c_SelfServicePasswordReset|Password Reset]] URL
-   Password Complexity of Service Accounts \(Plugin Applicability: Service Bridge\)
-   Notify Users During Password Reset/Change Process
-   Enforce Application Scope Restrictions
-   [[sc-access-control|Access Control]] Requirements \(Plugin Applicability: Communities\)
-   Record History Access Role Allowlist
-   Restrict Role Access for Attachments
-   Only Allow PDFs from Predefined List of Trusted URLs
-   Prevent Emailing One-Time Password During LDAP Server Outage
-   Convert Inbound [[email|Email]] Images to Attachments
-   Review Extraneous Explicit Role Access Control Condition

**Parent Topic:**[Deleted hardening settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/instance-security-hardening-settings/hardening-settings-deleted.md)

## Related

- [[security-hardening-settings|Hardening settings]]
- [[sec-center-v2|Security Center]]
- [[ca-policies|Policies]]
- [[adaptive-authentication|Adaptive authentication]]
- [[users|Users]]
- [[c_Authentication|Authentication]]
- [[c_SelfServicePasswordReset|Password Reset]]
- [[sc-access-control|Access control]]
- [[email|Email]]
