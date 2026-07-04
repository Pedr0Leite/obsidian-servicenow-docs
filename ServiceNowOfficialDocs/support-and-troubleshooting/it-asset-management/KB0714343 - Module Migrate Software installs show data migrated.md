---
title: "Module \"Migrate Software installs\" show data migrated"
aliases:
  - KB0714343
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714343
kb_number: KB0714343
last_modified: 2024-04-07
---

## Module "Migrate Software installs" show data migrated

  

### Issue

# Symptoms

* * *

Access module "Migrate Software installs" to migrate software from "cmdb\_software\_instance" to "cmdb\_sam\_sw\_install" but get following message.

@@@

Data has already been migrated   
Data is already present in the 'cmdb\_sam\_sw\_install' table 

@@@

![](sys_attachment.do?sys_id=e16a2466db42b450e515c22305961972)

# Release

* * *

Kingston

# Cause

* * *

Once data is present in the install table (cmdb\_sam\_sw\_install) we assume the migration has been done from the instance table  (cmdb\_software\_instance) and no further action is permitted.

# Resolution

* * *

Delete the data in software install table (cmdb\_sam\_sw\_install). Once data deleted, we should be able to access module "Migrate Software installs" to migrate software data.

![](sys_attachment.do?sys_id=7d6a2466db42b450e515c22305961983)

# Additional Information

* * *

Can use "Table Cleanup" module to clear data from "cmdb\_sam\_sw\_install"
