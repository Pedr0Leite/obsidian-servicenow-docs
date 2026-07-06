---
title: "Emails to multiple addresses auto-filled by a client template may end up as send ignored"
aliases:
  - KB0743821
tags:
  - servicenow
  - support-kb
  - email-client-templates
  - notifications
  - scripting
  - send-ignored
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743821
kb_number: KB0743821
last_modified: 2026-07-02
---

## Emails to multiple addresses auto-filled by a client template may end up as send ignored

  

### Issue

Emails end up as send-ignored if generated through the email client where a client template auto-fills more than one email address in any one of the To, CC, or Bcc fields.

Opening the email record shows the error:

SMTPSender: no recipients, email send ignored

### Release

All

### Cause

The To, CC, and Bcc fields of an email client template are of type String. If you are using javascript to auto-fill more than one email address in one of these fields, you will need to use an array to add the multiple addresses. Otherwise, the multiple email addresses will be concatenated as a single string and will not be a valid email address.

### Resolution

In the To, CC, or Bcc field of an email client template, add the multiple email addresses to an array and join the array. For example:

javascript: var emailAddresses = \[\];  
emailAddresses.push("test@example.com");  
emailAddresses.push(current.caller\_id.email);  
emailAddresses.push(current.caller\_id.manager.email);  
emailAddresses.join();

**  
Alternate solution**

If you plan to reuse this code in multiple email client templates, you can:

1\. Create a new script include.  
2\. Check the Client Callable checkbox.  
3\. Add a function on line 3 of the Script field to build and join the array of email address. If dot-walking, you'll need to pass in the current object to the function. Example:

addEmailAddresses: function(current) {  
var emailAddresses = \[\];  
emailAddresses.push("test@example.com");  
emailAddresses.push(current.caller\_id.email);  
emailAddresses.push(current.caller\_id.manager.email);  
return emailAddresses.join();  
},

4\. Click Submit.

5\. In the To, CC, or Bcc field of the email client template, call the script include. If dot-walking, you'll need to pass the current object to the script include. Example:

javascript: new <\_scriptIncludeName>().addEmailAddresses(current);

### Related Links

[Reviewing emails getting ignored by inbound actions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535493 "Reviewing emails getting ignored by inbound actions")

[Emails are getting set to "type" "send-ignored" for seemingly no reason](https://support.servicenow.com/kb_view.do?sysparm_article=KB0790932 "Emails are getting set to \"type\" \"send-ignored\" for seemingly no reason")

[Invalid character in email address domain causes error "SMTP Sender: no recipients, email send ignored. The value in the recipient is not a valid email"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0853472 "Invalid character in email address domain causes error \"SMTP Sender: no recipients, email send ignored. The value in the recipient is not a valid email\"")

## Related

- [[KB0743785 - Orphaned duplicate request is created via inbound email action using Cart() API]] - other email/scripting edge case
- [[KB0745172 - Identify the source of emails sent from ServiceNow]] - tracing email records

