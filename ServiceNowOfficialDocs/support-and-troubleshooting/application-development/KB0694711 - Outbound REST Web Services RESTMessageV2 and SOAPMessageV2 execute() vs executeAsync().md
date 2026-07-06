---
title: "Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()"
aliases:
  - KB0694711
tags:
  - servicenow
  - support-kb
  - restmessagev2
  - soapmessagev2
  - outbound-integration
  - mid-server
  - ecc-queue
  - performance
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694711
kb_number: KB0694711
last_modified: 2026-05-18
---

## Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()

  

### Issue

RESTMessageV2 and SOAPMessageV2 are Javascript APIs that ServiceNow customers can use to create SOAP or REST style web service calls out of ServiceNow. The API's can be used either with the execute() method or the executeAsync() method. The API's can be used with a MID Server or without a MID Server. This document discusses the behavior under the covers when combining these two options in various combinations and the consequent implications on performance.

There are a few major concepts that you need to understand before reading this article is ServiceNow "semaphores" and "worker threads". These are explained in many places, but essentially ServiceNow limits the number of threads available to handle inbound UI requests, web service traffic and background jobs/operations. When designing an outbound web service (from ServiceNow to some remote endpoint) you should consider which of these thread pools are being used and for how long, and balance the pros and cons.

If you open Diagnostics > Stats (/stats.do), you can see the current status of the thread pools for your node in the following sections. All ServiceNow instances have multiple nodes and every user session gets tied to a specific node.

1\. The "Default" semaphore pool handles UI requests. There are 16\* Default threads per node.

2\. The "API\_INT" semaphore pool handles Web service requests. There are 4\* API\_INT threads per node.

3\. The "Scheduler Workers" handle background jobs/operations. There are 8\* Scheduler Worker threads per node.

\* These numbers are the default settings for all instances as of the Orlando release of ServiceNow, 2020.

You might want to refer to the following article for additional information about ServiceNow's /stats.do page:

