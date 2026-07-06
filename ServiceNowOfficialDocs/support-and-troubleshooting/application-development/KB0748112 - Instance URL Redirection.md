---
title: "Instance URL Redirection"
aliases:
  - KB0748112
  - Instance URL Redirection
tags:
  - servicenow
  - support-kb
  - instance-administration
  - url-redirection
  - custom-url
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748112
kb_number: KB0748112
last_modified: 2025-04-10
---

## Issue

URL redirection is not supported or recommended by ServiceNow.

There are a couple of scenarios where URL redirection will be encountered:

**Scenario 1**  
After an instance rename, the old instance URL will be active from 2 to a maximum of 7 days, depending on what URL retention period is selected. This means that if a user tries to open the old instance URL, it will redirect to the new instance name. When the old URL retention period has ended the user trying to open the old URL will see this message: "This site can't be reached". This default message cannot be edited.

**Scenario 2**

If both instances are live, the URL redirect is not supported or recommended by ServiceNow, even if it is not implemented on the customer's side which is possible if they use a Server-Side Processor.

## Resolution

## Additional Information

**Related Links:**  
Associating custom URLs to your instance   
[https://docs.servicenow.com/csh?topicname=custom-url.html&version=latest](https://docs.servicenow.com/csh?topicname=custom-url.html&version=latest)

**Processors**   
[https://docs.servicenow.com/csh?topicname=c\_Processors.html&version=latest](https://docs.servicenow.com/csh?topicname=c_Processors.html&version=latest)

## Related

- [[KB0550841 - Customer instance rename policy]]
- [[KB0781923 - Would Custom URLs cause problems for MID Servers]]
