---
title: "Software Asset Management potential savings showing incorrect data"
aliases:
  - KB0723690
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723690
kb_number: KB0723690
last_modified: 2024-04-07
---

## Software Asset Management potential savings showing incorrect data

  

### Issue

# Potential Savings show up as zero even though the Software installed is reclaimed.

  

![](/sys_attachment.do?sys_id=afbe78a2db0ab450e515c2230596192c)

  

![](/sys_attachment.do?sys_id=63be78a2db0ab450e515c22305961932)

### Release

All Releases

### Cause

The potential savings show up as zero, whenever there exist more unlicensed installs than the available licenses, as these installs are not licensed for/paid for and hence reclaiming these would not have any potential savings.

### Resolution

Run Reconciliation manually to reconcile the software products in the environment and review the licenses available.
