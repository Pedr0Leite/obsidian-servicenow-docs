---
title: "User Impersonation Activity Logger"
aliases:
  - User Impersonation Activity Logger
tags:
  - servicenow-dev-program
  - code-snippet
  - user-impersonation-activity-logger
  - business-rules
---

# User Impersonation Activity Logger

A ServiceNow server-side utility that automatically creates a log when an action is performed under impersonation, helping distinguish between admin-added and user-added notes.

# Challenge

The challenge lies in distinguishing between actions performed by administrators impersonating users and those performed by the users themselves. Without a reliable way to track impersonation activity, it becomes difficult to ensure transparency and accountability in ticket histories. This lack of clarity can lead to confusion during audits, misinterpretation of updates, and potential compliance risks. Addressing this issue is critical to maintaining trust and operational efficiency.

## Description

This script identifies if the current user session is under impersonation (e.g., an admin impersonating another user).  
If true, it automatically appends a message in the **Logs** indicating that the note was added during impersonation.  
This improves auditability and clarity when reviewing ticket histories.

## Functionality

The User Impersonation Activity Logger provides the following capabilities:
- Detects if the current user is impersonating another user
- Automatically appends a log message stating the impersonation context
- Works in **Business Rule** and Global Scoped Tables
- Logs both actual user and impersonated user details
- Provides clear distinction for audit and tracking

## Usage Instructions

### Add as Business Rule

```javascript
// When: before update
// Table: incident 
// Script:
(function executeRule(current, previous /*null when async*/) {

//Add the logic here

})(current, previous);
```


## Prerequisites

- Need admin access to check the impersonation logs later


## Dependencies

- GlideSystem API
- GlideImpersonate API
- gs.getSession()


## Category

Server-Side Components / Business Rules / User Impersonation Activity Logger


## Screenshots
<img width="3024" height="536" alt="image" src="https://github.com/user-attachments/assets/3ae408db-175f-4281-a9d7-f21df16314e7" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
