---
title: "Is it possible to restrict REST calls for some users only?"
aliases:
  - KB0639032
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639032
kb_number: KB0639032
last_modified: 2024-04-07
---

## Is it possible to restrict REST calls for some users only?

  

### Issue

Is it possible to restrict REST calls for some users only?  

Problem

* * *

As users become more knowledgeable, they may start using REST calls to retrieve data from instances. Some administrators want the option to disable REST for some users.  

Symptoms

* * *

Administrators see REST messages coming from different users on the instance transaction logs. Administrators could get asked to avoid REST API calls done by clients like powershell, Postman, REST explorer, Excel scripts, and other REST clients directly into the instance.  

Cause

* * *

There are no settings that restrict REST access for some users. If a user has access to the record, the REST API is available for that record as well. Technically, everything is "accessible" by default. This means that the API is defined for all tables, but the web service must still pass both user authentication, Data Policies, and ACLs to get to the data.  
  
  
Resolution

* * *

We recommend educating users if their actions are affecting instance performance. REST transactions are visible in instance transaction logs. If users abuse REST services, educate them on how they can tune their queries to reduce the impact on the instance.  
  

<table><tbody><tr><td><strong>To validate the transactions created on Today, with URL starting with /, Response time &gt; 5000 and created is not guest: &lt;instance&gt;</strong>/syslog_transaction_list.do?sysparm_query=sys_created_onONToday%40javascript%3Ags.beginningOfToday()%40javascript%3Ags.endOfToday()%5EurlSTARTSWITH/%5Eresponse_time%3E5000%5Esys_created_by!%3Dguest%5Etype%3Drest</td></tr></tbody></table>

  
Administrators can also create [transaction quota rules](https://docs.servicenow.com/csh?topicname=c_TransactionQuotas.html&version=latest "transaction quota rules") to limit some access to requests, but this is not recommended because it should not restrict required internal REST calls from those users. Use the available transaction quotas as as example (such as, search for <instance>/sysrule\_quota\_list.do?sysparm\_query=conditionLIKErest). Note that this is a very advanced feature, so fully test on a development instance before making changes on production.
