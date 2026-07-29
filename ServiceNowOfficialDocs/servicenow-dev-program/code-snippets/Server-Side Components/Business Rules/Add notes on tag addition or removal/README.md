---
title: "Add notes on tag addition or removal"
aliases:
  - Add notes on tag addition or removal
tags:
  - servicenow-dev-program
  - code-snippet
  - add-notes-on-tag-addition-or-removal
  - business-rules
---

This business rule will operate on the label_entry table to log notes whenever tags are added or removed from specific tables. To implement this, create three system properties:
1. custom.tag_entries.log_removal (true/false): Set this to true to enable logging of tag removals.
2. custom.tag_entries.tables: A list of tables, separated by commas, where notes should be managed.
3. custom.tag_entries.log_addition (true/false): Set this to true to enable logging of tag additions.
One challenge with tags is identifying who added or removed them from records. With these business rules in place, this information will be easily accessible.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add woknotes for 75 percent SLA/README|Add woknotes for 75 percent SLA]]
