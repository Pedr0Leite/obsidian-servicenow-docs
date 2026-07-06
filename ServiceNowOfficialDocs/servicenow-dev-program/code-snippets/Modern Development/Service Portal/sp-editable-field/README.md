---
title: "sp-editable-field"
aliases:
  - sp-editable-field
tags:
  - servicenow-dev-program
  - code-snippet
  - sp-editable-field
  - service-portal
---

# sp-editable-field
`sp-editable-field` directive allows to render an interactive field label which allows user to directly modify the value by showing a miniform with just one field.

The following table lists all of the scope bindings that can be passed to the directive

| Property              | Description                                                        |
|-----------------------|--------------------------------------------------------------------|
| fieldModel            | fieldModel object that can be obtained via $sp.getForm API         |
| table                 | table name                                                         |
| tableId               | record sys_id                                                      |
| block                 | display as a block level element                                   |
| editableByUser        | if true allows user to edit the field value                        |
| onChange              | function to execute when onChange event occurs within the form     |
| onSubmit              | function to execute when onSubmit event is triggered from the form |
| asyncSubmitValidation |                                                                    |


## Usage example


### Editable user's email address
![editable user's email](2021-10-17-00-17-56.png)

**HTML temlate**
```html
<sp-editable-field table="sys_user" table-id="data.userSysId" editable-by-user="true" field-model="data.sysUserModel.email"></sp-editable-field>
```

**Server Script**
```javascript
(function() {  
	var sysUserForm = $sp.getForm('sys_user', gs.getUserID());
	data.userSysId = gs.getUserID();
	data.sysUserModel = sysUserForm._fields;	
})();
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/Active Tickets Dashboard/README|Active Tickets Dashboard]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/Search Sources/README|Search Sources]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/dark-mode-switcher/README|dark-mode-switcher]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/instance-badge/README|instance-badge]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/sn-avatar/README|sn-avatar]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/sn-choice-list/README|sn-choice-list]]
