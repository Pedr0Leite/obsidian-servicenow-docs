---
title: "Receipients are blank when initiated email using email client  for bulk users group"
aliases:
  - KB0815549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815549
kb_number: KB0815549
last_modified: 2024-04-08
---

## Receipients are blank when initiated email using email client for bulk users group

  

### Issue

we can send bulk emails if the total number of recipients (To, CC and BCC) exceed the default limit (100- glide.email.smtp.max\_recipients), the recipients are chunked into multiple emails.

If we add bulk emails in BCC and we have only one email added to  TO , rest the chunked emails will not add To email.

### Release

All

### Related Links

1\. This use case has a single email address in "To", but it can contain multiple email addresses and possible need of chunking (i.e, if the list is greater than 100).   
2\. In case if an email address is selected among "To" email addresses to copy to all the emails, the user with that email address will receive duplicate emails.

To avoid that, we keep one To email address in on email, remaining chunked emails will send without To email.

As per [https://tools.ietf.org/html/rfc2822](https://tools.ietf.org/html/rfc2822):  
"The destination fields (To, CC, BCC) specify the recipients of the message. Each  
destination field may have one or more addresses, and each of the  
addresses indicate the intended recipients of the message. The only  
difference between the three fields is how each is used."  
  
As per RFC, having only BCC without "To" and "CC" is a valid message.

  

\* Same way, we add above property splits the emails when the max number of emails reached in the “To” field. If we add CC to that email, CC will send with only one email not will all the split emails.
