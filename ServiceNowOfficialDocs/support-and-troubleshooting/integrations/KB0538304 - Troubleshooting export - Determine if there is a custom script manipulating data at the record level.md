---
title: "Troubleshooting export - Determine if there is a custom script manipulating data at the record level"
aliases:
  - KB0538304
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538304
kb_number: KB0538304
last_modified: 2024-05-19
---

## Troubleshooting export - Determine if there is a custom script manipulating data at the record level

  

### Issue

This issue is related to exporting data from the instance. The export takes too long and might even cause some scheduled export to fail as a result of a record level script manipulation.

## Symptoms

-   Export takes too long
-   Not all data is exported
-   Scheduled export fails to run

### Cause

There is one or more occurrence of line-level script manipulation that can slow the export process significantly.

### Resolution

To solve the issue, first identify the calculated field that is causing the slowness.

1.  Navigate to the list view of the table you are trying to export from.
2.  Right-click the header and select **Personalize Dictionary**.
3.  Ensure that the **Calculation** field is showing in the column list.
4.  Use **Filter Out** or **Show Matching** to only show fields with the **Calculation** field set to **not empty**.
5.  Check each field and verify that the **Calculation** value is appropriate to run per record.

The following example shows a valid **Calculation** value for a field that should not effect performances:

current.time\_worked.dateNumericValue()/1000

The following example shows a calculated field that might affect performances significantly, assuming the **Company** field has no index. 

var ga = new GlideAggregate('incident');   
var count = 0;   
ga.addQuery('company',current.company);   
ga.addAggregate('COUNT');   
ga.query();   
  
if ( ga.next() ){   
  count=ga.getAggregate('count');   
}   
  
count
