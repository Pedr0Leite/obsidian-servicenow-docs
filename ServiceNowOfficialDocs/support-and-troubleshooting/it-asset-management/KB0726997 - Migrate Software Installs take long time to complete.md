---
title: "Migrate Software Installs take long time to complete"
aliases:
  - KB0726997
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726997
kb_number: KB0726997
last_modified: 2024-11-02
---

## Migrate Software Installs take long time to complete

  

### Issue

# Description

* * *

Customer tried to run the "Migrate Software Installs" module but it takes long time (ie:6 days) to complete and it creates million of records in the Software Installations (cmdb\_sam\_sw\_install) table.

![](sys_attachment.do?sys_id=f223f27b1b48cd507a5933f2cd4bcbe0) 

# Procedure

* * *

Attached 2 scripts that will help to improve the migration.

1.  "SAMPMigration" script include: sys\_script\_include\_ac7ac9d4c38132002757dccdf3d3ae1c.xml  
    2\. "Create a Software Normalization" Business Rule: sys\_script\_9ec2b34d37101000deeabfc8bcbe5d43.xml

**After the migration complete, please revert the scripts to out of the box version.**

Although there is no known harm to have the modified scripts on the SN platform, it is advised to revert them to their original version to avoid unintended consequences on Software Asset Management. This also helps in smooth transitions to future upgrades of the SN platform. 

# Applicable Versions

* * *

Kingston and above

# Additional Information

* * *

When run "Migrate Software Installs" module, it will

\- create a new record in the \[cmdb\_sam\_sw\_install\] table and run all the business rules defined.  
\- Create software Discovery Model for non-existing records  
\- Normalize software Discovery Model
