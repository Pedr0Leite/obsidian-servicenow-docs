---
title: "Password Strength Checker"
aliases:
  - Password Strength Checker
tags:
  - servicenow-dev-program
  - code-snippet
  - password-strength-checker
  - regular-expressions
---

# Password Strength Checker

This code snippet checks the strength of a given password based on various criteria, including length, lowercase letters, uppercase letters, digits, and special characters.

**Note: This code is written in ES2021, which is supported in scoped applications where it is enabled (default for new scopes since Utah).**

## How to Use

1. Copy and paste the `passwordStrength.js` code into your project.

2. To check the strength of a password, call the `checkPasswordStrength` function with the password as the argument.

   ```javascript
   const password = "YourPassword123!";
   const result = checkPasswordStrength(password);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
