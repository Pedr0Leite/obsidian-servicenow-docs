---
title: "How to adjust the Date format within a client script to align with the User Date format"
aliases:
  - How to adjust the Date format within a client script to align with the User Date format
tags:
  - servicenow-dev-program
  - code-snippet
  - how-to-adjust-the-date-format-within-a-client-script-to-align-with-the-user-date-format
  - client-scripts
---

# When getting a date from another table, it's usually in the format (YYYY-MM-DD). To display it in the user's preferred format on the client side, use the method below.

If date is fetched from a query(like GlideAjax), date returned from query pass that date object into "new Date()"

# Example

```
var user_date = formatDate(new Date(<returnDateObj>), g_user_date_format)

g_form.setValue('<field_name>',user_date);

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
