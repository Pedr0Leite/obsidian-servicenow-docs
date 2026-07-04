---
title: "Is Rollback Action available in the Flow Designer"
aliases:
  - KB0820128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820128
kb_number: KB0820128
last_modified: 2025-11-17
---

## Is Rollback Action available in the Flow Designer

  

### Issue

Rollback Action in the Flow Designer

### Release

All Versions

### Resolution

Rollback in legacy Workflow is prone to error and must be reimagined. While we have rollback on the radar, it is not on our immediate roadmap for consideration. Customers interested in Rollback should implement via design pattern, by including Flow logic for validation/checking/tracking with a final conditional to determine if rollback is necessary, and call a subflow or include the automation logic to rollback the desired changes.

### Related Links
