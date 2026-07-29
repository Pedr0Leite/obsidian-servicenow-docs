---
title: "What would be the technical impact, if any, if the property glide.email.smtp.max_recipients and set it to 1"
aliases:
  - KB0792611
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792611
kb_number: KB0792611
last_modified: 2024-04-07
---

## Issue

Customer would like to like to confirm if there would be any technical impact of setting the property glide.email.smtp.max\_recipients to 1 instead of 100.

This is because customer had a business requirement where they want to limit the sharing of email addresses of external people.

## Resolution

By setting 'glide.email.smtp.max\_recipients' to 1, you will cause an email that is sent to, say, 20 recipients to be broken up into 20 separate emails, each to one of the 20 recipients.  
  
Depending on your volume of recipients per email typically, this change could generate a much higher volume of individual email records.  
Your system will definitely not improve performance because it causes more emails to be sent.  
  
There is risk of slower notification sending performance due to higher volume.  
  
Please fully test it on development before making changes to prod.  
  
To speed up delivery, please review  
Speed up email delivery by disabling notifications for users with bounced emails  
[https://community.servicenow.com/community?id=community\_blog&sys\_id=932e6a6ddbd0dbc01dcaf3231f961953](https://community.servicenow.com/community?id=community_blog&sys_id=932e6a6ddbd0dbc01dcaf3231f961953)
