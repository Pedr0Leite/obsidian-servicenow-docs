---
title: "MID Server Down on Scheduled Export Set Jobs"
aliases:
  - KB0790988
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790988
kb_number: KB0790988
last_modified: 2024-04-08
---

## MID Server Down on Scheduled Export Set Jobs

  

### Issue

-   Export sets allow you to push data from an instance to an external file.
-   Sometimes Export Set Jobs fail with Error Message -

The MID Server 'XXXXX' is down

![](sys_attachment.do?sys_id=a7cdd089db00b4d0471f9c41ba96195a)

### Release

-   All

### Cause

-   MID Server fetches the data to be exported.
-   But if there are not enough privileges for Service account running MID Server.
-   The export target will not be reachable.
-   MID Server in this process might go Down.
-   Thus Export Set Job will be failed.

### Resolution

-   Add MID Server Service account to an admin group/privileged group to export the set from the instance to target.
-   Scheduled Export Set Job would succeed as expected.

![](sys_attachment.do?sys_id=a3cdd089db00b4d0471f9c41ba96195d)

### Related Links

**Useful documents :**

[Export Sets](https://docs.servicenow.com/csh?topicname=c_ExportSets.html&version=latest "Export Sets")

[Scheduled Export](https://docs.servicenow.com/csh?topicname=c_ExportSets.html&version=latest "Scheduled Export")
