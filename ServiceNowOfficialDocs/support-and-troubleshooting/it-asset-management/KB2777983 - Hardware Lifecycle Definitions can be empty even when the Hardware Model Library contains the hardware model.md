---
title: "Hardware Lifecycle Definitions can be empty even when the Hardware Model Library contains the hardware model"
aliases:
  - KB2777983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2777983
kb_number: KB2777983
last_modified: 2026-02-12
---

## Hardware Lifecycle Definitions can be empty even when the Hardware Model Library contains the hardware model

  

### Issue

● A hardware model is present in Hardware Model Library, but no lifecycle milestones are shown in Hardware Lifecycle Definitions for the same model

### Symptoms

● Hardware Model Library shows the model details (example: Arista DCS-7050DX4-32S-F)  
● Hardware Lifecycle Definitions list shows No records to display for the same Product model / Model number  
● Users expect lifecycle milestones such as End of Sale, End of Support, End of Life, but the lifecycle list remains empty

### Release

Not release specific

### Cause

● Hardware Model Library content and Hardware Lifecycle Definitions content are sourced differently  
● A model can exist in Hardware Model Library  
● Lifecycle milestones are populated only when manufacturer-published lifecycle dates are available in the vendor sources used by ServiceNow content  
● If the manufacturer does not publish lifecycle dates for a specific model or series, or the lifecycle data is not available through the content source, ServiceNow content cannot populate Hardware Lifecycle Definitions even though the model record exists

### Resolution

● This behavior is expected when lifecycle milestones are not available from the manufacturer sources used for content delivery  
● Validate whether official lifecycle dates exist for the model or series from the manufacturer’s published documentation  
● If official lifecycle dates exist and you want them available as content, submit a Content Request with vendor proof so the content team can review and potentially add lifecycle coverage in a future update  
● Content Request process reference  
KB0790305 – Content Request Process  
[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0790305](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790305)
