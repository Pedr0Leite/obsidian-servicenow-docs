---
title: "Track Tag Removal Using Delete Business Rule"
aliases:
  - Track Tag Removal Using Delete Business Rule
tags:
  - servicenow-dev-program
  - code-snippet
  - track-tag-removal-using-delete-business-rule
  - business-rules
---

**Configure the following business rule on the label_entry table:**

1.Ensure the "Delete" operation is selected and the rule runs onBefore.

2.Retrieve the table name where the tag is removed.

3.Update the worknotes to track who removed the tag and when it was removed.
<img width="952" height="460" alt="image" src="https://github.com/user-attachments/assets/020525dc-c98d-4ae8-94f9-d77cca6680e7" />
<img width="1665" height="739" alt="image" src="https://github.com/user-attachments/assets/46c930eb-c031-4e1e-b1e6-31a3c64debb0" />


**Output:**

<img width="1139" height="818" alt="image" src="https://github.com/user-attachments/assets/ed07f380-f279-4eca-82a5-208ae54054e7" />

<img width="780" height="401" alt="image" src="https://github.com/user-attachments/assets/283b40e1-1d7c-42aa-85f8-b8e9c6ccc3d0" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
