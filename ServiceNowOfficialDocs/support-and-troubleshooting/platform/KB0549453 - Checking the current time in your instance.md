---
title: "Checking the current time in your instance"
aliases:
  - KB0549453
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549453
kb_number: KB0549453
last_modified: 2025-03-07
---

## Checking the current time in your instance

  

### Issue

If you ever want to know what the current time is set to in your instance you may take the following steps as an administrator.

### Release

All Releases

### Resolution

 **To see the current time in your instance:**  

1)  Login as an administrator

2)  Elevate your security privileges so that you have the security\_admin role. You can read more about that here: [Security\_admin role](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/administer/security/concept/security-admin-role.html "Learn more about  Security_admin role")

3)  Go to System Definition -> Scripts - Background (you will not see this if you do not elevate your privileges)

4)  Enter the following command in the "Run script" window:

gs.info(gs.nowDateTime());

5) Click the "Run script" button

You should see output similar to:

\*\*\* Script: 2025-03-07 16:20:00
