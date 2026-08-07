---
title: "Not getting push notifications on mobile"
aliases:
  - KB0789034
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789034
kb_number: KB0789034
last_modified: 2024-04-08
---

## Not getting push notifications on mobile

  

### Issue

Customer reports, they are not receiving push notification into their mobile device. They can see, it's getting captured in the logs.

### Cause

OOB REST Message "ServiceNowMobileApp Push" (ded0e522ff1231009738fffffffffffc) which sends this notifications is missing in affected instance.

### Resolution

Please XML Export this REST Message from your other instance where it's available along with respective Resources and XML Import it in affected instance  and it should fix the issue.

NOTE: In case you don't have any other instance, you can always find it in an OOB developer instance.
