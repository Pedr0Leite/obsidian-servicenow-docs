---
title: "Troubleshooting Instance Response Times | Homepages"
aliases:
  - KB0656152
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656152
kb_number: KB0656152
last_modified: 2026-03-31
---

## Troubleshooting Instance Response Times | Homepages

  

### Issue

Homepage transactions make up 30% to 50% of all user transactions for most customers. This is the first thing a users sees when logging in and the last item checked at the end of the day. If a user's homepage is slow, they will notice: this is the most common incident that Customer Support receives. Most of these incidents can be traced back to a slow homepage blocking the user's other request.

The ServiceNow homepage model is a wide-open canvas that enables your users to make the platform work as they prefer, which is a key feature of the platform. However, sometimes widgets or reports added to a homepage can take30 seconds to load.

This article provides a few steps/techniques to help improve overall response times and improve your customers' user experience before these users start to report the issue to your admin team.

### Release

All releases

### Cause

Suppose a user is reporting that the platform seems randomly slow throughout the day and you determine that the source is a homepage that takes 30 seconds to load on a different browser tab that has the auto-refresh set to 5 minutes.

The user experience therefore is that every so often ServiceNow hangs but the user cannot reproduce the issue or provide steps to reproduce. This issue occurs because every 5 minutes or so a home page about 10% of the time takes 30 seconds to load, which blocks the current transaction.

### Resolution

To solve this issue, rather than attempting to improve the slow widget or report, which can be ver time consuming, mitigate the impact by removing the widget, changing the user's homepage, or disabling auto-refresh. Try to do this check weekly or monthly.

**NOTE:** If you do decide to try to determine which homepage widget or report is causing the issue and take action to resolve it, see [KB0634929 - Quickly identifying the causes of homepage slowness](https://support.servicenow.com/kb_view.do?sysparm_article=KB0634929 "KB0634929 - Quickly identifying the causes of homepage slowness").

To find the affected users and disable auto-refresh:

1 - Go to a filtered transaction list:  
https://<instance\_name>.service-now.com/syslog\_transaction\_list.do?sysparm\_offset=&sysparm\_list\_mode=grid&sysparm\_query=sys\_created\_onONToday@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()%5Esql\_count%3E0%5Eresponse\_time%3E20000%5Esys\_created\_by!%3Dguest%5Eurl%3D/home.do%3Fsysparm\_auto\_request%3Dtrue%5EGROUPBYsys\_created\_by%5EORDERBYDESCresponse\_time&sysparm\_first\_row=1&sysparm\_view=

2 - Target the users (Created By) with the highest record count. Some of these users will have hundreds of homepage transactions a day so target those users first.

3 - Disable the user's auto-refresh option, which is usually not needed, by impersonating the user and setting this option off. For more information, see [KB0634955 - How to change the homepage refresh behavior](https://support.servicenow.com/kb_view.do?sysparm_article=KB0634955 "KB0634955 - How to change the homepage refresh behavior").
