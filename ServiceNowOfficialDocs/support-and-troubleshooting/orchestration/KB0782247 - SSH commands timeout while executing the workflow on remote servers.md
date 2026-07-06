---
title: "SSH commands timeout while executing the workflow on remote servers"
aliases:
  - KB0782247
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782247
kb_number: KB0782247
last_modified: 2024-04-08
---

## SSH commands timeout while executing the workflow on remote servers

  

### Issue

SSH commands timeout while executing the workflow on remote servers.

Errors observed in the workflow context and the ECC queue.

xml version="1.0" encoding="UTF-8"?><results error="Error; job finished with status ERROR: Timed out while waiting for command to complete on channel 6 in state EXECUTING" post\_processing\_time="0" probe\_time="300284" result\_code="900000"><result error="Error; job finished with status ERROR: Timed out while waiting for command to complete on channel 6 in state EXECUTING"?  
  

### Release

Mid servers enabled with ServiceNow SSH client (SNCSSH - mid.ssh.use\_snc) used for Orchestration activities.

### Cause

The commands defined in the Run Command Activity in the workflow take longer than the default time of 5 minutes to be completed  
  
mid.ssh.command\_timeout\_ms Default value is 300000ms .i.e 5 mins.

### Resolution

Incrementally increase the mid server parameter "mid.ssh.command\_timeout\_ms" value and execute the workflow, it would be completed successfully.  
  

### Related Links

[MID Server parameters](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "MID Server parameters")  
  
[Add a MID Server parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "Add a MID Server parameter")
