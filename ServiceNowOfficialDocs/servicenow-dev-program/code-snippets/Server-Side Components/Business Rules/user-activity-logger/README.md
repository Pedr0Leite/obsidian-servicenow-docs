---
title: "user-activity-logger"
aliases:
  - user-activity-logger
tags:
  - servicenow-dev-program
  - code-snippet
  - user-activity-logger
  - business-rules
---

# User Activity Logger

A ServiceNow server-side script to log user activity with timestamps and session details.

## Description

This script creates an audit log entry whenever called, recording the current user's information, session ID, and timestamp. Useful for tracking user activities across the platform and maintaining an audit trail of user actions.

## Functionality

The User Activity Logger provides the following capabilities:
- Captures current user information (name and user ID)
- Records session ID for tracking purposes
- Creates timestamped audit trail records
- Provides success/error logging with descriptive messages
- Returns the system ID of the created log entry for further processing

## Usage Instructions

### In Business Rules

```javascript
// When: before insert
// Table: incident
// Script:
(function executeRule(current, previous /*null when async*/) {
    // Call the activity logger
    userActivityLogger();
})(current, previous);
```

### In Scheduled Jobs

```javascript
// Run this as a scheduled job to periodically log user sessions
userActivityLogger();
```

### In Script Includes

```javascript
var ActivityLogger = Class.create();
ActivityLogger.prototype = {
    initialize: function() {
    },
    
    logActivity: function() {
        return userActivityLogger();
    },
    
    type: 'ActivityLogger'
};
```

## Prerequisites

- Access to `sys_audit` table
- `gs.getUser()` API access
- Appropriate permissions to insert records into audit tables

## Dependencies

- GlideRecord API
- GlideDateTime API
- gs (GlideSystem) API



## Category

Server-Side Components / Business Rules / User Activity Logger

## Hacktoberfest 2025

Created for ServiceNow Hacktoberfest 2025 🎃

## License

MIT License

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
