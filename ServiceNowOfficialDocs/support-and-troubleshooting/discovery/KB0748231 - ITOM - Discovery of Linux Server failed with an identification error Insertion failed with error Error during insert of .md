---
title: "ITOM - Discovery of Linux Server failed with an identification error : Insertion failed with error Error during insert of cmdb_ci_nas_file_system (10.XX.XX.X:/)"
aliases:
  - KB0748231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748231
kb_number: KB0748231
last_modified: 2024-04-07
---

## Issue

Linux OS Discovery pattern failed in payload processing with an error during insert of cmdb\_ci\_nas\_file\_system (10.XX.XX.X:/)

**STEPS TO REPRODUCE**

01) Discovery of Storage server running on Network Attached Storage(NAS) on Linux Operating System.

02) Failed with below errors while processing payload:

Pattern logs errors:

Errors:

  
Description: 2019-04-18 06:38:17: Identification CI Errors:  
Insertion failed with error Error during insert of cmdb\_ci\_nas\_file\_system (10.XX.X.XX:/)  
Identification Relation Errors: Insertion failed with error

While digging deep into the errors, you will find below errors in the node logs while inserting:

FAILED TRYING TO EXECUTE ON CONNECTION 8: INSERT INTO cmdb\_ci\_nas\_file\_system ("nas\_path","nas\_ip\_address","sys\_id","nas\_hostname") VALUES(?,?,cast(? as char(32)),?),INSERT INTO cmdb\_ci\_file\_system ("type","capacity","sys\_id","mount\_point") VALUES(?,?,cast(? as char(32)),?),INSERT INTO cmdb\_ci\_storage\_volume ("size\_bytes","volume\_id","sharable","sys\_id","media\_type","size","delete\_on\_termination","free\_space","free\_space\_bytes") VALUES(?,?,?,cast(? as char(32)),?,?,?,?,?)  
General Data Exception detected by database (ORA-01438: value larger than specified precision allowed for this column)

## Resolution

01) We need to modify CMDB\_CI\_STORAGE\_VOLUME table columns "free\_space\_bytes" and "size\_bytes" to NUMBER(25,2) at the database level

02) And also set the sys\_dictionary values to 25 on the table \[cmdb\_ci\_storage\_volume\] columns "free\_space\_bytes" and "size\_bytes"

03) Technical Support Team can help to make these changes in the Database using a Change Process, please do contact for any info.
