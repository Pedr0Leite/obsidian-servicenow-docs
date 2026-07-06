---
title: "Restricing files with extension \".svg\" will cause the default system icons to fail"
aliases:
  - KB0784534
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784534
kb_number: KB0784534
last_modified: 2025-07-17
---

## Restricing files with extension ".svg" will cause the default system icons to fail

  

### Issue

Restricting files with the extension ".svg" will cause the default system icons to fail

### Release

All Release

### Resolution

Some of the default icons used in the platform are ''svg" files. This can be seen here:

https://<instance\_name>.service-now.com/nav\_to.do?uri=%2Fdb\_image\_list.do%3Fsysparm\_query%3Dactive%3Dtrue%5EnameLIKEsvg

Thus if the users exclude or restrict "svg" files, then the icons would fail upon upgrading or if the user installs plugins that contain icons.
