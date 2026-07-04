---
title: "Non Sam role able to edit alm_license record"
aliases:
  - KB0995940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995940
kb_number: KB0995940
last_modified: 2024-08-13
---

## Issue

-   When navigating to below table
-   \-Other asset 
-   \-New
-   \-Software entitlement
-   ![](sys_attachment.do?sys_id=d86703f51ba6b090c17111751a4bcb2b)

-   User with non sam-role able to edit or update the record for alm\_license table
-   https://instancename.service-now.com/nav\_to.do?uri=%2Falm\_license.do%3FWIZARD:action%3Dfollow%26sys\_action%3D%26sys\_id%3D-1%26sys\_target%3Dalm\_asset%26sysparm\_query%3Dsys\_class\_name%253dalm\_asset%26sysparm\_referring\_url%3Dalm\_asset\_list.do%253fsys\_id%253d-1%254099%2540sys\_target%253dalm\_asset%254099%2540sysparm\_fixed\_query%253d%254099%2540sysparm\_group\_sort%253d%254099%2540sysparm\_parent%253da28d237047622100158b949b6c9a710d%254099%2540sysparm\_query%253dsys\_class\_name%253dalm\_asset%254099%2540sysparm\_target%253d%254099%2540sysparm\_view%253d%26sysparm\_target%3D%26wiz\_action%3Dsysverb\_new%26wiz\_collection%3D%26wiz\_collectionID%3D%26wiz\_collection\_key%3D%26wiz\_collection\_related\_field%3D%26wiz\_view%3D

## Resolution

-   In Paris if we navigate to below table
-   \-Other asset 
-   \-New
-   \-Software entitlement
-   ![](sys_attachment.do?sys_id=fda743391ba6b090c17111751a4bcb5a)
-   The page is editable and saves the record in alm\_license table.
-   This is Due to invoke of ACL -record/alm\_license/create
-   This ACL is evaluated to false in Quebec but not evaluated at all in Paris
-   [https://instancename.service-now.com/sys\_security\_acl.do?sys\_id=8cab69251b302000aebbfbcd2c07137f](https://instancename.service-now.com/sys_security_acl.do?sys_id=8cab69251b302000aebbfbcd2c07137f "https://instancename.service-now.com/sys_security_acl.do?sys_id=8cab69251b302000aebbfbcd2c07137f")
-   The issue is fixed in Quebec from Platform end and user can upgrade to Quebec.
