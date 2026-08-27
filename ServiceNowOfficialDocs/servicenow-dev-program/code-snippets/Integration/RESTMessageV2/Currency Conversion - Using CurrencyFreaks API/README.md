---
title: "Currency Conversion - Using CurrencyFreaks API"
aliases:
  - Currency Conversion - Using CurrencyFreaks API
tags:
  - servicenow-dev-program
  - code-snippet
  - currency-conversion---using-currencyfreaks-api
  - restmessagev2
---

# Currency Conversion- Using CurrencyFreaks API
## Overview
This API allows to convert an amount from USD to any selected currency in real-time using live exchange rates fetched from the CurrencyFreaks API.

## Configuration Steps
### Get Your CurrencyFreaks API Key
1. Go to https://currencyfreaks.com
2. Sign up for a free account.
3. Navigate to Dasboard ->API Keys.
4. Copy your API key - you'll need it in ServiceNow.

### Create a REST Message in ServiceNow
- Name: CurrencyFreaks API
- Endpoint: https://api.currencyfreaks.com/v2.0/rates/latest?apikey=${apikey}&symbols=${symbols}
- HTTP Method: GET

### Example Response
```json
{"date":"2025-10-30 00:00:00+00","base":"USD","rates":{"EUR":"0.861846","SAR":"3.7502","KWD":"0.30678","INR":"88.4075"}}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
