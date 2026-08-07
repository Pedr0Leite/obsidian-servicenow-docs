---
title: "HTMLUtils"
aliases:
  - HTMLUtils
tags:
  - servicenow-dev-program
  - code-snippet
  - htmlutils
  - script-includes
---

# Creates an HTML Table from an object

@param  {String} [title] - Title above table
@param  {Object} [table] - Object with headers attribute and row multi dimension array
@returns {String} HTML Table

### Example
```js
var table = {
header:['col1','col2'],
rows:[['row1col1','row1col2'],
        ['row2col1','row2col2']]
}

var hU = new HTMLUtils();
hU.createHTMLTable("Test",table);
```
### Output
```html
<p style='margin: 10px 0px 10px;'><b>Test</b></p><table class='template_TBL table'><tbody><tr><td>col1</td><td>col2</td></tr><tr><td>row1col1</td><td>row1col2</td></tr><tr><td>row2col1</td><td>row2col2</td></tr></tbody></table>
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
