---
title: "Gmail replies not working in align with Default -Inbound Email Property - Discarding Everything after (glide.pop3.reply_separators)"
aliases:
  - KB0751478
  - Gmail replies not truncated by glide.pop3.reply_separators
tags:
  - servicenow
  - support-kb
  - inbound-email
  - gmail
  - reply-separators
  - email-properties
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751478
kb_number: KB0751478
last_modified: 2026-05-05
---

## Gmail replies not working in align with Default -Inbound Email Property - Discarding Everything after (glide.pop3.reply\_separators)

  

### Issue

Gmail replies not working in align with Default -Inbound Email Property - Discarding Everything after (glide.pop3.reply\_separators)

### Symptoms

1.  In Inbound Email Properties
2.  Look for "Discard everything below this text if found in a reply body :"- (_**glide.pop3.reply\_separators**_) by default set to \\n\\n-----Original Message-----,\\n\\n \_\_\_\_\_ \\n\\nFrom:

It will work fine with Outlook and Hotmail and most email applications.

But Recently Gmail replies don't carry **From:** 

So When SN instance receives replies from Gmail, it doesn't discard the previous replies, hence the whole email chain is carried on to the Task when it is added in Reply Inbound action.

### Release

All releases including Kingston, London and Madrid

### Cause

Gmail Replies no longer carry the traditional format (like outlook) when you reply, it has been modified to a single line (see difference below)

# ![](/sys_attachment.do?sys_id=8ed1da2793a8c758e7eef35d6cba1061)

# ![](/sys_attachment.do?sys_id=0ed1da2793a8c758e7eef35d6cba1004)

### Resolution

Instead of "FROM: ", you can opt for "wrote: " (for only gmail inbound)   
  
which might solve the issue for maximum emails from gmail., unless customer writes "wrote:" in the actual reply (latest). 

So you can amend the property -

glide.pop3.reply\_separators **\-\\n\\n-----Original Message-----,\\n\\n \_\_\_\_\_ \\n\\nFrom:,wrote:**

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Notes are added to emphasize points, remind users of something, or indicate minor problems that could arise as a result of executing the steps in the article.

## Related

- [[KB0755997 - Reply email is ignored and does not update target record]]
- [[KB0751477 - Unable to locate incident ___SYS_ID_NUMBER___ for inbound email processing due to different domains]]
- [[KB0520595 - Inbound Email overview and troubleshooting]]</td></tr></tbody></table>

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Warning" src="/Warning_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Warning</strong>: A warning should be used when corruption, data loss, or downtime is possible if instructions are not obeyed.</td></tr></tbody></table>

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0520595 - Inbound Email overview and troubleshooting|Inbound Email overview and troubleshooting]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529478 - Emails to incidents come in as winmail.dat attachments|Emails to incidents come in as winmail.dat attachments]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749517 - Inbound email embedded images are being added as attachments to the target record|Inbound email embedded images are being added as attachments to the target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749826 - Unable To fetch Email Address of actual sender in the forwarded emails|Unable To fetch Email Address of actual sender in the forwarded emails]]
