---
title: "How Software Model Display Name Is Calculated in ServiceNow"
aliases:
  - KB2740637
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2740637
kb_number: KB2740637
last_modified: 2026-01-27
---

## How Software Model Display Name Is Calculated in ServiceNow

  

### Summary

**Purpose**  
• Explains how the Software Model Display name is generated in ServiceNow  
• Clarify which OOB components are involved  
• Describe which values are considered during calculation

* * *

**When the calculation occurs**  
• When a Software Model record is saved  
• Applies to both insert and update actions

* * *

**How Display Name works (OOB behavior)**  
• ServiceNow automatically recalculates the Display name during save  
• The system reads a defined set of identity values from the Software Model  
• A single Display name is generated using the populated values  
• The generated value overwrites the existing Display name  
• This behaviour is expected and by design

* * *

**Values considered for Display Name (in order)**  
• Manufacturer, Product, Version, Edition, Named user type, Platform, Language, Database option, Unit of consumption, Condition name, SAP License Metric (only when SAP plugin is active)

• Only values that are populated are used  
• Empty or default values are ignored during generation

* * *

**Out-of-Box components involved**

Business Rule  
• Calculate display\_name  
• https://<instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=b5113661d7131100bbc783e80e61035b

Script Includes  
• ModelUtils  
• http://<instance\_name>.service-now.com/sys\_script\_include.do?sys\_id=e5e5e63edbdf33001f9b765f369619d9

• SAMPSWModelUtil  
• https://<instance>.service-now.com/sys\_script\_include.do?sys\_id=25808468675423003b4687cb5685efa5

* * *

**Important notes**  
• Display name is a system-managed field  
• Any change to the Software Model can trigger recalculation

* * *

**Key takeaway**  
• Software Model Display name is always system-calculated based on the available identity values and is recalculated on every save using OOB logic.
