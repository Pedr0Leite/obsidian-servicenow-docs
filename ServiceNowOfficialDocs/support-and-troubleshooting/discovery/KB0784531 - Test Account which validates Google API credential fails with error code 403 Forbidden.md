---
title: "\"Test Account\" which validates Google API credential fails with error code 403 Forbidden"
aliases:
  - KB0784531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784531
kb_number: KB0784531
last_modified: 2026-05-22
---

## "Test Account" which validates Google API credential fails with error code 403 Forbidden

  

### Issue

The "Test Account" which validates Google API credential failed with below error while creating a Cloud Discovery schedule from Discovery Manager.

 **"Identification sections in pattern failed: section: GCP Service Account Identification, error: Match step predicate is not matched"**

![](sys_attachment.do?sys_id=442317f0db8c38d066e0a345ca96193e)

-   The exact error is available in the discovery pattern log.   Go to latest Discovery status and open the latest Discovery status job for account validation:
-   The step "Get GCP accounts" in pattern "**Google Cloud Platform (GCP) - Validate Service Account**" fails with Status 403 Forbidden.  
      
    

"Exception occurred while executing operation Cloud REST Query. Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: com.snc.sw.exception.CommandFailureException: Cloud request failed. URL: https://cloudresourcemanager.googleapis.com/v1/projects Status: 403 Response: HttpResponseProxy{HTTP/1.1 **403 Forbidden** \[Vary: X-Origin, Vary: Referer, Content-Type: application/json; charset=UTF-8, Date: Fri, 08 Nov 2019 10:16:03 GMT, Server: ESF, Cache-Control: private, X-XSS-Protection: 0, X-Frame-Options: SAMEORIGIN, X-Content-Type-Options: nosniff, Server-Timing: gfet4t7; dur=613, Alt-Svc: quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000, Accept-Ranges: none, Vary: Origin,Accept-Encoding, Connection: close\] ResponseEntityProxy{\[Content-Type: application/json; charset=UTF-8,Chunked: false\]}} (script\_include:GoogleApiCommand; line 124)."

![](sys_attachment.do?sys_id=c82317f0db8c38d066e0a345ca96193f)

### Release

-   New York

### Cause

-   The "**Cloud Resource Manager API**"  is not enabled in the Google Cloud Console.
-   The discovery pattern "**Google Cloud Platform (GCP) - Validate Service Account**" use the API endpoint "https://cloudresourcemanager.googleapis.com/v1/projects" to validate Google API credential.
-   The "**Cloud Resource Manager API**" should be enabled in Google Cloud console to use this API endpoint.  
    -   **Note : "Cloud Resource Manager API"** needs to be enabled on the project which contains the service account used by ServiceNow discovery.

### Resolution

Follow the below steps to navigate to the "Cloud Resource Manager API" page

1.  Log in to Google Cloud Platform Console   
      
    [https://console.cloud.google.com/](https://console.cloud.google.com/)  
      
    
2.  Make sure to change the project to the one that contains the service account used by ServiceNow discovery.
3.  From Navigation Menu, choose "APIs & Services" and then "Library"  
      
      
              ![](sys_attachment.do?sys_id=c42317f0db8c38d066e0a345ca961942)  
      
      
    
4.  In the API "Library" Page, search for "Cloud resource manager" and then choose "Cloud Resource Manager API"  
      
              ![](sys_attachment.do?sys_id=082317f0db8c38d066e0a345ca961930)  
      
    
5.  Now Click "Enable" to enable the API.  
      
    

![](sys_attachment.do?sys_id=402317f0db8c38d066e0a345ca961941)
