---
title: "Flow Designer is not triggering"
aliases:
  - KB0815176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815176
kb_number: KB0815176
last_modified: 2025-11-12
---

## Flow Designer is not triggering

  

### Issue

Flow on a custom table that does not trigger when conditions are met but works from Test in flow designer. Copying the flow works as expected.

### Release

 All

### Cause

Checked the flow's sys\_hub\_flow record and the latest snapshot is empty.

### Resolution

Make a minor revision (i.e. modifying the description), and publish the flow and this creates the latest snapshot and flow triggers as expected.
