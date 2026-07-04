---
title: "SAM: Validate Connection fails when configuring Miro Integration profile"
aliases:
  - KB2719199
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2719199
kb_number: KB2719199
last_modified: 2026-04-17
---

## SAM: Validate Connection fails when configuring Miro Integration profile

  

### Issue

When a user validates connection on the Miro Integration profile, using 'Validate Connection' button, the following is presented:   
'Connection validation is not successful. Please check connections and credentials and try again.'

### Symptoms

After clicking on 'Validate connection' on the integration profile, outbound logs corresponding to the same timestamp (on sys\_outbound\_http\_log table) indicate the following error response:

{

"status" : 403,  
"code" : "insufficientPermissions",  
"message" : "Access Denied",  
"type" : "error"  
}

on the API call towards Miro application URL: https://api.miro.com/v2/orgs/<organization\_id>/members?limit=100

(<organization\_id> will correspond to the org id value configured on the customer instance)

### Facts

When you attempt to run a test from Postman using the same 'Bearer' token and the URL associated with the failed outbound log request,  the request fails with the same error.

### Release

Any. 

### Cause

The error indicates that the access is being denied by Miro when calling the API to fetch organization members.

### Resolution

1.  Ensure that minimal user permissions are provided as per the documentation  
    [Docs: Software Asset Management - SaaS License Management Integrate with SaaS applications - Integrating with Miro Enterprise](https://www.servicenow.com/docs/csh?topicname=integrate-with-miro-enterprise.html&version=latest)
2.  Attempt to re-fetch an OAuth token using 'Get OAuth token' from the instance, ensuring that
    1.  on the SSO sign page, you login using the same account/credential that you had configured on Miro portal.
    2.  the step must be executed by a ServiceNow admin, who also has the Company Admin role in Miro application.
3.  If the access continues to be denied on the refreshed token, please reach out to Miro support team for assistance.

### Related Links

[Documentation](https://www.servicenow.com/docs/csh?topicname=integrate-with-miro-enterprise.html&version=latest)
