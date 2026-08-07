---
title: "Password Reset SMS Verification: Random orphan characters in the SMS passcode"
aliases:
  - KB0727102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727102
kb_number: KB0727102
last_modified: 2024-05-22
---

## Password Reset SMS Verification: Random orphan characters in the SMS passcode

  

### Issue

# Symptoms

Two additional characters ahead of the 4 digit SMS verification code for password reset.

# Release

Kingston

# Cause

An empty line in the message and SMS alternate tab of the Password Reset - Send SMS Code.

# Resolution

From the Navigation filter:

1.  Go to Email -> Notifications -> Password Reset - Send SMS Code
2.  Under "What it will contain" tab remove the empty line  above ${event.parm2} in the "message" and "SMS alternate" tabs, which is causing the addition of those extra characters.

# Additional Information

https://**_\[INSTANCE\_NAME\]_**.service-now.com/nav\_to.do?uri=%2Fsysevent\_email\_action.do%3Fsys\_id%3D7cd0c421bf200100710071a7bf0739bd%26sysparm\_record\_list%3Dactive%253dtrue%255enameSTARTSWITHpass%255eORDERBYorder%26sysparm\_record\_row%3D3%26sysparm\_record\_rows%3D6%26sysparm\_record\_target%3Dsysevent\_email\_action%26sysparm\_view%3Dadvanced%26sysparm\_view\_forced%3Dtrue
