---
title: "Currency conversion to USD"
aliases:
  - Currency conversion to USD
tags:
  - servicenow-dev-program
  - code-snippet
  - currency-conversion-to-usd
  - business-rules
---

This script is designed to automatically convert the value of the Annual Budget field (annual_budget) from its original currency to USD. It uses the fx_currency and fx_rate tables to fetch the latest exchange rates and performs the conversion only when valid data is available. 🔍 Key Features:

Field Focus: Converts the annual_budget field based on the currency specified in budget_currency. Validation: Ensures both the currency code and amount are valid before proceeding. Currency Check: If the currency is already USD, it bypasses conversion. Exchange Rate Lookup: Retrieves the most recent exchange rates for both the source currency and USD. Conversion Logic: Applies the formula USD Amount=(Original AmountSource Rate)×USD Rate\text{USD Amount} = \left(\frac{\text{Original Amount}}{\text{Source Rate}}\right) \times \text{USD Rate}USD Amount=(Source RateOriginal Amount​)×USD Rate. Error Handling: Clears the USD field if any required data is missing or invalid.

This script ensures accurate and up-to-date currency conversion for budgeting purposes and is well-commented for maintainability and clarity

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
