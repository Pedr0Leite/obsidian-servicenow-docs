---
title: "SAP HANA DB identifier not working as expected when it see multiple running processes 'hdbindexserver' on the same server"
aliases:
  - KB0745579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745579
kb_number: KB0745579
last_modified: 2024-04-07
---

## SAP HANA DB identifier not working as expected when it see multiple running processes 'hdbindexserver' on the same server

  

### Issue

# Symptoms

SAP HANA DB identifier not working as expected when it see multiple running processes 'hdbindexserver' on the same server.

For example: from the image attached, instead of finding all of the SAP HANA DB application, but it found only the last running process.

![](sys_attachment.do?sys_id=7649a4eedb02b450e515c22305961978)

# Release

All Version

# Environment

Server with have multiple running process 'hdbindexserver'.

# Cause

Based on OOB identifier 'SAP HANA DB', it will look for these Criterion attributes \[sys\_class\_name,instance,sid\] and since it couldn't find the matching once, it will fallback to parent's rules which is 'Application Rule' identifier.

When it found the match from this Application Rule' identifier and since these all three processes are on the same Linux machine, so it keep overwritten till execute the last pattern.

Expected to see all three SAP HANA DB  
But, seeing only 1 SAP HANA DB

# Resolution

This issue has been filed in PRB1334177.

Workaround: need to deselected the 'Allow fallback to parent's rules' from this SAP HANA DB identifier entry https://<instancename>.service-now.com/nav\_to.do?uri=cmdb\_identifier\_entry.do?sys\_id=0ecc6ab3ff100200ab8fffffffffff06

# Additional Information

To easy see this issue like an image, paste XML payload to Jsonblob.
