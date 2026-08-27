---
title: "View Scorecard does not show survey information/charts"
aliases:
  - KB0960952
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960952
kb_number: KB0960952
last_modified: 2024-03-06
---

## View Scorecard does not show survey information/charts

  

### Issue

Clicking View Scorecard does not display any related survey answer information or charts.

### Release

Paris

### Cause

Mandatory field 'Filter field' did not have a value.

### Resolution

There is a mandatory field called 'Filter field' which needs a value (ex: Name)  
  
When reproducing this issue I found the error below in the error logs:  
org.mozilla.javascript.EcmaError: Cannot convert null to an object.  
Caused by error in plugin://com.snc.assessment\_core/ui.jtemplates/asmt\_scorecard.xml.15 at line 87  
  
84: var groupField = metricType.display\_field + '';  
85:  
86: var type = new GlideRecord(metricType.table + '');  
\==> 87: refFieldLabel = type.getElement(groupField).getED().getLabel();  
  
The backend code that displays the scorecard is expecting a value for this field to process.  
  

### Related Links

The field can be populated manually from the list view
