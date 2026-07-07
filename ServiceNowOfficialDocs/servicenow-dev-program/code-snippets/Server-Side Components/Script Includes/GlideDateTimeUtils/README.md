---
title: "GlideDateTimeUtils"
aliases:
  - GlideDateTimeUtils
tags:
  - servicenow-dev-program
  - code-snippet
  - glidedatetimeutils
  - script-includes
---

# ClientDateTimeUtils
This Script Include contains useful functions related to date/time calculations that can be called using GlideAjax.
As there is very limited javascript functions related to Date & Time, this will be very useful for client side calculations of date & time.

## Example Script
```javascript
var ga = new GlideAjax('ClientDateTimeUtils');
ga.addParam('sysparm_name', 'getNowDateTimeDiff');
ga.addParam('sysparm_fdt', g_form.getValue('last_date'));
ga.addParam('sysparm_difftype', 'day');
ga.getXMLAnswer(function(response){
	if(parseInt(response)<2){
		alert("Last date cannot be less than 2 days from today");
	}
});
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
