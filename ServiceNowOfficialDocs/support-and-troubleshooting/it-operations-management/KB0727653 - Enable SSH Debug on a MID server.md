---
title: "Enable SSH Debug on a MID server"
aliases:
  - KB0727653
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727653
kb_number: KB0727653
last_modified: 2026-03-29
---

## Enable SSH Debug on a MID server

  

### Issue

SSH debugging is not currently enabled. 

### Release

All

### Resolution

How to enable **SSH** debugging to assist with issues you may encounter with Discovery.

1.  Choose MID server you want to enable this on.
2.  Click Configuration Parameters tab
3.  Click New
4.  Choose mid.ssh.debug from the drop down.
5.  Set it to the target IP you are trying to discover.  Note you can set to "true" instead of target IP but this will log all SSH debug messages regardless of the target IP. 
6.  Submit

See images for reference below.

![](sys_attachment.do?sys_id=0ea560739373b6dcc2513f986cba1020)

# ![](sys_attachment.do?sys_id=8aa560739373b6dcc2513f986cba1033)

# ![](sys_attachment.do?sys_id=0aa560739373b6dcc2513f986cba1038)

You can verify this by grabbing the MID logs and looking for mid.ssh.debug:

![](sys_attachment.do?sys_id=4ea560739373b6dcc2513f986cba1049)

### Related Links

-   [MID server Parameters](Read%20newest "MID server Parameters")
