---
title: "Flow Designer tables extending var_dictionary do not coalesce on name and element"
aliases:
  - KB0856407
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856407
kb_number: KB0856407
last_modified: 2024-04-08
---

## Flow Designer tables extending var\_dictionary do not coalesce on name and element

  

### Issue

Flow Designer Update set error  
FAILED TRYING TO EXECUTE ON CONNECTION glide.28 (connpid=1854487): INSERT INTO sys\_metadata  
java.sql.BatchUpdateException: Duplicate entry 'var\_\_m\_sys\_hub\_action\_output\_9999999999a210108136231cd3961900-ta' for key 'name'  

java.sql.BatchUpdateException: Duplicate entry 'var\_\_m\_sys\_hub\_action\_input\_0999999999a210108136231cd3961900-ta' for key 'name'

### Release

Madrid and lower

### Cause

There are several tables from Flow Designer which extend var\_dictionary (which itself extends sys\_dictionary) but do not have any coalesce strategy. Records on sys\_dictionary coalesce on the same columns contained in the unique compound key, which are 'name' and 'element'. That means two records with different sys IDs are treated as the same record as long as the name and element values match.  
  
The Flow Designer tables do not follow the same rules, and coalesce on sys ID instead. That means, two records with the same name and element values will be treated as distinct records if the sys ID values are different. If you attempt to import a record like this via XML or update set, you will get unique key violation errors like this: java.sql.BatchUpdateException: Duplicate entry 'var\_\_m\_sys\_hub\_step\_ext\_input\_1e53f456db60b380ca7e9c9adb96197e-e' for key 'name'

### Resolution

The workaround/fix is to upgrade to New York release and recreate the update set. New York and later releases have a new method of creating update set for flows which should resolve this issue
