---
title: "Azure Service Principal Credential verifcation from command line (CLI) "
aliases:
  - KB0723531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723531
kb_number: KB0723531
last_modified: 2025-10-09
---

## Azure Service Principal Credential verifcation from command line (CLI)

  

### Issue

# Contents

* * *

1.  [Overview](#OVERVIEW)
2.  [Common Error](#HEADING_2)
3.  [Cause](#HEADING_3)
4.  [Prerequisite](#HEADING_4)
5.  [Verification](#VERIFICATION)
6.  [Additional Information](#ADDITIONAL_RESOURCES)

# 1\. Overview

* * *

There are situations where the Azure Discovery fails with multiple errors and it goes difficult to understand where the issue is from, it could be Azure Credential, ServiceNow Cloud API, MID server or any other reasons, this article will demonstrate to verify the Azure credentials from Command line to narrow down the issue.

# 2\. Common Errors

* * *

Failed to execute API - Failed with status code and message: 403: {"error":{"code":"AuthorizationFailed","message":  
"The client '572864c1-e43f-43b3-8770-d51eaa7db603' with object id '572864c1-e43f-43b3-8770-d51eaa7db603' does not have authorization to perform action   
'Microsoft.Resources/subscriptions/locations/read' over scope '/subscriptions/51da9d66-1794-405e-b15f-6d9838208edd'."}} (script\_include:CloudRESTAPIInvoker; line 122)

java.lang.IllegalArgumentException: Invalid uri 'https://management.azure.com/subscriptions/ 6d1fadd8-05a4-4b22-9dec-5e7ca49f8674/resourcegroups?api-version=2015-01-01':   
escaped absolute path not valid", which says the subscription is invalid, and couldn't recognise it for discovery. 

Custom operation Cloud REST - add response to context failed to execute script due to Custom operation Failed to run script due to the following error: JAVASCRIPT\_CODE\_FAILURE: com.snc.sw.exception.CommandFailureException: Failed to execute cloud request. Reason: SSLHandshakeException:PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target (script\_include:AzureApiCommand; line 58). Check the discovery logs for more details.

# 3\. Cause

* * *

-   The Secret Key might be expired 
-   The Secret key associated with the Application Id is not matching 
-   Unknown Application ID and Secret Key 
-   The User with the Subscription ID have no access or no Reader roles 

# 4\. Prerequisite 

* * *

As mentioned in our documentation ([Create a service account for Azure](https://docs.servicenow.com/csh?topicname=azure-service-account-cloud-mgt.html&version=latest "\"Create a service account for Azure\"")), to configure the Azure credentials and Service Principal, you will need: 

-   Directory ID
-   Application ID
-   Application Key
-   Subscription ID

Subscription ID is used while configuring the Service Principal and other used for Azure Credentials, the customer might have Parent subscription ID and multiple Application ID along with Application Key. 

# 5\. Verification

* * *

**Note:** Once the Credentials are saved in the ServiceNow Credentials table, the provided secret key is not visible and it will not be possible to know, the customer needs to have all the information handy for verification.

-   Log in to Azure cloud Shell (If not available, customer needs to install)

![](/sys_attachment.do?sys_id=7b0d82e31bab01509f20ece7624bcb0b)

-   Keep the APP\_ID handy and copy, execute command "az role assignment list --assignee APP\_ID"

![](/sys_attachment.do?sys_id=2f0d82e31bab01509f20ece7624bcb08)

-   Command returned no output which means there are no roles provided to the APP\_ID

![](/sys_attachment.do?sys_id=b30d82e31bab01509f20ece7624bcb0d)

-   Command returned output with some result and we can see the "Reader" role provided to the APP\_ID

# 6\. Additional information

* * *

-   [Create an Azure service principal with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest "Create an Azure service principal with Azure CLI") \[Microsoft\]
