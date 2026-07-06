---
title: "How to disable Password Reset UI Page for all users."
aliases:
  - KB0781990
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781990
kb_number: KB0781990
last_modified: 2024-04-08
---

## How to disable Password Reset UI Page for all users.

  

### Issue

-   The ServiceNow Password Reset application enables an end-user to use a self-service process to reset or change the password. Alternatively, an organization can implement a process that requires a service desk agent to reset passwords for end-users.
-   The requirement is to disable the password reset UI page. 
-   Even after removing the password reset process for users/groups, the users are able to access the password reset UI page which has been saved in bookmarks/favorites. 

### Release

-   All Versions.

### Resolution

-   The password reset UI page will not have any access restrictions and is open to the public. This is because users should be able to access the password reset page even without login to ServiceNow instance.
-   To remove access to the UI Page, you have to follows the below steps.   
      
    1.  Create an ACL that restricts access to the password reset page.(Navigate to SystemSecurity-->Access Control(ACL)  
          
        -   https://<Instance\_Name>.service-now.com/sys\_security\_acl\_list.do?sysparm\_query=
        -   Create New Record as shown in below screenshot:  
              
              
            ![](sys_attachment.do?sys_id=c77ce33cdb0cb0d016d2a345ca9619d2)  
              
            
    2.  Remove Password Reset page from "Public Pages"(sys\_public).  
          
        -   https://<Instance\_URL>.service-now.com/nav\_to.do?uri=sys\_public.do?sys\_id=7103e9b2d7032100b9bc43d60e6103cc
