---
title: "Discovery : Model ID not populated for Printers"
aliases:
  - KB0783763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783763
kb_number: KB0783763
last_modified: 2024-04-08
---

## Issue

Model ID is not populated by Discovery for Printers of Certain Manufacturers such as Dell, Kyocera, etc . Since Model ID is not populated, discovery will automatically set the Model ID to unknown and therefore an Asset will not be created for the Printers

## Resolution

In order to make sure the Model ID is populated for all the printers, follow the below steps :

1) Navigate to the CI Classification -> SNMP -> Standard Network Printer

2) In the trigger probes related list, remove the condition script for SNMP-SNMP - HP Printer Model record and save the record.

3) After performing the above steps, re-run discovery and you should now be able to see the model ID is populated.
