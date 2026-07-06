---
title: "Event is matched to the same interval even after the 'alert active interval' passes."
aliases:
  - KB0746261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746261
kb_number: KB0746261
last_modified: 2024-04-07
---

## Event is matched to the same interval even after the 'alert active interval' passes.

  

### Issue

# Symptoms

The alert active interval determines how Event Management handles a new event that is similar to events that appear on an existing alert. Based on the active interval, event, and existing alert information, the event information is added to either the existing alert or a new alert.  
  
In some cases the new event is being matched to the same alert even though the alert active interval passes.

# Release

All Releases.

# Environment

When Event Management plugin is activated.

# Cause

The Alert State might be 'Open' or 'Reopen' by the time new event comes in. Since the alert is open the event is matched to the same alert even though alert active interval passed.

# Resolution

Works as expected.

# Additional Information

[https://docs.servicenow.com/csh?topicname=t\_EMSetTheAlertActiveInterval.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EMSetTheAlertActiveInterval.html&version=latest)
