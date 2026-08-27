---
title: "Reply email is ignored and does not update target record"
aliases:
  - KB0755997
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755997
kb_number: KB0755997
last_modified: 2024-04-07
---

## Reply email is ignored and does not update target record

  

### Issue

# Symptoms

When you reply to an email notification, the reply email is ignored with the below error message. 

<table><tbody><tr><td><pre style="margin: 0; line-height: 125%;">1</pre></td><td><pre style="margin: 0; line-height: 125%;">watermark's target table '&lt;table_name&gt;' does not match any Inbound Action table, setting to 'Ignored' state
</pre></td></tr></tbody></table>

# Release

All releases

# Cause

When an email notification is sent, it is for a record on a particular table and once you reply to this email, if there are no inbound actions configured for this table, this error will be thrown. 

# Resolution

In order to process all reply emails to this table, you need to create a new inbound action for this table and type 'Reply'. 

# Additional Information

[Create an inbound email action](https://docs.servicenow.com/csh?topicname=t_CreatingAnInboundEmailAction.html&version=latest)
