---
title: "Orchestration activity failing with the error : \"Unable to resolve host name: ****** and default MID Server null is down/invalid\"
aliases:
  - KB0748693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748693
kb_number: KB0748693
last_modified: 2024-04-07
---

## Issue

# Symptoms

Orchestration activity fails with the error "Unable to resolve host name: \*\*\*\*\*\* and default MID Server null is down/invalid"

# Release

All

# Cause

Default mid server for Orchestration is not set.

# Resolution

1) Navigate to Orchestration -> Mid Server Configuration -> Mid Server Properties

2) Set the value for the "Default MID Server to use for Orchestration Activities"

3) Also navigate to Mid Server -> Applications

4) Select Orchestration

5) Make sure a value is set for the Default Mid Server field

Alternative Solution:

If the default mid server is not present, the DNS name and IP(s) must be created manually, as in below doc:

[https://docs.servicenow.com/csh?topicname=t\_MapIPAddressToDNSName.html&version=latest](https://docs.servicenow.com/csh?topicname=t_MapIPAddressToDNSName.html&version=latest)
