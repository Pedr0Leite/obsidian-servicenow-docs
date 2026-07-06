---
title: "Error during AWS Discovery: AWS was not able to validate the provided access credentials (Service: AmazonEC2; Status Code: 401; Error Code: AuthFailure; Request ID: 12345606-12345-1234-1234-123456789123) "
aliases:
  - KB0749275
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749275
kb_number: KB0749275
last_modified: 2024-04-07
---

## Error during AWS Discovery: AWS was not able to validate the provided access credentials (Service: AmazonEC2; Status Code: 401; Error Code: AuthFailure; Request ID: 12345606-12345-1234-1234-123456789123)

  

### Issue

Cloud AWS Discovery was failing with Authentication errors though it is validated that the given credentials are working good from other instance.

AWS was not able to validate the provided access credentials (Service: AmazonEC2; Status Code: 401; Error Code: AuthFailure; Request ID: 58bd2406-5cdf-4fc3-a83b-a8da9c999d32) 

Below errors in observed in System logs:

\=================

Failure to handle chunked result: com.snc.cloud.mgmt.modules.svccatalog.orchestration.BPOException: AWS was not able to validate the provided access credentials (Service: AmazonEC2; Status Code: 401; Error Code: AuthFailure; Request ID: 58bd2406-5cdf-4fc3-a83b-a8da9c999d32): com.snc.cloud.mgmt.modules.svccatalog.orchestration.result.StepResultHandler.checkCAPIReturnStatus(StepResultHandler.java:263)   
com.snc.cloud.mgmt.modules.svccatalog.orchestration.result.StepResultHandler.validateResult(StepResultHandler.java:164)   
com.snc.cloud.mgmt.modules.svccatalog.orchestration.result.StepResultHandler.process(StepResultHandler.java:92)   
com.snc.cloud.mgmt.modules.svccatalog.service.impl.BlueprintOrchestratorImpl.handleChunkedResult(BlueprintOrchestratorImpl.java:82)   
com.snc.cloud.mgmt.modules.svccatalog.service.impl.CloudOrchestrationServiceImpl.handleChunkCompletion(CloudOrchestrationServiceImpl.java:312)   
com.snc.cloud.mgmt.modules.svccatalog.scriptinterface.BPOrchestratorServiceScript.jsFunction\_handleCAPIResultChunk(BPOrchestratorServiceScript.java:103) 

MID Server agent logs throws the below errors:

\=================

05/18/19 03:43:34 (064) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 Worker starting: APIProxyProbe   
05/18/19 03:43:34 (064) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 dynamicRouteId : admin-433710e6-64be-46f3-b4cc-c02ffc181379   
05/18/19 03:43:34 (080) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 SEVERE \*\*\* ERROR \*\*\* Could not load credentials. Cannot process the request. - 'null'   
05/18/19 03:43:34 (080) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 Route Headers - {credentials=\*\*\*\*\*\*\*\*, identity=\*\*\*\*\*\*\*\*, accountaliasname=$(CloudCredential.Alias), endpoint=, project=\*\*\*\*\*\*\*\*, provider=aws-ec2, cloudoperation=ListDatacenters}   
05/18/19 03:43:34 (080) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 About to start route...   
05/18/19 03:43:34 (333) Camel (camel-1) thread #4 - ProducerTemplate Creating ec2 connection with params, identity '$(CloudCredential.access\_key)', region 'null'   
05/18/19 03:43:34 (341) Camel (camel-1) thread #4 - ProducerTemplate \*\*\* Script: Creating AWS API Client for : ec2   
05/18/19 03:43:35 (941) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 SEVERE \*\*\* ERROR \*\*\* Could not complete API call AWS was not able to validate the provided access credentials (Service: AmazonEC2; Status Code: 401; Error Code: AuthFailure; Request ID: 771fad75-b67a-4ffa-b105-9d5e01a387c9)   
05/18/19 03:43:35 (941) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 Enqueuing: C:\\midserver\\rbmadriditom\\agent\\work\\monitors\\ECCSender\\output\_0\\ecc\_queue.377a4228db21b3006f10764cbf961996.xml   
05/18/19 03:43:35 (957) Worker-Interactive:APIProxyProbe-377a4228db21b3006f10764cbf961996 Worker completed: APIProxyProbe time: 0:00:01.877 

### Release

This issue is observed in London and Madrid releases.

### Cause

The cause of the error is unclear at this point in time. It seems like one or more configured credentials which are already present in the credentials table is causing the problem.

### Resolution

Please remove all the configured credentials from the ServiceNow Instance and try to add the AWS credentials first. 

See if the discovery goes good. After you confirm that AWS discovery is successful, then you can add other credentials one after the other.
