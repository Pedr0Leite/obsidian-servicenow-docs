---
title: "CSV Parser"
aliases:
  - CSV Parser
tags:
  - servicenow-dev-program
  - code-snippet
  - csv-parser
  - script-includes
---

# Script Include: CSVParser

A script includes that parses concatenated CSV string and returns and array of the JSON objects for each row of the CSV data.

## Example usage

```
var csv = "John, Doe, 33\nJane, Doe, 32\nJack, Doe, 11\nJosh, Doe, 13"  // Your CSV data
var delimiter = ","
var headers = ["first_name", "last_name", "age"] // Your CSV data headers
var result = parser.parse(csv, headers, delimiter);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
