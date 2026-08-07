---
title: "Event Management: When alert grouping is enabled, parent alerts are opened with a state of closed for incoming events"
aliases:
  - KB0714793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714793
kb_number: KB0714793
last_modified: 2024-04-07
---

## Event Management: When alert grouping is enabled, parent alerts are opened with a state of closed for incoming events

  

### Issue

# Symptoms

* * *

  

In alert grouping, parent alerts are opened with a state of closed for events which are coming in.

# Release

* * *

All

#   

# Cause

* * *

1\. A parent alert is created after the alerts are created.   
2\. When alerts are created in 'em\_alert' table, a schedule job runs to identify the patterns in the alerts. If it finds one, it creates a new alert(parent) and ties the alerts(secondary) to it.   
3\. In this case, I see that when the alerts(secondary) were created, the state was 'closed'. This caused the parent alert to be opened with state 'closed'.   
4\. You can check the created timestamp on parent and child alerts to understand this.   
5\. In this case, we need to understand why the secondary alerts are being created with state 'closed'.

#   

#
