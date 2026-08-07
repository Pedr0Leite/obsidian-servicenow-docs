---
title: "[SAMP-SaaS] Salesforce SaaS integration profilefailing with error \"No Valid Salesforce base URL\" and Error 429 – too many requests in logs"
aliases:
  - KB0827989
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827989
kb_number: KB0827989
last_modified: 2024-04-08
---

## \[SAMP-SaaS\] Salesforce SaaS integration profilefailing with error "No Valid Salesforce base URL" and Error 429 – too many requests in logs

  

### Issue

When we run the Salesforce integration profile and its related jobs it might fail with below errors as in below:

"No Valid Salesforce base URL" and Error 429 – too many requests in logs

### Release

All Environments with Software Asset Management Professional

### Cause

Getting the OAuth next token must be broken.

If you check the Salesforce integration profile page, you might see the below error information/error message.

Warning MessageOAuth Access or Refresh tokens are not available. Verify the OAuth configuration and click the 'Get OAuth Token' link below to request a new token.

Error MessageLast refresh failed at 2020-06-05 13:31:20. Check the job logs and have a ServiceNow admin re-run the failed jobs. If the problem persists, the admin should check OAuth credentials and retrieve new tokens.

### Resolution

1) Was the Salesforce app created by an admin account on the Salesforce admin portal?  
2) Make sure that the OAuth setting enabled?  
3) Check if the Client ID and Client Secret correct?  
4) Please try 'Get OAuth Token' and see if you are able to get the token successfully with no issues?  
5) Once you click on the "Get OAuth Token" on the integration profile, it will take you to Salesforce UI and asking for the Username and Password.  
6) Once entered, it will prompt you to provide some access rights for SaaS License Management. And you need to approve the access and the flow should be successful.  
  
If you still see the issues and if possible delete the current related profile and try creating a new [Create a Salesforce integration profile](https://docs.servicenow.com/csh?topicname=create-integration-profile-salesforce.html&version=latest "Create a Salesforce integration profile") from the scratch.
