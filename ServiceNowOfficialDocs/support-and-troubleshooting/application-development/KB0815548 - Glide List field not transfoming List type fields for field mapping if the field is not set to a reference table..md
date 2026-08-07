---
title: "Glide List field not transfoming \"List\" type fields for field mapping if the field is not set to a reference table."
aliases:
  - KB0815548
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815548
kb_number: KB0815548
last_modified: 2024-04-08
---

## Glide List field not transfoming "List" type fields for field mapping if the field is not set to a reference table.

  

### Issue

If we use LIST type column without any reference in the transform map filed mapping, target record is not updating.

Reproducible in a Madrid and New York instance  
1) Create a transform map from a staging table to a target table with a 'List' type column with no reference association  
2) In the transform map, Create a field map between a source list to a target list type  
\* After transform, Notice the target column is not manipulated

### Release

Madrid and New York

### Resolution

Please use this workaround :

Remove the mapping in the Transform Map and use OnBefore Script   
\=====   
(function runTransformScript(source, map, log, target /\*undefined onStart\*/ ) {   
  
target.setDisplayValue('<TARGET\_FIELD\_NAME>', source.<SOURCE\_FIELD\_NAME>);   
  
})(source, map, log, target);   
\=====

### Related Links

This is fixed in Orlando
