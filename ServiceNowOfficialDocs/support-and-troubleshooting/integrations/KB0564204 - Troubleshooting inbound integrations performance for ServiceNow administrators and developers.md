---
title: "Troubleshooting inbound integrations performance for ServiceNow administrators and developers"
aliases:
  - KB0564204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564204
kb_number: KB0564204
last_modified: 2026-05-08
---

## Troubleshooting inbound integrations performance for ServiceNow administrators and developers

  

### Issue

This article addresses some concerns that occur when troubleshooting (or designing) an inbound integration. This article uses the term "inbound" to mean an integration where ServiceNow is the _provider_ as opposed to the _consumer_. In other words, an inbound integration is one that originates from outside ServiceNow. The primary audience of this document is customer developers who build integrations that pull data out of, or push data into, ServiceNow.

## Table of Contents

-   [ServiceNow Application Node Architecture and Integration Semaphores](#mcetoc_1ifipd49u4nd)
-   [Favor More Quick Transactions Over Fewer Slow Transactions](#mcetoc_1j0d3d2i581f)
-   [When using the /api/now/table API](#mcetoc_1iiv5vgqpao)
    -   [Use the sysparm\_no\_count Argument](#mcetoc_1iiv5vgqpao) 
    -   [Use the pagination with sysparm\_limit, sysparm\_order, and sysparm\_offset](#mcetoc_1j0d3d2i581g)
    -   [Use the sysparm\_fields operator](#mcetoc_1j0d3d2i581h)
    -   [Consider if Table API is the right solution](#mcetoc_1jkordind6)
-   [User and session management](#mcetoc_1iiv5vgqpap)
    -   [Integration User Setup](#mcetoc_1iiv5vgqpaq)
    -   [Session Handling](#mcetoc_1ifipd49u4ng)
-   [Data imports](#mcetoc_1ifipd49u4nh)
    -   [Text indexing](#mcetoc_1ifipd49u4ni)
    -   [Set the appropriate Web Service Import Set mode](#mcetoc_1ifipd49u4nj)
    -   [Scripts triggered from transform maps or insert/update operations](#mcetoc_1ifipd49v4nk)
    -   [Make an implementation-specific assessment of third-party import tools (for example, Perspectium or SnowMirror)](#mcetoc_1ifipd49v4nl)
    -   [Test a Full Import Run](#mcetoc_1ifipd49v4nm)
-   [Routing Integration work to Worker Nodes](#mcetoc_1j0d3d2i581j)

## ServiceNow Application Node Architecture and Integration Semaphores

Application Nodes are Java Virtual Machines (JVMs) and every customer instance is comprised of a cluster of these JVMs. Each JVM is running the Tomcat Servlet which has a pool of HTTP threads to receive transactions from the internet. The Tomcat threads do not immediately process the transactions they receive, instead they put them into dedicated queues for distinct types of transactions. Then a pool of threads dedicated to each queue processes the transactions before sending back the response over another Tomcat thread when they are done. This queue and pool combination allows separation of processing between, for example, end user transactions and web service transactions. Semaphores protect each type of transaction from overloading the system and also from impacting each other.

Out of the box, each ServiceNow Application Node has a dedicated queue and pool of threads known as "API\_INT" semaphores designed to handle integration traffic. Each instance has 4 API\_INT semaphore threads and 50 slots in the API\_INT queue by default - note that in rare cases this can be customized by ServiceNow on a customer's behalf if needed. Traffic is mapped to the API\_INT queue based on a URL regex pattern and list of arguments located in the sys\_semaphore table.

![](/sys_attachment.do?sys_id=23b5ba0b47bbb69cf64de825126d4340)

If all API\_INT semaphores are busy handling transactions, any additional transactions will go in the queue. If the queue reaches its max capacity (50 by default) it will start immediately rejecting any new incoming transactions with the HTTP code 429. This is known as semaphore exhaustion and ServiceNow has automated alerts to notify customers when this occurs (see [KB0635977 Integration Semaphore (SOAP/API\_INT) Exhausted on instance alert](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635977 "KB0635977 Integration Semaphore (SOAP/API_INT) Exhausted on instance alert")). When troubleshooting a semaphore exhausted alert the cause may be a systemic bottleneck (for example, database overload, Application node out-of-memory, etc.) or the cause may be specific to the nature of the transactions. For example, a burst of 1,000 transactions sent all at once, each taking 10 second to process, may quickly overload the API\_INT semaphore queue and the designer of the integration should introduce some rate limiting in their design.

## Favor More Quick Transactions Over Fewer Slow Transactions

As explained above, your ServiceNow instance is comprised of a cluster of JVMs with a finite number of API\_INT threads dedicated to processing integration traffic. If all the API\_INT threads get used up on a node, any additional requests will go into the queue and incur wait time. If some of your integration traffic is taking a long time to complete, then it is possible that other integration traffic will not have available resources to process their requests. For this reason it is recommended to keep the processing time for each individual integration request very short.

The below chart shows how many requests of various execution times could be safely executed given a certain period of time. Assuming your instance has 4 API\_INT threads, each node could handle the following volumes with relative levels of safety. Safe is determined as taking 25% or less of available resources. Warning is determined as 50%. Danger is determined as anything above 100%. Mostly this chart has been created to help visualize how impactful slow requests can be and the advantage of using many smaller requests over a few larger requests. In the real world, of course, request frequency fluctuates from minute to minute and your instance will have a mix of requests taking different durations. By favoring many fast requests over a few slow transactions you give the instance the best chance to evenly load balance requests across the cluster and avoid too many slow requests all landing on the same node at the same time.

There is no official recommendation for how quickly integration requests must complete, however, a general guidance that our team gives is to aim for 50 milliseconds per request and try to never have a request longer than 500 milliseconds. In order to keep your request execution time low, you may need to consider how you can break large processing requests into smaller chunks with techniques like pagination or queueing.  Also, keep in mind that requests will automatically timeout after 5 minutes, so you definitely don't want your requests to run anywhere near that. 

![](/sys_attachment.do?sys_id=27b5ba0b47bbb69cf64de825126d4322)

## When using the /api/now/table API

### Use the sysparm\_no\_count Argument 

Every time a request is made to the /api/now/table API, there are two queries that are executed. One query returns the records that match the filter and the other query returns the count of matching records. This second query is never necessary. For large scale integrations this extra query can add a great deal of extra pressure on your ServiceNow instance. Always add the following REST parameter to your requests.

-   sysparm\_no\_count=true: This excludes the "SELECT COUNT(\*)" operation on the database, improving transaction response time and saving database resources

Refer: [https://developer.servicenow.com/dev.do#!/reference/api/yokohama/rest/c\_TableAPI](https://developer.servicenow.com/dev.do#!/reference/api/yokohama/rest/c_TableAPI)

If you need to see the number of returned records due to pagination requirements, then you can still see the total number of returned records in each request by looking at the header `"X-Total-Count"` that sends the number of records being returned. This is true even when sysparm\_no\_count has been set to true.

### Use the pagination with sysparm\_limit, sysparm\_order, and sysparm\_offset

For Large data sets, use pagination parameters like sysparm\_limit, sysparm\_order and sysparm\_offset to retrieve records in smaller chunks.​

See [https://www.servicenow.com/docs/csh?topicname=c\_TableAPI.html&version=latest](https://www.servicenow.com/docs/csh?topicname=c_TableAPI.html&version=latest) for official documentation.

#### sysparm\_limit

This restricts the number of records that can be returned in a single request. It is recommended to keep this number as low as required in order to keep your requests executing quickly. This parameter defaults to 10,000, however, this may need to be much lower than 10,000 to keep your requests within safe thresholds. Often the thing that is making the Table API slow is the Access Control Lists (ACLs) that must execute against every record before it can be sent to a user. It is not uncommon for ACLs to take 50 milliseconds per record, so with 10,000 records that adds up to over 8 minutes of processing for ACLs alone! You might need to keep your batch size very small - as low as 10 records per batch - if this is the case.

#### ORDERBY ORDERBYDESC

The ORDERBY parameter controls what field or fields are used to order the results. The ORDERBY parameter must used within the value side of the key/value parameter sysparm\_query. For example, to get all active incidents in ascending order, ordered by their sys\_created\_on value, you would use "sysparm\_query=active=true^ORDERBYsys\_created\_on". By default ORDERBY uses ascending order - i.e., ordered so that it returns with the lowest numerical values first. You can reverse this by using the ORDERBYDESC parameter instead. A common pagination technique is to pick a highly unique chronological field to order your results and start each new pagination request with the last value of that field from the previous request. For example, if you are requesting 100 records at a time and ordering ascending by the number field, and the last record received was INC100234, then you could start your next request with the following parameters "sysparm\_query=number>INC100234^ORDERBYnumber&sysparm\_limit=100".

If the field you pick is not totally unique, you will not be able to simply use the Greater Than > or Greater Than Or Equal To >= operator. You will need to consider some type of duplication check and protection against requesting the same window of records over and over.

#### sysparm\_offset

This parameter is used to specify the starting point of the window of results that you want to return. Suppose you are requesting records from a table 100 records at-a-time. After your 10th request you want to get the next hundred records starting at 1,000, so you could include the following parameters "sysparm\_limit=100&sysparm\_offset=1000".

Beware that the sysparm\_offset operator can be very inefficient when the offset becomes in the hundreds of thousands. This is because the database must scan through many records to get to the start of the offset. If your offset is going to get that high it is probably better to use sysparm\_limit with ORDERBY and Greater Than condition on a chronological field.

### Use the sysparm\_fields operator

By default the Table API returns all fields from the target table. This can be incredibly slow as each field will take some amount of time to process. It is highly recommended to only include the necessary fields when using the Table REST API. The sysparm\_fields parameter receives a comma-separated list of fields to return in the response. Invalid fields are ignored.

### Consider if Table API is the right solution

ServiceNow offers many different options for integrating and Table API is not the best suited for every use case. In particular, Table API is not well suited for large scale data export of logs or other ephemeral data. A more robust solution like Stream Connect might be a much better option. The below referenced blog post from ServiceNow's community site has a flow chart that is very helpful to consider which ServiceNow Integration strategy is best suited for your business needs. The document was written by Jochen Geist (Principal Platform Architect in ServiceNow's Impact organization) and had been kept up-to-date as of March, 2026:

[Integration Design - How to choose the best pattern to integrate ServiceNow with other systems](https://www.servicenow.com/community/architect-blog/integration-design-how-to-choose-the-best-pattern-to-integrate/ba-p/2874114 "Integration Design - How to choose the best pattern to integrate ServiceNow with other systems")

The diagram below can be downloaded from the Community site link above or you can [click here for a MyNow presentation about Integration Best Practices](https://mynow.servicenow.com/now/best-practices/assets/integrations-integrations-workshop-presentation).  
![](/sys_attachment.do?sys_id=ebb5ba0b47bbb69cf64de825126d4344)

## User and session management

### Integration User Setup

Ensure that each one of your integrations uses a separate user account. It may be convenient to use a generic user account such as "sn.integration.user" for ALL integrations, but this is not a good practice. If you have dedicated accounts for each of your integrations, then it is easy to troubleshoot the specific integration causing the issue. Also, if you want to quickly switch off a single integration in an emergency, an administrator can lock out a specific account.

It seems obvious, but integrations should use a local user account as opposed to a remotely authenticated account type (for example, LDAP). Having remotely authenticated integration users can add excessive overhead to the integration request process and cause serious performance issues.

### Session Handling

As stated above, each production instance of ServiceNow uses an application _cluster_ to divide processing requirements across at least two physical application (app) servers and a variable number of _nodes (_Apache Tomcat instances wrapping ServiceNow code) hosted on those app servers. To ensure sessions are evenly distributed between the various Tomcats in the instance cluster, ServiceNow routes all incoming transactions through a load balancer inside our networkIf a transaction contains a certain cookie (provided in a previous response), then the load balancer sends the transaction to the application server specified in the cookie. If the cookie is not provided, then the transaction is arbitrarily routed to one of the nodes in the cluster based on an algorithm in the load balancer.

When the transaction reaches the node, the Tomcat servlet checks for the presence of a second cookie. This second cookie is used to determine if the user related to the given transaction has already been authenticated. If the cookie is present, then the transaction is associated with an existing session object. If the cookie is not present, then the transaction must be authenticated and a new session object is created.

![](/Integations%20-%20LoadBalancingSessions.pngx)

Understanding how cookies are used in ServiceNow session management is an important factor in determining how to design your inbound integration.

In most cases, a simple web service client does not include cookies in each subsequent request. Because the cookies are not included, ServiceNow does not know to use the same session as the previous request and creates a new session in Java for each request. If there are too many sessions in Java, the application can run out of memory, to mitigate this risk ServiceNow sets a short session timeout value (5 minutes by default) for all integration traffic. The default integration timeout value can be overwritten in the "GetIntegrationSessionTimeout" Installation Exit.

The ServiceNow product documentation recommends that you always include cookies so that your integration uses persistent sessions. This avoids excessive session creation and memory issues. However, this method also has potential drawbacks.

-   If cookies are included to ensure persistent sessions, the integration "sticks" to a single node. This might mean that one of your nodes receives a lot more integration traffic than the others and may become overloaded. Users logged into that node may experience sub-optimal performance.
-   Using persistent sessions can also potentially be a problem because it "un-parallelizes" the integration. The ServiceNow application only allows one transaction per session at a time. This behavior is called **session synch**. When integrations are not using persistent sessions, they use an asynchronous model. This allows parallel requests from the same integration to be processed at the same time. However, when integrations are using persistent sessions, session synch causes the integration to use a synchronous model where each request must wait for the previous one to complete.

Before creating a new integration, consider the impact of your session management configuration. The following is not an exhaustive list of considerations, but can demonstrate the principles involved.

#### What Session Management Option is Best for My Performance?

There is no one-size-fits-all answer to this question. To determine what model is going to work best for your situation, review your specific business case. Consider:

-   how many requests will be sent from the integration per second (**frequency**)?
-   how long will it take to process each request (**duration**)?

As stated earlier, if your integration is including the cookies to achieve persistent sessions, then a feature called **session synch** limits integration to 1 operation at a time. This means that if you send more requests than the number that can be processed in a timely manner, your requests start to accumulate **wait time**. Before you configure your integration for session persistence, consider if your duration and frequency rates require more than one operation to be processed at a time. If your duration multiplied by your frequency is greater than 1, then your integration will start to fall behind.

\[Duration\] \* \[Frequency\] < 1

So, for example, you have an integration that has a maximum frequency of 10 requests per second and a highest expected response time of 200 milliseconds per request. Given these assumptions, after only one second of peak activity, 1 second of wait time is built up.

.2 seconds Avg. duration of request \* 10 requests per second = 2 seconds of processing  
(This causes an integration with persistent sessions to fall behind 1 second for every second that transactions continue at this rate)

##### Rejected Requests  
\[Updated for the Paris release on Oct 26, 2020\]

##### Session Sync Limit

If your integration exceeds the threshold of requests that can be processed by a single thread, then any subsequent transactions start to queue. This might not be a problem if the queueing only happens for short periods of times. However, if there are more than 10 "waiters" for a single session, or the current executing transaction takes longer than 120 seconds, ServiceNow starts to automatically reject any additional requests to the same session. These requests are returned to the client with HTTP code 202.

##### Semaphore Queue Depth Limit

If your integration is not reusing session cookies then there is the possibility of overflowing the semaphore "queue". Each semaphore pool has a queue to handle waiting requests before processing. If too many requests are waiting in the queue, then new requests to that semaphore pool will be immediately rejected with HTTP 429. As of writing, Oct 26, 2020, the default queue depth of the Default semaphore pool is 150 and all other pools have a default depth of 50 max queued requests.

##### What you can do

If the frequency/duration combination of your integration is too much to be handled synchronously, then your first step should be to try to improve the integration. Devise a way to process the requests more quickly or to reduce the frequency of requests per session. Determine if there is something that can easily be done to reduce the duration of your web service requests.

-   Are you querying a specific date range based on the incident.sys\_created\_on, but have no database index on that field?
-   Are you pulling back more data than you need? Can you reduce the number of records queried/updated? Can you reduce the number of fields supplied in the payloads?
-   Is there an inefficient business rule being executed (see the slow business rule log in Geneva or perform the same query through the UI while Debug Business Rules is turned on)?
-   Is your integration client set to re-use TCP connections (avoiding multiple SSL handshakes)?

If you have reviewed the efficiency of the operations being performed and determined that they are reasonably efficient, then you should look at ways to reduce the frequency of the requests. Often there is a way to reduce the frequency of requests at the web service client. Here are several options:

-   If you can control the number of requests sent out per unit of time on the client-side, this might be an easy way to throttle the integration down to workable levels.
-   To reduce the frequency of requests from a web service client, break it into smaller parts.
-   Have multiple active client threads, each with their own session. This can pose a maintenance challenge for the integration administrator, but might be worth considering. The more client threads that you divide your web service requests between, the more you can make use of ServiceNow's load balancing feature.
-   Do not reuse sessions. See the following section for more details about this option.

#### Do I Need to Reuse Sessions?

The best practice documentation in the product documentation encourages reuse of sessions. While this is the recommended best practice, many customers can safely implement their web services without reusing sessions by adjusting the factors that contribute to the amount of average active sessions per node.

Most customers do not reuse sessions for web services. This allows each request to get load balanced across the instance cluster for better scalability. Session build up is less of an issue because glide.integration.session\_timeout default is now 1-minute and can be overwritten via system property or in an Installation Exit (sys\_installation\_exit table).

Frequency and session timeout length are the main factors that affect the number of active sessions. For example, you have an integration that sends a request approximately every 5 seconds. If you have a 1-hour session timeout on your instance with 2 nodes and you are not reusing sessions, this results in about 360 active sessions per node at any given point in time. 

1 \* 60 \* 60 / 5 / 2 = 360

\[Session timeout\] / \[Avg. requests per second\] / \[Number of nodes\] = \[Avg. active sessions per node\]

By lowering the global session timeout value of your instance (glide.ui.session\_timeout), you can reduce the number of active sessions at any given point in time. The base system value for this property is 30 minutes. In Fuji Patch 7 and later versions of ServiceNow, an independent timeout value for integration users is available. By default, the integration timeout value is set to 5 minutes and can be configured independent of the global glide.ui.session\_timeout using the GetIntegrationSessionTimeout Installation Exit.

Another question is, how many active sessions is too many? You can estimate if your system will run out of memory due to a high number of sessions. To see how many sessions are being used on each node of your instance, view the ServiceNow Performance homepage. Check the 30-day view and note the max session values per node trend.

![](/30DaySession.pngx)

For more information, see [ServiceNow Servlet](https://docs.servicenow.com/bundle/tokyo-platform-administration/page/administer/platform-performance/concept/c_ServiceNowServlet.html "ServiceNow Servlet").

Also on the ServiceNow Performance homepage, check how close you are to the heap memory threshold. Generally, memory should not be spiking above 80% usage on a regular basis (1.6k). There have been cases where 7,000 active sessions have taken 85% of heap memory. From these figures, we can generally estimate that every 820 users represents about 10% of available memory (heap memory is fixed at 2GB per node). The overall memory usage of your instance also depends on other factors of your ServiceNow usage. If your normal memory garbage collection goes from 50% to 70% (1k to 1.4k), then adding another 10% of consistent memory usage (820 active user sessions per node) might put you over the edge.

![](/Integrations30DayHeap.pngx)

  

## Data imports

* * *

When planning go-live and ongoing large scale data imports, consider the points in this section. These are often overlooked and can cause import processing delays as well as performance degradation across the instance:

### Text indexing

For initial large scale data imports (more than 500k records in quick succession), do the following:

-   Turn off text indexing on the target table. For each of the records being imported, a text\_index event is inserted into the sysevent table. By flooding the sysevent table, the inserts get progressively slower (5 – 6 seconds per row). This exponentially increases the time your import takes to run. More importantly, it also severely impacts the "normal" operation of an instance (remember that the sysevent table holds text index events, metric update events and all "regular" events in the default event queue). The most common symptom is that notifications are not generated, but many other actions can be delayed.
-   After the import is complete, re-enable the text index property on the collect record in sys\_dictionary. Take this opportunity to fine-tune the fields that are text searchable. This is especially important for CMDB tables, sys\_user, and any table that is likely to have multiple/frequent updates to inconsequential fields. Adding the no\_text\_index=true attribute to all fields you do not want to be searchable by Zing improves performance for searching for artifacts you do want searched, as well as reducing the overheads on event processing.

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><p><strong>Note</strong>:&nbsp;<span style="text-align: start;">In order to make&nbsp;the data that was imported while text indexing was turned off available through text search, run a separate re-indexing operation for the relevant table(s). For more information, see&nbsp;<a title="Regenerate a text index for a table" href="https://docs.servicenow.com/bundle/tokyo-platform-administration/page/administer/search-administration/task/t_RegenerateATextIndexForATable.html" target="_blank" rel="noopener noreferrer">Regenerate a text index for a table</a>.</span></p></td></tr></tbody></table>

### Set the appropriate Web Service Import Set mode

By default no two Import Set Transform Maps can be executed on the same staging table and target table at a time. This is to avoid duplicates or out-of-order updates being created by two Import Sets trying to touch the same target record at the same time. In order to enforce this behavior, the thread that is executing the Transform Map will obtain an exclusive database lock - also called a "mutex" - for the duration of the Transform Map execution. In the case of multi-threaded web service imports, this sometimes leads to performance issues because many threads are fighting for the same mutex. In the logs you will see messages similar to "Mutex ImportSetTransformer.incident\_ acquired after spinning X times". If the performance issues are bad enough, this can cause the API\_INT queue to become overloaded and all new inbound web service requests will be rejected with HTTP code 429 - indicating a queue overload.

If you have a web service Import Set that will be multi-threaded (meaning more than one transaction may come into ServiceNow at one time) then you may want to override the default behavior of enforcing the ImportSetTransformer mutex. You can control the import set mode in the following ways:

1.  In import sets that specify one or more coalesce fields, records with a matching coalesce value are transformed from source to target table serially (one at a time) to prevent duplicates. In import sets that do not specify any coalesce field, records are transformed concurrently. You can control this behavior using the glide.import\_set\_insert\_serialized\_when\_no\_coalesce property.  
     
2.  The system property glide.soap.import\_set\_insert\_serialized.<table name>, controls how the instance inserts records from web service calls into a specific import set table. When true, this property prevents identical simultaneous inserts from creating duplicate records by serializing the database insert operations. If a target table does not have any coalesce fields defined in a transform map or you are certain that there is no danger of two threads making duplicate or out-of-order updates to the same target record, then set this property to false to improve web service import set performance. The property glide.import\_set\_insert\_serialized.<table name> provides the same functionality.

   

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><p><strong>Note</strong>: Setting&nbsp;these properties to false can result in the creation of duplicate records or out-of-order updates<span style="text-align: start;">. For more information, see <a title="Web service import set mode: Controlling insert behavior" href="https://docs.servicenow.com/csh?topicname=r_ImportSetMode.html&amp;version=latest">Web service import set mode: Controlling insert behavior</a>.</span></p></td></tr></tbody></table>

### Scripts triggered from transform maps or insert/update operations

Be aware of business rule / transform map logic that is triggered by the import. If there are synchronous business rules / transforms that perform sub-optimal glide record queries (for example, Pull data from large un-indexed record sets), this increases the execution time of importing each record. This gets progressively slower as the datasets increase (see point about full-run tests). Continual requests for large un-indexed datasets also flush the buffer pool on the database, which has a negative impact on the entire instance. If a slow operation like this is identified, see if the operation can be improved by following best practices for scripting and query execution.

One way to improve the speed of an import is to move slow script execution to an Asynchronous Business Rule. The import itself can complete without having to wait for the slower scripts to complete. However, be very careful about using Asynchronous Business Rules because you are essentially creating a multi-threaded situation. When moving some operation to a multi-threaded design, ask yourself if anything is dependent on the completion of the operation. If something is dependent on the completion of an asynchronous operation, then there is the potential for a race condition. For example, suppose you are importing tasks and filling in the category and sub-category fields with an asynchronous business rule. Then, suppose you have a business rule that fires on insert and assigns the incident to a certain assignment group based on the incident category and sub-category. If the asynchronous business rule takes long enough to complete, this could result in unexpected behavior. This is just a simplified example, but you should consider the pattern. What could happen if the operation you are running asynchronously takes 10 seconds to complete?

One last thing that should be considered is the **Run Business Rules** option. If you are using a transform map for your import, take notice of the **Run Business Rules** option on the Transform Map form. Whenever possible, this option should be cleared. Clearing the option tells the system to bypass all scripts, engines, auditing, and the customer update tracking mechanism (usually not applicable to tables that are the target of an import). Before doing this, of course, you should make sure that you do not need any of those to run – if you need only one or two business rules to run, you might want to replicate the logic in those rules in a transform map script so you can clear the option and avoid the other costly operations of the scripts and engines. Clearing **Run Business Rules** often saves 50-90% of execution time for an import. To see the full list of items that are skipped by clearing the **Run Business Rules** option, [Execution order of scripts and engine](https://docs.servicenow.com/bundle/tokyo-application-development/page/script/general-scripting/reference/r_ExecutionOrderScriptsAndEngines.html "Execution order of scripts and engine"). 

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;Clearing the Run Business Rules option does&nbsp;<span style="text-align: start;">not bypass the update of the sys_ fields (sys_created_on, sys_created_by, sys_updated_on, sys_updated_by, sys_mod_count)</span>.</td></tr></tbody></table>

### Make an implementation-specific assessment of third-party import tools (for example, Perspectium or SnowMirror)

Third-party tools that successfully export data from ServiceNow also advertise the capability to import data into another instance. Their products are typically only tested at a generic level and do not take into account the text indexing policies and custom logic that may be implemented in the target instance. Even if you have successfully leveraged one of these replication buses in another project, take time to check how the engine will behave with a particular instance.

If the tool of choice relies on scheduled jobs to poll for/subscribe to information from an external source, check the number of scheduled jobs that have been provisioned for this purpose. Remember that each node in the cluster is checking in for 'past due' jobs every 30 seconds. If you have 20 subscriber jobs configured, then the first node to check in to the queue picks all of them up (as long as there is space in his scheduler queue). They then sit in the scheduler queue on that node, waiting for the 8 schedulers process the initial 8 jobs. 

Also, verify that the priority of critical scheduled jobs, such as the events processors (various), SMTP sender, and POP reader, are set to 25. This ensures that core platform functionality can proceed normally if the scheduler workers are conducting import-related activities.

Finally, check for any custom table that is used as part of the replication bus to 'stage' the incoming data. Staging tables (those that extend from sys\_import\_set\_row) are cleaned by the scheduled job named Import Set Deleter. You can access the configuration of this job by navigating to **Sys Import Sets > Scheduled Cleanup** in the application navigator. The data retention period for this job is set for 7 days, but often needs to be set to a shorter period of time. If the retention period is set for, say, 7 days and you perform an import of millions of records over a couple days, the import staging tables will grow very large (perhaps multiple Gb), causing the insert/update transactions to take longer and longer as more and more data is processed.

### Test a Full Import Run

Performing a full import is an important part of checking that data transforms correctly and in a timely fashion without affecting other platform components. It is possible to pass over something that seems inconsequential, or to just plain miss something, that can ultimately causes issues when it running your import in production. 

## Routing Integration work to Worker Nodes

For customers with large installations, sometimes the ServiceNow nodes may be split into different node types. The most common split is to have nodes split into UI versus Worker nodes. When a UI/Worker split is implemented, Worker nodes are removed from the load balancer pool and do not take any inbound traffic. UI nodes, conversely, run only critical system jobs and do not take any of the background processing workload. This protects UI traffic from being impacted by application layer resource contention from the background processing workload. However, this protection comes at a cost.

Since Worker nodes are removed from the load balancer pool, they do not take any Integration traffic either. This means that all the Integration traffic gets concentrated on the UI nodes while the Worker API\_INT queue sits idle - a potential waste of resources on Worker nodes as well as a potential risk for UI nodes since the combination of all UI traffic plus all Integration traffic may overload system resources. In order to allow Integration traffic to run on Worker nodes, ServiceNow creates a dedicated Load Balancer pool and corresponding URL. Normally the name of the Worker node URL will be the normal URL plus the word, "worker". So, if your normal ServiceNow URL is acme.service-now.com, then the Worker URL would be acmeworker.service-now.com. By pointing Integration traffic to the Worker URL pressure can be offloaded from the UI nodes to the Worker nodes. This needs to be done by the owners of the various Integration clients who are consuming ServiceNow's web service endpoints.

### Release

All versions

### Resolution

Recommendations for Optimal Instance Performance: [https://www.servicenow.com/community/now-platform-articles/recommendations-for-optimal-instance-performance/ta-p/2308391](https://www.servicenow.com/community/now-platform-articles/recommendations-for-optimal-instance-performance/ta-p/2308391)

Developer Portal: Technical Best Practices: [https://developer.servicenow.com/dev.do#!/guides/tokyo/now-platform/tpb-guide/scripting\_technical\_best\_practices](https://developer.servicenow.com/dev.do#!/guides/tokyo/now-platform/tpb-guide/scripting_technical_best_practices)

KB0829067 Performance Resource Page: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0829067](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829067)

Technical Support 24/7: [http://www.servicenow.com/support/contact-support.html](http://www.servicenow.com/support/contact-support.html)
