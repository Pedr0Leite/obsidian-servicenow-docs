---
title: "VariableHelper"
aliases:
  - VariableHelper
tags:
  - servicenow-dev-program
  - code-snippet
  - variablehelper
  - script-includes
---

## Variable Helper

 Working with variables in ServiceNow is no fun sometimes, especially [Multi Row Variable Sets](https://docs.servicenow.com/bundle/paris-application-development/page/script/server-scripting/concept/c_ScriptableServiceCatalogVariables.html#d2332110e207).  For that reason I created a helper Script Include to make my life easier.  

 There are 4 parameters that can be passed as an object when instantiating the Script Include or after with setter functions.  All default to false;


 * <b>useDisplayValue</b>:  This will return the display value of all variables instead of value
 * <b>expandRef</b>      :  This will return any reference field as an object. 
 * <b>useLabel</b>       :  Variable/Field Labels will be used instead of name.
 * <b>debug</b>          :  Enable additional logging


### Example

```
var helperOptions = {
  "useLabel": true,
  "useDisplayValue": true ,
  "expandRef": false
};
var varHelper = new variableHelper(helperOptions); 
varHelper.setDebug(true); //example of using setter function

var myVariables = varHelper.getVariables(myGlideRecordObject); //Get an object containing all variables
var myMRVS = varHelper.getMRVS(myGlideRecordObject.variables[mrvsName]); //Get a specific MRVS as an array of objects
  
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
