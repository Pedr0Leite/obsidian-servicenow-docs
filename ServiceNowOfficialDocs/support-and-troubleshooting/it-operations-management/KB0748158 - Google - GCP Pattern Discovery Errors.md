---
title: "Google - GCP Pattern Discovery Errors  "
aliases:
  - KB0748158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748158
kb_number: KB0748158
last_modified: 2024-04-07
---

## Google - GCP Pattern Discovery Errors

  

### Issue

# Overview

Google Cloud Platform (GCP) Discovery patters available at ServiceNow Store, installing/configuring the GCP Serverless Pattern: [Google Cloud Platform discovery](https://docs.servicenow.com/csh?topicname=gcp-cloud-discovery.html&version=latest "Google Cloud Platform discovery") 

-   Below are the available patterns for Discovery.
    -   Google Cloud Platform (GCP) - Storage
    -   Google Cloud Platform (GCP) - Virtual Server
    -   Google Cloud Platform (GCP) - Disk Types
    -   Google Cloud Platform (GCP) - External IP Addresses
    -   Google Cloud Platform (GCP) - Load Balancer - HTTP
    -   Google Cloud Platform (GCP) - Load Balancer - TCP - UDP
    -   Google Cloud Platform (GCP) - Logical Datacenters
    -   Google Cloud Platform (GCP) - Networking
    -   Google Cloud Platform (GCP) - SSH Keys  
          
        
-   User/Admin can choose either all the above patterns or specific pattern to be active as per the requirement. 

# Issue / Error

-   The GCP Discovery pattern fails with below error 

2019-04-29 06:29:15: Exception occurred while executing operation Cloud REST Query. Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: com.snc.sw.exception.CommandFailureException:   
Cloud request failed. URL: https://www.googleapis.com/compute/v1/projects/GCP/regions?maxResults=500 Status: 400 Response: HTTP/1.1 400 Bad Request \[Vary: X-Origin, Content-Type: application/json; charset=UTF-8, 

# Release

-   As per the Documentation, GCP discovery is supported from London P7 and Madrid P2

# Environment

-   Instance installed with the application "Discovery and Service Mapping Patterns"

# Cause

-   The pattern failure because of mismatch in the GCP Credentials.

# Resolution

-   Configuring GCP API Credentials needs below information.

"https://<Instancename>.service-now.com/gcp\_credentials.do"

-   -   Client\_email  = Email 
    -   Secret\_Key   = Secret Key  
          
        
-   Above both of the details will be populated while creating the ServiceAccount in GCP and the output of JSON will be as below 

{
  "type": "service\_account",
  "project\_id": "_project-id_",
  "private\_key\_id": "_some\_number_",
  "**private\_key**": "-----BEGIN PRIVATE KEY-----\\n....
  =\\n-----END PRIVATE KEY-----\\n",
  "**client\_email**": "<api-name>api@_project-id_.iam.gserviceaccount.com",
  "client\_id": "...",
  "auth\_uri": "https://accounts.google.com/o/oauth2/auth",
  "token\_uri": "https://accounts.google.com/o/oauth2/token",
  "auth\_provider\_x509\_cert\_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client\_x509\_cert\_url": "https://www.googleapis.com/...<api-name>api%40_project-id_.iam.gserviceaccount.com"
}

-   From the above output of JSON, we need "Private\_Key" and "Client\_Email" 

-   Configuring GCP ServiceAccount needs below information.

"https://<Instancename>.service-now.com/cmdb\_ci\_cloud\_service\_account.do"

-   -   Account ID = Project name 
    -   Credentials = Which we created as above (GCP API)
    -   Datacenter = Always "cmdb\_ci\_google\_datacenter" 

-   The Account ID is the Project name, while creating a ServiceAccount for "Private\_Key" and "Client\_Email" it initially requests on which Project user wanted to create.
-   The Credentials we must have created for the Project name since the reason the Project name will not be available in above JSON
-   Admin need to validate the credentials with project name with project ID provided in the JSON 

-   Configuring GCP Patterns at Serverless discovery.

https://<instacnename>.service-now.com/discovery\_schedule\_list.do?sysparm\_query=discover%3DHostless&sysparm\_first\_row=1&sysparm\_view=

-   Navigator >> Discovery Schedule >> GCP Serverless Schedule >> Serverless Execution Patterns 

![](/sys_attachment.do?sys_id=218e3862db0ab450e515c223059619d3)

-   Open any of the patterns as above, observe the fields to fill under "Discovery Pattern Launcher Parameters" 

![](/sys_attachment.do?sys_id=258e3862db0ab450e515c223059619d8)

-   Fill the Value for the Parameter accurately, please note the Values are case sensitive. 

# Additional Information

-   Refer: [Authenticating to a Cloud API Service](https://cloud.google.com/video-intelligence/docs/common/auth "Authenticating to a Cloud API Service")
-   Communicate with GCP admin to get all the required information
