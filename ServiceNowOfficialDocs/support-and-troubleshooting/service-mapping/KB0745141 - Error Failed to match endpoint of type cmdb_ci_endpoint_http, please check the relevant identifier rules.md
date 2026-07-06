---
title: "Error: Failed to match endpoint of type cmdb_ci_endpoint_http, please check the relevant identifier rules"
aliases:
  - KB0745141
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745141
kb_number: KB0745141
last_modified: 2025-09-30
---

## Error: Failed to match endpoint of type cmdb\_ci\_endpoint\_http, please check the relevant identifier rules

  

### Issue

The error _Failed to match endpoint of type cmdb\_ci\_endpoint\_http, please check the relevant identifier rules_ appears while adding the entry point for a Business service.

 ![Select Entry Point Type screen showing error](sys_attachment.do?sys_id=d3e328f59790be5024a7739c1253afea "Select Entry Point Type screen showing error")

### Release

All

### Cause

One of the reasons might be due to setting mandatory fields on 'cmdb\_ci\_endpoint\_http' table which are not mandatory OOB.

### Resolution

-   Go to 'sys\_db\_object' table.
-   Search for 'cmdb\_ci\_endpoint\_http' under Name and open it.
-   Search if there are any fields that are Mandatory and set them to not Mandatory.

### Related Links

 [Service mapping error on creation of any business service: Failed to match endpoint of type: cmdb\_ci\_endpoint\_http, please check the relevant identifier rules](https://support.servicenow.com/kb_view.do?sysparm_article=KB0720802 "Service mapping error on creation of any business service: Failed to match endpoint of type: cmdb_ci_endpoint_http, please check the relevant identifier rules")
