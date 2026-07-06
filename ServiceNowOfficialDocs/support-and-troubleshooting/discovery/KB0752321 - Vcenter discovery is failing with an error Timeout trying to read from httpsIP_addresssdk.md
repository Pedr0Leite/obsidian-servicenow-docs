---
title: "Vcenter discovery is failing with an error \"Timeout trying to read from https://IP_address/sdk\""
aliases:
  - KB0752321
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752321
kb_number: KB0752321
last_modified: 2024-04-07
---

## Issue

# Symptoms

VCenter discovery is failing with error "Timeout trying to read from https://IP\_address/sdk"

# Release

All Releases

# Resolution

You can resolve the issue by increasing the vcenter timeout probe parameter.

1\. Navigate to the probe **VMWare - vCenter Datacenters.**

https://<instance\_name>.service-now.com/discovery\_probes.do?sys\_id=1e4b29618f071200c2fe0b5437bdee19

2\. From the probe parameters related list, click New.

3\. Fill in the fields, as appropriate.  
Name : **vcenter\_timeout**

Value: default 30000 milliseconds (30 seconds).

You can start with 30000 and increase as you see fit.

# Additional Information

[https://docs.servicenow.com/csh?topicname=vcenter-probes.html&version=latest](https://docs.servicenow.com/csh?topicname=vcenter-probes.html&version=latest)
