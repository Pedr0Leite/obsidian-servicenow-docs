---
title: "Error messages on Employee Center Portal after instance upgrade"
aliases:
  - KB0994652
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994652
kb_number: KB0994652
last_modified: 2023-08-25
---

## Issue

After upgrading to Rome, error messages similar to the below ones can be seen on the ESC portal when a case is opened from My cases.

![](sys_attachment.do?sys_id=9f60d1cb1bce701038739979b04bcb1e)

## Resolution

Script Include 'hr\_CaseAjax' might have been customized and skipped during the last upgrades; therefore it is missing the 'getERTValueEmployee' method:  
https://instance\_name.service-now.com/sys\_script\_include.do?sys\_id=b25370019f22120047a2d126c42e7000  
  
Go ahead and either revert the Script Include 'hr\_CaseAjax' to OOB or incorporate your customizations into the latest store version of the same.
