---
title: "Alert group in Event Management stops working"
aliases:
  - KB0687565
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687565
kb_number: KB0687565
last_modified: 2025-01-03
---

## Alert group in Event Management stops working

  

### Issue

# Symptoms

* * *

Alert group in Event Management stops working

# Release

* * *

From Jakarta

# Cause

* * *

Alert Aggregation is not enabled

# Resolution

* * *

1\. Check Service Analytics > Properties, make sure "Enable alert aggregation" is ticked  
  
2\. Navigate to schedule jobs, make sure all Service Analytics scheduled jobs are active.

List of the scheduled jobs:

[https://docs.servicenow.com/csh?topicname=c\_ServiceAnalyticsOverview.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ServiceAnalyticsOverview.html&version=latest)  
  

Also please note:

Automated alert groups are built to check Metric Name field and the Configuration item field of alerts by default.

If Metric Name is empty, it uses only the Configuration item field.  
  
Event Rule can be used to create Metric Name for the alerts.
