---
title: "Restrict Fields on Template"
aliases:
  - Restrict Fields on Template
tags:
  - servicenow-dev-program
  - code-snippet
  - restrict-fields-on-template
  - client-scripts
---

**Details**

This is a on change client script on sys_template table. This script will restrict users to select defined fields while template creation.
Type: OnChange
Field: Template
Table: sys_template

**Use Case**

There is an OOB functionality to restrict fields using "**save as template**" ACL, but it has below limitations:
1. If the requirement is to restrcit more number of fields (example: 20), 20 ACLs will have to be created.
2. The ACls will have instance wide effect, this script will just restrict on client side.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
