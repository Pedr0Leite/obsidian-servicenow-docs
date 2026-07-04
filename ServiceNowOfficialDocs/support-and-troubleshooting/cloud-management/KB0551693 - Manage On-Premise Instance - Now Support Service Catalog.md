---
title: "Manage On-Premise Instance - Now Support Service Catalog"
aliases:
  - KB0551693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551693
kb_number: KB0551693
last_modified: 2026-05-13
---

## Issue

The **Manage On-Premise Instance** catalog can be used by our on-premise customers to **register** or **update** or **retire** their instance information in Now Support CMDB.

### Target User

**Manage On-Premise Instance** is available to users with the customer\_admin OR partner\_admin role only. This is only applicable to our self-hosted/on-premise customers. 

### Procedure

Use the steps in this section to register or update an On-Premise instance on Now Support. If you need to make any modifications to the registration request (such as changing the **Used For** field) after you submit the request, click the **Cancel** button and submit a new request. This catalog doesn't update the Instance ID field which is unique. if you need to update the Instance ID of the On-Prem instance, please reach out to Support with a Case.

Login to [Now Support](https://support.servicenow.com)[](https://support.servicenow.com/)

For regulated Market Support

-   GCC :  [https://hiwave.servicenowservices.com](https://hiwave.servicenowservices.com/)
-   NSC :  [https://hifive.servicenowcloud.mil](https://hifive.servicenowcloud.mil/)

1.  Click **Service Catalog**
2.  Click **Manage On-Premise Instance**.  
      
    ![Manage On-Premise Instance catalog form to fill out](/sys_attachment.do?sys_id=c46ce2da933062905736b25d6cba10b5)
3.  In **Company**, type the company name.
4.  In **Used For**, click the drop-down and select what is appropriate.
5.  In **Stats Page**, provide the following information.  
    The easiest method of obtaining this information is to copy/paste the instance stats.do (https://<instance-name>/stats.do).  
    -   Build date
    -   Build tag
    -   Instance name
    -   Instance Id (instance IDs are unique and cannot be reused)  
          
        Sample input values would look like below:  
        ![Sample input values for Stats page](sys_attachment.do?sys_id=c86ce2da933062905736b25d6cba10b7)
6.  Validations performed on the entered stats page  
    -   If any of the 4 fields mentioned above are not provided, you cannot submit the request
    -   If an existing instance ID is provided in the stats page, the catalog will look for any name or assigned version changes to the instance, if not, an error is thrown to the user and the catalog cannot be submitted  
          
        
7.  Click **Submit**.
8.  A change request is created that contains the link to the newly created/updated instance record  
      
    ![Instance record that is created; Change form](sys_attachment.do?sys_id=735ca2da933062905736b25d6cba1084)  
      
    ![Link to the created Instance Record](sys_attachment.do?sys_id=c46ca2da933062905736b25d6cba1086)

## Resolution

Use the Catalog to update the On-Prem instance
