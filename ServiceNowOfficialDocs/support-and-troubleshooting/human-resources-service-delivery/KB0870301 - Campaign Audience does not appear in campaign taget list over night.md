---
title: "Campaign Audience does not appear in campaign taget list over night"
aliases:
  - KB0870301
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870301
kb_number: KB0870301
last_modified: 2025-09-03
---

## Campaign Audience does not appear in campaign taget list over night

  

### Issue

When a new campaign is created, the audience is not added to the campaign target list until the next afternoon.

### Cause

Out of box configuration for the scheduled job.

### Resolution

In an out of box instance, the scheduled job 'Content Automation: Update Campaign Audience' is configured to run sometime in the afternoon EST (about 4:30 PM EST). This is the job that adds the audience to the campaign. By default, this runs every 24 hours based on the 'Starting' value. If you would like to modify this to run at night, the out of box values can be updated. Below is an example:

\- Update Run to 'daily'

\- Update Time to '01 00 00'

  

The configurations mentioned would run this job every day at 1 am instead of every day in the afternoon. Above is just an example, this can be set to run at a time that fits your business requirements.   

  

### Related Links

# [Components installed with Content Automation](https://docs.servicenow.com/bundle/orlando-hr-service-delivery/page/product/human-resources/reference/installed-w-content-auto.html "Components installed with Content Automation")
