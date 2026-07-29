---
title: "Cascade Problem Worknote to Origin Task"
aliases:
  - Cascade Problem Worknote to Origin Task
tags:
  - servicenow-dev-program
  - code-snippet
  - cascade-problem-worknote-to-origin-task
  - business-rules
---

Cascade Problem Worknotes to Origin Task

Script Type : Business Rule Trigger: after update Table: problem Condition: Work Notes Changes

Goal : To Notify to that particular record(ticket) when Problem record has updated the worknotes.

Walk through of code :
So when there is update/change in the worknotes of a problem record this Business rule will cascade the worknotes to that attached Origin Task record so that it will be update in that particular record as well. In this some validation have been used to avoid unnecessary data cascade, this Business will work only for the open problem, mean this it will exclude the Closed & Resolved State Problem which have been already addressed. So once the worknote is posted it will updated respectively to the origin task.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
