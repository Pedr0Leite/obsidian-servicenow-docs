---
title: "When attempting to create an updateset in a scoped Application, it is getting created in the 'global' instead of the scoped Application"
aliases:
  - KB0813696
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813696
kb_number: KB0813696
last_modified: 2024-04-08
---

## When attempting to create an updateset in a scoped Application, it is getting created in the 'global' instead of the scoped Application

  

### Issue

When attempting to create an updateset in a scoped application, it is getting created in the 'global' instead of the scoped Application

  

Steps to reproduce -

         1.Create an Application with the option \[create from global\]

         ![](sys_attachment.do?sys_id=8a0f5049db0c70905a959c41ba9619e7)

        2. Select the created Application in Application Picker

  

            ![](sys_attachment.do?sys_id=860f5049db0c70905a959c41ba9619ea)

  

         3. Navigate to Local updateset and create new

         4. By default, when a scoped Application is selected, updateset will be created in the scoped Application. However, here the updateset is created in the global scope.

  

           ![](sys_attachment.do?sys_id=0a0f5049db0c70905a959c41ba9619ee)

          5.As the scope of this Application is global while creating the Application, chosen the option - "create from global", the scope of the application in the sys\_scope table is showing as global

  

           ![](sys_attachment.do?sys_id=820f5049db0c70905a959c41ba9619ed)

  

  

  

  

  

### Cause

1\. Created this Application by choosing the option \[start from global\]

  

2\. Hence, the scope of the Application is global

  

3\. As a result, when creating an updateset, it is picking the scope of the Application - "Global" from the sys\_scope table

### Resolution

It is the expected behavior
