---
title: "Check if number has 10 digits"
aliases:
  - Check if number has 10 digits
tags:
  - servicenow-dev-program
  - code-snippet
  - check-if-number-has-10-digits
  - regular-expressions
---

# Digit Length Validator

## Description

This script checks if a string contains exactly a specified number of digits. Useful for validating numeric input. The digit count can be adjusted in the code.

## Usage
To change the required digit count, update the number in the regular expression
```
var digitLengthRegex = /^\d{N}$/;  // Replace N with desired digit count
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Credit Card Number Validator/README|Credit Card Number Validator]]
