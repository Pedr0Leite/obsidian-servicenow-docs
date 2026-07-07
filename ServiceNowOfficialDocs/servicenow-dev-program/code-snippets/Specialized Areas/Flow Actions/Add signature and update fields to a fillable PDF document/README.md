---
title: "Add signature and update fields to a fillable PDF document"
aliases:
  - Add signature and update fields to a fillable PDF document
tags:
  - servicenow-dev-program
  - code-snippet
  - add-signature-and-update-fields-to-a-fillable-pdf-document
  - flow-actions
---

Use case: Add signatures and update information on a fillable PDF

This has a logic check to see if the PDF has editable fields or not. If there are no fillable fields, it throws an error.

PdfMergeSignRequestor and PDFGenerationAPI have been used here.

It takes the below inputs:

Signature image: the Sys_id of the signature image in the Attachments table.

PDF record: Sys_id of the PDF record in the Attachments table.

Target table: Target table name (ex: sc_req_item, sc_task, etc.)

Target record: sys_id of the target record.

Output screenshots:

![image](https://github.com/user-attachments/assets/26fe1a1c-9339-4f65-bb0f-0f1d258c460e)

![image](https://github.com/user-attachments/assets/9a651aa2-b914-440b-8fc7-f7f593f9a2e8)


![image](https://github.com/user-attachments/assets/5a283faa-c4ec-49d4-b4b8-cbbd6f2ce7c3)

![image](https://github.com/user-attachments/assets/0c8ea249-720a-47a3-9a96-9efc5de8abb3)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Adhoc Assessment Generator Flow Action/README|Adhoc Assessment Generator Flow Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Assign Role/README|Assign Role]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Calculate Ticket Age/README|Calculate Ticket Age]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Check MID Server Availability/README|Check MID Server Availability]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Create Student Weekday Pickup Schedule/README|Create Student Weekday Pickup Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Flow Actions/Data Stream/README|Data Stream]]
