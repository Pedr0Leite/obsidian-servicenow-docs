---
title: "Nested WHERE orWHERE GlideQueries"
aliases:
  - Nested WHERE orWHERE GlideQueries
tags:
  - servicenow-dev-program
  - code-snippet
  - nested-where-orwhere-glidequeries
  - glidequery
---

# WHERE Clauses with Nested GlideQueries

Creating a query with multiple groupings of AND and OR statements would be impossible to decipher,
so `GlideQuery` forbids them.

An example of this would be the following, where the query system would be unable to tell if this
should be 

`WHERE (caller_id is david.miller AND state is 1) OR (caller_id is beth.anglin)` 

versus

`WHERE (caller_id is david.miller) AND (state is 1 OR caller_id is beth.anglin)` 

```javascript
secondQuery = new GlideQuery('task')
	.where('caller_id.user_name', 'david.miller')
	.where('state', 1)
	.orWhere('caller_id.user_name', 'beth.anglin')
	.select(['sys_id'])
	.toArray(10);
```

Instead, using the equivalent nested GlideQuery in the JavaScript file shows the proper way of nesting
OR WHERE queries.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/Basic Wrappers/README|Basic Wrappers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/Conditional Field Selection/README|Conditional Field Selection]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/Field Default/README|Field Default]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/FlatMap to Nest New Queries/README|FlatMap to Nest New Queries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/Get Delegates/README|Get Delegates]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideQuery/Get User's Roles from User Name/README|Get User's Roles from User Name]]
