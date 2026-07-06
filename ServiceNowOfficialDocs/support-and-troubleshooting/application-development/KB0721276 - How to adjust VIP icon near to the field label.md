---
title: "How to adjust VIP icon near to the field label"
aliases:
  - KB0721276
tags:
  - servicenow
  - support-kb
  - client-scripts
  - VIP
  - ui-customization
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721276
kb_number: KB0721276
last_modified: 2026-04-27
---

## Issue

ServiceNow provides an OOB feature to place an icon in front of the field label. E.g. VIP icon is highlighted in front of Caller field in Incident form. The icon position can be adjusted so it can be placed next to the field label.

## Resolution

If we take an example as 'Highlight VIP Caller' OOB client script, following lines of the script set the position of VIP icon on the field label

  

//check for VIP status  
if (caller.vip == 'true') {  
var bgPosition = "95% 55%";  
if (document.documentElement.getAttribute('data-doctype') == 'true')  
bgPosition = "5% 45%";

  
  
![](sys_attachment.do?sys_id=b01ffce2db0ab450e515c223059619ce)  
  

  

Modifying the value on the variable 'bgposition' will adjust the icon position near to field Label.

  

//check for VIP status  
if (caller.vip == 'true') {  
var bgPosition = "70% 30%";  
if (document.documentElement.getAttribute('data-doctype') == 'true')  
bgPosition = "70% 70%";  
  
  
![](sys_attachment.do?sys_id=741ffce2db0ab450e515c223059619d3)

## Related

- [[KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
