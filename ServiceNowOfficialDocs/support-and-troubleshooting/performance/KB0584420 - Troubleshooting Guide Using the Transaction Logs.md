---
title: "Troubleshooting Guide: Using the Transaction Logs"
aliases:
  - KB0584420
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0584420
kb_number: KB0584420
last_modified: 2026-04-23
---

## Troubleshooting Guide: Using the Transaction Logs

  

### Issue

<table style="border-collapse: collapse; width: 100%;" border="1"><colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup><tbody><tr><td>Originally written</td><td>2016</td></tr><tr><td>Lastest revision</td><td>Oct 20, 2025</td></tr></tbody></table>

You can use the information in this troubleshooting guide to help track down the cause of an issue by examining the relevant entries in the Transaction Log table.

One key technique for understanding an issue is to track down the historical transaction details related to a reported example. The key to finding transaction details is using the Transaction Logs table \[syslog\_transaction\]. This article describes the features and usage of this table. The details in this table are very rich and might provide enough information to solve the issue. Even if they do not provide enough information to solve an issue, they can provide many leads that you can investigate.

![](sys_attachment.do?sys_id=b77411dc970f7e5068d477121153af6d)

### Using Transaction Logs to Troubleshoot Performance Issues

#### Where is the bottleneck?

One key question in any performance issue is "Where is the bottleneck?". Because the transaction logs show you the breakdown of where time is being spent it is helpful to understand the source of bottlenecks. The transaction logs include timings for server, client, SQL, business rules, client scripts, UI Policies, wait time, and more. By understanding what each of these fields means, you can be well on your way to isolating the cause of a given performance issue. 

#### What was the user doing?

