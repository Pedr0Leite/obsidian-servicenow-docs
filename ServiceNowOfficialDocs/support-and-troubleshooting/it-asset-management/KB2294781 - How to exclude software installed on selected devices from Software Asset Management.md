---
title: "How to exclude software installed on selected devices from Software Asset Management"
aliases:
  - KB2294781
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2294781
kb_number: KB2294781
last_modified: 2025-09-15
---

## How to exclude software installed on selected devices from Software Asset Management

  

### Summary

To exclude software installed on selected devices from Software Asset Management, we need to use the following system property:

**Property: com.snc.samp.exclude\_device\_flag**

### Facts

1.  This property (com.snc.samp.exclude\_device\_flag) is not a true/false property.
2.  It is a string property.

### Release

All

### Instructions

**Property Functionality:**

1.  On the cmdb\_ci\_hardware table, select a true/false column, for example: Exclude from SAM \[u\_exclude\_from\_sam\].
2.  Then we need to add the column name "**u\_exclude\_from\_sam**" as a value in this property.
3.  Then run "**SAM — Adjust Installs for excluded CIs**" scheduled job  
      
    Example:  
    **u\_exclude\_from\_sam** is a true/false field on cmdb\_ci\_hardware table, we should use "u\_exclude\_from\_sam" as the value on the property  
      
    **Steps to Apply:**  
    **1st**  
    \[-\]Navigate to Software Asset > system properties >All Properties.  
    \[-\]Delete the value from the property(**com.snc.samp.exclude\_device\_flag**)  
    \[-\]Select Save.  
    \[-\]Run the scheduled job (**SAM — Adjust Installs for excluded CIs**), the system starts managing the software installed on all previously excluded devices.  
      
    **2nd**  
    \[-\]Navigate to Software Asset > Administration > Properties.  
    \[-\]Open the property(**com.snc.samp.exclude\_device\_flag**)  
    \[-\]Add "**u\_exclude\_from\_sam**" as value .  
    \[-\]Select Save.  
    \[-\]\[Run the scheduled job (**SAM — Adjust Installs for excluded CIs)**
