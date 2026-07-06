---
title: "Scheduled email of report does not get sent"
aliases:
  - KB0750339
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750339
kb_number: KB0750339
last_modified: 2026-05-05
---

## Scheduled email of report does not get sent

  

### Issue

After configuring a "Scheduled Email of Report" and selecting "Execute Now", no email gets sent at the scheduled time.

### Release

All releases

### Cause

bThe user set as the run\_as user does not have access to read the configured Report, or that user is otherwise invalid, e.g. set to not active and/or locked out.

### Resolution

ja(1) Verify by logging in as the run\_as user or impersonate that user and go to the defined Report record that is configured in the "Scheduled Email of Report" record.  If you see "Record not found" that explains why the email is not sent, change the run\_as to blank or change it to another user that you confirmed has access to read the Report and run Execute Now or let the schedule run and confirm the report email is sent.

(2) Again checking the run\_as user, go to that user's record in the sys\_user table and make sure it is not set to inactive and/or locked out.  Make sure that the user is active and not locked out and again has access to the report as in (1) above.  Then run Execute Now or let the schedule run and confirm the report email is sent.
