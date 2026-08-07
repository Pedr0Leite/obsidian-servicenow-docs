---
title: "SSN Formatting"
aliases:
  - SSN Formatting
tags:
  - servicenow-dev-program
  - code-snippet
  - ssn-formatting
  - regular-expressions
---

This script will both check if a given string is an SSN (9 numerical characters with out hyphens or 12 with hyphens in the 4th and 7th positions) and then return a formatted version of the string as per your choice including or excluding hyphens via the "includeHyphens" variable. If used is servicenow this could be instead mapped to a field rather than set in the script but allows for a more programmically approach to the solution. If the input does not match the form of an SSN (see above) it will console log out that it's not a valid SSN. This includes cases where only one of the 2 hyphens are present (i.e. XXX-XXXXXX or XXXXX-XXXX). This could be expanded to check if the input is in one of those two forms and correct for it without failing but I've chosen to leave the script in this form.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
