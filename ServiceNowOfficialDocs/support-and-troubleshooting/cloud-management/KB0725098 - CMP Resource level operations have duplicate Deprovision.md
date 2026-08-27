---
title: "CMP Resource level operations have duplicate Deprovision "
aliases:
  - KB0725098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725098
kb_number: KB0725098
last_modified: 2024-01-28
---

## CMP Resource level operations have duplicate Deprovision

  

### Issue

# Description

* * *

Every stack post provisioned will have Stack level & Resource Level operations, the user can perform operations as below.

**Stack Life Cycle operations:** 

-   Modify Lease Schedule > Change the Lease Schedule for the Stack 
-   Modify Lease                     > Extend or Reduce the LeaseEnd Date
-   Stop                                      > Stop the Stack 
-   Start                                      > Start the stopped Stack
-   Deprovision                       > Deprovision the Stack

   
**Resource Life cycle Operations:** 

-   Start                             > Start the stopped Virtual Server 
-   Stop                             > Stop the running Virtual Server
-   Deprovision              > Deprovision the Virtual Server

Above Lifecycle operations are default for all the stacks, the user has the capability to create their own Operations as per the requirement

Issue

* * *

-   User created their own Resource Block and successfully provisioned the stack, but, the Resource level operations have multiple Deprovision operations.

![](/sys_attachment.do?sys_id=ad0ca02edb42b450e515c223059619c4)

-   One Deprovison operation works as expected but the other does not take any action.

# Environment

* * *

-   ServiceNow instance with CMPv2 plugin activated 

# Cause

* * *

-   When the user created the new operation for the ResourceBlock, one catalog generated for extension operation and one for resource operation.

# Workaround

* * *

  
**Scenario 1**: The user might need to have both the Deprovison operations visible but want to have different names, then modify the duplicate operation as below.  
  

-   Log into the instance
-   Impersonate to the user having privileges to modify ResourceBlcok
-   Navigate to "**sn\_cmp\_rb\_op\_signature\_list.do**"
-   Search for "Deprovision" at "Name" (Observe Multiple operations as per the Interface)
-   Search for the newly created extended interface  in "Interface" section
-   Rename the name as per your requirement (Example: Interfacename\_Deprovision)   
      
    ![](/sys_attachment.do?sys_id=a10ca02edb42b450e515c223059619ca)  
      
    
-   Go back to Stack at Cloud User Portal and verify the Resource Operations
-   Observe the Resource have still two Deprovison operations, but, one renamed and other which actually works still show as "Deprovision"

  
**Scenario 2**: The user do not want to show multiple Deprovison Operations, need only to show the operation which actually works.  
  

-   Log into the instance
-   Impersonate to the user having privileges to modify ResourceBlcok
-   Navigate to "**sn\_cmp\_rb\_op\_signature\_list.do**"
-   Search for "Deprovision" at "Name" (Observe Multiple operations as per the Interface)
-   Search for the newly created extended interface  in "Interface" section
-   Refer to the "**Acces Type**" section and observe the Deprovision access type is "**Public**"
-   Change the "**Acces Type**"  from "**Public**" to  "**Private**"   
      
    ![](/sys_attachment.do?sys_id=650ca02edb42b450e515c223059619cf)  
      
    
-   Go back to Stack at Cloud User Portal and verify the Resource Operations
-   Observe the Resource have only one Deprovison operation available which actually works.  
      
    

**Scenario 3**: The user would like to actually delete the duplicate interface operations rather modify the access type or rename.  
  

-   Log into the instance
-   Impersonate to the user having privileges to modify ResourceBlcok
-   Navigate to "**sn\_cmp\_rsrc\_opr\_cat\_item\_list.do**"
-   Verify the duplicate Deprovision operations and delete one which is not needed.

**Note:** Even after the duplicates were deleted, there is a possibility that the Deprovison operation still be visible at the Lifecycle operations, this is due to a known bug "**PRB1324325**".

# Additional Information

* * *

Refer: [Manage a stack](https://docs.servicenow.com/csh?topicname=cloudmgt-manage-stacks.html&version=latest "Manage a stack"), [Launch a stack](https://docs.servicenow.com/csh?topicname=cloudmgt-launch-stack.html&version=latest "Launch a stack")
