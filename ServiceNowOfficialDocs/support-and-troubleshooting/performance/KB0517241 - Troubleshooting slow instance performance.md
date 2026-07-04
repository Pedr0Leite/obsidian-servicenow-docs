---
title: "Troubleshooting slow instance performance"
aliases:
  - KB0517241
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0517241
kb_number: KB0517241
last_modified: 2026-04-23
---

## Troubleshooting slow instance performance

  

### Issue

When your instance is exhibiting signs of slow performance, this article may be able to help you understand the common symptoms, causes, and ways to resolve the issue.

You may also wish to review the video below for information about troubleshooting performance issues with the Session Debug feature:

### Symptoms

-   Unable to log in to an instance.
-   The instance no longer responds to keyboard or mouse commands.
-   Operations seem to run slow or slower than they did before.
-   Slow performance across all or specific applications in the instance.
-   Slow response time when entering data into applications.
-   The graphical user interface (GUI) takes too long to refresh.

### Release

All releases

### Cause

-   Network connectivity issues exist.
-   Tables do not have indexes, causing the system to take longer to return results. This is due to the large amounts of data that must be processed.
-   Scripts are stuck in an infinite loop.
-   A script(s) created an inefficient query in the database or is running full table scans on large tables.
-   Nested queries in the MySQL server have brought the database to a halt due to certain conditions.
-   The Java virtual machine (JVM) memory use is high or the memory heap is not big enough to store all the data.
-   A large number of calls are made to the database, causing high disk input/output (I/O) on the database server.
-   The central processing unit (CPU) load on the server is too high.
-   There is a high level of transaction concurrency.

### Resolution

Slow performance can be related to a single cause or a combination of issues. Before analyzing each possible cause, it is important to answer two main questions:

1.  Who is experiencing slow response times?
2.  What applications are affected? 

If slow performance is experienced by:

-   A single user and affects all or a specific application in the instance: [KB0997495 - How to troubleshoot a 'slow' transaction?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997495 "KB0997495")
-   All users and affects all applications in the instance: [KB0517282 - Troubleshooting general performance issues on all applications](/kb_view.do?sysparm_article=KB0517282 "Troubleshooting case where all-users experience performance issues on all applications")
-   All users and affects a specific application in the instance, see [KB0517280 - Troubleshooting case where all-users experience performance issues on a specific application](/kb_view.do?sysparm_article=KB0517280 "Troubleshooting case where all-users experience performance issues on a specific application")

If the issue continues to exist after following the troubleshooting guidelines:

-   Clearly identify the issue or question.
-   Search in the [ServiceNow product documentation](https://docs.servicenow.com/ "product documentation") for your issue.
-   Search for your issue in the [ServiceNow Community](http://community.service-now.com "ServiceNow Community").
-   Post a question on the ServiceNow [Community forums](http://community.service-now.com/forums "Community forums"). New users must create an account on the ServiceNow Community in order to post.
-   Open an incident via email or the online [Technical Support](http://www.servicenow.com/support/contact-support.html "Technical Support") system.
-   Contact the Technical Support team.
