---
title: "[SAMP\Software Model] How the Software Model is tied to a discovered model when there is no Upgrade/Downgrade rights "
aliases:
  - KB0832795
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0832795
kb_number: KB0832795
last_modified: 2024-04-08
---

## \[SAMP\\Software Model\] How the Software Model is tied to a discovered model when there is no Upgrade/Downgrade rights

  

### Issue

-   In Software Installation table for Software Discovery Model "VMware Workstation 15.5", the Software Model populated as "VMware, Inc. Workstation 12 Pro" though there are no entitlements available or upgrade/downgrade rights provided. But how the system is populating software model for the discovered model.

### Release

-   Instance with Software Asset Management Professional plugin enabled.

### Cause

-   The cause would be some of "VMWare" software models are corrupted with incorrect Version condition. It should be "starts with", but it shows "**Starts with**" with "**S**" in upper case.
-   This leads to incorrect stamping.

![](sys_attachment.do?sys_id=ee9ea08ddb4078d0fec4fb24399619ab)

### Resolution

-   When reconciliation starts, we try to stamp the installs with the software models that are on the entitlements or the downgrade rights of the entitlements using the internal column "software\_model".
-   In order to resolve this, the corrupted "VMWare" software models should be fixed.   
    

![](sys_attachment.do?sys_id=2e9ea08ddb4078d0fec4fb2439961921)
