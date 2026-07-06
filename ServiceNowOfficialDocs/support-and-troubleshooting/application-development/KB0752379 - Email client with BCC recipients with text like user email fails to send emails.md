---
title: "Email client with BCC recipients with text like \"user <email>\" fails to send emails"
aliases:
  - KB0752379
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752379
kb_number: KB0752379
last_modified: 2024-04-07
---

## Email client with BCC recipients with text like "user " fails to send emails

  

### Issue

# Symptoms

If we add email id's with name and email like "example<example@abc.com>" in BCC - the email will be discarded.

# Release

All

# Cause

BCC emails will discard from email hence email will not send to BCC email ids. Check the below screenshot of the log attached 

  

![](/sys_attachment.do?sys_id=a0ea2ce6db42b450e515c223059619f3)

  

# Resolution

While adding BCC use the email id in this format "[example@abc.com"](mailto:example@abc.com") instead of "example<example@abc.com>"
