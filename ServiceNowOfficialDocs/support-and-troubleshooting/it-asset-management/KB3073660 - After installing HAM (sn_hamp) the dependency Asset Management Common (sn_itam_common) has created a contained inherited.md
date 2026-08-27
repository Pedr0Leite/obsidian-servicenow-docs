---
title: "After installing HAM (sn_hamp) the dependency Asset Management Common (sn_itam_common) has created a contained inherited role for it_project_user and asset. "
aliases:
  - KB3073660
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3073660
kb_number: KB3073660
last_modified: 2026-06-09
---

## After installing HAM (sn\_hamp) the dependency Asset Management Common (sn\_itam\_common) has created a contained inherited role for it\_project\_user and asset.

  

### Issue

https://<instance>.service-now.com/now/nav/ui/classic/params/target/sys\_user\_role\_contains.do%3Fsys\_id%3Dfd4a119e2fe6721089d7c61bcfa4e344%26sysparm\_record\_rows%3D28%26sysparm\_view%26sysparm\_record\_scope%3D8bc357701b9e0010cf95dd33dd5ada6c%26sysparm\_record\_target%3Dsys\_metadata%26sysparm\_record\_list%3Dsys\_scope%253D8bc357701b9e0010cf95dd33dd5ada6c%255Esys\_nameCONTAINSproject%26sysparm\_nostack%3Dtrue%26sysparm\_record\_row%3D28

### Release

Current HAM (sn\_hamp) release

### Cause

The role was part of the Asset Common scope not Global scope.

### Resolution

After changing to Asset Common scope, the contained role was removed.  
  
HAMP Dev team has confirmed that this role will not be include in the base system verison in the next upcoming release.
