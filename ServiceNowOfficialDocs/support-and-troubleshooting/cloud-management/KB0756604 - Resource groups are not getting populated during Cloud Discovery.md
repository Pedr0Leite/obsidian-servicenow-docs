---
title: "Resource groups are not getting populated during Cloud Discovery"
aliases:
  - KB0756604
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756604
kb_number: KB0756604
last_modified: 2024-04-07
---

## Resource groups are not getting populated during Cloud Discovery

  

### Issue

-   When the Cloud discovery initiated and completed successfully, it is observed all the Cloud resources are getting populated but the "Resource Groups" are not populated to "cmdb\_ci\_resource\_group" table even when there are multiple Resource Groups are available on the Console.

### Release

-   London P\* Madrid P\* 

### Cause

-   It is observed that CI Metadata is missing with Containment rules and having additional hosting rules for the Resource Group.

### Resolution

1.  Log in to the instance.
2.  Navigator >> Metadata Editor >> Containment rules >> and make sure "Logical Datacenter" and "Cloud Service Account" contains Resource Group.  
      
               ![](/sys_attachment.do?sys_id=86aa8470db8cf0d022e0fb2439961945)  
      
    
3.  Navigator >> Metadata Editor >> Hosting rules >> and make sure there are no entries   
      
              ![](/sys_attachment.do?sys_id=c2aa8470db8cf0d022e0fb2439961936)  
      
    
4.  If any of the "Containment Rules" are missing, need to add them manually.
5.  Navigator >> cmdb\_metadata\_containment\_list >> Click on New and add the missing containment rule
