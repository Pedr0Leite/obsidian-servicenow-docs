---
title: "Modify the page associated with a scripted list menu item in Service Portal"
aliases:
  - KB0657736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657736
kb_number: KB0657736
last_modified: 2025-06-20
---

## Modify the page associated with a scripted list menu item in Service Portal

  

### Issue

Scripted list menu items, which are meant to be dynamic, are not honoring the Page field in the menu items. 

### Resolution

To resolve this, you can add a **\_\_page** object while generating your list.

Add page object to scripted list

The following example demonstrates how to modify this functionality in an default Request Menu Item: 

1.  Navigate to [https://yourInstance.service-now.com/sp\_rectangle\_menu\_item.do?sys\_id=7c686d00d7200200a9ad1e173e24d4e9](https://yourInstance.service-now.com/sp_rectangle_menu_item.do?sys_id=7c686d00d7200200a9ad1e173e24d4e9)
2.  Part of the default script populating the incident items using Glide Record query in addition the page object **\_\_page**  
    
    ```
    var z = new GlideRecord('incident');z.addActiveQuery();z.addQuery('caller_id', gs.getUserID());z.orderByDesc('sys_updated_on');z.setLimit(max);z.query();while (z.next()) {    var a = {};    $sp.getRecordValues(a, z, 'short_description,sys_id,number,sys_updated_on');    if (z.short_description.nil())        a.short_description = "(No description)";    a.__table = z.getTableName();    a.type = 'record';    a.__page = 'form'; // __page should be string value of the page ID you would like to redirect    a.sortOrder = z.sys_updated_on.getGlideObject().getNumericValue();    t.items.push(a);}
    ```
    

**Note:** For this to work, the type of the menu item should always be set **record.**

**Additional information**

The HTML code is used to display a drop-down tree menu, specifically in the header Menu Widget, using an Angular template, **spDropdownTreeTemplate**.

Get the Angular template: [https://yourInstance.service-now.com/sp\_ng\_template.do?sys\_id=492127b05b301200e39fc7ad31f91a50](https://yourInstance.service-now.com/sp_ng_template.do?sys_id=492127b05b301200e39fc7ad31f91a50)
