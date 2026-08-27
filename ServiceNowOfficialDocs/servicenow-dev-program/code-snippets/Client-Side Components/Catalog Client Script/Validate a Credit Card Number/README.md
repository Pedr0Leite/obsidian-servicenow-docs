---
title: "Validate a Credit Card Number"
aliases:
  - Validate a Credit Card Number
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-a-credit-card-number
  - catalog-client-script
---

**Description of the Credit Card Number Validation Script**
Purpose
The script validates a credit card number entered by the user in a ServiceNow form. 
It checks if the number is a valid 16-digit credit card number using a combination of a regular expression and the Luhn algorithm for basic validation.

**Validation Criteria**
Format:
The credit card number must consist of exactly 16 digits.
**Luhn Algorithm:**
The script implements the Luhn algorithm to determine if the credit card number is potentially valid. 
This algorithm helps catch common errors in credit card numbers, such as transposed digits.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
