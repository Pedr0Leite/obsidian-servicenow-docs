---
title: "PAN Card Validation Script"
aliases:
  - PAN Card Validation Script
tags:
  - servicenow-dev-program
  - code-snippet
  - pan-card-validation-script
  - regular-expressions
---

Description
This client script in ServiceNow is designed to validate the format of a PAN (Permanent Account Number) card during form submission.
By ensuring that the PAN card number entered adheres to the expected format, this script enhances data integrity and user experience. 
If the entered PAN number is invalid, the script alerts the user, preventing form submission until a valid PAN number is provided.

Key Features

1. Format Validation: Checks PAN card format (5 letters, 4 digits, 1 letter).
2. User Alerts: Provides immediate feedback for invalid entries.
3. Submission Control: Prevents form submission with invalid PAN numbers.
4. Customizable: Easily adjustable for different field names.
5. Client-Side Efficiency: Quick validation without server delays.
6. Data Integrity: Ensures only correctly formatted PAN numbers are accepted.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
