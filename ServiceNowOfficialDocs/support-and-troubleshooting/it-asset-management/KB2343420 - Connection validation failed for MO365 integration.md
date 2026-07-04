---
title: "Connection validation failed for MO365 integration "
aliases:
  - KB2343420
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2343420
kb_number: KB2343420
last_modified: 2025-09-06
---

## Issue

When customer is trying to perform the integartion with the M365 using the below DOC, they might face an Error like "Connection validation failed" when they performing the Test connection. 

Integrating with Microsoft 365: [https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html)

## Resolution

Customer must allow service principals to call Power BI APIs by toggling the required setting in the Power BI Admin Portal:  
  
Step 1: Open Power BI Admin Portal  
\* Navigate to: [https://app.powerbi.com/admin-portal](https://app.powerbi.com/admin-portal)  
  
Step 2: Enable Required Setting  
\* Go to Tenant settings → under Developer settings  
\* Find: Allow service principals to use Power BI APIs  
\* Set this to Enabled  
  
Step 3: Restrict if Needed  
\* If you restrict it to a specific security group, make sure your Service Principal (App Registration) is a member of that group in Azure AD.  
  
Step 4: Save Changes and Retry  
\* After saving, retry your Test Connection in ServiceNow.

## Additional Information

Please refer to the DOC: [https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/task/enable-service-principal-authentication-microsoft.html](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/task/enable-service-principal-authentication-microsoft.html)  
  
NOTE we have recent **PRB1911342** which says that "**Power BI user activity is optional but it becomes mandatory**". 

  
With the Y release, a new "Validate the Connection" option was introduced when integrating with Microsoft 365. When a user selects the "Download Activity" option, the system now attempts to validate the connection to Power BI using the endpoint: [https://api.powerbi.com/v1.0/myorg/admin/activityevents](https://api.powerbi.com/v1.0/myorg/admin/activityevents).

Prior to the Y release, configuring Power BI was optional, however, with the latest release, Power BI validation appears to have become mandatory, which is not the intended behaviour. 

Currently, if the Power BI API call fails during connection validation, it prevents the execution of any activity-related jobs. This is because the system treats a failure in any of the activity APIs—such as the Reports API or the Power BI API—as a complete validation failure, thereby blocking all related jobs.
