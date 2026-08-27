---
title: "How does the status of MID service reflect on the instance?"
aliases:
  - KB0750372
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750372
kb_number: KB0750372
last_modified: 2024-04-07
---

## How does the status of MID service reflect on the instance?

  

### Issue

# Overview

The Scheduled job "MID Server Monitor" makes a call to the script include "MonitorMIDServer" which sends heartbeat messages to all MID servers and notes the time it did. If the mid servers respond to the heartbeat messages then the status remains "up" else they are marked "down".

This covers two scenarios:

1.  The MID service on host is UP but mid server record on instance reflects DOWN.
2.  The MID service is DOWN but mid server record on instance shows it as UP.
