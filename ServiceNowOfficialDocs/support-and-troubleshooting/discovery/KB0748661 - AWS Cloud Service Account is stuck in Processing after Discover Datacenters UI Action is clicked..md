---
title: "AWS Cloud Service Account is stuck in \"Processing\" after \"Discover Datacenters\" UI Action is clicked."
aliases:
  - KB0748661
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748661
kb_number: KB0748661
last_modified: 2024-04-07
---

## AWS Cloud Service Account is stuck in "Processing" after "Discover Datacenters" UI Action is clicked.

  

### Issue

# Symptoms

\=> After clicking "Discover Datacenters" UI Action, the "Datacenter discovery status" field shows the following with no further update:

<date/time stamp>: Processing....

\=> Cloud API "Method Name" is "List Datacenters" and "Route Status" field value is "executing" with no further update

\=> The Error message in ecc\_queue input where topic is "APIProxyProbe":

com.snc.automation\_common.integration.exceptions.UnknownException: Could not initialize APIProxyProbe  
at com.snc.cmp.mid.probe.APIProxyProbe.probe(APIProxyProbe.java:326)  
at com.service\_now.mid.probe.AProbe.process(AProbe.java:96)  
at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:125)  
at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)  
Caused by: java.lang.NullPointerException  
at com.snc.cmp.mid.probe.APIProxyProbe.probe(APIProxyProbe.java:98)  
... 6 more

# Release

 Use case release was London Patch 6

# Cause

In the aws\_credential record, the "AWS Account" field is referencing a non-existent record in the aws\_account\_admin table. This table is associated with AWS Cloud discovery in releases before Jakarta. This field is not required to be populated when "cloud api" and "cloud management core" plugins, introduced with the Jakarta release, are active. The aws\_credential record was imported from another instance but the "aws\_account\_admin" record referenced in the "AWS Account" field was not.

Note the line in the XML of the aws\_credential record.

<aws\_account display\_value="">11111111111111111111111111111111</aws\_account>

Show XML:

<xml>  
<aws\_credentials>  
<access\_key>ACCESSKEYACCESSKEYAC</access\_key>  
<active>true</active>  
<applies\_to>all</applies\_to>  
<authentication\_key/>  
<authentication\_protocol/>  
<aws\_account display\_value="">11111111111111111111111111111111</aws\_account>  
<classification>aws</classification>  
<mid\_list/>  
<name>AWSCREDENTIAL</name>  
<order>100</order>  
<password>COPYOFSECRETKEYCOPYOFSECRETKEYCOPYOFSECR/password>  
<privacy\_key/>  
<privacy\_protocol/>  
<secret\_key>COPYOFSECRETKEYCOPYOFSECRETKEYCOPYOFSECR</secret\_key>  
<ssh\_passphrase/>  
<ssh\_private\_key/>  
<sys\_class\_name>aws\_credentials</sys\_class\_name>  
<sys\_created\_by>USERNAME</sys\_created\_by>  
<sys\_created\_on>2019-04-17 17:20:18</sys\_created\_on>  
<sys\_domain>global</sys\_domain>  
<sys\_id>21111111111111111111111111111111</sys\_id>  
<sys\_mod\_count>5</sys\_mod\_count>  
<sys\_updated\_by>USERNAME</sys\_updated\_by>  
<sys\_updated\_on>2019-05-06 18:39:53</sys\_updated\_on>  
<tag/>  
<type>aws</type>  
<user\_name>COPYOFACCESSKEYCOPY</user\_name>  
</aws\_credentials>  
</xml>

# Resolution

1\. Create the AWS credential from scratch and not populate the "AWS account" field. Then reference this in the Cloud Service Account records "AWS Credential" field.

or  
  
2\. Export XML from originating instance the legacy (existed in pre-Jakarta) "aws\_account\_admin" record referenced in the "AWS Account" field in the AWS credential record and import XML into problem instance.
