---
title: "MarkInactiveUsersonList"
aliases:
  - MarkInactiveUsersonList
tags:
  - servicenow-dev-program
  - code-snippet
  - markinactiveusersonlist
  - server-side
---

There is a list type field named 'Reviewers' on Policy records.
On the list view of Policies, we want to highlight with field styles, where any of the user listed under Reviewers is inactive.
In the screenshot attached below, Daniel Zill is inactive user, and if he is present in Reviewers, the respective column value is applied with defined field styles.
<img width="809" height="370" alt="image" src="https://github.com/user-attachments/assets/b483207e-f3ba-4db7-a717-d392694eaf50" />
<img width="433" height="107" alt="image" src="https://github.com/user-attachments/assets/5129038f-d210-40f4-bcd8-1727d791edca" />

The condition to check if any inactive user is present in Reviewers must be written on 'Value' (actual Server script) and the styles to applied must be mentioned on 'Style'.
Refer below screenshot:
<img width="911" height="239" alt="image" src="https://github.com/user-attachments/assets/477e52cb-bdad-439d-a1cc-5b6be0415c20" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
