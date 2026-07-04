---
title: "'SAM - Import User Subscriptions' job failing with error: No valid bindings were found for organization and technical account combination"
aliases:
  - KB1360341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1360341
kb_number: KB1360341
last_modified: 2026-05-29
---

## 'SAM - Import User Subscriptions' job failing with error: No valid bindings were found for organization and technical account combination

  

### Summary

Scheduled Job 'SAM - Import User Subscriptions' failing with error: No valid bindings were found for organization and technical account combination

System Log:-

Error Error: SamImportUserSubscriptionsAdobe: Failed to run job. Please look into logs for more details. SAM:SAM - Import User Subscriptions

Error SAM:SAM - Import User Subscriptions: Error: SamImportUserSubscriptionsAdobe: Failed to run job. Please look into logs for more details.: no thrown error com.glide.ui.ServletErrorListener

Error SamImportUserSubscriptionsAdobe: Error: SampAdobeAdminUnhandled exception for profile : b7e87f02db0e9090b34a8f3813961910 : Error: {"error\_description":"No valid bindings were found for organization and technical account combination","error":"invalid\_token"} \*\*\* Script

### Release

SAMP Plugin 

### Instructions

**Solution Proposed:**

  
It's an issue with the adobe integration setup. Check with Adobe Admin or Adobe Support team on this and the below links provide more details about the error message:  
  
[https://helpx.adobe.com/enterprise/kb/UMAPI-UST.html](https://helpx.adobe.com/enterprise/kb/UMAPI-UST.html)  
[https://experienceleaguecommunities.adobe.com/t5/adobe-target-discussions/jwt-generated-by-adobe-is-an-invalid-jwt/td-p/280321](https://experienceleaguecommunities.adobe.com/t5/adobe-target-discussions/jwt-generated-by-adobe-is-an-invalid-jwt/td-p/280321)  
  
a) This can be caused because the tech\_acct value inside connector-umapi.yml file corresponds to other value than technical account ID inside the integration at [https://console.adobe.io](https://console.adobe.io) . Doublecheck the technical account ID value from the current integration and copy it inside this file  
  
b) This can also be caused because the public certificate from the integration is expired; renew the private and public key, then re-upload the public key, then replace the old private key with the new generated one. Doublecheck the path inside connector-umapi.yml file to point to teh right file  
  
c) check if the Integration is made for the correct Organization; first select the Organization inside the drop down menu located in the top left corner at [https://console.adobe.io/integrations](https://console.adobe.io/integrations), then doublecheck the technical account ID value for the active integration along with the other metadata (Org ID, secret, client ID...)
