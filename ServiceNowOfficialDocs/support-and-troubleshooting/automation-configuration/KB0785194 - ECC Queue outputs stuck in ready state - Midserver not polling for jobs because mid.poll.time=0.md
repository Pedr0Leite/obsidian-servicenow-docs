---
title: "ECC Queue outputs stuck in ready state - Midserver not polling for jobs because mid.poll.time=0"
aliases:
  - KB0785194
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785194
kb_number: KB0785194
last_modified: 2026-04-23
---

## ECC Queue outputs stuck in ready state - Midserver not polling for jobs because mid.poll.time=0

  

### Issue

We have seen customers who have had issues with their AMB channel connecting on their environments follow the documentation and decide to disable the AMB channel and use the mid parameter mid.poll.time instead. 

When doing so, to poll 'instantly', they set this parameter value to 0.

### Release

Any

### Cause

If in the config.xml for the midserver not polling for jobs you can see this line:

<parameter name="mid.poll.time" value="0"/>

This is an invalid value of time.

### Resolution

Set the parameter to a valid value e.g. 5 (seconds). This is a sufficient polling time for most customers.