By observing the **URL** field in the transaction logs you can determine what page the user was accessing. Also, in the case of a form submission, there will be parameters included in the transaction URL. Understanding the meaning of URL paths and the parameters included after the "?" can greatly assist in interpreting exactly what was happening in a given transaction. (For more information, see [Navigating by URL](https://docs.servicenow.com/ "Navigating by URL").)

By observing the **User Agent** field you can determine the browser and OS that the user was using. This information is very important if the issue is a client-side issue and you need to know how to reproduce the issue. Finding out the exact "Steps to Reproduce" an issue is an important part of troubleshooting any issue. Some issues can only be reproduced on a certain browser version and operating system combination, so the User Agent field can help piece this together. One thing that can be tricky is that User Agent strings may be difficult to decipher. A tool like [UserAgentString.com](http://www.useragentstring.com/index.php "UserAgentString.com") can help.

By observing the **IP address** field you can determine from what network a transaction originated. This information can be very helpful when diagnosing issues that seem to occur intermittently, impacting some users or regions, but not others. For example, the issue might occur when the user is logging on from within their corporate network, but not when logging in from their home network. Or perhaps performance issues are being reported by a certain user group located in the same geographic location. You might be able to prove that transactions coming from certain IP addresses are slower than others.

#### Where did the issue occur?

Because ServiceNow has a "clustered" architecture with multiple Java nodes, knowing where in the ServiceNow architecture a certain issue was experienced is important. The **Session ID** and **System ID** fields are key here. Session ID indicates all transaction related to a particular user's session. Sessions begin when a user logs in to a system. If the user must log in again, a new session is created. The default timeout for sessions is 30 minutes of inactivity. System ID tells you the node on which the issue occurred. Imagine a case where all transactions for one node were affected, but no transactions on the other nodes. This piece of information would be critical in isolating the possible cause. Knowing where the issue occurred is also important so that you can search through the detailed System Logs that are node specific (accessed via the Log File Downloader or Log File Browser).

#### What was happening during the period of impact?

This question often comes up when an issue was experienced by multiple users during a certain window of time, but then the issue stopped. You can use the Transaction Log table to determine the transactions or scheduled jobs that were executing during a given time period. Determining this information can be a little tricky. One reason is that the **Created** field in the Transaction Log table reflects the time the transaction completed, not the time when it started.

Take the following example as an illustration: Suppose a period of slowness was reported between 7:15 and 7:45 AM. Further, suppose that the root cause was a transaction that started at 7:10 AM and ended at 9:15 AM. Searching for all transactions created between 7:15 and 7:45 AM would not reveal the transaction that caused the issue because the transaction didn't finish until 9:15 AM and therefore would have a Created time of 9:15 AM.

There is another time stamp field that can help here. The field **Processing start time** (start\_process\_at) shows the time when a transaction was given a thread and actually began to be processed. This could be different from what the user thinks is the start time because there may be network wait, semaphore wait or session wait accumulated prior the start of transaction processing.

To find very long running transactions, you might want to search a broader time frame (perhaps an hour on either side of the period of impact) and include a condition for Response time that is greater than 120,000 milliseconds (or 2 minutes). This type of search should complete within 10 to 20 seconds, even if you are searching a 24-hour time span.

### How it works

The Transaction Log table \[syslog\_transaction\] captures many of the transactions that come through ServiceNow product. This includes user transactions, integration transactions (SOAP, REST, etc.) and background transactions (scheduled jobs). However, it does not capture the following types of transactions:

-   Some very short, asynchronous transactions like AJAX or Angular
-   Some high volume REST transactions
-   Asynchronous Message Bus (AMB) transactions for things like Record Watcher or Agent Chat
-   Transactions that did not complete do to failures or cancellation. There is different table to see cancelled transactions.

#### Note about the accessing the Transaction Log table

Because the Transaction Log table is very large, you should always exercise caution when querying it. For most customers, a 24-hour of time is the maximum span of time that should be queried on the Transaction Log table. Any more than that and the queries can become quite slow. However, if you have a specific filter on an indexed field you could query a larger period without trouble. For this reason, the modules that access the table (System Diagnostics > Transactions, System Diagnostics > Transactions (background), and System Diagnostics > Transactions (all users)) all have a default filter on Created On = Today and excluding any transactions initiated by the "guest" user. However, in some customer systems, even querying a 24-hour period might be too much for the system to handle in a reasonable amount of time. For that reason, the best practice is to first access the table by URL and use the sysparm\_filter\_only=true parameter to display only the list filter. From that point, you can specify a very limited query for only the information that you need. Try to specify the shortest time period required using a Between filter paired with some other restrictive filters such as Response time > 1000 or Created by = joe.employee.

NOTE: Seeing many transactions created by the "guest" user is perfectly normal behavior in ServiceNow. The "guest" user is just the user that the system attributes for transactions where the user is currently not authenticated, like if they access a public page or if they access a private page but are redirected to the login screen due to not being authenticated yet.

#### Steps to efficiently query for relevant log entries

1.  Find out the User ID of the person who experienced the issue from the user table (sys\_user).  
      
    
2.  Find out when they experienced it; down to the minute if possible.  
      
    
3.  Find out what that user was doing when the issue happened.  
      
    
4.  Log in to the instance as an admin user.  
      
    
5.  Go to <my\_instance\_name>/syslog\_transaction\_list.do?sysparm\_filter\_only=true.  
      
    
6.  Expand the graphical filter builder for the list and add the following filter to grab all transactions by that user around the reported time:  
    \[Processing start time\] \[between\] \[<some\_time\_before\_event>\] and \[<some\_time\_after\_event>\]  
    \[Created by\] \[is\] \[<user ID of affected\_user>\]  
      
    
7.  Click Run.  
      
    
8.  From the list of transactions that comes back, see if the URLs or response times seem to match the description of the issue that was given by the user.

Also of interest might be [KB0997495 - How to troubleshoot a slow transaction](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997495 "KB0997495 - How to troubleshoot a slow transaction").

### Definitions of the Fields of the Transaction Log table

If you haven't already done so, click the gear icon on the list to personalize the columns that are displayed in the list. The columns described in this section might be useful to you.

#### Server Metrics (listed alphabetically by field label)

-   **App Scope (app\_scope):** The parent scope from which the transaction was executed. This is the last application scope that the thread was in when the transaction ended. A given thread may go through many different application scopes during the course of execution.  
      
    
-   **ACL Time (acl\_time):** Total time in milliseconds spent executing Access Control Lists (ACL) for the transaction. Whenever an ACL executes (regardless of if the ACL answer is cached or not) there is a stopwatch that starts before execution and ends directly after execution. All these durations get added to the transaction's total ACL Time. This means that ACL Time includes any JavaScript, Java or SQL that gets executed in the course of executing the ACL. You should expect this time should be fairly low - under 1 second in most cases. One exception is when a large number of records are being shown to the end user, for example in a report or multi-row export. In those cases, it is expected that ACL time will increase linearly with the number of records being shown.  
      
    
-   **Business Rule Time: (business\_rule\_time)** The number of milliseconds spent executing Business Rules or Script Jobs. Script Jobs includes scheduled script executions and asynchronous Business Rules. This is inclusive of time spent downstream from the first Business Rule called. The timer starts once a Business Rule begins and stops only when that Business Rule is complete, including any time spent waiting on SQL to complete or any other Business Rules or processes that are triggered from the script of the top Business Rule. There are other ways that SQL can get triggered outside of Business Rules, so it is entirely possible that SQL Time may be listed as being greater than Business Rule time; however, you should keep in mind that whatever time spent running SQL was triggered by a Business Rule will be included in the calculation of Business Rule Time.  
      
    
-   **Created: (sys\_created\_on)** The moment the transaction was recorded. Note that transactions are recorded at the end of the transaction. Therefore, to determine the start time of a transaction (including scheduled jobs), you must subtract the Response time value from the Created time.  
      
    
-   **Created By: (sys\_created\_by)** The User ID (sys\_user.user\_name) of the user who performed the transaction. Most background/scheduled jobs are run by a special user called "system". Transactions initiated by a user's pre-authentication will be marked by a special system user called "guest".  
      
    
-   **IP Address: (ip\_address)** The source IP address of the transaction inbound to ServiceNow.  
      
    
-   **Interaction ID: (interaction\_id)** Corresponds to the interaction\_id field in the Client Interaction (sys\_client\_interaction) table. The Client Interaction table tracks groups of transactions related to a single user action in Next Experience based UI's, like Workspaces.  
      
    
-   **Transaction Number: (transaction\_number)** A sequential number, unique to the node where the transaction was executed, that starts at 0 when a node is restarted. This number can be used to find a transaction in the Node Logs.  
      
    
-   **Network Time: (network\_time)** As of Zurich, this is the time it takes the server to write all the bytes of the response to the output stream - not the time it takes to transmit those bytes across the internet. This is not what most people expect from a measurement named Network Time. It is much lower than what most people would expect, usually in the range of 0 to 5 milliseconds. This metric is mostly not helpful.  
      
    
-   **Processing start time** (start\_process\_at) shows the time when a transaction was given a thread and actually began to be processed.  
      
    
-   **Response Time: (response\_time)** The number of milliseconds spent by the server in fulfilling the transaction. Does not include server time spent prior to a redirect (HTTP 302). Does not include time spent on subsequent, partial page requests (i.e., AJAX) or serving up a resource (CSS, JavaScript, images, etc). Does include wait time from waiting for a semaphore or waiting for a previous transaction on the same session to complete. Therefore, this can be a confusing and inflated metric because some transactions may have 90% or more of their response time spent waiting for another transaction to complete. For this reason, "Transaction processing time" may give a better idea of what transaction is truly causing a slow down.  
      
    
-   **Script Time (script\_time):** Time taken in milliseconds evaluating JavaScript in the Mozilla Rhino engine. Note that, in ServiceNow, all configurable code as well as much of our out-of-box code and templating engine are implemented with JavaScript. The Rhino Engine has access to the Java layer and the entire platform, so Script Time in inclusive of anything executed as a result of a JavaScript call.  
      
    
-   **Semaphore wait time (semaphore\_wait\_time):** Wait time in milliseconds caused by all semaphores being in use.  
      
    
-   **Session: (session)** The Java session ID of the user who was logged in. This ID is useful for identifying log messages output by this same user in the System Logs. For background jobs the Session ID will contain the name of the worker that is executing the job.  
      
    
-   **Session wait time (session\_wait\_time):** Wait time in milliseconds caused by the same user session initiating a second transaction before the first has completed. The second transaction must wait until the first completes. Note that this default behavior has changed in Yokohama - see [KB0683357 Revised Session Sync - Increasing Transaction Concurrency](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0683357 "KB0683357 Revised Session Sync - Increasing Transaction Concurrency").  
      
    
-   **SQL Time: (sql\_time)** The number of milliseconds spent waiting for the request and response to the database. This can be artificially bloated in cases where a resource that is involved in handling the request/response to the database is overloaded (e.g., application server CPU, network bandwidth between app server and db server). One thing to note is that homepages employee multithreading and can execute multiple SQL statements simultaneously. SQL Time is the total of all SQL executed as part of a transaction on the main thread or child threads and therefore SQL time for home.do transactions is often greater than the total transaction processing time.  
      
    
-   **System ID: (system\_id)** This field includes the name of the node upon which the transaction was executed. System ID is also used in the sys\_trigger and sys\_cluster\_state tables.  
      
    
-   **Sys ID: (sys\_id)** The unique identifier of a Transaction Log record. The first 12 characters of the sys\_id are used as the transaction ID in the Node Logs. This will be displayed in the logs as "txid={first 12 of sys\_id}".  
      
    
-   **Table: (table)** The table that was displayed, for example, incident, change\_request.  
      
    
-   **Total wait time (total\_wait\_time):** Time in milliseconds that the transaction spent waiting before the server was able to process it. This is session\_wait\_time + semaphore\_wait\_time.  
      
    
-   **Transaction Pattern: (transaction\_pattern)** The unique hash code identifying an anonymized URL - this can be used to link a specific transaction in the logs with the Slow Transactions module (sys\_transaction\_pattern table).  
      
    
-   **Transaction processing time (transaction\_processing\_time):** Server response time, minus wait time. A good way to measure what transactions are actually using all the processing time. This time is inclusive of everything that happens inside ServiceNow's application, e.g., SQL queries, Javascript, template rendering, caching, ACLs, UI Policies, etc. Note that transaction processing time is not simply the combination of sql\_time + acl\_time + business\_rule\_time + cpu\_time. These various timers can overlap and no simple formula will suffice.  
      
    
-   **Type: (type)** The type of transaction (such as form or list).  
      
    
-   **URL: (url)** The destination address from the inbound HTTP request. In the case of Scheduled Job transactions, this will be the prefix "JOB:" followed by the name of the job.  
      
    
-   **User Agent: (user\_agent)** A user agent string is a unique identifier to identify the browser and operating system that initiated the transaction (see [http://www.useragentstring.com/index.php)](http://www.useragentstring.com/index.php%29).  
      
    
-   **View: (view\_id)** The View (sys\_ui\_view table) that was used for this form/list.

#### Client Transaction Timings

Timings that track operations on the client-side (i.e. on the browser or mobile device). Not available for all transaction types. Not available on Safari. Generally, client timings are only available for the "Core UI" of ServiceNow, however, as of 2025 some of these metrics are being supported for Next Experience transactions like /api/now/graphql, /$uxapp, /api/now/v1/batch, /api/now/uxf/databroker/exec, and so forth.

-   **Client Transaction: (client\_transaction)** True if the transaction has successfully recorded client timings.  
      
    
-   **Client Response Time: (client\_response\_time)** The number of milliseconds between navigationStart and loadEventEnd. In other words, the total time, including server time, between when a page was requested and the HTML load event completed firing. This would include onLoad client scripts and any onChange scripts that fired as a result. In other words, this is inclusive of server time, browser time, javascript and any time spent on the HTTP request or HTTP response. This is the most inclusive timing metric and therefore should be bigger than other times. There are exceptions to this rule, like SQL Time, that can count cumulative time from multiple threads.  
      
    
-   **Client Network Time: (client\_network\_time)** Reflects a calculated value.  
      
    -   For the **Core UI** transaction types, the client\_network\_time calculation is the total "duration" as measured as follows:  
          
            **\[End to end transaction duration\] - \[server time\] - \[browser render time\] = client\_network\_time**  
          
        -   You may notice slight inconsistencies with this formula for some transactions, but it is mostly accurate.  
              
            
        -   One item of note is that transactions that are directly preceded by an HTTP 302 redirect will reflect the transaction response time of the previous transaction in their client\_network\_time. This is the current behavior of the product and there is not a plan to change this behavior \[as of Oct 30, 2018\]. This is documented in [PRB632265](https://support.servicenow.com/problem.do?sysparm_query=number=PRB632265 "PRB632265"). This misattribution of server time as client network time is most commonly seen in transactions in the Core UI Service Catalog because all Service Catalog transactions use a 302 redirect. From the point you start to order an item until the point where you hit the order summary page, there is a first transaction that hits service\_catalog.do processor, and then a second transaction redirected to the appropriate page.  
              
            
        -   For browsers that don't support the Performance Timing DOM object, client\_network\_time is determined by the difference between the point in time when the page started loading and when the page was requested, minus server time. This can result in bloated times since some time that is actually browser time is being recorded as network time. Almost all browsers support the API. See a list of supported browsers at [https://developer.mozilla.org/en-US/docs/Web/API/Performance](https://developer.mozilla.org/en-US/docs/Web/API/Performance)  
              
            
    -   As of 2025, client\_network\_time is being used to track response times for transactions related to the **Next Experience UI**, like Configurable Workspaces. The calculation is made as follows:  
          
            **\[responseEnd\] - \[fetchStart\] - \[syslog\_transaction.response\_time\] = client\_network\_time**    The responseEnd is the timestamp immediately after the browser receives the last byte of the resource or immediately before the transport connection is closed, whichever comes first. The fetchStart is the time a resource fetch started. For more information about troubleshooting Next Experience performance, see [KB1640661 How to troubleshoot Slow Transactions or Page Load Issues in Next Experience Workspace and Portal Experiences](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1640661 "KB1640661 How to troubleshoot Slow Transactions or Page Load Issues in Next Experience Workspace and Portal Experiences").

-   **Browser time (browser\_time):** **Core UI** only. Browser time is measured differently depending on if you are using List V2 or List V3.  
      
    \[Live V2 and earlier\] The number of milliseconds between responseEnd and loadEventEnd. In other words, the time between when the current page initially finished downloading the initial wireframe HTML page and the time when the "load" event and all consequent actions have completed. Includes time to download all the linked resources (e.g., images, CSS, JavaScript). Does NOT include time for scripts to execute!  
      
    \[List V3 - Available with Helsinki\] \[Possibly also for all transactions in Jakarta and later, this paragraph of the KB needs revision\] In List V3 browser\_time tracks the time between when JavaScript first starts to run against the time when the AJAXClientTimings request is sent back to the server. This is a bigger chunk of time than the old way of doing the window.performance.timing events of loadEventEnd - responseEnd. So, do not be surprised when you notice browser\_time increase in the metrics after moving to List V3. It may partially reflect an actual slow down in user experience but it certainly also includes a simple change in the way the metric is measured. One confusing impact is that in List V3 it is not uncommon to see browser\_time be 2 or 3 times bigger than client\_response\_time. This is because client\_response\_time still follows the old model of using the window.performance.timing object.  
      
    
-   **Client Script Time: (client\_script\_time) Core UI** only. The number of milliseconds spent executing client scripts.

### Additional Client Timings Details

Starting in Fuji, ServiceNow uses the window.performance object to handle calculations of most client timings. This object is a web standard that is supported by all modern browsers for a decade as of 2025. For more information about this window.performance, see the following resources:

  
[https://developer.mozilla.org/en-US/docs/Web/API/Performance](https://developer.mozilla.org/en-US/docs/Web/API/Performance)

[https://www.html5rocks.com/en/tutorials/webperformance/basics/](https://www.html5rocks.com/en/tutorials/webperformance/basics/)

[http://w3c.github.io/navigation-timing/](http://w3c.github.io/navigation-timing/)

[https://www.w3.org/TR/navigation-timing/#dom-performancetiming-requeststart](https://www.w3.org/TR/navigation-timing/#dom-performancetiming-requeststart)

The following image shows a quick reference of the timeline of the navigation timing web standard.

![](sys_attachment.do?sys_id=3f74dd9c970f7e5068d477121153afe7)

### Release

Article covers all versions as of Zurich

### Resolution

N/A
