---
title: "Issue with missing variables in sla condition."
aliases:
  - KB0831345
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831345
kb_number: KB0831345
last_modified: 2026-06-24
---

## Issue with missing variables in sla condition.

  

### Issue

You have reported an issue with variables in sla condition.  
SLA definition conditions are missing.

As a result of this missing conditions, SLA's are not properly attached to the respective RITM.

Browser Console displays the errors as below

  
Uncaught TypeError: Cannot read property 'getOperator' of undefined  
at e.\_initValues (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:6116)  
at e.\_init (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:4541)  
at e.create (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:4525)  
at buildFieldsPerType (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:2909)  
at updateFields (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:2346)  
at e.build (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:4593)  
at e.buildRow (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:4391)  
at e.addNewSubCondition (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:4287)  
at e.buildQuery (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:3736)  
at e.build (js\_includes\_last\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:3678)  
  
Uncaught TypeError: Cannot read property 'conditionRow' of null  
at e.\_setFilterBasedOnType (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:6426)  
at e.\_getVariableResponse (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:6416)  
at fn (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:6406)  
at e.\_query0 (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:18742)  
at e.\_responseReceived (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:15461)  
at e.\_processReqChange (js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:15319)  
js\_includes\_doctype.jsx?v=05-07-2020\_2135&lp=Wed\_Apr\_29\_02\_53\_27\_PDT\_2020&c=27\_527:845 \[00:00:00.163\] \*\*\* WARNING \*\*\* GlideAjax.getXMLWait - synchronous function - processor: PickList

![](sys_attachment.do?sys_id=cf4b9aaf4729cb103542f24c736d43fb)

### Release

All

### Cause

The Variable not displaying is Inactive.

### Resolution

Review the Variables used in the sla definition start conditions, verify and ensure they are active.  
  
This should fix the issue with the Start conditions and should get rid of the browser console errors. This should also enable the form to load properly and display the pause and stop conditions.
