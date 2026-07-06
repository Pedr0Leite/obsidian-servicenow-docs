---
title: "Discovery Behavior : Does not trigger any other probes except for Shazzam."
aliases:
  - KB0749472
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749472
kb_number: KB0749472
last_modified: 2024-04-07
---

## Discovery Behavior : Does not trigger any other probes except for Shazzam.

  

### Issue

# Symptoms

Discovery completes without triggering any probes except for Shazzam probe.

# Release

Any

# Cause

In the discovery IP range if we have an IP network with netmask /32, the discovery fails.

# Resolution

xx.xx.xx.xx/32 netmask is nothing but a single IP. So, instead of using /32 netmask we can use below 2 configurations

1.  Create an IP address list and enter the IP that you would like to run discovery on.
2.  Create an IP address range and set starting and ending IP as the IP that you would like to discover.
