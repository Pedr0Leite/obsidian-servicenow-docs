---
title: "To check incidents having a VIP caller"
aliases:
  - To check incidents having a VIP caller
tags:
  - servicenow-dev-program
  - code-snippet
  - to-check-incidents-having-a-vip-caller
  - background-scripts
---

# VIP Caller Incidents Background Script

## Description
This background script fetches all incidents where the caller is marked as a VIP user
and prints the incident number and short description in the logs.

## Usage
1. Go to **System Definition > Scripts - Background** in ServiceNow.
2. Paste the script into the editor.
3. Click **Run Script**.
4. Check the output in the logs.

## Prerequisites
- The User table must have a **VIP checkbox** (`vip` field).
- The Incident table must have a `caller_id` reference field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
