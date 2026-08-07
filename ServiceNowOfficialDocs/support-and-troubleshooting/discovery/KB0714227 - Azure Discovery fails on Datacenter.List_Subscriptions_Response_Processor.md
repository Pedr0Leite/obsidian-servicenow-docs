---
title: "Azure Discovery fails on  Datacenter.List_Subscriptions_Response_Processor"
aliases:
  - KB0714227
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714227
kb_number: KB0714227
last_modified: 2024-04-07
---

## Issue

# Description

* * *

Azure Discovery fails on  Datacenter.List\_Subscriptions\_Response\_Processor, with below error.

![](sys_attachment.do?sys_id=da8ca4aedb42b450e515c2230596195f)

Error: **Discovery Subscription Error: Error executing translator script: Azure Datacenter.List\_Subscriptions\_Response\_Processor**

# Applicable Versions

* * *

 Jakarta P\* Kingston P\* 

# Cause

* * *

Review MID server Logs the Discovery could able to capture the Subscription ID and the location ID but not getting updated 

01/01/18 14:08:44 (421) Worker-Interactive:APIProxyProbe Received route response : {"value":\[{"id":"**/subscriptions/0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx/locations/eastasia**","name":"eastasia","displayName":"East Asia","longitude":"114.188","latitude":"22.267"},  
  
                                                                                             {"id":"**/subscriptions/0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx/locations/southeastasia**","name":"southeastasia","displayName":"Southeast Asia","longitude":"103.833","latitude":"1.283"},  
  
                                                                                             {"id":"**/subscriptions/0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx/locations/centralus"**,"name":"centralus","displayName":"Central US","longitude":"-93.6208","latitude":"41.5908"},  
  
                                                                                             {"id":"**/subscriptions/0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx/locations/eastus**","name":"eastus","displayName":"East US","longitude":"-79.8164","latitude":"37.3719"}  etc...  
  

Orchestration Trails for IRE (Identification Reconciliation Engine) failure on Computer.Interface 

"Error identification\_engine : **INVALID\_INPUT\_DATA In payload invalid data source \[ServiceNow\]** exist  
  
{"interfaceName":"Compute Interface","provider":"azure-compute","methodName":"ListDatacenters","credentialName":null,"credentialId":"f8bc593edba463045a9473d78c961967","  
  
apiAliasName":"ITapp Azure Compute Manager.List all Datacenters","version":"1.0","type":"CAPI","invokedBy":null,"cloudServiceAccount":"**0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx**",  
  
"ldc":null,"ldcId":null,"ldcObjectId":null,"endpointURL":null,"correlationId":null,"invocationInitiator":"Azure Datacenter","immediateInvocator":  
  
"Azure Datacenter","invocatingNode":{"cloudAccount":null,"location":null,"resourceName":"Azure Datacenter","alias":"Azure Datacenter","ciInstanceId":null,"ciTypeId":null,"parentResourceAlias":null,  
  
"isProvisioned":false,"qdr":false},"enclosingExpression":null,"parameters":\[{"key":"SubscriptionID","value":"**0xaxbbbx-xefd-xffe-xxxd-xxcxxxxbdxxx**"}\],"translators": 

While the discovery happens the probes could able to capture the Subscription ID from the Azure Datacenters, but the IRE is failing to write to the cmdb\_ci table because of the missing **"Discovery Source"** in dictionary entries.

Accidentally or due to some third-party integrations (SCCM),  choice list item 'ServiceNow' for element discovery\_source is removed or renamed from the system. OOB 'ServiceNow' choice exists for discovery source. I could see 'Service-now' in the customer instance but not 'ServiceNow'.  

# Solution 

* * *

 Please make sure 'ServiceNow' is there among the list of discovery sources or use another existing discovery source when sending the payload to IRE.

-   Login to Instance
-   Navigate to cmdb\_ci (cmdb\_ci\_list.do) 

https://<instance-name>.service-now.com/cmdb\_ci\_list.do?sysparm\_list\_mode=grid&sysparm\_query=&sysparm\_offset=

-   Table Configure > Dictonary Entries 

https://<instance-name>.service-now.com/sys\_dictionary\_list.do?sysparm\_domain\_restore=false&sysparm\_query=name%3Dcmdb\_ci&sysparm\_referring\_url=&sysparm\_list\_mode=grid&sysparm\_offset=

-   Dictionary Entries > Search for "discovery\_source" in "Column name" and open the record 

https://<instance-name>.service-now.com/sys\_dictionary.do?sys\_id=1f6368e6db002300ec9d5f135e961944&sysparm\_record\_list=name=cmdb\_ci^elementLIKEsource^ORDERBYname&sysparm\_record\_target=sys\_dictionary&sysparm\_record\_row=1&sysparm\_record\_rows=1

-   Related List > Choices > Verify the Lables > OOB there should be an Source for "ServiceNow" > If there is no Source with Lable "ServiceNow" > Create a choice with label "ServiceNow" with Value "ServiceNow" 

https://<instance-name>.service-now.com/sys\_choice.do?sys\_id=-1&sys\_is\_list=true&sys\_is\_related\_list=true&sys\_target=sys\_choice&sysparm\_checked\_items=&sysparm\_collection=sys\_dictionary&sysparm\_collectionID=1f6368e6db002300ec9d5f135e961944&sysparm\_collection\_key=&sysparm\_collection\_label=Choices&sysparm\_collection\_related\_field=&sysparm\_collection\_related\_file=&sysparm\_collection\_relationship=9355cd9b0a000704053ea63b163e74b9&sysparm\_fixed\_query=&sysparm\_group\_sort=&sysparm\_list\_css=&sysparm\_query=&sysparm\_referring\_url=/sys\_dictionary.do%3fsys\_id%3d1f6368e6db002300ec9d5f135e961944%26sysparm\_record\_list%3dname%3dcmdb\_ci%5eelementLIKEsource%5eORDERBYname%26sysparm\_record\_target%3dsys\_dictionary%26sysparm\_record\_row%3d1%26sysparm\_record\_rows%3d1&sysparm\_target=&sysparm\_view=

-   Execute Discovery and verify the results
