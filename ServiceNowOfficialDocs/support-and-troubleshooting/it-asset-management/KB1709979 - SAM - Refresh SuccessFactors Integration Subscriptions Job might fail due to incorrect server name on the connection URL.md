---
title: "SAM - Refresh SuccessFactors Integration Subscriptions Job might fail due to incorrect server name on the connection URL"
aliases:
  - KB1709979
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1709979
kb_number: KB1709979
last_modified: 2026-05-19
---

## SAM - Refresh SuccessFactors Integration Subscriptions Job might fail due to incorrect server name on the connection URL

  

### Issue

SAM - Refresh SuccessFactors Integration Subscriptions Job might fail due to incorrect server name on the connection URL 

When you configure a Direct Integration Profile for "SuccessFactors Subscription" and are able to generate Oauth token successfully .But the Scheduled Job " SAM - Refresh SuccessFactors Integration Subscriptions " fails please check the response status for the connection url.

Make sure all steps to configure the SAP SuccessFactors integration with the SuccessFactors Spoke application are finished, 

[https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-successfactors.html](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-successfactors.html)

On the connection URL it states to provide Successfactor instance URL, The instance name refers to " API server" name for OData v2 from below that is used for their SuccessFactors "SuccessFactors\_Instance\_Name" based on location, make sure customer's provide the right one.

[https://help.sap.com/docs/SAP\_SUCCESSFACTORS\_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html%29)

### Symptoms

You would see show 404 response status error with incorrect Successfactor "connection" URL in the http outbound logs.

### Release

All

### Cause

### Resolution

  
\-->Step to Create connection record for the OData API step from the instructions  in the doc below 

[https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-successfactors.html.](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/integrate-with-successfactors.html#title_create-conn-rec-sf%29.)  
  
\-->The instructions suggest using the SuccessFactors instance URL(instance url refers to API server name from SAP appended with odata/v2 as endpoint).

 https://<SuccessFactors\_Instance\_Name>/odata/v2. 

\-->As per SAP documentation for the OData API, found that they have a list of API servers customer can hit. 

[https://help.sap.com/docs/SAP\_SUCCESSFACTORS\_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html.](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/af2b8d5437494b12be88fe374eba75b6.html%29)

\-->If  Customer provided SuccessFactors "Instance" is not in the above list, then you will see request failures leading to job failures

\-->Refer to this above documented list from SAP to find an "API server" for "successfactor\_instance\_url" to be substituted as successfactor instance name in Connection URL for the Create connection record in the OData API step .  
  
  
  
  

### Related Links
