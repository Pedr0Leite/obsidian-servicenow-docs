---
title: "Special handling notes popup in agent workspace are empty"
aliases:
  - KB0790969
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790969
kb_number: KB0790969
last_modified: 2024-01-28
---

## Special handling notes popup in agent workspace are empty

  

### Issue

Special handling notes issue in agent workspace. Creating a note in "sn\_shn\_notes" table works fine in the native UI, but the popup is empty when viewing the same case in agent workspace.

### Release

ALL

### Cause

If the 'Message' field is empty and only 'Short Description' is filled, Agent workspace displays an empty popup while the native UI displays the 'Short Description' in the popup. 

### Resolution

This is caused because the "Message" field on the "sn\_shn\_notes" record is empty.  
Please add any text to the "Message" field so that Special Handling notes are displayed on Agent Workspace.  
  

### Related Links

[Add special handling notes to records in Agent Workspace](https://docs.servicenow.com/csh?topicname=workspace-configuration.html&version=latest "Add special handling notes to records in Agent Workspace")
