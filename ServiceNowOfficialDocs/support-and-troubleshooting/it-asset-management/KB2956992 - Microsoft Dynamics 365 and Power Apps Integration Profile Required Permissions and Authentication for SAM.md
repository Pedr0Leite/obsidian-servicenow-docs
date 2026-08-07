---
title: "Microsoft Dynamics 365 and Power Apps Integration Profile: Required Permissions and Authentication for SAM"
aliases:
  - KB2956992
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2956992
kb_number: KB2956992
last_modified: 2026-05-26
---

## Issue

  
When setting up the Microsoft Dynamics 365 and Power Apps Integration Profile in ServiceNow Software Asset Management (SAM), it is unclear which permissions are required, why the Global Reader role is needed, and whether the integration uses a user's token or an application registration's service principal for authentication.

## Resolution

**Steps to Resolve**  
1\. Global Reader role is required for downloading subscriptions, as noted in the documentation.

2\. Note that the documentation contains a typo, stating 'Global Administrator' instead of 'Global Reader' in the step for creating and getting an OAuth token.Doc request submitted by development team to correct it 

 .Select Create and Get OAuth Token.  
Important:  
This step must be executed by a user with the Global administrator role in the Microsoft admin center.  
  
[https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html)

3\. The user performing the 'Get OAuth Token' step must have the Global Reader role, and this is a one-time requirement.

4\. Subsequent integration flows use the retrieved token, not the user's credentials.

5\. For Application permissions, ensure the application is granted 'LicenseAssignment.Read.All' and 'User.Read.All' permissions on the Microsoft Entra ID portal. 

6\. If activity data is not required, uncheck the 'Download Activity' option in the integration profile.

7.IF customer is using Delegated permissions, then ServiceNow will retrieve the token of the user, and that requires a user with the Global Reader Role?  
  
8.If customer is using Application permissions, then ServiceNow leverages the configured app credentials (client secret) to obtain a token on behalf of the application itself    
For this customer just need to assign the LicenseAssignment.Read.All and User.Read.All permission assigned to the application on the Microsoft Entra ID portal to pull users

9\. Please note that if customer intend to pull activity data, the only available permission from Microsoft for this is user\_impersonation from Dynamics CRM, which is a delegated permission. Hence, the user fetching the token for the connection and credential associated with the Activity flow in the profile would need to have the Dynamics Administrator role in the Power Platform.  
If activity data is not required, customer can simply uncheck the Download Activity option in the integration profile.
