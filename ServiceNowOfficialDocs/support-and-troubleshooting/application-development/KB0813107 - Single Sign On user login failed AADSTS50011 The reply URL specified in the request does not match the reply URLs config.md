---
title: "Single Sign On  user login failed: AADSTS50011: The reply URL specified in the request does not match the reply URLs configured for the application"
aliases:
  - KB0813107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813107
kb_number: KB0813107
last_modified: 2024-04-08
---

## Single Sign On user login failed: AADSTS50011: The reply URL specified in the request does not match the reply URLs configured for the application

  

### Issue

User login fails after redirection from Servicenow instance to Azure (https://login.microsoftonline.com/<id>/login when Multi Provider SSO is configured for Azure.

Message: AADSTS50011: The reply URL specified in the request does not match the reply URLs configured for the application: 'https://<instancename>.service-now.com'.  
  

### Cause

When Active Directory Web app is deployed to Azure error occurs when you have to not added the ServiceNow instance URL to the Azure Active Directory application 

### Resolution

When Active Directory Web app is deployed to Azure, ensure you add ServiceNow URL to the Azure Active Directory application

1.Go to the Azure portal sign in and click on the Azure Active Directory icon on the left. Then click on the ‘App registrations’ icon in the middle pane.  In the search box enter the application from the error message and choose ‘All apps’ from the dropdown.

2.Click on your application, then the Settings icon, select the ‘Reply URLs’ from the list. Paste in the ServiceNow instance URL to name of the URL.

Refer to [Microsoft Documentation](https://docs.microsoft.com/en-us/archive/blogs/jpsanders/azure-app-service-error-aadsts50011-the-reply-address-http-azurewebsites-netsignin-oidc-does-not-match-the-reply-addresses-configured-for-the-application "Microsoft Documentation") for more information.
