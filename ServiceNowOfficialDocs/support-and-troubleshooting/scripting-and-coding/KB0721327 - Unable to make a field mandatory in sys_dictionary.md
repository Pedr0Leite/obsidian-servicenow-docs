---
title: "Unable to make a field mandatory in sys_dictionary"
aliases:
  - KB0721327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721327
kb_number: KB0721327
last_modified: 2024-01-28
---

## Issue

# Description

* * *

You have the option of making a field "mandatory" at the sys\_dictionary level, or from the client-side. When attempting to set Mandatory as True on the sys\_dictionary record for the field, you wil see the checkbox set to read-only.

![](/sys_attachment.do?sys_id=583aa026db42b450e515c2230596193a)

One possibility for this might be due to you currently being within a different application than the one for the field's table. ServiceNow provides a client-script which explicitly sets a few options on the sys\_dictionary form to read-only when your current app scope does not match the table's scope. The script is called "Disable Mandatory for out of scope table".

# Procedure

* * *

The best solution here is to simply switch your current app scope to the one for the table your working with using the Application picker.

# Additional Information

* * *

Documentation:

\- Application Picker | [https://docs.servicenow.com/csh?topicname=c\_ApplicationPicker.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ApplicationPicker.html&version=latest)
