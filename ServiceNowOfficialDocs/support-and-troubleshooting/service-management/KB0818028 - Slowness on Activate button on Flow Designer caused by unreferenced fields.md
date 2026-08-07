---
title: "Slowness on Activate button on Flow Designer caused by unreferenced fields"
aliases:
  - KB0818028
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818028
kb_number: KB0818028
last_modified: 2025-08-05
---

## Slowness on Activate button on Flow Designer caused by unreferenced fields

  

### Issue

Customer was facing slowness issue on a Flow when clicking on "Activate" button.

### Release

### Cause

From the logs we were able to find that there is a unknown field 'quiescence' in table which is not referenced properly and it is stopping Flow Designer to be activated.

Logs:

<table style="border-collapse: collapse; width: 0%; height: 59px;" border="1"><tbody><tr style="height: 163px;"><td style="width: 80%; height: 163px;"><p><span style="font-size: 10pt;">=======================================================================================================================================</span><br><span style="font-size: 10pt;">2020-03-03 15:39:31 (693) Default-thread-13 9727F7CA1BD744502A4E8597DC4BCB6C txid=8ff8f7821bd7 WARNING *** WARNING *** getGlideElement called for unknown field 'quiescence' in table 'sys_hub_flow_logic'</span><br><span style="font-size: 10pt;">2020-03-03 15:39:31 (693) Default-thread-13 9727F7CA1BD744502A4E8597DC4BCB6C txid=8ff8f7821bd7 WARNING *** WARNING *** setValue called for unknown field 'quiescence' in table 'sys_hub_flow_logic'</span><br><span style="font-size: 10pt;">2020-03-03 15:39:31 (752) Default-thread-13 9727F7CA1BD744502A4E8597DC4BCB6C txid=8ff8f7821bd7 WARNING *** WARNING *** getGlideElement called for unknown field 'quiescence' in table 'sys_hub_flow_logic'</span><br><span style="font-size: 10pt;">2020-03-03 15:39:31 (752) Default-thread-13 9727F7CA1BD744502A4E8597DC4BCB6C txid=8ff8f7821bd7 WARNING *** WARNING *** setValue called for unknown field 'quiescence' in table 'sys_hub_flow_logic'</span><br><span style="font-size: 10pt;">=======================================================================================================================================</span></p></td></tr></tbody></table>

Please check below screenshot to see when there is an unreferenced/Unknown field, it will be shown as \[record\] instead of actual field name. Check actions highlighted in the below screenshot.

![](/sys_attachment.do?sys_id=012002141ba71590f81c86ae6e4bcb50)

### Resolution

Creating flow from scratch will help resolve configuration issues.  
Make sure before you remove any fields from flow, which are not referenced in the later part of flow.  
Please consider testing in subprod instances before moving to prod instances.
