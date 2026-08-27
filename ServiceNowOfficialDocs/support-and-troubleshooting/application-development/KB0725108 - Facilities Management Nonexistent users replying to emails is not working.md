---
title: "Facilities Management: Nonexistent users replying to emails is not working"
aliases:
  - KB0725108
tags:
  - servicenow
  - support-kb
  - inbound-email-actions
  - facilities-management
  - business-rules
  - access-control-acl
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725108
kb_number: KB0725108
last_modified: 2024-04-22
---

## Facilities Management: Nonexistent users replying to emails is not working

  

### Issue

The following KB provides information around behavior where a non-user responds to an email where there is an inbound email action that performs a specific action.

The expected behavior is that the email response will update the corresponding record. However, by default the transaction will not get processed.

-   A user, who does not exist in the platform, responds to an email and expects a Facilities record to be updated. However, no update occurs.
-   An admin user checks the email log and sees the following message: "Unable to locate facilities\_request 1ca10935db596f000a845099dc961927 for inbound email processing”.

### Cause

By default, any transaction made against a ServiceNow instance requires there to be an active user for that transaction.

Since the user does not exist in the instance, the transaction is not processed.

### Resolution

To remediate the issue, perform the 3 following steps:

1\. Modify the Business Rule to allow non-users to have write permission to Facility records (can also disable the Business Rule too). 

[https://INSTANCE.service-now.com/sys\_script.do?sys\_id=43524ed1df203100dca6a5f59bf26317](https://INSTANCE.service-now.com/sys_script.do?sys_id=43524ed1df203100dca6a5f59bf26317)

2\. Create a write ACL on **facilities\_request** table for the field that the email is supposed to update.

3\. Create a write ACL on **facilities\_request\_task**  for the field that the email is supposed to update.

## Related

- [[KB0744324 - Unable to process Inbound email action on emails received from inactive and locked out accounts]] - another case where the inbound action requires an active platform user
- [[KB0790953 - User not recognized for incoming emails]] - related inbound email user-matching issue
- [[KB0727612 - Copy inbound email into the Work Notes or Additional Comments field of a target record]] - inbound email action scripting pattern
- [[processing-inbound-emails]] - official docs on how inbound email processing determines the acting user

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0727619 - The Field actions menu for an inbound email action is not showing all fields|The Field actions menu for an inbound email action is not showing all fields]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
