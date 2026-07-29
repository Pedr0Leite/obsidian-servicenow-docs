---
title: "PCF Discovery error \"No containment or hosting rules defined for dependent class [cmdb_ci_pcf_space_instance]\"
aliases:
  - KB0779936
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779936
kb_number: KB0779936
last_modified: 2024-04-08
---

## PCF Discovery error "No containment or hosting rules defined for dependent class \[cmdb\_ci\_pcf\_space\_instance\]"

  

### Issue

-   Pivotal Cloud Foundry (PCF) Discovery fails with store version 1.0.49
-   No containment or hosting rules defined for dependent class \[cmdb\_ci\_pcf\_space\_instance\]. Add containment/hosting rules for '{"className":"cmdb\_ci\_pcf\_space\_instance","values":{"pcf\_guid":"1ffc47a2-e593-41f2-aeb0-3af5bf987ae9","discovery\_source":"ServiceNow","install\_status":"1","name":"pcf-event-alerts-db","url":"/v2/service\_instances/1ffc47a2-e593-41f2-aeb0-3af5bf987ae9","sys\_class\_name":"cmdb\_ci\_pcf\_space\_instance"}}',Too many other errors

### Release

-   Affected Instance: Madrid Patch 6
-   Discovery and Service Mapping Patterns version: 1.0.49

### Cause

-   Upon reviewing Metadata Editor there are NO containment rules available OOB for "CloudFoundry Space Service Instance".
-   OOB with store release containment rules should be automatically added.

### Resolution

-   The containment rules are provided OOB from store release 1.0.54
-   Meanwhile, add containment rules manually in Metadata Editor
-   After adding correct containment rules manually, pattern executed successfully.
-   Following are the container rules.

![](sys_attachment.do?sys_id=94e8eff8dbc474d04cfbeeb5ca961923)

![](sys_attachment.do?sys_id=9ce8eff8dbc474d04cfbeeb5ca961925)

![](sys_attachment.do?sys_id=14e8eff8dbc474d04cfbeeb5ca961927)

![](sys_attachment.do?sys_id=98e8eff8dbc474d04cfbeeb5ca961928)
