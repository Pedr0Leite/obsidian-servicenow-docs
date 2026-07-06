---
title: "Deleting Orphaned Records using Javascript"
aliases:
  - KB0783518
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783518
kb_number: KB0783518
last_modified: 2026-06-11
---

## Issue

This article is to show how to delete or remove the orphaned records from a table using Javascript instead of using the SNOW API.

E.g 'discovery\_credentials' table.

## Resolution

1.  Run the script below to change the 'sys\_class\_name' to "discovery\_credentials" of the orphaned records.  
    Given the sys\_ids of the records and use in an encoded query of the GlideRecord:
    
    ```
    var equery = "sys_idIN15642a73dbc627009c8a92d8db961999,,1fcb3facdb03130082d422371b96190e,,81c228f7dbb63340a7429cb6db961944,,82459b24dbdda3408d92e5951b9619a2,,9404dad1db0bab00c1e4302b7c96196a,,a7e342bedbf7a340dda51db41b961944,,a8116d82db0bb3009c8a92d8db96197c";var gr1 = new GlideRecord('discovery_credentials');gr1.addEncodedQuery(equery);gr1.query();while(gr1.next()){  gs.print(gr1.sys_class_name);  gr1.sys_class_name='discovery_credentials';  gr1.update();}
    ```
    
2.  Once the sys\_class\_name is updated, the record can be opened from the list.
3.  Delete the records.

## Additional Information

[KB0716609 - Detect and remove orphan records using JavaScript](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716609 "KB0716609 - Detect and remove orphan records using JavaScript")
