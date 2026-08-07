---
title: "Date time values in email sent might not match Date Time of the related incident record activities"
aliases:
  - KB0747497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747497
kb_number: KB0747497
last_modified: 2024-04-07
---

## Date time values in email sent might not match Date Time of the related incident record activities

  

### Issue

# Symptoms

* * *

When looking up the Date Time stamp of an Email that was sent and comparing this with the time stamp shown in the incident Activities, they could not match.

# Cause

* * *

This happens because the timestamp shown in the incident record is based on the timezone of the logged in user. This timezone can be set up in user preferences and it can be different to the timezone set for the system.

# Resolution

* * *

It is expected behavior. 

The Email will be sent with the timezone of the user who triggered the notification.

Most notifications are run by System using the system time zone. However, the "Email Client" (the email icon on some records) sends notifications with the logged-in user timezone.

![Emails date time fields](sys_attachment.do?sys_id=3cfb2ceadb42b450e515c2230596194d "Emails date time fields")
