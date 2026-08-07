---
title: "Automated Alert Group is created for alerts that are bound to different CIs"
aliases:
  - KB0696604
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696604
kb_number: KB0696604
last_modified: 2024-04-07
---

## Automated Alert Group is created for alerts that are bound to different CIs

  

### Issue

# Symptoms

* * *

Sometimes Automated Alert group is created for alerts that are bound to different CIs

# Release

* * *

Any

# Cause

* * *

Working as designed

# Resolution

* * *

This is expected. Alerts can be bound to the same group even if they use different Cis.

  
In an High-level, we look at the CI and metric name of each alert.   
If we see that that CI1 with Metric1 and CI2 with Metric2 appears together across several alerts (i.e we see several alerts with those cis and metrics that appears at the same time, and we see this on several accessions), we will think these CIs are related, and next time we see them together we will put them in the same group.  
  
(In this case CI1 and Metric1 are the alert features)
