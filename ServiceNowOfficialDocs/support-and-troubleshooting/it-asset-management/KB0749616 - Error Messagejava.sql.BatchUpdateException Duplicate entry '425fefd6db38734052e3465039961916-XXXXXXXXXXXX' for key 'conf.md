---
title: "Error Messagejava.sql.BatchUpdateException: Duplicate entry '425fefd6db38734052e3465039961916-XXXXXXXXXXXX' for key 'config' "
aliases:
  - KB0749616
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749616
kb_number: KB0749616
last_modified: 2024-04-07
---

## Error Messagejava.sql.BatchUpdateException: Duplicate entry '425fefd6db38734052e3465039961916-XXXXXXXXXXXX' for key 'config'

  

### Issue

# Symptoms

Experiencing errors while importing normal values from one instance to another instance.

Error:

Error Messagejava.sql.BatchUpdateException: Duplicate entry '425fefd6db38734052e34650XXXXXX-XXXXXXXXXXX' for key 'config'   
  

# Release

All releases

# Steps to reproduce

01) Activate plugin Field Normalization.

02) Filter navigator > Filed Normalization > Configurations > Normalizations

03) Open any record in the table \[fn\_normalize\_config\].

04) Under related lists, click on Normal Values.

05) Try to import xml file of these normal value records from different instance.

06) You will see the errors below:

Error Messagejava.sql.BatchUpdateException: Duplicate entry '425fefd6db38734052e3465039961916sysid- Valuenamexxxx' for key 'config'.

# Cause

Out of the box, there is a unique key with combination of fields \[config,value\]. It is checking if there is any existing record with the combination of both 'config' & 'Value'.

In this case, it found an existing record in the parent table \[fn\_value\] and as a result it couldn't import the records and throwing such errors.

# Resolution

This is expected while trying to import the records with the same fields 'Value' & 'config'.To avoid such errors, please make sure you don't have any existing records with the same combination.
