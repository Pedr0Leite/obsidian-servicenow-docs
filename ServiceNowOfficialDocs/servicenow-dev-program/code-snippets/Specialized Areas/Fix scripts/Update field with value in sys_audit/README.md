---
title: "Update field with value in sys_audit"
aliases:
  - Update field with value in sys_audit
tags:
  - servicenow-dev-program
  - code-snippet
  - update-field-with-value-in-sys-audit
  - fix-scripts
---

Hopefully this is something you never need to use.   It will udpate with either the newest or oldest entry from sys_audit.

## Example

```Javscript
var updateArgs = {
    encodedQuery: 'u_some_cool_field=blahblahblahL',
    table: 'my_cool_table',
    updateField: 'field to update in target table',
    auditField: 'field name in sys_audit',
    sort: 'DESC'
}


try {

    gs.print(updateRecords(updateArgs).join('\n'));
} catch (ex) {
    gs.error(ex.message || ex);
}

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
