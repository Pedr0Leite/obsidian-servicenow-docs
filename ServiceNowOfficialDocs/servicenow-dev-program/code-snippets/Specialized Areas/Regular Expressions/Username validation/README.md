---
title: "Username validation"
aliases:
  - Username validation
tags:
  - servicenow-dev-program
  - code-snippet
  - username-validation
  - regular-expressions
---

## Strong Username Validation Script
This script validates a username entered in a ServiceNow catalog item form. It prevents form submission if the username does not meet the required format.

### Validation Criteria
The username must start with a letter (a–z or A–Z).
It must be at least 6 characters long.
It can only contain letters and numbers.

## Usage
Add the script as an onSubmit client script in the catalog item. If the username is invalid, an error message is shown and the form is not submitted.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
