---
title: "Receiving SLA/OLA warning and breach emails unexpectedly"
aliases:
  - KB0712981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712981
kb_number: KB0712981
last_modified: 2024-04-07
---

## Receiving SLA/OLA warning and breach emails unexpectedly

  

### Issue

# Symptoms

* * *

Unexpected notifications from SLA and OLA warning and breach events

# Release

* * *

Kingston Patch 6

# Cause

* * *

No RITM records matched the Start Conditions of the SLA Definition(s) in question until August 14, 2018.

# Resolution

* * *

The earliest task\_sla record (which started on August 14, 2018), did not trigger a notification until it reached 75% of its duration on August 23, 2018 (which is expected per the design of the user's SLA workflow).   
  
Therefore, the behavior seen is expected. Though all of the pieces have been in place for some time to send notifications, there was never a RITM record which matched the SLA Definition's Start Conditions until August 14, 2018. Once the RITM which matched the SLA Definition's Start Conditions was created, an appropriate task\_sla record was attached. After that task\_sla record reached 75% of its business duration, the first notification/e-mail was sent on August 23, 2018.
