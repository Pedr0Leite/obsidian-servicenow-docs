---
title: "Password Validation Script"
aliases:
  - Password Validation Script
tags:
  - servicenow-dev-program
  - code-snippet
  - password-validation-script
  - catalog-client-script
---

Description of the Combined Password Validation Script
Purpose
The script validates the password entered by the user in a ServiceNow catalog item form. It ensures that the password meets strong security criteria and does not include the user's first or last name, enhancing overall security.

Validation Criteria
Strong Password Requirements:

At least 8 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Contains at least one digit.
Contains at least one special character (e.g., @$!%*?&).
First and Last Name Restrictions:

The password cannot contain the user's first name or last name.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
