---
title: "Embedded survey email issue on Outlook Actionable Messages"
aliases:
  - KB0962260
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962260
kb_number: KB0962260
last_modified: 2025-01-03
---

## Embedded survey email issue on Outlook Actionable Messages

  

### Issue

When we configure Outlook Actionable messages described below, the survey is not embedded in the Outlook email: [Now Platform capabilities](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/administer/survey-administration/task/embed-survey-in-outlook-email.html)

### Cause

The email is sent to a group email which is not supported as per the documentation: [Send an actionable message via email in Office 365](https://docs.microsoft.com/en-us/outlook/actionable-messages/send-via-email#supported-scenarios)

### Resolution

All the emails are sent to a group, in this case Outlook Actionable Message is not supported as stated above.  
Please send the survey to individual users' email.
