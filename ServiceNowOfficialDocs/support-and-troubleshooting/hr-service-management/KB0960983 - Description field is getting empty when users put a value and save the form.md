---
title: "Description field is getting empty when users put a value and save the form"
aliases:
  - KB0960983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960983
kb_number: KB0960983
last_modified: 2024-03-30
---

## Description field is getting empty when users put a value and save the form

  

### Issue

-   When users are trying to update the Description field with a value on the HR task form and click on Save, the field is getting blank

**STEPS TO REPRODUCE :**

-   Login to the affected instance 
-   Navigate to HR cases and open any of the HR cases which is in the ' Work In progress' State
-   In the related links click on ' Add  Task'
-   Fill in all the details on the HR task form and give a value in the description field 
-   Save the form 
-   We can see that the description field is getting blank

### Cause

-   The issue is caused because of the out of the box business rule " Sync description with rich\_description "

### Resolution

-   The issue is caused because of the out of the box business rule " Sync description with rich\_description "
-   https://<instance\_name>.service-now.com/sys\_script.do?sys\_id=a9b9acc8532f2300ff25ddeeff7b1294&sysparm\_record\_scope=d4ac3fff5b311200a4656ede91f91af2&sysparm\_nostack=true
-   This Business rule is copying the value from the field rich\_description over to the description 
-   If users are not entering a value in the rich\_description, on save when the BR runs it is copying the empty value to the description field
