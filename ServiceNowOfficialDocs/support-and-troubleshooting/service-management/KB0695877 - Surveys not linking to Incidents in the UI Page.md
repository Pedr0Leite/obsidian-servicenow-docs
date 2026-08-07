---
title: "Surveys not linking to Incidents in the UI Page"
aliases:
  - KB0695877
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695877
kb_number: KB0695877
last_modified: 2024-04-07
---

## Surveys not linking to Incidents in the UI Page

  

### Issue

When trying to take a survey, you do not see the "This Survey is in regards to...."

### Release

Kingston Patch 7

### Cause

This message is not seen because the Survey link that is being sent in the email notification is for the survey and not the survey with the assessment instance

### Resolution

Use the "Survey User Invite" email notification and a Trigger condition so an assessment instance record is generated on the asmt\_assessment\_instance table through the Trigger Condition and the Email notification will see the new record and send out an Email containing the Survey Link with the appropriate information in it. The message will show then.
