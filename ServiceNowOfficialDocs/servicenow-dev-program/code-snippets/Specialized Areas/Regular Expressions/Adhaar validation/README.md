---
title: "Adhaar validation"
aliases:
  - Adhaar validation
tags:
  - servicenow-dev-program
  - code-snippet
  - adhaar-validation
  - regular-expressions
---

# Regular Expression on Catalog Client script

*****************

8th october:

This script will validate the Adhaar number.

Adhaar is a 12 digit unique identification number issued by the Unique Identification Authority of India (UIDAI) for Indian residents.

The script will validate Adhaar through regex, and if it is not valid, the variable is cleared with a field message.

The preferred OOB method for catalog variables is listed here : https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/service-catalog-management/task/define-regex-vrble.html . The same regex can be defined in "Variable Validation Regex" module.


Regex details :

/^[2-9][0-9]{3}[0-9]{4}[0-9]{4}$/

// ^ → Start of the string

// [2-9] → The first digit must be between 2 and 9

// [0-9]{3} → Followed by exactly 3 digits (0–9)

// [0-9]{4} → Followed by exactly 4 digits (0–9)

// [0-9]{4} → Followed by exactly 4 digits (0–9)

// $ → End of the string

*****************

With the help of this code, you can easily validate the input value from the user. If it is not an Adhaar, you can clear it and throw an error message below the variable. The same validation can be used for fields instead of variables.

* [Click here for script](script.js)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Credit Card Number Validator/README|Credit Card Number Validator]]
