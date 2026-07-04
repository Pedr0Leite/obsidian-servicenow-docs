---
title: "HR case not getting created when submitted "
aliases:
  - KB2808019
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2808019
kb_number: KB2808019
last_modified: 2026-03-02
---

## HR case not getting created when submitted

  

### Issue

**Problem**  
When trying to submit the case through the portal and backend, it is not created and returns the error 'Sorry, either the data don't exist or you don't have the access'. This issue occurs in the QA instance, while the same process works fine in the dev instance. 

### Release

NA

### Cause

**Root Cause**  
1\. The QA instance had an ACL configured with a script that referenced a system property containing an extra table ('sn\_hr\_core\_case\_workforce\_admin') not present in the dev instance. This caused a security constraint failure when users attempted to submit the HR case, as the ACL blocked access to the workforce\_admin table in the QA environment.  
  

### Resolution

**Steps to Resolve**  
1\. Identify the ACL in the QA instance that fails during submission: https://XXXXXXXX.service-now.com/sys\_security\_acl.do?sys\_id=661d9db40b3222004f526f3ef6673a7a  
2\. Investigate the script include 'hr\_license' function 'hasHrAccess' linked to this ACL, which references a system property: https://XXXXXXX.service-now.com/sys\_properties.do?sys\_id=bc364ac90b232200ecbe6f3ef6673a39  
3\. Compare the property values between dev and QA instances. .The QA instance includes 'sn\_hr\_core\_case\_workforce\_admin' in the property value, which is missing in the dev instance.  
4\. Remove 'sn\_hr\_core\_case\_workforce\_admin' from the property value in the QA instance. This resolves the issue, as demonstrated by successfully submitting the HR case after the change.
