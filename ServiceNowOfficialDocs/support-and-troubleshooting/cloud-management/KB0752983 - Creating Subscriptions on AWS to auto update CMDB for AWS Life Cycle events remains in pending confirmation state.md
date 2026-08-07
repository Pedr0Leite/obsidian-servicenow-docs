---
title: "Creating Subscriptions on AWS to auto update CMDB for AWS Life Cycle events remains in pending confirmation state"
aliases:
  - KB0752983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752983
kb_number: KB0752983
last_modified: 2025-04-07
---

## Creating Subscriptions on AWS to auto update CMDB for AWS Life Cycle events remains in pending confirmation state

  

### Issue

While trying to create the auto update CMDB in ServiceNow for an AWS life cycle event by creating subscriptions, the subscriptions on AWS console can remain in a "pending confirmation" state.

### Release

All

### Cause

There might be multiple reasons as to why the subscriptions created on AWS console might remain in pending state. But, the underlying factor is once a subscription is created, AWS reaches out to the ServiceNow instance over a REST API call. This request should be confirmed on the instance. During next steps in the process, the API call gets routed to the MID Server and then onto the instance. All communications happen directly between the instance and AWS.

### Resolution

1.  Check the URL format being used in the creation of the endpoint on AWS. It should be formatted as    
              https://username:password@InstanceName.service-now.com/api/now/cloud\_event 
2.  Identify if the user being used in the endpoint URL on AWS has the right roles associated. The right roles in order to perform cloud management are:  
      
                 On AWS Console:              AWS Management Console administrator  
                 On ServiceNow Instance:   Cloud Management: admin or sn\_cmp.cloud\_admin  
      
    More information on associating the user account with the right roles can be found documented at: [Create the credentials that enable Cloud Management to access your AWS data](https://docs.servicenow.com/csh?topicname=aws-create-creds-cloud-mgt.html&version=latest "Create the credentials that enable Cloud Management to access your AWS data")
3.  Check if the password field contains the "@" symbol. If the password field has the "@" symbol try using a different password which does not contain the "@" symbol. while parsing the URL, if AWS reads the @ symbol it expects the endpoint URL to begin right after.
4.  Check if the IP for the AWS host is allowed to communicate with the instance. This can be checked under ip\_access table.
5.  Navigate to sn\_cmp\_cloud\_event table and try to list the AWS related events. Every time a subscription is created with the right parameters, including the user accounts and the URL, AWS reaches out to the instance over a REST API call. And this event should be recorded in the sn\_cmp\_cloud\_event table. 

  
If none of the above steps yield any results, setup cloudwatch to capture logs on the AWS console and try to list the log pertaining to the REST call. In the logs, to identify, try to list the sections that has the destination pointing to the endpoint URL. This message section should contain the provider response along with a status code. This should help narrow down what might be causing the subscription to not show up on the ServiceNow Instance.
