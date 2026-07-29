---
title: "API Token Expiry Warning"
aliases:
  - API Token Expiry Warning
tags:
  - servicenow-dev-program
  - code-snippet
  - api-token-expiry-warning
  - scheduled-jobs
---

API Token Expiry Warning Script
**Overview**
This script provides proactive monitoring and alerting for OAuth API tokens stored in the ServiceNow oauth_credential table. It identifies tokens nearing expiry within a configurable countdown window and sends notification emails to administrators, helping prevent sudden integration failures due to expired credentials.
**Problem Solved**
API tokens used for integrations have expiration timestamps after which they become invalid. Without early warnings, tokens can expire unnoticed, causing integration outages, failed API calls, and increased support incidents. This solution enables administrators to receive timely alerts allowing proactive token renewal and smoother integration continuity.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Bucket Group Reporting/readme|Bucket Group Reporting]]
