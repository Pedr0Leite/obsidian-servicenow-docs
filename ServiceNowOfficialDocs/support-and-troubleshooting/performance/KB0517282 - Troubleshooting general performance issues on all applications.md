---
title: "Troubleshooting general performance issues on all applications"
aliases:
  - KB0517282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0517282
kb_number: KB0517282
last_modified: 2026-01-08
---

## Troubleshooting general performance issues on all applications

  

### Issue

If slow performance is experienced by all users and also affects all applications in the instance, see below for symptoms, causes, and ways to resolve the issue.

### Symptoms

When users report performance problems, slowness, or interrupted access on all applications, there are a number of possible symptoms:

-   Transactions take longer than expected. 
-   Unable to connect to the instance. 
-   Low or out-of-memory alerts appear.
-   Some Java applications use a lot of memory compared to native applications.
-   Program absorbs more and more system memory as it runs.
-   Stats and threads are accessible, but the user interface is not.

### Release

### Cause

Any of the following issues can be a cause, or contribute to the performance:

-   There is no network connectivity. 
-   Network issues exist between the instance and user.
-   The Java Virtual Machine (JVM) memory utilization level is high or the memory heap is not big enough to store all data. 
-   A large number of calls are made to the database, which causes high disk input/output (I/O) on the database server.
-   The central processing unit (CPU) load on the server is too high.
-   There is a high level of transaction concurrency.

### Resolution

 **Note:** Prior to completing the following steps, collect the necessary information needed to troubleshoot the performance issue. For more information, see [Gathering node data via stats.do and threads.do](/kb_view.do?sysparm_article=KB0517269 "Gathering node data via stats.do and threads.do").

To troubleshoot slow performance experienced by all users on all applications:

1.  Test the network connectivity to the instance and verify that there are no existing issues. For more information, see [Managing network connectivity issues](/kb_view.do?sysparm_article=KB0517267 "Managing network connectivity issues").  
2.  Verify that the instance is not running out of JVM memory. For more information, see [Troubleshooting JVM memory issues](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547765).
3.  Verify that the instance is not experiencing high concurrency. 

  The ServiceNow internal role is required to complete the following steps

1.  Verify that the disk I/O does not indicate overuse or high levels of saturation. 
2.  Verify that there are sufficient CPU resources to satisfy demand. For more information, see [Identifying high CPU utilization on the server](/kb_view.do?sysparm_article=KB0517276 "Identifying high CPU utilization on the server").  

If the issue continues to exist after following the steps in this article:

-   Clearly identify the issue or question.
-   Search in the [ServiceNow product documentation](https://docs.servicenow.com/ "product documentation") for your issue.
-   Search for your issue in the [ServiceNow Community](http://community.service-now.com/ "ServiceNow Community").
-   Post a question on the ServiceNow [Community forums](http://community.service-now.com/forums "Community forums"). New users must create an account on the ServiceNow Community in order to post.
-   Open an incident via email or the online [Technical Support](http://www.servicenow.com/support/contact-support.html "Technical Support") system.
-   Contact the Technical Support team.

 For more information on how to submit an incident, see [Customer Support](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260 "Customer Support").

### Related Links

For more information on related topics, review the following product documentation pages:

  

-   [Monitoring Performance on Threads](https://docs.servicenow.com/csh?topicname=c_MonitorPerformanceOnThreads.html&version=latest "Monitoring Performance on Threads")

  

For more topic-related issues, review the following Knowledge Base article:

-   [Troubleshooting slow performance](/kb_view.do?sysparm_article=KB0517241 "Troubleshooting slow performance")
