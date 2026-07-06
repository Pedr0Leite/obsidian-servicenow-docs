---
title: "Why does Cloud Discovery of Azure Australia Central, Australia Central 2 & France South Datacenters fail with 'Failed with status code and message 400 error No registered resource provider found for location and API version' ?"
aliases:
  - KB0695349
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695349
kb_number: KB0695349
last_modified: 2026-05-19
---

## Why does Cloud Discovery of Azure Australia Central, Australia Central 2 & France South Datacenters fail with 'Failed with status code and message 400 error No registered resource provider found for location and API version' ?

  

### Issue

When running Cloud Discovery for Microsoft Azure, below entries might show up in Discovery log:

\> \[location\] Discovery Error  
\> \[location\] Discovery Processing with error  
\> \[location\] -- ITapp Azure Compute Manager.List available hardwares -- Error Level for these entries is Information.

In Cloud API Trail, below might show in error details:

java.lang.RuntimeException: Failed to execute API - Failed with status code and message: 400: {"error":{"code":"NoRegisteredProviderFound","message":"No registered resource provider found for location 'xxx' and API version '2016-03-30' for type 'locations/vmSizes'. The supported api-versions are '2015-05-01-preview, 2015-06-15, 2016-03-30, 2016-04-30-preview, 2016-08-30, 2017-03-30, 2017-12-01, 2018-04-01, 2018-06-01'. The supported locations are 'xxx'....

### Release

This behavior is seen in ServiceNow Jakarta & higher releases. 

### Cause

This is a limitation by Microsoft Azure which is not allowing us to discover Australia Central, Australia Central 2 & France South Azure regions to ensure data residency, sovereignty, compliance. 

Please review the following related documentation from Microsoft Azure : 

[Microsoft: Azure geographies](https://azure.microsoft.com/en-us/global-infrastructure/geographies/)

Australia Central and Australia Central 2 are dedicated to Australian and New Zealand government organizations and partners. 

France South: Reserved for France Central customers requiring in-country disaster recovery. 

### Resolution

You may follow the next procedure to exclude these Azure regions from Cloud Resource Discovery. 

If Cloud Management v2 plugin 'com.snc.cloud.mgmt' is NOT activated :  

1.  Disable the existing Cloud discovery schedules for Azure Service Account.
2.  Open Azure Service Account from Cloud Management > Cloud Infrastructure > Service Account. 
3.  From Logical Datacenter list, Select the regions required to be excluded and Delete them. 
4.  Create new discovery job for the Service Account.

If Cloud Management v2 plugin 'com.snc.cloud.mgmt' is activated : 

1.  Disable the existing Cloud discovery schedules for Azure Service Account.
2.  Access Azure Cloud Account/s, Navigate to Cloud Admin Portal > Manage >  Cloud Accounts
3.  If Azure Cloud Account is 'Published', Change its state to 'Draft'
4.  Delete the affected Azure Regions as illustrated below :   
    ![delete Datacenter from Cloud Account.png](sys_attachment.do?sys_id=8aa01d04470d4f9811eaf24c736d43e3)   
    5\. Publish the Cloud Account.
5.  From Discovery Jobs, Create a new Cloud Resource Discovery Schedule for the Cloud Account.
