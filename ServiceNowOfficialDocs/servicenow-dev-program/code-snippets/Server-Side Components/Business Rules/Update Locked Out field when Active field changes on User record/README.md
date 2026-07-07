---
title: "Update Locked Out field when Active field changes on User record"
aliases:
  - Update Locked Out field when Active field changes on User record
tags:
  - servicenow-dev-program
  - code-snippet
  - update-locked-out-field-when-active-field-changes-on-user-record
  - business-rules
---

# Use Case <br/>
As per OOB, the "Locked out" field will be set to true if Active field set to false. But, the vice-versa case is not implemented. For example, If Employee is on long leave like maternity leave etc., then the user account will be set inactive temporarily and reactivated upon his/arrival to office. This causes, user account to be Active and Locked out as true which makes the login to fail
# Business Rule <br/>
Name: Update Locked Out field<br/>
Table: User [sys_user] <br/>
Advanced: true <br /><br/>

**When to run section:**<br/>
When: Before <br/>
Insert: true <br/>
Update: true <br/>
Filer Conditions: Active -- Changes to -- true [AND] Locked out -- is -- true<br/><br/>
![image](https://github.com/user-attachments/assets/835f6d9c-8d60-4b1a-9159-bda5576fe088)

**Advanced section:**<br/>
Script:<br/>
(function executeRule(current, previous ) {

	current.locked_out = !current.active; 

})(current, previous);

![image](https://github.com/user-attachments/assets/0fd67e77-38f3-449d-9647-047406f8d23e)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
