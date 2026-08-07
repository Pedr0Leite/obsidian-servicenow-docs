---
title: "Find months between two dates"
aliases:
  - Find months between two dates
tags:
  - servicenow-dev-program
  - code-snippet
  - find-months-between-two-dates
  - script-includes
---

# getMonths

Helper function that calculates total months between two specified dates e.g. total months between 2020-01-01 and
2022-01-01 is 24!

## Usage

```javascript
var helper = new DateUtils();

gs.log(helper.getMonths('2020-01-01', '2022-01-01')); // This returns 24
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