[13 reasons why the stats.do page is your best friend for troubleshooting](https://community.servicenow.com/community?id=community_blog&sys_id=6cfda22ddbd0dbc01dcaf3231f961907 "13 reasons why the stats.do page is your best friend for troubleshooting")

NOTES:

1\. If at all possible, avoid solutions that include making the UI wait on an external integration endpoint. This includes Workflows that do not have a timer before an Activity that makes an outbound web service call (see [KB0647534 - How does a Workflow Timer help?)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0647534 "KB0647534 - How does a Workflow Timer help?")

2\. If there is no way to avoid making the UI wait on an external integration endpoint, then you should set a very low timeout threshold and use the direct execute() method. Ideally, you should also attempt to let the end user know why they are having to wait for a response - at a minimum, a little message that indicates the system is waiting on an external source and how long the system might wait for a response.  
![](sys_attachment.do?sys_id=bd964e99db3e1918770be6be13961912)

3\. The illustrations here will all use RESTMessageV2 as the example, but the same behavior applies to SOAPMessageV2 as well.

4\. As of ServiceNow's New York release the lag in the creation/execution of scheduled jobs has been hugely reduced as the scheduler thread (that runs on each node) now claims new jobs every 1 second. This is good. It means the asynchronous methods below that leverage scheduled jobs incur 5-9 seconds less automatic lag time. For large customers (those with 5 or more nodes per side, this was never a big lag time since each node claims jobs individually)

5\. RESTResponseV2/SOAPResponseV2 getter methods, such as getBody() and getStatusCode(), will cause SOAPMessageV2/RESTMessageV2 to wait for a response - just as if you had called waitForResponse(ms)! So, you should be aware that these methods will cause the initiating thread to hang while waiting for the HTTP Response body or HTTP Response status code to be populated.

## Timeouts

* * *

### Connection Timeout

The connection timeout is the maximum time a client (i.e. the ServiceNow instance or MID server) will wait for a TCP connection to be established with the web service endpoint. This can be set manually for each request using the [setHttpTimeout(milliseconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RMV2-setHttpTimeout_N "setHttpTimeout(milliseconds)") method. This timeout value applies to both synchronous and asynchronous requests.

### ECC Timeout

ECC timeout is how long getStatusCode, getBody, or waitForResponse will wait for a response when the executeAsync() method has been used. Note that the ECC timeout will NOT impact the timeout of the HTTP web service request itself nor the timeout of the ecc response handling when setEccTopic() or setEccCorrelator() are being used!

ECC timeout is influenced by a number of factors:

-   The properties "glide.rest.outbound.ecc\_response.timeout" and "glide.soap.outbound.ecc\_response.timeout" respectively control the specific timeouts for REST and SOAP requests that use executeAsync (i.e., requests that are processed via ECC).
-   If the property "glide.http.outbound.max\_timeout.enabled" is set to true (as it is by default), then a max ECC timeout will be enforced by the property "glide.http.outbound.max\_timeout". This max ECC timeout is 30 seconds by default and cannot be set to greater than 30 seconds.
-   The above properties can be overwritten by the value passed in to [waitForResponse(seconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RESTResponseV2-waitForResponse_N "waitForResponse(seconds)") which receives its arguments in milliseconds. However, the timeout still cannot be greater than 30 seconds as long as "glide.http.outbound.max\_timeout.enabled" is set to true.  
      
    Note: Waiting for a response after using executeAsync, as described above, is not ideal. It effectively makes the system synchronous again. The initiating thread must wait for the asynchronous thread to complete. This will be described in more detail later in the article.

## Timeout Properties

* * *

The following are timeout-related sys\_properties:

-   **glide.http.connection\_timeout**  
    -   Connection timeout (see Timeout section above)
    -   Can be overridden at request-level via [setHttpTimeout(milliseconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RMV2-setHttpTimeout_N "setHttpTimeout(milliseconds)")
    -   Default: 10000 (units in milliseconds)
-   **glide.http.timeout**  
    -   Socket timeout (see Timeout section above)
    -   Can be overridden at request-level via [setHttpTimeout(milliseconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RMV2-setHttpTimeout_N "setHttpTimeout(milliseconds)")
    -   Default: 175000 (units in milliseconds)
-   **glide.http.outbound.max\_timeout.enabled**  
    -   Applies when waiting for response from ecc\_queue
    -   If enabled, will use value of **glide.http.outbound.max\_timeout** even if you try to override with [waitForResponse(seconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RESTResponseV2-waitForResponse_N "waitForResponse(seconds)") using a higher value
    -   If disabled, will use the maximum of either [waitForResponse(seconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RESTResponseV2-waitForResponse_N "waitForResponse(seconds)") or **glide.rest.outbound.ecc\_response.timeout** value
    -   Default: true
-   **glide.http.outbound.max\_timeout**  
    -   Applies when waiting for response from ecc\_queue
    -   Specifies the max time to wait for response from ecc\_queue if **glide.http.outbound.max\_timeout.enabled** is true -- even if user calls [waitForResponse(seconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RESTResponseV2-waitForResponse_N "waitForResponse(seconds)") with a higher value
    -   If **glide.http.outbound.max\_timeout.enabled** is false, this property is ignored
    -   Default: 30 (units in seconds) -- NOTE: this property has an upper bound of 30 seconds
-   **glide.rest.outbound.ecc\_response.timeout**  
    -   Applies when waiting for response from ecc\_queue
    -   Specifies the max time to wait for response from ecc\_queue if **glide.http.outbound.max\_timeout.enabled** is false -- even if user calls [waitForResponse(seconds)](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=r_RESTResponseV2-waitForResponse_N "waitForResponse(seconds)") with a higher value
    -   If **glide.http.outbound.max\_timeout.enabled** is true, this property is ignored
    -   Default: 300 (units in seconds)

## Call Directly from the instance

* * *

This is the default behavior. In order to use a MID Server, you must explicitly specify the MID Server to be used. In this case an HTTP request will be sent from your ServiceNow instance to the web server end point that you specify.

### Keeping it simple with execute(): No MID Server, direct REST call, execute()

Using the **execute()** method means that a web service call will execute directly from the ServiceNow instance on the currently executing thread _and we will wait for the response to be returned_. If the execute() method is used then the thread will pause until a response is received. This method can be problematic depending on how long it takes for the request to be processed and a response returned to ServiceNow. While ServiceNow is waiting for a response, whatever thread initiated the call will be frozen. For example, if the call was initiated by end user activity, then the end user will experience a frozen screen until the response is returned.

Benefits: Using execute() is simple. You call the method and it returns the Response object in one line of code. Then you do your response handling against response object API (SOAPResponseV2 or RESTResponseV2).

Drawbacks: The executing thread is frozen until the response comes back. While a direct call is by far the simplest option, if your web service call is initiating from the UI, this can be a problem.

![execution thread](/sys_attachment.do?sys_id=b9964e99db3e1918770be6be13961916)

### Breaking out of your dull synchronous life with executeAsync()

Usually executeAsync() is used with a MID Server. However, you can also use it without a MID Server. Using the **executeAsync()** method without a MID Server will send the SOAP/REST request through a scheduled job (sys\_trigger table) and the details of the response to the REST request will be stored in the ECC Queue (ecc\_queue table). This means that the currently executing thread will move to the next line directly after executeAsync() is called and will not need to wait on that line of code for the response to come back. This helps improve performance time for requests triggered by the UI!

### RESTMessageV2: No MID Server, executeAsync(), no response handling

One option is to use executeAsync() without using any of the response handling methods. However, this option has some drawbacks. Besides not being able to handle the response (which might be a deal breaker), executeAsync() also introduces a couple layers of complexity due to using a scheduled job and the ECC queue. Since the request now executes on a scheduled job, this means whatever latency was hitting the users from the UI will now be shifted to the scheduled job queue. This could be problematic if the scheduled job queue fills up with slow web service request calls or other jobs. Also, this method incurs the slight overhead of creation and execution of a scheduled job - a process that usually takes around 0 to 1 seconds (as of New York). That can have a noticeable performance impact if you need your web service to execute within couple milliseconds. The user who initiated the original thread won't have to wait, which is good, but the overall response time for the integration will be impacted. This makes executeAsync() a questionable choice for any integration that needs to execute in near real-time. However, if your integration can tolerate a few seconds of added latency to each request, maybe this will work for you.

![async rest client job](/sys_attachment.do?sys_id=b5964e99db3e1918770be6be1396191a)

Shifts the processing off the initiating thread to a scheduled job, which is good, but it still freezes the scheduled thread while waiting for a response and creates some lag time due to job scheduling.

So, the above method improves the situation in some ways because now the UI is not getting hung while we wait for the web service response. However, since we are not waiting for the response we have no way to handle the response! Our web request has presumably been sent out across the ether to do its work, but how do we know if it worked or not - what response came back? Ground control to Major Tom, can you hear me Major Tom?!

### RESTMessageV2: No MID Server, executeAsync(), waitForResponse()

To overcome the issue of not being able to handle the response, sometimes people decide to use the waitForResponse(seconds) method. However, I am going to recommend that unless you are using a MID Server, this is almost never a good idea! Why, you say? I will tell you why. Because the method **waitForResponse()** causes the initiating thread to freeze again, so we are back to poor response times on the initiating thread - the problem we were trying to avoid by becoming asynchronous. The fact is, when used in combination with waitForResponse(), executeAsync() is no longer asynchronous.

![async rest client job](/sys_attachment.do?sys_id=35964e99db3e1918770be6be1396191c)

This configuration is never a good idea. Besides adding lag time to create/process the scheduled job, it freezes two instance threads the whole time! Just use the direct execute() method instead. That way you skip the lag and use just one thread.

But don't worry, I have a solution that allows you to use executeAsync _and_ process the response without freezing the initial thread! ANNOUNCER VOICE: Now introducing (queue generic fanfare music) the **setEccTopic()** method!

### RESTMessageV2: No MID Server, executeAsync(), setEccTopic()

The setEccTopic() method takes a little more development work, but it allows for truly asynchronous request handling, while at the same time benefitting from the ability to define a custom "sensor" that will handle the response. There are still some drawbacks to this method. We now have two scheduled jobs that must be created, scheduled, picked up and processed and therefore have at least 1-2 seconds of added latency before we can start processing the response (remember the diagram says 6-10 because it was designed before New York improved the initial latency of scheduled jobs). However, by and large, this is a good solution as long as your web service can tolerate the added latency and the response can be handled on a different thread than the initiating request. See below diagram. Also, there is an in-depth discussion of this method's usage here: [KB0563615 - RESTMessageV2 API EccTopic Support](https://support.servicenow.com/kb_view.do?sysparm_article=KB0563615 "KB0563615 - RESTMessageV2 API EccTopic Support").

![async discovery sensor](/sys_attachment.do?sys_id=b1964e99db3e1918770be6be1396191e)

Compounds lag effect of scheduled job queue due to now using two jobs instead of one and still freezes worker thread. However, it handles the response without freezing the initializing thread.

**Summary**

If waitForResponse() is not used, then executeAsync() method will allow the executing thread to continue immediately without waiting for a response. This can speed things up considerably - an important concern when your web service is triggered by the UI or has other time sensitive dependencies for some reason. On the other hand, if response handling is required, then you will need to weigh the options. The following is a list of options:

1\. Use the setEccTopic() method in combination with executeAsync() to spin up a new background thread to process the response (more on that later). setEccTopic() allows asynchronous response handling, but like all executeAsync() method implementations, it does suffer from the inherent lag of scheduling a job and the potential of latency from other jobs causing queue overload. Also, this will not work for solutions that need to be displayed immediately, i.e., in whatever code triggered the RESTMessageV2 class in the first place.

2\. Another option is to have some type of polling design where the UI makes quick requests back to the Server to see if the results it is looking for are available.

Drawbacks: Most web service implementations expect some type of response handling for the requests that are sent out. Using the waitForResponse() method allows you to process a request, but then loses any performance advantage from being processed asynchronously. 

## Using a MID Server

* * *

Using a MID Server is a way to have a web service request initiated from a point within your, ServiceNow's customer's, network. A MID Server is a Java Virtual Machine that sits inside your network firewall and talks to the ServiceNow instance \[mostly\] through a SOAP integration.

There are two places where you can configure a SOAP or REST web service to use a MID Server. You can do it either directly in the javascript via the RESTMessageV2.setMIDServer(string) method, or through the use\_mid\_server field in the sys\_rest\_message\_fn table if you are defining your RESTMessage methods that way.

### Use execute() or executeAsync(), they work the same

When a MID Server is used, the execute() command implicitly becomes asynchronous and both methods act the same way.

### RESTMessageV2: MID Server, executeAsync(), no waiting

You might use a MID Server + executeAsync() if you want to have your REST/SOAP request be initiated from inside your network. If you don't need to wait for a response or you have some other method of getting the response (like a bi-directional integration with a correlation ID, for example) then this might be a good option. It will allow the initiating thread to be immediately released, optimizing ServiceNow semaphore resources (Default/API\_INT).

![api int thread pool](/sys_attachment.do?sys_id=39964e99db3e1918770be6be13961918)

### RESTMessageV2: MID Server, executeAsync(), waitForResponse()

If you use a MID Server + executeAsync() + waitForResponse() then we are back to freezing the initiating thread. This is potentially the worst case scenario in terms of the performance. It has the largest amount of lag time, highest number of points of failure, and most frozen threads waiting for responses.  

![api int thread pool](/sys_attachment.do?sys_id=3d964e99db3e1918770be6be13961914)

You should really try to avoid this. The good news is that similar to the setEccTopic method, there are two methods that can be used with a MID Server to handle responses in a truly asynchronous fashion.

### RESTMessageV2: MID Server, executeAsync(), setEccParameter('skip\_sensor', 'true'), setEccCorrelator()

If you want your web service call to be initiated from within your network via MID Server and you want to handle the response efficiently, using the below method might be a more efficient way to achieve your goals. However, you should consider that there are multiple points of failure and each step will incur some lag time. Make sure to use proper timeout/retry settings and write exception handling to ensure that failed operations will be noticed.

![custom business rule](/sys_attachment.do?sys_id=21964e99db3e1918770be6be13961911)

Requests which are routed via a MID should use the 'setEccParameter('skip\_sensor', 'true')' and 'setEccCorrelator('\[arbitrary string\]')' methods when they are created. Both of these parameters have an important function:

-   Instead of modifying the 'topic' on the output ecc\_queue record setEccCorrelator() will leave topic as 'RESTProbe' (which the MID recognizes) but will add an arbitrary string to the 'agent\_correlator' field. The MID will process this request as normal and write a corresponding payload back as an input ecc\_queue record with the same value in the 'agent\_correlator' field
-   By default there is an expectation that any input ecc\_queue record written by a MID server will have a corresponding Discovery sensor to process that record within the instance. In the case of asynchronous REST requests this is not the case (as processing must be performed, for example, via a custom business rule on the ecc\_queue table). Without setting 'skip\_sensor = true' the asynchronous REST request will still function as expected however the input ecc\_queue record will be set to a state of 'error' with the text 'No sensors defined'. Using 'skip\_sensor = true' avoids this

To process the response to asynchronous REST requests routed via a MID server (and using setEccCorrelator()) an after insert business rule should be created against the ecc\_queue table. This should:

-   Have a condition similar to the following such that it only processes input records with a specific value in the agent\_correlator field:

```
current.agent_correlator == "[arbitrary string]" && current.topic == "RESTProbe" && current.queue == "input" && current.state == "ready"
```

-   Contain code in its script to set the state of the input record to processed:

```
current.state = "processed";
current.processed = gs.nowDateTime();
current.update();
```

Note that it is OK to use current.update() in an 'insert' business rule as this will NOT cause the business rule to be recursive - clearly this type of behaviour should be avoided in an 'update' business rule as the business rule will trigger itself and so become cyclical.

### Release

Any

### Resolution

See above

### Related Links

-   [KB0659194 - Troubleshooting outbound REST web services](/kb_view.do?sysparm_article=KB0659194 "KB0659194 - Troubleshooting outbound REST web services")
-   [KB0563615 - RESTMessageV2 API EccTopic Support](https://support.servicenow.com/kb_view.do?sysparm_article=KB0563615 "KB0563615 - RESTMessageV2 API EccTopic Support")
-   [KB0716391 - Best practices for RESTMessageV2 and SOAPMessageV2](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716391 "KB0716391 - Best practices for RESTMessageV2 and SOAPMessageV2")
-   [Developer site: Direct RESTMessageV2 API](https://developer.servicenow.com/app.do#!/api_doc?v=kingston&id=c_RESTMessageV2API "Developer site: Direct RESTMessageV2 API")
