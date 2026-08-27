---
title: "How to fix schedule gaps between weekend and Monday business hours"
aliases:
  - KB0855880
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855880
kb_number: KB0855880
last_modified: 2025-10-24
---

## How to fix schedule gaps between weekend and Monday business hours

  

### Issue

If unexpected notifications are sent between midnight Sunday and Monday business hours (8:00 a.m.) despite configuring a weekend schedule (cmn\_schedule), the is because weekend schedules do not automatically cover the early Monday morning period before business hours begin. 

### Release

All supported releases

### Resolution

Weekend schedules only cover Saturday and Sunday from 00:00:00 to 23:59:59. This creates a gap in coverage from 00:00:00 on Monday morning (just after midnight Sunday) until the start of business hours on Monday at 8:00 AM.

To resolve this issue, create an additional schedule entry that covers the period between 23:59:59 (11:59:59 PM) on Sunday and 8:00 AM on Monday when your business hours begin.
