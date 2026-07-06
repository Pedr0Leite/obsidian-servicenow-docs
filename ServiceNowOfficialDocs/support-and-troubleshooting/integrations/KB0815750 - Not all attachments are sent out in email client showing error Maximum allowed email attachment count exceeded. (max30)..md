---
title: "Not all attachments are sent out in email client showing error \"Maximum allowed email attachment count exceeded. (max:30). Email sent without one or more of its attachments\"
aliases:
  - KB0815750
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815750
kb_number: KB0815750
last_modified: 2025-09-09
---

## Not all attachments are sent out in email client showing error "Maximum allowed email attachment count exceeded. (max:30). Email sent without one or more of its attachments"

  

### Issue

When sending out an Email in a client template, typically from an active record opened in a browser, not all or none of the attachments get sent out.

An error can be seen in the Email logs "Maximum allowed email attachment count exceeded. (max:30). Email sent without one or more of its attachments".

This issue happens in a context where an Email client template are used that dynamically fill in the body of the new Email.

This is unexpected because the system limit set with property "**glide.email.outbound.max\_attachment\_count**" is higher than the number of files attached to the Email sent.

### Release

All

### Cause

The limit "glide.email.outbound.max\_attachment\_count" is exceeded because it is not only the number of files manually attached in the Email that counts but also all the embedded tags that point to a sys\_attachment record within the Body of the Email client template.

When you take a look at the HTML source of the Email body template, you will see this kind of code: **src="/sys\_attachment.do?sys\_id=545097bcdbexxxxxxx971d9619b6"** and this counts toward an attachment.

### Resolution

When pre-filling the templates, make sure not to include logos or other images, otherwise increase the number of total attachments with property "glide.email.outbound.max\_attachment\_count"

### Related Links

[Email body/attachment size limit system properties](https://support.servicenow.com/kb_view.do?sysparm_article=KB0785037 "Email body/attachment size limit system properties")

[Email server size limit prevents emails from being sent or received](https://support.servicenow.com/kb_view.do?sysparm_article=KB0521772 "Email server size limit prevents emails from being sent or received")

[Attachment Limit properties](https://www.servicenow.com/docs/csh?topicname=r_AttachmentLimitProperties.html&version=latest)
