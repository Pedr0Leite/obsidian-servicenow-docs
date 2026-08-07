---
title: "Script Debugger"
aliases:
  - KB0815530
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815530
kb_number: KB0815530
last_modified: 2025-11-18
---

## Script Debugger

  

### Summary

The Script Debugger allows application developers to debug server-side JavaScript. The Script Debugger can assist in debugging unexpected results when steps to reproduce an issue are available. A generic flow to use the script debugger would be to:

![Debug Flow](sys_attachment.do?sys_id=af7665161b6660103013751f034bcb16 "Debug Flow")

1.  Review code
2.  Set breakpoints in places of interest
3.  Open the debugger
4.  Reproduce the issue
5.  Live view code in debugger to understand behavior

### Release

All currently supported environments.

### Instructions

When a CI is created, a business rule calls script include AssetandCI.createAsset() to create an asset for such CI. Let's use this OOB process as an example on how to use the Script Debugger.

1.  Open the script include AssetandCI.
2.  Click on the line number for the line of interest to create a breakpoint.
3.  Click on the "Open Script Debugger".  
    ![Open Script Debugger](sys_attachment.do?sys_id=e37665161b6660103013751f034bcb18 "Open Script Debugger")
4.  Reproduce issue and the code should stop at the breakpoint.
5.  Open the tab with the script debugger.
6.  On Script Debugger further investigate issue.  
    ![Script Debugger](sys_attachment.do?sys_id=eb7665161b6660103013751f034bcb33 "Script Debugger")
7.  Above we can see the three main sections of the Script Debugger:  
    -   Left: Breakpoints/Call Stack
    -   Middle: Javascript code
    -   Right: Objects in memory

Issues

Script Debugger not called

Not all scripts work with script debugger, discovery\_sensor scripts is an example. Furthermore, the debugger is for the current user session only. Therefore scripts running in a different user session will not be debugged. The debugger is used often with Business Rules and Script Includes. As a workaround, create a script include and call it from the code which needs to be debugged.In the following example a script include DebugSensor was created to be called by a discovery sensor in order for it to be caught by the Script Debugger.

![DebugSensor](sys_attachment.do?sys_id=6b7665161b6660103013751f034bcb15 "DebugSensor")

**Note:** Discovery inputs are processed in a different session. In order to be able to debug such scripts, see [Ecc Queue Processing](https://hi.service-now.com/kb_view.do?sysparm_article=KB0718653 "Ecc Queue Processing") section "Debug Processing of ECC Queue Records".

### Related Links

-   [Script Debugger](https://docs.servicenow.com/csh?topicname=script-debugger.html&version=latest "Script Debugger")
