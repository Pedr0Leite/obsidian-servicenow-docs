---
title: "Missing ACLs for \"sn.cmp.cloud_service_designer\" role  to add input paramters on Blueprint"
aliases:
  - KB0722849
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722849
kb_number: KB0722849
last_modified: 2025-08-25
---

## Missing ACLs for "sn.cmp.cloud\_service\_designer" role to add input paramters on Blueprint

  

### Issue

# Symptoms

* * *

Cloud Management Platform provides Operation inputs by default according to the Blueprint, also,  it provides flexibility for users to configure additional input parameters as  per the requirement, 

How to add Operation input Parameters to [Configure blueprint operations](https://docs.servicenow.com/csh?topicname=create-blueprint-cmp.html&version=latest#blueprint-operations "Configure blueprint operations"). (Refer: Procedure)

The **"sn.cmp.cloud\_service\_designer"** role to a user  will provide privileges to configure, modify and delete a Blueprint and the same user with role **"sn.cmp.cloud\_service\_designer"** should also be eligible to create his own Input parameters to a specific Blueprint, but, it was  observed that the user with only role **"sn.cmp.cloud\_service\_designer"** adding the input parameters will show success message but the newly added parameter would go missing post a refresh on the Blueprint, this article will demonstrate to add the input parameters successfully and get the visibility for the user with role **"sn.cmp.cloud\_service\_designer"**. 

# Issue details - Steps to Reproduce

* * *

-   Login to the instance 
-   Hop with a user who is having only **"sn.cmp.cloud\_service\_designer"** role 
-   Navigate to **"Cloud User Portal"** 
-   Design >> Blueprints >> Create a Blueprint >> Configure the Blueprint with resources
-   Once the Blueprint resources added  >> Click on Operations >> Provision >> Click on Blueprint Container Provision option >> Right side of the page we see the Inputs   
     

![](sys_attachment.do?sys_id=2f5b2c6adb42b450e515c223059619c1)

-   Click on the + to add a new blueprint operation input 
-   Fill the Name and Mapping Filed with required inputs and checkbox the Show option and  Save the Input, it will immediately show us a  Success message.  
      
    

![](sys_attachment.do?sys_id=335b2c6adb42b450e515c223059619c7)

-   Mostly, we believe the input parameter saved successfully, but, **refresh the Blueprint and verify the newly added parameter it will not be available**
-   Repeat the same steps with the user having **"Admin"** access, the **newly added parameter will be still visible even after refreshing the Blueprint** 
-   This means the issue is only observed when the user is having no admin access and only have **"sn.cmp.cloud\_service\_designer"**

 Environment

* * *

-   Jakarta P\* and Kingston P\* 

# Cause

* * *

-    The issue is because there are no ACLs added to that table **(sn\_cmp\_rb\_op\_impl\_param)** for the service designer role. 

# Workaround

* * *

-   Adding ACLs to the Role on the table "sn\_cmp\_rb\_op\_impl\_param" will fix the issue and save the Input parameters successfully and get visibility.

### Procedure 1

-   Login to the instance 
-   Impersonate with a user having Admin access 
-   Navigate to  sn\_cmp\_rb\_op\_impl\_param\_list.do

            https://<instance>.service-now.com/sn\_cmp\_rb\_op\_impl\_param\_list.do?sysparm\_list\_mode=grid&sysparm\_query=&sysparm\_offset=

-   Configure table  sn\_cmp\_rb\_op\_impl\_param >> Related Links >> Access Controls 

            https://<Instance>.service-now.com/sys\_db\_object.do?sys\_id=sn\_cmp\_rb\_op\_impl\_param&sysparm\_refkey=name&sysparm\_domain\_restore=false&sysparm\_referring\_url=

-   Click on New and add ACL operations **"Create" "Execute" "Delete" "Write" and "Read"** 

**![](sys_attachment.do?sys_id=f35b2c6adb42b450e515c223059619cc)**

### Procedure 2

-   Attached XML update sets to this article, please download and import to fix the issue  
      
    

# Permanent Fix 

* * *

-    The ACL issue for the table "sn\_cmp\_rb\_op\_impl\_param" is permanantly from London Patch 3
