---
title: "HR Agent Workspace Case does not load"
aliases:
  - KB0995981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995981
kb_number: KB0995981
last_modified: 2026-02-12
---

## HR Agent Workspace Case does not load

  

### Issue

HR Agent Workspace Case does not load

HR Agent Workspace Case is blank

Cannot open HR Cases in HR Agent Workspace

### Release

All release

### Cause

Customized \[sys\_ux\_custom\_content\_root\_elem\] record "HR Workspace" Component sn-component-hr-agent-workspace-bundle

### Resolution

Revert the customized \[sys\_ux\_custom\_content\_root\_elem\] record

Check \[sys\_ux\_custom\_content\_root\_elem\] list of records to see if anything else was customized and use the updated out-of-the-box (OOB) version
