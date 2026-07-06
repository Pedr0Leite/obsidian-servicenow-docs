---
title: "Notification emails are not generated when the Message HTML field contains a hyperlink"
aliases:
  - KB0716520
tags:
  - servicenow
  - support-kb
  - notifications
  - mail-script
  - email-notifications
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716520
kb_number: KB0716520
last_modified: 2024-04-07
---

## Notification emails are not generated when the Message HTML field contains a hyperlink

  

### Issue

# Symptoms

* * *

1.  Emails are not generated from specific notification(s). Email sending works as expected for other notifications.
2.  Preview Notification generates an empty preview for the email notification regardless of event creator and preview record.

![blank preview](sys_attachment.do?sys_id=81ea6ce6db42b450e515c22305961954 "blank preview")

# Release

* * *

All releases

# Cause

* * *

If the Message HTML and/or the email template in the email notification contains a hyperlink, then email rendering fails and no email (or preview) is created.

Example: ${[mail\_script:testScript}](www.testwwwebsite.com "mail_script:testScript}")

![hyperlink inside Message HTML](sys_attachment.do?sys_id=45ea6ce6db42b450e515c22305961959 "hyperlink inside Message HTML")

  

# Resolution

* * *

Remove the hyperlink on the mail script snippet.

#

## Related

- [[KB0695226 - Having a misplaced href tag prevents notifications from firing]]
- [[KB0694768 - Email client only supports one email client template per table]]
- [[KB0723602 - Unable to get the non-english value of translated text field or translated html field when using the email template]]
