---
title: "Can hthd_user role be used to create and update ECC queue"
aliases:
  - KB0722330
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722330
kb_number: KB0722330
last_modified: 2024-04-07
---

## Can hthd\_user role be used to create and update ECC queue

  

### Issue

Can hthd\_user role be used to create and update ECC queue

  
  

# Issue

* * *

hthd\_user role is used in OOTB Help the Help Desk function to generate necessary ECC queue input to insert the computer CI data. So, does that mean the hthd\_user role can be used in other scenarios to create any ECC queue records we need? 

It seems possible as in default ACL the hthd\_user role has the permission to create and change ECC records same as "discovery\_admin" role. However, if you try to do that with hthd\_user role, it would fail.

# Cause

* * *

The reason for the failure is due to an OOTB business rule "Restrict hthd\_user to HTHD input only". In this business rule "hthd\_user" role has been restricted to create or update ECC queue only if the ECC record is Input and with topic "WMILoader", otherwise, the insert or update would be aborted. The OOTB design is that "hthd\_user" role should only be used with Help the Help Desk feature. 

# Solution

* * *

You may consider changing the ACL of ecc\_queue table to allow another role to create and update ECC records. Alternatively you may use more powerful roles like "discovery\_admin", "mid\_server" to create/update ECC records.
