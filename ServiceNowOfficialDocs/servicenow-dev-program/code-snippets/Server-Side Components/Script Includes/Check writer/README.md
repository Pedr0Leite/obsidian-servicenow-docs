---
title: "Check writer"
aliases:
  - Check writer
tags:
  - servicenow-dev-program
  - code-snippet
  - check-writer
  - script-includes
---

# RegexUtils

I am sure ServiceNow users need a check right? This Script Include gets a number and converts to an English style check.

e.g. 123456789 is printed as:

one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine

## Usage

```javascript
var checkWriter = new global.CheckWriter();

gs.log(checkWriter.write(123456789)); // prints: one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
