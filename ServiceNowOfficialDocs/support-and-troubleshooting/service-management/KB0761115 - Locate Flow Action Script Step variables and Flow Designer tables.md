---
title: "Locate Flow Action Script Step variables and Flow Designer tables"
aliases:
  - KB0761115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761115
kb_number: KB0761115
last_modified: 2026-02-02
---

## Locate Flow Action Script Step variables and Flow Designer tables

  

### Issue

Finding Flow Designer tables in your instance can be challenging because most flow work happens in the designer interface. This article helps you locate these tables, particularly those storing input and output variables for Flow Action Script Steps. 

### Release

All releases

### Resolution

1.  To view input and output variable configurations, go to the sys\_hub\_step\_instance table. Add the Inputs and Outputs fields to the form layout if they aren't visible.
2.  To find actual values of input and output variables, go to the sys\_hub\_action\_instance table. Add the following fields to the form layout if they aren't visible: 
    -   Inputs
    -   Action type.Outputs
    -   Action type parent.Outputs
    -   Compiled snapshot.Outputs
3.  To locate all Flow Designer tables, go to https://<instance\_name>.service-now.com/sys\_db\_object\_list.do?sysparm\_query=sys\_update\_nameISNOTEMPTY%5EnameSTARTSWITHsys\_hub
