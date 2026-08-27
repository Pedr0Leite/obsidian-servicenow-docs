---
title: "Email Notifications of Type Meeting Invitation Don't Send Images"
aliases:
  - KB0755834
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755834
kb_number: KB0755834
last_modified: 2024-04-07
---

## Email Notifications of Type Meeting Invitation Don't Send Images

  

### Issue

# Symptoms

When user creates a CAB Meeting record and sends a notification to all the attendees with images in the notification body, email is sent to the respective attendees, however the email received doesn't contain the images

# Cause

The cause of this issue is the Type of notification being sent. The notification in question is of type - Meeting Invitation. The emails sent out from the notification of type Meeting Invitation are of icalender formatted emails.

In current design Servicenow doesn't support HTML content in Meeting invitations / icalender formatted emails.

Resolution

Since it is not supported in current design, customers will need to raise enhancement requests so that the requirement may get considered in future releases
