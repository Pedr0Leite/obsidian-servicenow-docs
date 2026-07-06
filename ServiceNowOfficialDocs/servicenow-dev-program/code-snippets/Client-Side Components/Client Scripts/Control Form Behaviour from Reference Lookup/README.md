---
title: "Control Form Behaviour from Reference Lookup"
aliases:
  - Control Form Behaviour from Reference Lookup
tags:
  - servicenow-dev-program
  - code-snippet
  - control-form-behaviour-from-reference-lookup
  - client-scripts
---

# Use Case

Clicking the lookup icon on a reference field opens the list view for the referenced table. On clicking the 'New' button to create new records on the reference table, 'Default' form view for that table is displayed. There might be a requirement to control the form's behaviour when the new record form is opened from a designated field on a specific table.


# Usage

Write a client script/scripted UI policy on the reference table and add the code in ```script.js``` file.


# Explanation

The URL parameters contains the necessary information about the originating table and field from where the lookup icon is clicked. These parameters can be extracted using the client-side class ```GlideURL```. Key parameters of interest here:
  - ```sysparm_nameofstack: "reflist"``` ==> Will always be reflist when form has originated from a reference lookup icon click
  - ```sysparm_target: "change_request.cmdb_ci"``` ==> Will be in the format <table_name>.<field_name>

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
