---
title: "User Profile Field Validation"
aliases:
  - User Profile Field Validation
tags:
  - servicenow-dev-program
  - code-snippet
  - user-profile-field-validation
  - business-rules
---

# Overview
This JavaScript code snippet is designed to validate user profile fields in ServiceNow before submission. It is particularly useful for ServiceNow developers looking to implement robust data validation mechanisms in user profiles.

# How It Works
The snippet uses a business rule that executes on form submission to validate user input:
- **Regular Expressions**: It utilizes regex patterns to check the format of the `phone` and `email` fields.
- **Error Messaging**: If the validation fails, an error message is displayed to the user, and the submission is aborted. 

# Implementation
- **Add to a Business Rule**: This snippet should be incorporated into a business rule configured to run on the user profile table.
- **Adjust Validation Patterns**: Modify the `phoneNumberPattern` and `emailPattern` variables to align with your specific requirements (e.g: international phone formats).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
