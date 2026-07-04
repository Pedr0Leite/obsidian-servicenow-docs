---
title: "Auto-refreshing widgets leads to semaphore exhaustion"
aliases:
  - KB0634655
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634655
kb_number: KB0634655
last_modified: 2025-01-07
---

## Auto-refreshing widgets leads to semaphore exhaustion

  

### Issue

Widgets using an auto-refresh mechanism may generate a very large number of requests to a REST API called **/api/now/sp/rectangle**. A very high number of these requests can lead to semaphore exhaustion on an instance. This is generally attributed to PRB956025 but often, it is really an issue with the portal implementation and can be relieved fairly easily.

### Symptoms

-   A sudden increase in requests to **/api/now/sp/rectangle/???**
-   General slowness and an increase in **429** responses from the server

### What is /api/now/sp/rectangle?

**/api/now/sp/rectangle** is a REST API used by Service Portal to facilitate communication between a widget’s controller and a server script. Specifically, this API is used whenever a widget calls **server.update()**, **spUtil.update()**, or similar functions to invoke the widget’s server script. The widget’s server script is where the data model is populated so this is often done to either update or refresh the data.

### The Problem with auto-refreshing widgets

Service Portal was never designed with this use case in mind. Service Portal is a single page angular app and using methods like the standard javascript **setInterval()** function to create an auto-refresh actually creates a variable in the browser’s runtime that persists throughout the life of the angular app.

What happens, is that these timers are created in the browser’s runtime and every time a user navigates away from a page using an auto-refreshing widget and then back again, the timer is re-created. Now, there are two timers going for the same thing. Over time, a small number of users can unknowingly generate a very large number of these **sp/rectangle** calls just due to the fact that the old ones are never destroyed until leaving the portal altogether.

### How to diagnose performance issues caused by auto-refreshing widgets

1.  Look for is that high number of calls to **/api/now/sp/rectangle/???**
2.  Find the widget making the call  
    The API call provides that information. The request string contains the sys\_id of a widget instance, **sp \_instance**. A widget instance is a record mapping a widget to a page in the portal so it always contains a reference to the widget.
3.  Look for code to create an auto-refresh in the widget’s client script, or controller.

Most commonly, there is code like this:

setInterval(function(){  
  server.update();  
},3000);

This tells the browser to call **server.update()** every 3 seconds.

There are some other variants possible as well, but they will all follow this pattern and make a call to the server at some interval or inside a loop.

### How to reduce the number of calls

Reduce the number of calls by removing the code creating the auto-refresh. There may be more than one widget at fault so make sure to trace all of the **sp/rectangle** calls back to a widget and ensure they are all taken care of.

Since these are stored in the browser’s runtime, in some cases, the browser continues to send the requests regardless of whether the user’s session is active. If for example, the user goes home for the night but leaves the portal open on their desktop, the browser may continue to send those requests until the next morning.

Ultimately there is no perfect solution to keep the auto-refresh functionality and avoid performance issues but there are a few ideas that may help in the post from the community that this article was created from: [Are your auto-refreshing widgets causing instance slowdowns?](https://community.servicenow.com/community/service-automation-platform/blog/2017/06/26/auto-refreshing-widgets-sprectangle-and-instance-slowdowns "Are your auto-refreshing widgets causing instance slowdowns?")

### Related Links

For more information also refer to these articles

[KB0635134 - Resolving "Exhausted Default Semaphores" errors caused by Service Portal widgets having poorly defined record watcher (recordWatch) calls](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635134 "KB0635134")

[KB0639111 - Fine-tuning Record Watchers in Service Portal](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639111 "KB0639111")
