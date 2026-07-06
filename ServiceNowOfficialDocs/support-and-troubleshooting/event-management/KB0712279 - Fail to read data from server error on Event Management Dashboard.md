---
title: "Fail to read data from server error on Event Management Dashboard"
aliases:
  - KB0712279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712279
kb_number: KB0712279
last_modified: 2024-04-07
---

## Fail to read data from server error on Event Management Dashboard

  

### Issue

# Symptoms

* * *

The Event Management Dashboard does not display any tiles and instead gives the error "**Fail to read data from server**".

![](sys_attachment.do?sys_id=0cca20e6db42b450e515c223059619eb)

# Release

* * *

Since Geneva, and with the Event Management plugin installed.

# Cause

* * *

**The "All" Service Group record may be missing from the CMDB**, or Service CIs may not be a member of this group, or Service Groups may not have this as a parent.

All Monitored business service classes **must be a member of this group** and are automatically added when services are created. This group is required for Event Management to function correctly, and there are even business rules in the platform to actively prevent it being deleted.

Manually added Top level Service Group CIs should also be a member of this group.

Business services should list 'All' as a group they are a member of:

![](sys_attachment.do?sys_id=00ca20e6db42b450e515c223059619f1)

The "All" group should be listed in the Service Groups table, and should have the out-of-box sys\_id 0e7a06157f10310016181ccebefa91ce:

![](sys_attachment.do?sys_id=c0ca20e6db42b450e515c223059619f6)

# Resolution

* * *

1.  If the 'All' Service Group is not listed in **Event Management - Service Groups**, then [Download this link and Import the XML into your instance](sys_attachment.do?sys_id=4cca60e6db42b450e515c22305961907 "Download this link and Import the XML into your instance") which will add this record.
2.  In that same list, check that "All" is the only record that does not have a Parent value. **If any other groups are missing a parent value, then fill that in as the "All" group**.
3.  Open all \[Manual | Application | Technical \] Service CIs in forms, and check that they have All listed in the **Service Group Members** embedded list, and **add it if missing**.
