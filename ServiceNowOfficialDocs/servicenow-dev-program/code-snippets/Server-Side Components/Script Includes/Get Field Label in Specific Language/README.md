---
title: "Get Field Label in Specific Language"
aliases:
  - Get Field Label in Specific Language
tags:
  - servicenow-dev-program
  - code-snippet
  - get-field-label-in-specific-language
  - script-includes
---

# Get Field Label in Specific Language

This Script Include enables retrieving the label of a certain table field in any given language. 
Often in multi-language instances, the label of a field must be accessed via a script (e.g. to add it to the HTML of an email or add it to another fields like the description or work notes). Instead of retrieving the value each time individually this script include can be re-used (e.g. by multiple Business Rules or Mail Scripts). 

### Instruction

Call the Script Include via the following example code from any server-side script (e.g. Business Rule, Mail Script or Flow Action). If you want, you can also make the Script Include client callable and make it available to Client Scripts. Make sure to provide the correct table name, field name and language in your function call. Be aware, that in some cases the field may be located on a parent table. In this case, you would have to provide the parent table name to the script. 

```javascript
var util =new LanguageUtils();
gs.log(util.getLabel("incident", "category", "de"));
```


### Benefits
- If no label in the provided language can be found, the default English label is returned
- Re-use this Script Include and call it from different types of scripts (e.g. Business Rule, Mail Script or Flow Action)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
