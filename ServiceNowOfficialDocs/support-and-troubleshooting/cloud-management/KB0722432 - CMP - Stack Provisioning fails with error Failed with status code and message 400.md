---
title: "CMP - Stack Provisioning fails with error \"Failed with status code and message: 400\""
aliases:
  - KB0722432
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722432
kb_number: KB0722432
last_modified: 2024-01-28
---

## CMP - Stack Provisioning fails with error "Failed with status code and message: 400"

  

### Issue

#  Symptoms

* * *

Cloud Management Platform, Stack Provisioning fails with below error when the Catalog item/Blueprint  created from **CFT (CloudFormation Template)** 

  
**Error Detail from CAPI**   
  
java.lang.RuntimeException: **Failed to execute API - Failed with status code and message: 400**: <?xml version="1.0" encoding="UTF-8"?>  
<Error><Code>XAmzContentSHA256Mismatch</Code><Message>The provided 'x-amz-content-sha256' header does not match what was computed.</Message><ClientComputedContentSHA256>89d57bc62e30081f7b4d5367fc51ea4afa58f2f3a0a70e56d1b0feaa65fb1229</ClientComputedContentSHA256><S3ComputedContentSHA256>0b55a3737003658da1ba8d61cf4a2840b2f210e442b15519555474a36d589526</S3ComputedContentSHA256><RequestId>BD30EB678201A852</RequestId><HostId>2anYA+PBX6niXqupxKBBuDKm3HRG268eKw8lrJ6nXwAr/dAYqC4lGB16416Q4dMDeCbhUzdu1w8=</HostId></Error> (script\_include:CloudRESTAPIInvoker; line 125)  
at com.snc.cmp.connector.cloud.script.js.JavaScriptProducer.process(JavaScriptProducer.java:57)  
at org.apache.camel.util.AsyncProcessorConverterHelper$ProcessorToAsyncProcessorBridge.process(AsyncProcessorConverterHelper.java:61)  
at org.apache.camel.processor.SendProcessor.process(SendProcessor.java:145)  
at org.apache.camel.management.InstrumentationProcessor.process(InstrumentationProcessor.java:77)  
at org.apache.camel.processor.RedeliveryErrorHandler.process(RedeliveryErrorHandler.java:468)  
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)  
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)  
at org.apache.camel.component.direct.DirectProducer.process(DirectProducer.java:62)  
at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:190)  
at org.apache.camel.util.AsyncProcessorHelper.process(AsyncProcessorHelper.java:109)  
at org.apache.camel.processor.UnitOfWorkProducer.process(UnitOfWorkProducer.java:68)  
at org.apache.camel.impl.ProducerCache$2.doInProducer(ProducerCache.java:412)  
at org.apache.camel.impl.ProducerCache$2.doInProducer(ProducerCache.java:380)  
at org.apache.camel.impl.ProducerCache.doInProducer(ProducerCache.java:270)  
at org.apache.camel.impl.ProducerCache.sendExchange(ProducerCache.java:380)  
at org.apache.camel.impl.ProducerCache.send(ProducerCache.java:238)  
at org.apache.camel.impl.DefaultProducerTemplate.send(DefaultProducerTemplate.java:128)  
at org.apache.camel.impl.DefaultProducerTemplate.sendBodyAndHeaders(DefaultProducerTemplate.java:253)  
at org.apache.camel.impl.DefaultProducerTemplate.requestBodyAndHeaders(DefaultProducerTemplate.java:313)  
at org.apache.camel.impl.DefaultProducerTemplate$10.call(DefaultProducerTemplate.java:588)  
at java.util.concurrent.FutureTask.run(FutureTask.java:266)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)

  
**Route Error from CAPI**   
  
java.lang.RuntimeException: **Failed to execute API - Failed with status code and message: 403**: <ErrorResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">  
<Error>  
<Type>Sender</Type>  
<Code>AccessDenied</Code>  
<Message>User: arn:aws:iam::696619222101:user/aalabs-dev-ServiceNow-user is not authorized to perform: cloudformation:CreateStack on resource: arn:aws:cloudformation:ap-southeast-2:696619222101:stack/aalabs-staging-lablab97620190103151302805/\*</Message>  
</Error>  
<RequestId>19c02be9-0efd-11e9-b3c6-636b75993c08</RequestId>  
</ErrorResponse>  
(script\_include:CloudRESTAPIInvoker; line 125)  
at com.snc.cmp.connector.cloud.script.js.JavaScriptProducer.process(JavaScriptProducer.java:57)  
at org.apache.camel.util.AsyncProcessorConverterHelper$ProcessorToAsyncProcessorBridge.process(AsyncProcessorConverterHelper.java:61)  
at org.apache.camel.processor.SendProcessor.process(SendProcessor.java:145)  
 

# Environment

* * *

Kingston P\* & London P\* using **AWS CFT**

# Steps to Reproduce 

* * *

-   Login to the instance
-   Create a Cloud Formation Template ([Use an AWS CloudFormation template](https://docs.servicenow.com/csh?topicname=resource-blocks.html&version=latest "Use an AWS CloudFormation template")) 
-   Try creating the Template using attached "CFT-Example\_Error"
-   Navigate to Cloud User Portal >> Launch a Stack >> Verify the newly created catalog item from the CFT >> Launch 
-   Provide information as per the "General info" and "Provision" at the stack page >> Submit 
-   We can observe below error while the Provision fails with error mentioned above.

# Cause 

* * *

-   The CFT which is being used might have no invalid information.
-   The User has no permissions to execute some of the parameters provided in the CFT.

# Resolution

* * *

-   Communicate with AWS team for best practices on using CFT and modify the CFT accordingly.
-   Suggested to have the CFT verified with AWS if it can provision a VM successfully without ServiceNow CMP
-   If the CFT have no issues to provision at AWS using the user it is mean the same will not have issues provision from ServiceNow CMP.
-   Verify attached files **"CFT-Example\_Error"** vs **"CFT-Example\_Good"** to understand the issues and fix them accordingly along with AWS SME.

  

  

### Related Links

-   Cloud Management Platform, Stack Provisioning fails with below error when the Catalog item/Blueprint is created from **CloudFormation Template.**

Failed to execute API - Failed with status code and message: 400: <ErrorResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">  
<Error>  
<Type>Sender</Type>  
<Code>LimitExceededException</Code>  
<Message>Limit for stack has been exceeded</Message>  
</Error>  
<RequestId>cbf625b6-d405-4594-818e-18d25d7db00b</RequestId>  
</ErrorResponse>  
(script\_include:CloudRESTAPIInvoker; line 142)

-   By Default, a Maximum number of AWS CloudFormation stacks that you can create is 200 stacks.

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html)

-   Suggested to create a stack with the Cloud formation template on the AWS console and If it throws '"Stack Limit exceeded" error, Delete few unwanted Stack resources from AWS Console.
-   Launch the stack from Cloud user portal and it will be successful.
