---
title: "AMB (Asynchronous Message Bus) - an Architectural Overview"
aliases:
  - KB0622691
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622691
kb_number: KB0622691
last_modified: 2024-04-07
---

## Issue

Asynchronous Message Bus - an Architectural Overview

Intended Audience

* * *

This document is aimed at ServiceNow System Administrators, Network Administrators and other technical personnel who may be planning an upgrade from a pre-Geneva or pre-Madrid release or for those who are looking to increase their understanding of the post-Geneva or post-Madrid ServiceNow platform architecture. 

Overview

* * *

The trend in web development over the last ten years has been to move toward a Single Page App (SPA) model where most of the data is fetched after the initial form load. The rationale is that these types of applications offer an improved user experience. For example, when navigating through the application, only the data on the page that has changed is loaded. Also, they allow for immediate reflection of data changes.

As part of the Geneva release, ServiceNow introduced UI16 – a feature-rich and dynamic user interface that provides several innovative product features. Many of these new features rely on a major platform component named AMB (Asynchronous Message Bus). This article explains what AMB is, how it is used, and what you need to know prior to upgrading so you can assess its potential impact.

In Madrid the AMB feature was further developed to support Web Sockets.

<table class="noteTable" style="width: 845px; height: 47px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: This document discusses concepts and features and that were introduced in the Geneva and Madrid releases. Note that the application is a constantly evolving product and that the platform may be subject to future changes in upcoming releases.</td></tr></tbody></table>

What is Asynchronous Message Bus?

* * *

AMB is an API that has been developed with the specific intention of enabling "push communication" from the server to the client to deliver real-time dynamic content in the UI. In general terms, the server-side is the ServiceNow instance and the client-side is typically an end-user's browser.

With the Geneva release, an all-new UI was introduced named UI16. With this release, we introduced several notable new features and enhancements that utilize AMB extensively. These include:

-   Live Form Updates – real-time updates to data on forms, lists, and reports
-   Visual Task Boards
-   Connect Chat
-   Service Portal
-   MID Server ECC Queue Processing 

  
Why is AMB necessary?

* * *

HTTP was originally designed as a protocol for retrieving documents from remote servers. The simple request/response model works well for static websites, but has some limitations when serving dynamic content where a bi-directional link between client and server would be more beneficial.   Also with the HTTP model, communication is always initiated by the client and never the server – so with this model, the server cannot _push_ asynchronous events back to the client.  

To overcome this, one method web developers have used is short-polling. In this scenario, the client typically issues AJAX requests regularly asking for an update and the server responds back with a response. A number of scenarios exist where such an approach is both a viable and valid approach to use. For example, when we want to exert direct control of the level and frequency of data updates that are received. However, in other scenarios where there is more unpredictability over when an "event" will occur, the short-polling method has some downsides. For example, the client may repeatedly contact the server to check for changes even though there may not be any. 

To work around this issue, ServiceNow uses AMB which uses a Publish-Subscribe model. Instead of the client periodically checking in with the server for real-time information, the client instead subscribes to a _channel_ and the server notifies/pushes information down to the client as soon as it becomes available. This enables the delivery of real-time content without the associated overhead.

The two approaches can be contrasted as follows: 

**Short Polling:**

![](sys_attachment.do?sys_id=524d28a2db82b450e515c2230596197f)

In the diagram above, the client is only made aware that an event has occurred after the second response is provided by the server. Data freshness is determined by how frequently the client polls for changes.

**Publish/Subscribe model:**

With a Publish/Subscribe model the server pushes only relevant data to the client as soon as it is available. When an event of interest occurs, such as an update to a field on an incident form, the server immediately alerts the client.

For more information see:

