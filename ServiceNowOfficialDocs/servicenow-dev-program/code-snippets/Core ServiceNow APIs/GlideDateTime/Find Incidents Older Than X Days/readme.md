---
title: "Find Incidents Older Than X Days"
aliases:
  - Find Incidents Older Than X Days
tags:
  - servicenow-dev-program
  - code-snippet
  - find-incidents-older-than-x-days
  - glidedatetime
---

## Overview
This script retrieves incidents that were opened more than X days ago using **GlideDateTime** and **GlideRecord**.  
Useful for reporting, escalations, notifications, and cleanup tasks.

## Table and Field
- **Table:** `incident`
- **Field:** `opened_at`

## Parameters
- **X (number of days):** Defines the threshold for old incidents (e.g., 30 days).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert UTC Time To Local Time/readme|Convert UTC Time To Local Time]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Convert date format/README|Convert date format]]
