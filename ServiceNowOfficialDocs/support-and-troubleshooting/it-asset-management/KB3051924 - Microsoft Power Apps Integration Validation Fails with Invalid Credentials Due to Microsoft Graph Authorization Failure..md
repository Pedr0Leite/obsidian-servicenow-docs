---
title: "Microsoft Power Apps Integration Validation Fails with \"Invalid Credentials\" Due to Microsoft Graph Authorization Failure. Error: 403 Authorization_RequestDenied"
aliases:
  - KB3051924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3051924
kb_number: KB3051924
last_modified: 2026-05-30
---

## Microsoft Power Apps Integration Validation Fails with "Invalid Credentials" Due to Microsoft Graph Authorization Failure. Error: 403 Authorization\_RequestDenied

  

### Issue

When validating the Microsoft Dynamics 365 and Power Apps Subscription integration profile in SaaS License Management, the profile may fail with the message:

**Connection validation is not successful. Invalid Credentials.  
  
**

However, this message can be misleading. In this scenario, OAuth token generation was successful, but the backend Microsoft Graph API call failed during subscription download validation.  
  

The failing call was:

GET [https://graph.microsoft.com/v1.0/subscribedSKUs](https://graph.microsoft.com/v1.0/subscribedSKUs)  
Response status: 403

  
The Microsoft Graph response was:

{  
  "error": {  
    "code": "Authorization\_RequestDenied",  
    "message": "Insufficient privileges to complete the operation."  
  }  
}  
  

This confirms that the issue is not caused by an incorrect Client ID, Client Secret, or Tenant ID. The credentials are accepted, but the generated token does not have sufficient authorization to execute the Microsoft Graph API call required by the integration.

### Release

ALL

### Cause

The integration validation fails because the Azure app registration or delegated user context does not have the required Microsoft Graph permissions and/or admin consent required to access:

[https://graph.microsoft.com/v1.0/subscribedSKUs](https://graph.microsoft.com/v1.0/subscribedSKUs)  
  

The ServiceNow UI displays a generic “Invalid Credentials” message, but the outbound HTTP log confirms the actual failure is:

**403 Authorization\_RequestDenied**

**The above Error can be seen in the System Outbound HTTP logs. Please set the properties "glide.outbound\_http\_log.override" to TRUE and "glide.outbound\_http\_log.override.level" to value "all.   
  
[https://www.servicenow.com/docs/r/xanadu/api-reference/web-services/outbound-logging-properties.html](https://www.servicenow.com/docs/r/xanadu/api-reference/web-services/outbound-logging-properties.html)  
**  
Insufficient privileges to complete the operation. This can occur when one or more of the following are missing or not consented in Azure:

LicenseAssignment.Read.All  
User.Read.All  
Organization.Read.All  
Offline\_access

  
For delegated access, the Microsoft account used to generate the OAuth token must also have the required Microsoft Entra role context, such as Global Reader, Directory Readers, or another supported role required for the subscribedSKUs API.

### Resolution

Ask the Microsoft/Azure administrator to review the Azure app registration used by the ServiceNow Microsoft 365 Graph connection and confirm the following:  
  

1.  Add or verify the required Microsoft Graph API permissions:

**LicenseAssignment.Read.All**  
**User.Read.All**  
**Organization.Read.All**  
**Offline\_access  
  
**

1.  Select Grant admin consent for the tenant after adding or correcting the permissions.
2.  If delegated permissions are used, confirm that the user account used to create and retrieve the OAuth token has the required Microsoft Entra role context.  
      
    
3.  Verify the Dynamics CRM side of the configuration as well, especially:

user\_impersonation  
  

1.  In ServiceNow, regenerate the OAuth token for the Microsoft 365 Graph connection.  
      
    
2.  Return to the Microsoft Dynamics 365 and Power Apps Subscription integration profile and click Validate Connection again.

  
Expected result after the fix:

GET [https://graph.microsoft.com/v1.0/subscribedSKUs](https://graph.microsoft.com/v1.0/subscribedSKUs)  
Response status: 200

  
Once the required permissions are granted and admin consent is applied, the integration profile validation should complete successfully.
