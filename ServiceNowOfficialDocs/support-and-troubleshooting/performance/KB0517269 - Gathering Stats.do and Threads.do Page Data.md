---
title: "Gathering Stats.do and Threads.do Page Data"
aliases:
  - KB0517269
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0517269
kb_number: KB0517269
last_modified: 2026-06-29
---

## Gathering Stats.do and Threads.do Page Data

  

### Issue

The System Diagnostics application is one of the places to look for root causes of performance issues. The Diagnostics page is used to generate an overview of useful diagnostic information about a running instance and cluster nodes. To see how much memory each node is using, you can use the **stats** page for each node in System Diagnostics, which lists the available and in-use memory. Bear in mind that memory use will fluctuate, and it's not uncommon for it to reach beyond 95% usage before memory garbage collection reduces it back to normal levels.

Since Fall 2010 Stable 1, the performance of individual threads is now tracked by the instance and can be viewed by administrators. Thread performance can be monitored in two places: 

-   the Performance Graph Set
-   the transaction log

Running **stats.do** and **threads.do** is very useful when trying to identify and isolate the cause of a performance issue, specifically when your instance is presenting a low available central processing unit (CPU) percentage or a high number of transactions waiting to be processed. The information in the stats.do page matches up with the information in the threads.do page.

### Release

ALL

### Resolution

To gather stats and threads:

1.  On your browser, navigate to **https://_<instance-name>_.service-now.com/stats.do**. The **_<instance-name>_** should be populated to reflect the instance that is presenting slow response times.  
    -   Alternately, log in to your instance and navigate to **System Diagnostics > Stats**.
2.  Open a new tab or window in your browser and navigate to **https://_<instance-name>_.service-now.com/threads.do**.  
    -   Alternately, log in to your instance and in the **Type filter text** field, enter **threads.do** and press **Enter**.
3.  Press **Command + s** on your Mac or **ctrl + s** on your Windows PC to save the stats.do and threads.do pages to your desktop.
4.  On the case form, click the **Attachments** ![Attachments](/sys_attachment.do?sys_id=f96640a197f1cf540af678ce2153afd9 "Attachments") icon to add the files to the case record.

### Related Links

For more information on related topics, review the following ServiceNow product documentation pages:

-   [Platform Performance](https://docs.servicenow.com/csh?topicname=p_PlatformPerformance.html&version=latest?cshalt=yes "Platform Performance")
-   [Thread Performance Monitoring](https://docs.servicenow.com/csh?topicname=c_MonitorPerformanceOnThreads.html&version=latest "Thread Performance Monitoring")

For more topic-related issues, review the following _Knowledge Base_ article:

-   [Troubleshooting slow performance](/kb_view.do?sysparm_article=KB0517241 "Troubleshooting slow performance")
