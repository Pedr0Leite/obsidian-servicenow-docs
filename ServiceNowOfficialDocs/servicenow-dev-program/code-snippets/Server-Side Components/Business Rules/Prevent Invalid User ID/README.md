---
title: "Prevent Invalid User ID"
aliases:
  - Prevent Invalid User ID
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-invalid-user-id
  - business-rules
---

#  Prevent Invalid User ID

## Overview
This **ServiceNow Business Rule** prevents inserting or updating a record when:
- `user_name` is missing or invalid.
- Both `first_name` and `last_name` are missing or invalid.

## Functionality Breakdown

### 1. `isInvalid(value)`
- Detects invalid values in user fields.
- Returns `true` if:
  - Value is `null`, `undefined`, or empty (`""`)
  - Value (after trimming spaces and lowering case) equals `"null"`

Example:
```javascript
isInvalid(null);        // true
isInvalid("");          // true
isInvalid("NULL");      // true
isInvalid("john");      // false
```

### 2. `current.setAbortAction(true)`
- Stops the record from being inserted or updated.
- Used inside **Before Business Rules**.
- Prevents saving invalid data to the database.

### 3. `gs.addErrorMessage("...")`
- Displays a user-friendly error message at the top of the form.
- Helps users understand *why* the save was blocked.


##  Notes
- Case-insensitive — handles "null", "NULL", "Null", etc.  
- Works best in **Before Business Rules** to stop invalid data before saving.  
- Adding `gs.addErrorMessage()` helps users understand the validation reason.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
