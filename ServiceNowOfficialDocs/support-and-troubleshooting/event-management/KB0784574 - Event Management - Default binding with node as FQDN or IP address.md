---
title: "Event Management - Default binding with node as FQDN or IP address"
aliases:
  - KB0784574
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784574
kb_number: KB0784574
last_modified: 2025-03-31
---

## Issue

When the node is IP address or FQDN and if the IP or FQDN is not present in the hardware table then the OOB default binding behaves differently.

## Resolution

The default binding follows this logic:

If the node is CI name, FQDN, IP or MAC Address then we go to the hardware table and look for the corresponding fields with the node value, if any match is found bind it to that CI. In addition to this behavior if the node includes a dot and is not an IP Address, we take the variable (value) ahead of the first dot (.) and search for that value in the Hardware table under the name field.  
  
For example, if the node is a FQDN, subdomain.example.com, we search the CMDB for the value in the FQDN field. If there is no match, use the value before the first dot ("subdomain") to search the Name column.
