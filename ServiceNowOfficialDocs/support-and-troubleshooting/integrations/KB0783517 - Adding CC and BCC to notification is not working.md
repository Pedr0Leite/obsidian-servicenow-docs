---
title: "Adding CC and BCC to notification is not working"
aliases:
  - KB0783517
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783517
kb_number: KB0783517
last_modified: 2025-10-01
---

## Adding CC and BCC to notification is not working

  

### Issue

Adding CC and BCC in the notification either from the event parameter or by explicitly mentioned in the script is not working. 

### Cause

This issue is because of the fact that the property "glide.email.test.user" has the value with an email address.

### Resolution

 If "glide.email.test.user" property is set then ServiceNow only set the "To" Recipient in the Email Headers even if the configurations are for CC and BCC field over the script it will be disregarded. 

If this property is set to empty value then we set To / CC / BCC as well. Please empty this property to achieve populating CC and BCC.
