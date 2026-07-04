---
title: "Quick Reservation widget not setting  module in Dropdown based on Order defined"
aliases:
  - KB1006189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1006189
kb_number: KB1006189
last_modified: 2025-01-02
---

## Issue

Quick reservation widget not displaying from start correct reservable module based on defined order.  
  
Steps to reproduce:  
  
1\. Create 2-3 Reservable Modules with order (sn\_wsd\_rsv\_reservable\_module table)  
  
2\. Workplace Safety Management > Workplace service portal > Workplace Service Portal Home.  
3\. Observe, modules in drown-down will not be in order as defined in backend  
  
  
  
![](/sys_attachment.do?sys_id=a41ed7afdb59c110b3c099ead3961921)

## Resolution

  
For the order defined for Reservable Modules are not honoured when they are displayed in Quick Reserve dropdown,  
This seems to be a miss, internal team will address this in future. However, order is already defined in the make a new reservation module.  
  
  
Meantime, they fixed this in you dev instance by adding orderBy clause on order field before executing the query. Updated getActiveReservableModules in WSDReservableModuleService script include:  
  
  
moduleGr.addEncodedQuery(moduleEQ);  
moduleGr.orderBy('order'); //ADDED FOR CSTASK287649  
moduleGr.query();  
  
  
After this, the quick reserve's Reservable module dropdown displays RMs in proper order.  
  
Further, about auto-select module, please note, the last usage of Reservable module in Quick Reserve will be defaulted the next time.  
Basically, when you reserve a space for the first time, when you visit the portal next time, the module will be selected as per your last reservation. This is as per design.  
It's not just the Reservable module selection, but using it to perform a search - Like selecting Reservable module, Building, Floor, Date, Time slot will perform an auto search and these selection will be defaulted next time.

## Additional Information

  
**_getActiveReservableModules: function(encodedQuery) {_**  
**_var moduleGr = new GlideRecord(WSDConstants.TABLES.ReservableModule.name);_**  
**_var moduleEQ = this.DEFAULT\_ENCODED\_QUERY;_**  
  
**_if (encodedQuery)_**  
**_moduleEQ = WSDUtils.formatString('{0}^{1}', moduleEQ, encodedQuery);_**  
  
**_moduleGr.addEncodedQuery(moduleEQ);_**  
**_moduleGr.orderBy('order'); //ADDED FOR CSTASK287649_**  
**_moduleGr.query();_**  
  
**_var modules = \[\];_**  
**_while(moduleGr.next()) {_**  
**_if(moduleGr.canRead()){_**  
**_modules.push({_**  
**_sys\_id: moduleGr.getValue('sys\_id'),_**  
**_display\_value: moduleGr.getDisplayValue(),_**  
**_title: moduleGr.getDisplayValue('title'),_**  
**_name: moduleGr.getValue('name'), // on frontend we use name as display_**  
**_inline\_title: moduleGr.getValue('inline\_title'),_**  
**_apply\_to\_shift: WSDUtils.safeBool(moduleGr.getValue('apply\_to\_shift')),_**  
**_buildingSysIds : this.getAssociatedBuildingSysIds(moduleGr.getValue('sys\_id')),_**  
**_order: moduleGr.getValue('order') ? parseInt(moduleGr.getValue('order')) : null// using order for displaying types_**  
**_});_**  
**_}_**  
**_}_**  
**_return modules;_**  
**_},_**
