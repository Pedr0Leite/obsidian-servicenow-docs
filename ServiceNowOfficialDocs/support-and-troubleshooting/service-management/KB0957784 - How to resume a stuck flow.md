---
title: "How to resume a stuck flow"
aliases:
  - KB0957784
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957784
kb_number: KB0957784
last_modified: 2026-03-05
---

## How to resume a stuck flow

  

### Summary

Resume a flow stuck in a waiting or queued state by running the sn\_fd.FlowAPI.nudgeFlow() script with the flow context sys\_id.

### Release

All supported releases

### Instructions

**Note**: The sn\_fd.FlowAPI.nudgeFlow() API works with wait for condition actions and approvals in all versions. Support for timers was added beginning with the San Diego release.

To resume a stuck flow:

1.  Open the Flow Context \[sys\_flow\_context\] record for the stuck flow and copy the Sys ID.
2.  Go to **Scripts** > **Background**.
3.  Run the following script, replacing <sys\_flow\_context.sys\_id> with the sys\_id you copied in step 1:  
    
    sn\_fd.FlowAPI.nudgeFlow('<sys\_flow\_context.sys\_id>', 1); 
    

The second parameter (1) specifies the number of seconds the system waits before resuming the flow. You can adjust this value as needed.

### Related Links

[Build workflows](https://www.servicenow.com/docs/r/build-workflows/build-workflows.html)

[Flow API](https://www.servicenow.com/docs/r/api-reference/server-api-reference/ScriptableFlowAPI.html)
