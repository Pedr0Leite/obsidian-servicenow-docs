---
title: "Assign role for a day Util"
aliases:
  - Assign role for a day Util
tags:
  - servicenow-dev-program
  - code-snippet
  - assign-role-for-a-day-util
  - script-includes
---

# Utility: AssignRoleToUserForADay.js

## Overview
`AssignRoleToUserForADay.js` is a utility script designed to temporarily assign a role to a user for a single day. This can be useful for granting temporary permissions or access within an application.

## Features
- Assign a role to a user for 24 hours.
- Automatically revoke the role after the time period expires.
- Log actions for auditing purposes.

## Usage
1. **Import the script**:
    ```javascript
    var assignRoleToUserForADay = require('./Utility/AssignRoleToUserForADay');
    ```

2. **Call the function**:
    ```javascript
    assignRoleToUserForADay(userId, roleId)
        .then(() => {
            console.log('Role assigned successfully.');
        })
        .catch((error) => {
            console.error('Error assigning role:', error);
        });
    ```

## Parameters
- `userId` (String): The ID of the user to whom the role will be assigned.
- `roleId` (String): The ID of the role to be assigned.

## Example
```javascript
var assignRoleToUserForADay = require('./Utility/AssignRoleToUserForADay');

var userId = '12345';
var roleId = 'admin';

assignRoleToUserForADay(userId, roleId)
    .then(() => {
        console.log('Role assigned successfully.');
    })
    .catch((error) => {
        console.error('Error assigning role:', error);
    });
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
