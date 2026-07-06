---
title: "validate phone number"
aliases:
  - validate phone number
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-phone-number
  - client-scripts
---

Phone Number Validation — Client Script 
Overview

This Client Script validates that users enter their phone numbers in the strict format: (123) 456-7890.

It is triggered whenever the Phone field changes on a sys_user record. If the input does not match the required format, the script:

Displays an inline error message directly below the field.

Clears the invalid input so the user can re-enter the correct value.

This script is designed to be dynamic, simple, and user-friendly.

Features

Ensures phone numbers follow the exact format (123) 456-7890.

Provides immediate feedback via field-level error messages.

Clears invalid entries automatically to prevent submission errors.

Works on Classic UI forms and provides clear messaging to the user.

Usage Instructions
1. Create the Client Script

Navigate to System Definition → Client Scripts.

Click New to create a client script.

2. Configure the Script

Name: Phone Number Validation

Table: sys_user 

Type: onChange

Field: phone

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
