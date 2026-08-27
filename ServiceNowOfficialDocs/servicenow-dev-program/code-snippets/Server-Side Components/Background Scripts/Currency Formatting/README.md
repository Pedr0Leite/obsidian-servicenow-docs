---
title: "Currency Formatting"
aliases:
  - Currency Formatting
tags:
  - servicenow-dev-program
  - code-snippet
  - currency-formatting
  - background-scripts
---

Format currency values to your preferred locale and format.
Examples are provided for EUR, HUF with English and Hungarian number format.

formatString values:
    Valid values:
    
    %s: Replaced by the currency symbol associated with the country code specified in the format() call.
    %v: Replaced by the currency amount, such as 123.45.
    %c: Replaced by the ISO currency code specified in the format() call, such as USD or EUR.
    %l: Replaced with the passed in value, no formatting performed.
    %p: Replaced by the percent sign (%).
    For example, if the format string is '%s%v%c' and the value to format is 123.45 in US dollars, the returned formatted string is $123.45 USD. If the format string is '%s%l%c' and the value string to format is '56M' in Euros, the returned formatted string is €56M EUR.

setMaxFractionDigits:
    Maximum number of fraction digits to return. Does a rounding based on the closest right-most digit.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
