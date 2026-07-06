---
title: "Unable to access instance after user import runs"
aliases:
  - KB0789936
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789936
kb_number: KB0789936
last_modified: 2026-05-05
---

## Unable to access instance after user import runs

  

### Issue

Users are unable to log in after the import runs.

### Release

All versions

### Cause

-   The customer sets up a Pre script on the scheduled import for users. The script marks all/most users for deactivation.
-   The import is configured to unmark users still available in LDAP.
-   The Postscript is set up to deactivate any remaining users.
-   However, if there are any issues during the import (MID server, credential, etc.), all users will be deactivated.

### Resolution

  
The pre and post-script logic must take into account any issues with the import.
