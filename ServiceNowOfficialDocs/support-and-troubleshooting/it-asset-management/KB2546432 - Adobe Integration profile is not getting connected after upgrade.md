---
title: "Adobe Integration profile is not getting connected after upgrade"
aliases:
  - KB2546432
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2546432
kb_number: KB2546432
last_modified: 2025-10-05
---

## Adobe Integration profile is not getting connected after upgrade

  

### Summary

**Issue** : Adobe Integration profile is not getting connected after upgrade

**Verify** : Adobe integration profile and verify if its in "Published" state.

-   if yes, check available credentials.  if its using Oauth Token. Navigate to "Manage Tokens"--> Remove existing Adobe Oauth Token.
-   Navigate to integration profile--> connection and credentials
-   Make sure HTTP connection has Org ID 
-   Than open connection profile --> get new oAuth Token and than Re-run Scheduled import job for Adobe subscription import.
