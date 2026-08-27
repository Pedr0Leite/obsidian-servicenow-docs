---
title: "update variable role"
aliases:
  - update variable role
tags:
  - servicenow-dev-program
  - code-snippet
  - update-variable-role
  - fix-scripts
---

# Fix script to update varialbes write roles

- we use variables in catalog items for that we have to provide roles who can access the variable
- we tend to forget adding roles after creating many varialbes
- To update multiple variables write role this fix script will help to add them.


```
function updateItemOptionRoles() {
     var query = 'sys_scope=5f414691db10a4101b2733f3b9961961';   // sys_id of application
     var varGr = new GlideRecord('item_option_new');  // GlideRecord of variables table
     varGr.addEncodedQuery(query);
     varGr.query();
     gs.info('Starting update for ' + varGr.getRowCount() + ' records.'); 
     varGr.setValue('write_roles', 'role1, role2, role3'); // add the write roles 
     varGr.updateMultiple();
    gs.info('Updated ' + varGr.getRowCount() + ' records.');
 }
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
