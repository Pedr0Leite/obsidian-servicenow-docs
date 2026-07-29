---
title: "Get choices from Decision Table"
aliases:
  - Get choices from Decision Table
tags:
  - servicenow-dev-program
  - code-snippet
  - get-choices-from-decision-table
  - glideajax
---

# Prerequisites
## Decision table
> [!IMPORTANT]
> Create a Decision table with a result column of type '**Choice**', and at least one, **mandatory input** that is a reference to sc_cat_item.

You will have to define the decisions for each catalog item separately. One catalog item can have multiple results - this is how you will get multiple choices for your selectbox variable at the end.
If you have other inputs, i.e. for different values from different variables, you simple add those conditions for each decision line for the related catalog item.
> [!NOTE]
> If you created the choices inside the Decision Table, make sure the values are not too long. They end up getting truncated in the sys_decision_answer table, and sebsequently the values stored in sys_choice will not match. If necessary, change the default value to something short and unique (or use an existing choice list if you can).

## Variables in the Script Include
> [!IMPORTANT]
> Make sure the following variables have a valid value in your script include:
* `var decisionTableId = '';`  The Sys ID of the decision table. Store in a system property and set with gs.getProperty().
* `var dtInput1 = 'u_catalog_item';`  Make sure you set this to the technical name of the first input of your Decision Table. It will always start with u_. If unsure, check the **sys_decision_input** table.
* `var dtInput2 = 'u_catalog_variable';` Make sure you set this to the technical name of the second input of your Decision Table, if you have one. Multiply as needed (if you have more inuts), or remove / comment out if not.
* `var resultColumn = 'u_choice_result';` Set this to the technical name of the result column that contains your choices

## Variables in the client script
> [!IMPORTANT]
> Remember to define the target field (the one you want to add the choices to) in row 3: `var targetChoiceField = 'choice_field';`

If you want send values from other variables for your decision table to consider, add them as additional parameters, in line with what you have defined in the Script include, for instance: `dtChoiceAjax.addParam('sysparm_cat_variable', g_form.getValue('some_variable'));`

# Usage
Use the provided Script Include and Client Script, and update them as mentioned in the [Prerequisites](#prerequisites) section. The example client script is **onLoad**, but if you are looking to use variable values as additional inputs, you will want to have it run as an **onChange** script instead, or as a scripted UI Policy - it should work the same way.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/AjaxAsyncOnSubmit/README|AjaxAsyncOnSubmit]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Check Weekend - Client Side/README|Check Weekend - Client Side]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/EfficientGlideRecord (Client-side)/README|EfficientGlideRecord (Client-side)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Fetch Multiple Values in GlideAjax without JSON/README|Fetch Multiple Values in GlideAjax without JSON]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/Get Field Values/README|Get Field Values]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAjax/GlideAjax Example Template/README|GlideAjax Example Template]]
