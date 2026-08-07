---
title: "Flow Designer: Subflow Input Choice List - how to get the display value of selected value"
aliases:
  - KB0870836
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870836
kb_number: KB0870836
last_modified: 2024-02-26
---

## Issue

In Flow Designer you can get the value of a field, but not its display value. 

For a sub-flow, create an input type of choice and add a few key-value pairs (screenshot attached - [input](sys_attachment.do?sys_id=184673addb3d6410ab0202d5ca961978 "input"))

e.g.

Apple 1

Banana 2

Orange 3

  

Then reference this input field in the flow displays value as 1,2,3 instead of Apple, Banana, Orange (screenshot attached - [issue](sys_attachment.do?sys_id=ec46b3addb3d6410ab0202d5ca961993 "issue"))

  

  

## Resolution

It is working as expected, in this case it been passed as value, you can use "key Value Map" transformation to transform it desired value. (screenshot attached - [transform](sys_attachment.do?sys_id=2a4637addb3d6410ab0202d5ca96194f "transform"))  

Also here is the documentation reference related to transform maps:  
https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/flow-designer/reference/utilities-transform-functions.html
