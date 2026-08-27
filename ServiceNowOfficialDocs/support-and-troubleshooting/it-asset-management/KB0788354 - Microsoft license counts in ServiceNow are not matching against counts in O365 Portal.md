---
title: "Microsoft license counts in ServiceNow are not matching against counts in O365 Portal"
aliases:
  - KB0788354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788354
kb_number: KB0788354
last_modified: 2024-04-08
---

## Microsoft license counts in ServiceNow are not matching against counts in O365 Portal

  

### Issue

Microsoft license counts in ServiceNow are not matching against counts in O365 Portal. 

![](sys_attachment.do?sys_id=b8b39085db00b8d066e0a345ca9619fd)

Navigate to Software Asset --> Software subscriptions.

https://<Instance\_Name>.service-now.com/nav\_to.do?uri=%2Fsamp\_sw\_subscription\_list.do

Check the count of each software subscription with the one in O365 Portal, the count will defer.

### Release

All Versions.

### Cause

The cause of the issue "Integration Profile" being configured incorrectly, because of which the software subscriptions are not fetched properly.

### Resolution

1.  Cross check the "Integration Profile" used for Office 365.
2.  Navigate to Saas Licenses --> Integration Profiles
3.  https://<Instance\_Name>.service-now.com/samp\_sw\_subscription\_profile\_list.do?sysparm\_query=
4.  Open the profile which has been configured for Office 365.
5.  Check if all the fields are filled properly, especially the OAuth profile.
6.  The best we always recommend is to delete the profile in question which deletes all subscriptions records and OAuth token and rest message endpoints.
7.  After that create the profile again and can run schedule job manually 'SAM - Import User Subscription\` or wait for the schedule.

![](sys_attachment.do?sys_id=34b39085db00b8d066e0a345ca9619fc)
