---
title: "HTML Tags are included in email body"
aliases:
  - KB0748592
  - HTML Tags are included in email body
tags:
  - servicenow
  - support-kb
  - email
  - notifications
  - html-email
  - tinymce
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748592
kb_number: KB0748592
last_modified: 2025-07-08
---

## HTML Tags are included in email body

  

### Issue

When an email is sent to end user HTM tags are included in body of the email which will be something looks like below

![](sys_attachment.do?sys_id=fc8c24aedb42b450e515c22305961965)

  

### Release

All

### Cause

Most likely, they pasted HTML in to the TINYMCE editor, which was then encoded as wrong formate in HTML source code ("&lt;b&gt;Article:&lt;/b&gt;")

### Resolution

1) Go to notification and check for what it will contain Tab.

2) In what it will contain go to Message HTML and click on source code icon (<>) which will be in Message HTML editor.

3) Then paste the below source code in HTML Viewer which should look like ( This is sample source code, you can edit as per your requirement)

<p>Incident ${number} has been opened on your behalf</p>  
<p><strong>Inciednt:</strong> ${URI\_REF}</p>  
<p><strong>Short description:</strong> ${short\_description}</p>

4) After adding this formate in HTML source code message body looks like below

![](sys_attachment.do?sys_id=f48c24aedb42b450e515c22305961977)

## Related

- [[KB0745430 - HTML Entity names not displaying in Notification previews and Email previews]]
- [[KB0746264 - Emails are not formatted correctly in Outlook or older email applications]]
- [[KB0747524 - Email Preview looks different than in Outlook, Gmail or other Mail Application]]
- [[KB0727884 - How to fix HTML tags appearing in sent email notifications]]
