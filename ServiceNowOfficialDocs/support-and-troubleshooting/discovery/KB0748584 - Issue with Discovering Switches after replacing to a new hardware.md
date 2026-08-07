---
title: "Issue with Discovering Switches after replacing to a new hardware"
aliases:
  - KB0748584
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748584
kb_number: KB0748584
last_modified: 2024-04-07
---

## Issue

# Symptoms

After replacing a hardware Switch and during discovery the following error message is noticed in the **SNMP - Classify - Input** payload, though the Test Credentials is successful.

<result error="SNMP probe timed out. Target is either unreachable or there are no valid credentials for it." source="xx.xx.xx.xx">

# Release

Any version.

# Cause

New hardware Switches which were replaced don't have the agent file configured in order for the discovery to be successful.

# Resolution

The agent configuration file needs to be configured in line to the older hardware device (or) needs to be replaced by the internal Network team for the discovery to be successful.
