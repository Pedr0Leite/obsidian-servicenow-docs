---
title: "Issues with invalid Publisher and Manufacturer in Software Asset Management Professional"
aliases:
  - KB0961268
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961268
kb_number: KB0961268
last_modified: 2026-04-23
---

## Issues with invalid Publisher and Manufacturer in Software Asset Management Professional

  

### Issue

In Software Asset Management Professional module, it is critical to have a proper mapping and setup for Publisher (samp\_sw\_publisher) and Manufacturer (core\_company).  
We have identified multiple issues with different symptoms that caused by incorrect data on above tables.  
Here are the known issues and symptoms so far:

1.  [KB0961819 / PRB1497544 SAMP - Empty publishers linked to Software Product Result in License Workbench](https://support.servicenow.com/kb_view.do?sysparm_article=KB0961819 "KB0961819 / PRB1497544 SAMP - Empty publishers linked to Software Product Result in License Workbench")
2.  [KB0788895 / PRB1377933 Business rule 'Canonicalize Manufacturer Company Model' and 'Product should match publisher' cause error 'Publisher and Product manufacturer do not match'](https://support.servicenow.com/kb_view.do?sysparm_article=KB0788895 "KB0788895 / PRB1377933 Business rule 'Canonicalize Manufacturer Company Model' and 'Product should match publisher' cause error 'Publisher and Product manufacturer do not match'")

### Release

Any

### Cause

Each issue has detailed explanation in each KB article.

### Resolution

Apart from fixing the root cause mentioned in each KB article, you would need to execute the script to fix the incorrect data on Software Models, Software Discovery Models, Software Installs, etc.  
Please import attached file (sysauto\_script\_eb0355e065513010fa9b1e02edc28a2d.xml) to your instance.  
You should then find the scheduled script execution named "Core Company Fix Script" in sysauto\_script table (Run = On Demand).  
Execute the script. Note: Run in global domain if instance is domain separated.

If needed, observe the output in syslog table.    
  

Once the scheduled script is executed, verify that Publishers and Core companies are mapped correctly in Publisher table.

Verify Software Models, Software Discovery Models, Software Installs etc are updated correctly. If Normalized Publisher/Publisher field is not set correctly, then run below mentioned script:

Please import attached file (sysauto\_script\_9785060487a15110293c31173cbb3539.xml) to your instance.  
You should then find the scheduled script execution named "Fix Core Company References" in sysauto\_script table (Run = On Demand).

Execute the script. Note: Run in global domain if instance is domain separated.
