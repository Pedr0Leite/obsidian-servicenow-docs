---
title: "Financial Service Utilities"
aliases:
  - Financial Service Utilities
tags:
  - servicenow-dev-program
  - code-snippet
  - financial-service-utilities
  - script-includes
---

**Financial Service Utilities Script Include**


This Script Include provides a collection of utility functions commonly used in financial services applications. 
It includes functions for calculating interest, formatting currency, and calculating loan payments.

**Functions:**
**calculateInterest(principal, rate, time)**: Calculates simple interest.
principal: The principal amount.
rate: The annual interest rate (in percentage).
time: The time period in years.
Returns the calculated simple interest.

**calculateCompoundInterest(principal, rate, time, compoundingFrequency)**: Calculates compound interest.
principal: The principal amount.
rate: The annual interest rate (in percentage).
time: The time period in years.
compoundingFrequency: The number of times interest is compounded per year.
Returns the calculated compound interest.

**formatCurrency(amount, currencyCode):** Formats a currency amount.
amount: The amount to be formatted.
currencyCode: The currency code (e.g., "USD", "EUR").
Returns the formatted currency amount.

**calculateLoanPayments(principal, rate, term):** Calculates monthly loan payments.
principal: The principal loan amount.
rate: The annual interest rate (in percentage).
term: The loan term in years.
Returns the calculated monthly loan payment.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
