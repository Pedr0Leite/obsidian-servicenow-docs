---
title: "Enforce File Upload Restrictions for HR Document Submission"
aliases:
  - Enforce File Upload Restrictions for HR Document Submission
tags:
  - servicenow-dev-program
  - code-snippet
  - enforce-file-upload-restrictions-for-hr-document-submission
  - business-rules
---

This code ensures that when a user uploads a document related to a specific HR task, the uploaded file meets
certain criteria: it must be in JPG or JPEG format and must not exceed 2 MB in size. If either condition is violated,
the upload is halted, and an appropriate error message is displayed to the user, maintaining the integrity of the data 
being processed.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
