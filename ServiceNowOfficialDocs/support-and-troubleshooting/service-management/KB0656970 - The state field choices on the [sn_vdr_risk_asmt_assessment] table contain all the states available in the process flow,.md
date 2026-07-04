---
title: "The state field choices on the [sn_vdr_risk_asmt_assessment] table contain all the states available in the process flow, but the drop-down list shows only four states."
aliases:
  - KB0656970
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656970
kb_number: KB0656970
last_modified: 2024-04-07
---

## The state field choices on the \[sn\_vdr\_risk\_asmt\_assessment\] table contain all the states available in the process flow, but the drop-down list shows only four states.

  

### Issue

The state field choices on the \[sn\_vdr\_risk\_asmt\_assessment\] table contain all the states available in the process flow, but the drop-down list shows only four states.

Steps to replicate: 

1.  Navigate to sn\_vdr\_risk\_asmt\_assessment.do.
2.  Select the drop-down menu in the **State** field.

Desired Behavior: All 7 states should display.  
Unexpected/Actual Behavior: Only 4 states are displaying as options to select from.

  

  

### Cause

This is expected OOB behavior, controlled by the **Configure state choice list** Client Script

### Resolution

To change the states directly and not by state flows, then deactivate the client script: 

1.  Navigate to https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=ba7686d5eb2322006080a638a206fe36 
2.  Click on header UI Action to edit the record in the correct application (GRC: Vendor Risk Management application) 
3.  Uncheck **Active** field. Save.
