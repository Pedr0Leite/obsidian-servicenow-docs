---
title: "Six common performance pitfalls in Service Portal and how to avoid them"
aliases:
  - KB0634588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634588
kb_number: KB0634588
last_modified: 2025-06-04
---

## Six common performance pitfalls in Service Portal and how to avoid them

  

### Issue

This article shares several scenarios that can lead to performance problems in Service Portal, how to diagnose the issues, and how to avoid them.

#### 1\. Internet Explorer

Internet Explorer has several known issues related to memory management, which can cause performance problems in Service Portal. Read more about these issues and the best practices for avoiding them here: [Best practices for avoiding memory leaks in Service Portal when using Internet Explorer](https://community.servicenow.com/community/service-automation-platform/blog/2017/04/11/best-practices-for-avoiding-memory-leaks-in-service-portal-when-using-internet-explorer).

#### 2\. Auto-refreshing widgets

Auto-refreshing widgets can cause major performance issues. This is usually seen instance-wide in the form of semaphore exhaustion caused by a high number of calls to **/sp/rectangle/**.

This topic is further addressed in this article: [Are your auto-refreshing widgets causing instance slowdowns?](https://community.servicenow.com/community?id=community_blog&sys_id=377de269dbd0dbc01dcaf3231f96194b&view_source=searchResult "Are your auto-refreshing widgets causing instance slowdowns?") There is not really any way to do auto-refresh widgets without impacting system performance in some way.

#### 3\. Server scripts using large datasets or inefficient queries

Excessive data can cause performance issues, often slowing down widget loads or, in extreme cases, running an instance out of memory.

To avoid this:

-   Limit data to what users need, such as current incidents instead of all past ones.
-   Optimize data retrieval to prevent memory overload and slow page loads.

Large datasets can pose several challenges. 

-   Querying the data, evaluating ACLs, and running business rules take time. 
-   The data is sent to the controller via the **$scope.data** object. The size of this object has a direct relation to the amount of time it takes to JSON encode, send via HTTP, and then unpack in the browser.
-   Iterating through large datasets and processing each record is CPU-intensive, so consider this when designing a portal.

To avoid processing large amounts of data: 

-   Use effective filters to show users only the data they really need.
-   Do the minimal amount of data processing possible.
-   Place data-intensive widgets on separate pages to avoid impacting other pages with lighter data usage.

#### 4\. Scripted menu items

Scripted menu items, a powerful Service Portal feature, can cause performance issues if they display too much data or contain inefficient scripts, slowing down page loads across the portal. 

Like server scripts, scripted list menu items share similar performance issues and solutions. They impact page loading across the portal, which makes a bad query in a scripted list menu item more noticeable than in one widget instance.  

#### 5\. Loading large files and attachments

Common performance issues also arise from loading large files and attachments. For example: 

-   Simultaneously loading high-definition media files, although expected to take longer, can still impact performance 
-   Repeatedly loading large fonts in the sys\_attachment table
-   Embedding encoded images in CSS can increase HTTP request times

#### 6\. Record Watchers

Record watchers on high-traffic portal pages can cause performance issues if not managed carefully. Specifically:

-   Using too-broad filters or static filters with high traffic can lead to frequent server callbacks.
-   Each record update matching the filter triggers a callback, potentially causing semaphore exhaustion with many users.
-   Fine-tune filters to minimize server load and prevent performance degradation.

For more information, see [Fine-tuning record watchers in Service Portal](https://support.servicenow.com/kb_view.do?sysparm_article=KB0639111 "Fine tuning Record Watchers in Service Portal")

### Resolution

**To diagnose performance issues, try the following:**

1\. Use the SP Page Performance Diagnostic script to simplify identifying which widgets are causing the page slowdown. See also [How to identify a slow widget on a page.](https://support.servicenow.com/kb_view.do?sysparm_article=KB0744521 "How to identify a slow widget on a page")

2\. Test it in the platform UI to determine if the issue is portal-specific or platform-wide. To do this:

-   Test your queries in **Scripts - Background**. If they're slow or return a huge amount of data, performance will be the same in your service portal widget as well.

3\. Try to reproduce the slowness in a different browser since certain browsers handle things differently. This is especially important when using Internet Explorer because of its multiple known issues.

4\. Check to see if all pages in the portal are slow. Try the following:

-   Look at the header menu to check if scripted lists are an issue.
-   Check if the theme is loading any large font or image files.

If one page or a group of pages load slowly in every portal, the issue is unlikely to be the theme or scripted menu items, unless they are used in all portals. If so, try the following:

-   Open the page in the $sp portal (/$sp.do). This opens the page without a theme or header menu on the page.
-   If the page still loads slowly, focus on the widgets to see which one might be causing the slowdown.

5\. Check the javascript console and the network tab in the browser development tools. Slowdown could be caused by:

-   Errors in the javascript console 
-   A large number of HTTP requests that take a long time to resolve

**Note**: As a single-page application, the Service Portal communicates with the server via REST, making it challenging to identify request sources. However, the most common requests are to **/api/now/sp/rectangle/** followed by a sys\_id, which typically come from a widget using server.update() or similar. The sys\_id in the request identifies the widget instance making the call. Knowing the sys\_id helps with troubleshooting. 

6\. Check the syslog table for warnings about large JSON objects, which often indicate a widget is handling a large dataset. Look for warnings when:

-   Loading the portal page
-   Performing the action causing slowness

These warnings suggest a widget is working with an excessive dataset that may need optimization, such as trimming it down.

### Related Links

For more information on troubleshooting performance issues, see:

-   [5 Ways to Troubleshoot your Instance Performance](https://community.servicenow.com/community?id=community_blog&sys_id=a6ecae65dbd0dbc01dcaf3231f961969 "5 Ways to Troubleshoot your Instance Performance")
-   [Six Ways to Improve the Performance of Client Scripts](https://community.servicenow.com/community?id=community_blog&sys_id=47bc6e25dbd0dbc01dcaf3231f961967 "Six Ways to Improve the Performance of Client Scripts")
-   [Debug slow performance on the client-side using Chrome](https://community.servicenow.com/community?id=community_blog&sys_id=590e6a2ddbd0dbc01dcaf3231f9619b7 "Debug slow performance on the client-side using Chrome")

This article was created from a post in the ServiceNow community [Six common performance pitfalls in Service Portal and how to diagnose them](https://community.servicenow.com/community?id=community_blog&sys_id=dffda62ddbd0dbc01dcaf3231f9619b1 "Six common performance pitfalls in Service Portal and how to diagnose them")
