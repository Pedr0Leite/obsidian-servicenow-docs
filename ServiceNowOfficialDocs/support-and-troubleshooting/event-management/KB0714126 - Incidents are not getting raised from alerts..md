---
title: "Incidents are not getting raised from alerts."
aliases:
  - KB0714126
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714126
kb_number: KB0714126
last_modified: 2024-05-22
---

## Incidents are not getting raised from alerts.

  

### Issue

Incidents don't get raised from alerts.

### Cause

This is because job "**Event Management - Evaluate Alert Management Rules**" is not running. This job is responsible for triggering alert action rules.

### Resolution

This problem is observed in a multi-domain environment where the jobs are defined with a user who is not part of "Global Domain".

In this case, all the Event Management jobs were defined by the "**Event Management**" user, but the job "**Event Management - Evaluate Alert Management Rules**" is touched/modified by some user called "**System Administrator**".

![](sys_attachment.do?sys_id=dc5b286adb42b450e515c22305961930)

  

This user "System Administrator" is not part of the Global domain as you can observe from below screenshot.

  

![](sys_attachment.do?sys_id=105b286adb42b450e515c22305961936)

Update the job so that it's part of "Global Domain" with "Event Management" user as "Created by. You may recreate the job in Global Domain.
