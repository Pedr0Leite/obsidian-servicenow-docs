---
title: "Inbound emails get processed irrespective of satisfied email filter conditions"
aliases:
  - KB0755180
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755180
kb_number: KB0755180
last_modified: 2024-04-07
---

## Inbound emails get processed irrespective of satisfied email filter conditions

  

### Issue

Email Filter conditions satisfy the inbound emails but still these emails are being processed by inbound actions.

### Cause

1.)  Email Filters setup to filter the inbound emails based on certain conditions does pass through fine but the email filters do do not have any Filter actions. Hence system is not ignoring the inbound email though detected by the filter.  
2.)  Filter actions helps how the system should react when the conditions of the concerned filter evaluate to true.

### Resolution

1.) Open the concerned Email Filter record (System Mailboxes -> Filters) under related list add new Filter actions according to your use-case with a proper Type.

2.) If you would like to add filter actions through a advanced script, we can also do so by using the script field "Action Script" present on the same email filter.

### Related Links

[Create an Email Filter](https://docs.servicenow.com/csh?topicname=t_CreateAnEmailFilter.html&version=latest "Create an Email Filter")

[Email Filters](https://docs.servicenow.com/csh?topicname=c_EmailFilters.html&version=latest "Email Filters")
