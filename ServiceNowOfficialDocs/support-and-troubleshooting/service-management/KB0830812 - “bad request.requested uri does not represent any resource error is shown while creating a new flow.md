---
title: "“bad request.requested uri does not represent any resource\" error is shown while creating a new flow"
aliases:
  - KB0830812
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830812
kb_number: KB0830812
last_modified: 2024-04-08
---

## Issue

“bad request requested uri does not represent any resource" error is shown while creating a new flow

## Resolution

Please install the plugin Plugin: UI16 (com.glide.ui.ui16) to fix the issue, It is recommended to install the plugin first on lower environments.

After installing new UI will be provided . However you can still set a system user preference to force everyone onto U15:  
Table = sys\_user\_preference  
Name = use.concourse (Search for this name, if you do not find it then create one)  
System = true  
User = <blank>  
Type = string  
Value = false  
  
Steps-2: To restrict users from switching to this new UI 16 using "Switch UI" button from general settings, you can control it based on a system property i.e; user of which role should have access to this UI change button.  
"Configure roles allowed to switch between UI16 and UI15":  
[https://docs.servicenow.com/csh?topicname=t\_SwitchBtwnUi16AndUi15.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SwitchBtwnUi16AndUi15.html&version=latest)