[https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe\_pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

[https://en.wikipedia.org/wiki/Push\_technology](https://en.wikipedia.org/wiki/Push_technology)

How does AMB work?

* * *

A client transaction triggers a connection with the server. With the server listening for events, changes can occur in real time and the client is notified through the created connection in an asynchronous method. The server can continue to listen and notify the client of changes as they occur.

**Web Sockets vs. Long-polling:**

Prior to Madrid AMB was using a long-polling transport to emulate a server push:​

-   The client sends an HTTP request to the server at least every 30 seconds requesting new information​
-   The server holds the request open until new data is available​
-   Once available, the server responds and sends the new information​
-   When the client receives the new information, it immediately sends another request, and the operation is repeated​

Long-polling creates a request headers overhead of ~2000 Bytes/Request​

Madrid and later versions of ServiceNow attempt to use the WebSocket transport, a protocol supporting full-duplex communication:​

-   The server can send the content to the client without being first requested by the client​
-   The messages are passed back and forth while keeping the connection open​

The WebSocket request headers overhead is minimal ~8 Bytes/Request​.

WebSocket is supported by most modern user agents and proxies. If WebSockets is not supported, it will gracefully downgrade to Long-polling during TCP handshake.

Madrid+

* * *

In Madrid and later versions, AMB attempts to upgrade the HTTP connection to the WebSockets protocol. Following are some of the AMB HTTP transactions that can be seen when AMB-based features are used. These can be viewed using browser tools such as Firefox Firebug, Chrome Developer Tools, or tools with an HTTP profiling capability.

![](sys_attachment.do?sys_id=e24d28a2db82b450e515c22305961989) 

A closer look at WebSocket AMB requests 

* * *

Following are some of the AMB HTTP transactions that can be seen when AMB-based features are used. These can be viewed using browser tools such as Firefox Firebug, Chrome Developer Tools, or tools with an HTTP profiling capability.

<table class="noteTable" style="width: 840px; height: 47px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: The following request URLs are not an API and are subject to change. The bullet points in this section are strictly used to illustrate the validity of the traffic involved with AMB requests to give you&nbsp;a better understanding of AMB-based traffic..</td></tr></tbody></table>

**Request: /amb**

-   When viewed in Chrome developer tools WebSocket communication will only be shown as a single HTTP Request.
-   Select the Request whose name displays as "amb" in the "Network" tab of Developer tools
-   To see all details of the communication, click the "Frames" tab of the "amb" Request to see all the details communications like in the below screenshot
-   Each "Data" entry is the payload of a message and the arrow indicates if the message went up to or down from the server  
      
    ![](sys_attachment.do?sys_id=ae4d28a2db82b450e515c2230596198e)   
      

Potential impact on load balancer, proxy, or reverse proxy deployment from WebSocket

* * *

**Fallback Behavior**

On each page that leverages AMB, the system will issue an HTTP request to "amb". The request will attempt to Upgrade from HTTPS to WSS (WebSockets over SSL/TLS). If WebSockets is not supported by the infrastructure in-between the customer and ServiceNow's server it will gracefully downgrade to using Long-polling. Customers whose infrastructure does not support WebSocket will simply default to the pre-Madrid behavior without loss of functionality or negative impact.

**Testing/Troubleshooting Edge Cases**

There is a slight potential to fall into an edge case where the fallback behavior does not work as expected. If the infrastructure between yourself and ServiceNow does not support WebSocket but _incorrectly reports that it does support WebSocket,_ then the request to "amb" will Upgrade to WSS and will start using WebSocket messages only for those messages to fail since the infrastructure does not actually support WebSocket.

During your testing for Madrid, to ensure that your infrastructure does support WebSocket you can use a built-in test page in ServiceNow.

https://yourinstance.service-now.com/$websocket\_test.do

![](sys_attachment.do?sys_id=e64d28a2db82b450e515c22305961994)

Pre-Madrid/Fallback Behavior: Long-Polling

* * *

Following are some of the AMB HTTP transactions that can be seen when AMB-based features are used. These can be viewed using browser tools such as Firefox Firebug, Chrome Developer Tools, or tools with an HTTP profiling capability.

This section covers the pre-Madrid behavior of Long-polling. As mentioned above, Long-polling is also the fallback behavior for Madrid and later versions if WebSocket is not supported by the infrastructure between the customer and ServiceNow. The basic idea of Long-polling is that a request is always first sent to the server and then is held open without sending a response for a pre-determined duration. If an event occurs while the request is being held open or the request duration is exceeded, then a response will be immediately be sent back to the client and the client will send another request that is then held open and the cycle repeats.

![](sys_attachment.do?sys_id=224d28a2db82b450e515c2230596199a)

A closer look at Long-polling AMB requests

* * *

Following are some of the AMB HTTP transactions that can be seen when AMB-based features are used. These can be viewed using browser tools such as Firefox Firebug, Chrome Developer Tools, or tools with an HTTP profiling capability.

<table class="noteTable" style="width: 840px; height: 47px;" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle;"><strong>Note</strong>: The following request URLs are not an API and are subject to change. The bullet points in this section are strictly used to illustrate the validity of the traffic involved with AMB requests to give you&nbsp;a better understanding of AMB-based traffic..</td></tr></tbody></table>

**Request: /amb/handshake**

-   Initial connection between client and server - contains parameters such as available transport types, Bayeux version, etc.   
      
    ![](sys_attachment.do?sys_id=e64d28a2db82b450e515c223059619a3)  
      
    ![](sys_attachment.do?sys_id=aa4d28a2db82b450e515c223059619ab)

**  
Request: /amb**

-   Used to subscribe, unsubscribe, publish, and receive messages  
      
    ![](sys_attachment.do?sys_id=664d28a2db82b450e515c223059619b6)  
      
    ![](sys_attachment.do?sys_id=ba4d28a2db82b450e515c223059619c6)

**  
Request: /connect**

-   Long poll that waits for a new message from the server (IMPORTANT: this request is not part of the Connect (Chat) product)  
      
    ![](sys_attachment.do?sys_id=f24d28a2db82b450e515c223059619d3)  
      
      
    For snippets from the localhost log capturing a live form update, refer to Appendix 1.   
      

Potential impact on load balancer, proxy, or reverse proxy deployment from Long-polling 

* * *

Proxies are intermediate entities that can be involved in the delivery of requests and responses from the client to the server and vice versa. Common examples are web servers, web proxies, load balancers, and firewalls. It is common to have proxy and/or reverse proxy deployments for various reasons, including load-balancing, acting as an SSL endpoint, or as part of an integration with an SSO provider.

A potential cause for concern is that many proxies use a synchronous programming model for handling requests because the resources allocated to each request are held for the _duration_ of the request. These employ a thread-per-request model and, given the changes imposed by the AMB to the number of HTTP connections and length of long, open connections, customers upgrading to Geneva (or later release) should keep a close eye on deployments to avoid scenarios of thread/connection exhaustion on proxy components.  

Always ensure the number of available threads/connections is sufficiently sized for the number of logged-in (concurrent) user sessions. The "max allowed" connections may need to be set to an arbitrarily high value to support browser behavior without introducing any performance bottlenecks.

Such changes to proxy components are usually safe to make due to the nature of traffic that is passing through, which are mostly waiting long-polls, and not passing through constant volumes of data.

Also, ensure that any proxy components are capable of supporting HTTP (GZip) compression. This can radically reduce the network bandwidth requirement since an HTTP compression scheme is utilized. 

There may be an increase in CPU utilization on proxy components following the activation of compression support, so closely monitor CPU usage on proxy components following any configuration changes.

Load testing and AMB 

* * *

Many customers employ load-testing tools to validate performance and response times. However, many load-testing tools/scripts are designed around a synchronous communication model (where the client initiates a request and receives a response) and not with _asynchronous_ communication (where the response is "initiated" by the application back to the client) such as with platform features that utilize AMB.

The asynchronous nature of AMB can be incompatible with some load-testing tools and therefore an obstacle for customers who want to perform an "AMB load test." A complete understanding of the AMB architecture and functionality is necessary to achieve an appropriate set of test plans that faithfully replicate browser client-side behavior.

If you need help with load testing, contact your account manager.

Common Misconceptions - User Presence uses AMB 

* * *

User Presence is a UI16 feature that enables you to see the other users that are online when you are working in an instance. 

![](sys_attachment.do?sys_id=ba4d28a2db82b450e515c223059619e1)

Avatars are displayed in form headers and in multiple other places such as activity streams, visual task boards, live feeds, and Connect conversations. Online status is represented by a dot on the user's avatar. 

A common misconception is that the User Presence feature utilizes the AMB protocol. However, this is not the case. Instead of AMB, the feature makes REST API calls to determine the status of logged-in users. The requests can be seen on the stats.do page of the instance and commonly take the following form:

-   **POST /api/now/ui/presence** – Updates the current user's presence information and returns an array of online users

A dedicated semaphore pool named "Presence" services presence requests to isolate them from other UI transactions. Also, a transaction quota rule is defined on the instance. This automatically cancels any presence requests that have been running for more than 10 seconds and helps mitigate the risk of the semaphore pool being saturated by presence requests.

In some cases, depending on the number of logged-in concurrent users, this specific feature can significantly increase the number of open connections required and lead to greater demands on required network bandwidth. The actual required bandwidth depends on several factors, including number of users, applications used, etc. For our largest customers, high watermarks of ~100Mbps have been seen. Individual experience varies. 

ServiceNow Engineering teams are presently researching alternative solutions to reduce the network bandwidth requirement in future releases. Customers with additional concerns should contact their Support Account Manager or [ServiceNow Customer Support](http://www.servicenow.com/support/contact-support.html "ServiceNow Customer Support").

  
 

Appendix 1 - Live update on form in localhost logs 

* * *

User 'a' opens incident INC0000001 for viewing. Following are some of the log markers shown:

2017-03-10 03:22:13 (098) http-14 New transaction 7700C52313597200D4C050F32244B04E #10960 send /amb/meta/subscribe

2017-03-10 03:22:13 (105) AMB-thread-5 7700C52313597200D4C050F32244B04E record-watcher: channel-add: channel /rw/default/incident/c3lzX2lkPTljNTczMTY5YzYxMTIyODcwMDE5MzIyOWZmZjcyNDAw

2017-03-10 03:22:13 (106) AMB-thread-5 7700C52313597200D4C050F32244B04E record-watcher: responder-add: default

2017-03-10 03:22:13 (190) AMB-thread-5 7700C52313597200D4C050F32244B04E record-watcher: cache-change: <none>:<p>:insert:incident

2017-03-10 03:22:13 (191) AMB-thread-5 7700C52313597200D4C050F32244B04E #10960 send /amb/meta/subscribe -- total transaction time: 0:00:00.093, transaction processing time: 0:00:00.093, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: 10.255.29.64, chars: 0, uncompressed chars: 0, SQL time: 2 (count: 4), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:22:13 (349) http-14 New transaction 7700C52313597200D4C050F32244B04E #10961 send /amb/meta/subscribe

2017-03-10 03:22:13 (356) AMB-thread-7 7700C52313597200D4C050F32244B04E #10961 send /amb/meta/subscribe -- total transaction time: 0:00:00.007, transaction processing time: 0:00:00.007, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: 10.255.29.64, chars: 0, uncompressed chars: 0, SQL time: 0 (count: 2), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:22:13 (498) http-14 New transaction 7700C52313597200D4C050F32244B04E #10962 send /amb/sn/rp/incident/9c573169c611228700193229fff72400

2017-03-10 03:22:13 (526) AMB-thread-8 7700C52313597200D4C050F32244B04E Published amb message, sys\_id:d435c52313597200d4c050f32244b069

2017-03-10 03:22:13 (527) AMB-thread-8 7700C52313597200D4C050F32244B04E #10962 send /amb/sn/rp/incident/9c573169c611228700193229fff72400 -- total transaction time: 0:00:00.028, transaction processing time: 0:00:00.028, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: 10.255.29.64, chars: 0, uncompressed chars: 0, SQL time: 20 (count: 3), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:22:13 (556) glide.amb.cluster.synchronizer New transaction 7700C52313597200D4C050F32244B04E #10963 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400

2017-03-10 03:22:13 (563) AMB-thread-6 7700C52313597200D4C050F32244B04E #10963 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400 -- total transaction time: 0:00:00.008, transaction processing time: 0:00:00.008, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: , chars: 0, uncompressed chars: 0, SQL time: 0 (count: 2), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

User 'a' then makes a change to a field on the form and clicks the **Update** button.

At the same time, user 'b' is also viewing incident INC0000001. User 'b' sees the form dynamically update due to the change made by user 'a.'  This happens as the user is subscribed to the channel **/rw/default/incident/c3lzX2lkPTljNTczMTY5YzYxMTIyODcwMDE5MzIyOWZmZjcyNDAw** where it is able to receive dynamic updates:

2017-03-10 03:42:31 (471) glide.amb.cluster.synchronizer New transaction 1AE8416713197200D4C050F32244B0E8 #11290 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400

2017-03-10 03:42:31 (478) AMB-thread-5 1AE8416713197200D4C050F32244B0E8 #11290 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400 -- total transaction time: 0:00:00.006, transaction processing time: 0:00:00.006, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: , chars: 0, uncompressed chars: 0, SQL time: 1 (count: 3), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:42:32 (726) http-32 New transaction 1AE8416713197200D4C050F32244B0E8 #11292 send /amb/sn/rp/incident/9c573169c611228700193229fff72400

2017-03-10 03:42:32 (733) AMB-thread-8 1AE8416713197200D4C050F32244B0E8 Published amb message, sys\_id:8ad9c52313597200d4c050f32244b072

2017-03-10 03:42:32 (733) AMB-thread-8 1AE8416713197200D4C050F32244B0E8 #11292 send /amb/sn/rp/incident/9c573169c611228700193229fff72400 -- total transaction time: 0:00:00.008, transaction processing time: 0:00:00.008, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: 10.255.29.64, chars: 0, uncompressed chars: 0, SQL time: 2 (count: 4), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:42:32 (783) glide.amb.cluster.synchronizer New transaction 1AE8416713197200D4C050F32244B0E8 #11293 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400

2017-03-10 03:42:32 (790) AMB-thread-5 1AE8416713197200D4C050F32244B0E8 #11293 receive /amb/sn/rp/incident/9c573169c611228700193229fff72400 -- total transaction time: 0:00:00.007, transaction processing time: 0:00:00.007, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: , chars: 0, uncompressed chars: 0, SQL time: 0 (count: 2), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0

2017-03-10 03:42:39 (058) http-32 New transaction 1AE8416713197200D4C050F32244B0E8 #11295 /api/now/ui/presence

2017-03-10 03:42:39 (065) Presence-thread-12 1AE8416713197200D4C050F32244B0E8 #11295 /api/now/ui/presence Parameters -------------------------

    sysparm\_auto\_request=true

    cd=1489146160038

    api=api

2017-03-10 03:42:39 (069) Presence-thread-12 1AE8416713197200D4C050F32244B0E8 #11295 /api/now/ui/presence -- total transaction time: 0:00:00.011, transaction processing time: 0:00:00.010, total wait time: 0:00:00.001, session wait: 0:00:00.000, semaphore wait: 0:00:00.001, source: 10.255.29.64, chars: 334, uncompressed chars: 591, SQL time: 0 (count: 5), business rule: 0 (count: 0), phase 1 form length: 0, largest chunk written: 324, request parms size: 144, largest input read: 434

2017-03-10 03:42:41 (065) glide.amb.cluster.synchronizer New transaction 1AE8416713197200D4C050F32244B0E8 #11298 receive /amb/rw/default/incident/c3lzX2lkPTljNTczMTY5YzYxMTIyODcwMDE5MzIyOWZmZjcyNDAw

2017-03-10 03:42:41 (078) AMB-thread-5 1AE8416713197200D4C050F32244B0E8 #11298 receive /amb/rw/default/incident/c3lzX2lkPTljNTczMTY5YzYxMTIyODcwMDE5MzIyOWZmZjcyNDAw -- total transaction time: 0:00:00.013, transaction processing time: 0:00:00.013, total wait time: 0:00:00.000, session wait: 0:00:00.000, semaphore wait: 0:00:00.000, source: , chars: 0, uncompressed chars: 0, SQL time: 4 (count: 6), business rule: 0 (count: 1), phase 1 form length: 0, largest chunk written: 0, request parms size: 0, largest input read: 0
