---
title: "Email client only supports one email client template per table"
aliases:
  - KB0694768
tags:
  - servicenow
  - support-kb
  - email-client
  - email-notifications
  - notifications
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694768
kb_number: KB0694768
last_modified: 2026-04-16
---

## Email client only supports one email client template per table

  

### Issue

The email client functionality only supports one email client template per table even if there is an option to create more than one email client templates per table.

### Resolution

Regardless of how many email client templates have been set up for a table only one email client template is supported and will be used. The first email client template created would be the one that will always be used. If there are other processes that manually call different email client templates only the first email client template that was first created is applied.

Example

1\. Create two different email client templates for incident table:

-   Name: template1
-   Name: template2

2\. Through a script in a UI Action, manually call template2:

var url = 'email\_client.do?sysparm\_table=incidents&sysparm\_sys\_id='+<sys\_id>+'&sysparm\_target=incident&sys\_uniqueValue='+i<sys\_id>+'&email\_client\_template=template2&sys\_row=0&sysparm\_encoded\_record=&sysparm\_domain\_restore=false&sysparm\_stack=no';  
  
popupOpenEmailClient(url);

Actual behavior: Even though template2 is specified to be opened (from the URL parameter "email\_client\_template=template2") the email client would still open template1 because this was the first email client template that was created.

### Related Links

[The email client](https://docs.servicenow.com/csh?topicname=c_EnableTheEmailClient.html&version=latest "The email client")

## Related

- [[KB0716520 - Notification emails are not generated when the Message HTML field contains a hyperlink]]
- [[KB0695226 - Having a misplaced href tag prevents notifications from firing]]
- [[KB0723056 - Approving requests through email notifications, Inbound actions, sysapproval_approvers and user table]]
