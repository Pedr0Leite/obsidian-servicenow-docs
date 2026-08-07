---
title: "CMDBTransformUtil fails when one source table has multiple transforms updating different record types"
aliases:
  - KB0792306
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792306
kb_number: KB0792306
last_modified: 2025-04-07
---

## CMDBTransformUtil fails when one source table has multiple transforms updating different record types

  

### Issue

You may load the attached update set for reproduction matters.  
It contains a data source and some transform maps.

\- Please attach the excel file TestData.xlsx to this data source "IssueDemo".  
\- Load All Records and then Run the transform Transform\_Computers, the Transform\_Servers does not need to be selected.  
Transform\_Computers will appear to succeed, but will in fact have bombed out of the onBefore script, so look in the System Log (Warnings) where you will see:  
org.mozilla.javascript.EcmaError: Cannot convert null to an object.  
Caused by error in sys\_script\_include.86665601531002007c949096a11c0858.script at line 108

This is the OOTB script CMDBTransformUtil failing because it tries to obtain details of the fields from the Transform\_Servers mapping, in the context of a cmdb\_ci\_computer record.

The erroneous code seems to be here:

getTransformValues: function(source, map, log) {  
var values = {};  
var td = GlideTableDescriptor.get(map.target\_table);  
var entryGr = new GlideRecord(this.transformEntryTable);  
entryGr.addQuery('source\_table', map.source\_table);  
entryGr.query();

The search finds all field mappings for the source table, not just the ones for the map being processed.

### Resolution

To correct this issue he has added an additional query term:

entryGr.addQuery('map', map.sys\_id);

So we would have:

getTransformValues: function(source, map, log) {  
var values = {};  
var td = GlideTableDescriptor.get(map.target\_table);  
var entryGr = new GlideRecord(this.transformEntryTable);  
entryGr.addQuery('source\_table', map.source\_table);

entryGr.addQuery('map', map.sys\_id);

  
entryGr.query();
