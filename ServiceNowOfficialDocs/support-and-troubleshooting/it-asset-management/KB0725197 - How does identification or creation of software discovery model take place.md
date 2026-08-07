---
title: "How does identification or creation of software discovery model take place?"
aliases:
  - KB0725197
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725197
kb_number: KB0725197
last_modified: 2024-04-07
---

## Issue

When an entry is made in the cmdb\_sam\_sw\_install table, the business rule "create software normalization" is triggered which will perform a look up on the primary key value for the cmdb\_sam\_sw\_install table. If the primary key does not exist in the software discovery model table an insert will be performed. 

Business rule, create Software Normalization: https://#####.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=9ec2b34d37101000deeabfc8bcbe5d43

This primary key is built by another business rule "build primary key": https://#####.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=efd6bb4d37101000deeabfc8bcbe5d44

This is the code snippet that builds the primary key:

var pk = current.publisher + '.' + current.display\_name + '.' + current.prod\_id + '.' + current.version + '.' + current.revision;   
if ((current.edition != "") && (current.edition != "NULL")){  
pk = pk + '.' + current.edition;  
}

If the current record has a serial number then the primary key value is the serial number which is dependent on the revision as well.

So newer records will be created if the primary key does not match to a record with that primary key.
