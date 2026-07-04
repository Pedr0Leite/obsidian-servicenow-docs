---
title: "Admin users not able to view the Normalization Data Services scheduled job entries."
aliases:
  - KB0746726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746726
kb_number: KB0746726
last_modified: 2024-04-07
---

## Admin users not able to view the Normalization Data Services scheduled job entries.

  

### Issue

# Symptoms

After installing Normalization Data Services plugin, the system creates two scheduled jobs **Download Normalized Company Mappings** and **Download Normalized Company Names**.

![](sys_attachment.do?sys_id=bc49e0eedb02b450e515c22305961983)

Admin users were not able to view these scheduled jobs and instead see black scheduled jobs as below.

![](sys_attachment.do?sys_id=7049e0eedb02b450e515c22305961989)

# Environment

Normalization Data Services plugin is active

# Cause

There is a read ACL on the 'cds\_client\_schedule' such that only 'maint' users can view the scheduled jobs.  
  

```
Link for the read ACL: https://<instance-name>.service-now.com/nav_to.do?uri=sys_security_acl.do?sys_id=7bd4733913a8f3402207d8228144b098
```

# Resolution

Create a new read ACL in the cds\_client\_schedule table and give admin users read access like below.

![](sys_attachment.do?sys_id=f049e0eedb02b450e515c2230596198e)
