---
title: "Audit of \"Alert [em_alert]\" is not capturing all field data updates. "
aliases:
  - KB0812556
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812556
kb_number: KB0812556
last_modified: 2024-04-08
---

## Audit of "Alert \[em\_alert\]" is not capturing all field data updates.

  

### Issue

Before Madrid, the 'em\_alert' table did not have any field checked true for audit data, yet the table was set with "Audit" as true. In most cases, this would allow all fields on the table to be audited. In Madrid and afterwards, the table is still set with auditing enabled, but only work note changes are captured on the 'sys\_audit' table.   
  
  

### Release

Madrid onward. 

### Cause

The audit for 'em\_alert' table is limited to only a single field (i.e work\_notes) in order to limit the amount of 'sys\_audit' records created. Given the nature of this table, auditing every field as it was set in London and before has caused performance degradation to both the updating/creation of 'em\_alert' records and instance wide.

If still wants to enable audit for fields other than “work\_notes”, then we need to enable audit explicitly for required fields.

### Resolution

Enable field-level audit to capture the audit data required for your organization. Below is an example of how to do this (using the "State" field as an example): 

1.  Go to "sys\_dictionary.LIST" from application navigator   
    2\. Filter for table "em\_alert" and column name "state"   
    3\. Open the record and choose "Advanced View" under "Related Links"   
    4\. Enter "audit=true,edge\_encryption\_enabled=true" in field "Attributes" and save it. 

Repeat the process above for whatever fields your company deems as essential for auditing on the 'em\_alert' table. 

CAUTION: Please do NOT apply this to every field on the 'em\_alert' table for the reasons outlined above!
