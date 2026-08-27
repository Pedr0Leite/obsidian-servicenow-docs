---
title: "Determining why a Service Catalog Workflow is not invoked correctly by Requests"
aliases:
  - KB0547109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547109
kb_number: KB0547109
last_modified: 2024-04-30
---

## Issue

Catalog item does not fire off the workflow needed

  
Description  

* * *

Requesting a service catalog item causes no or incorrect workflow to be invoked.

Symptoms

* * *

Symptoms may include the following:  

-   No workflow is invoked.
-   An incorrect workflow is invoked. 

Resolution

* * *

The process for invoking service catalog workflows involves:

1.  When a user orders a catalog item, this creates both a Request and a Requested Item for that item.   
    There are two workflows:  
     - The Request workflow, which always runs when a service catalog request is made, regardless of what item was ordered. The Request workflow is the workflow associated with the Request \[sc\_request\] table:  
      
    ![](/sys_attachment.do?sys_id=191b682adb42b450e515c2230596196f)  
      
      
     - The Requested Item workflow, which runs against each requested item in the request. Requested Item workflows are associated with a specific [catalog item](https://docs.servicenow.com/csh?topicname=c_IntroductionToCatalogItems.html&version=latest "catalog item"):  
      
    ![](/sys_attachment.do?sys_id=991b682adb42b450e515c22305961981)  
      
      
    
2.  The Request workflow starts immediately, as soon as the item is ordered. 
3.  The Requested Item workflow starts on approval of the request (when the [Stage field](https://docs.servicenow.com/csh?topicname=r_StageFields.html&version=latest "Stage field") value of the Requested Item changes from **Waiting for Approval** to **Approved**).

Determine whether any of the troubleshooting steps below are true for your environment:

-   [Review the context](https://docs.servicenow.com/csh?topicname=r_AdministeringWorkflowContexts.html&version=latest "Review the context") of the Request workflow. If the Requested Item workflow has not started, this may be due to an issue with the Request workflow.
-   Ensure that you associate the workflow with the requested item \[sc\_req\_item\], not with the request.
-   Check that you have not changed (either manually or otherwise) the default value of the **Stage** field on the Requested Item, which may prevent the workflow from being invoked.
