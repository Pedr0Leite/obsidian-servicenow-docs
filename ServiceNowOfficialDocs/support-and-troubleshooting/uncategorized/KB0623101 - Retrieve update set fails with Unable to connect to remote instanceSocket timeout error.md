---
title: "Retrieve update set fails with \"Unable to connect to remote instanceSocket timeout\" error"
aliases:
  - KB0623101
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623101
kb_number: KB0623101
last_modified: 2024-04-07
---

## Retrieve update set fails with "Unable to connect to remote instanceSocket timeout" error

  

### Issue

Retrieving an update set fails with "Unable to connect to remote instanceSocket timeout"  

Problem

* * *

Retrieving an update set fails with "Unable to connect to remote instanceSocket timeout" error.  

Symptoms

* * *

The wrapper logs show:

\-- wrapper.log ----  
INFO   | jvm 2    | 2017/06/09 10:26:08.081 | - Required proxy credentials not available for BASIC <any realm>@servername:port  
INFO   | jvm 2    | 2017/06/09 10:26:08.081 | - Preemptive authentication requested but no default proxy credentials available  
\-- wrapper.log ----

The localhost shows:

\--localhost-----  
2017-06-07 10:09:43 (092) Default-thread-11 SESSIONID SEVERE \*\*\* ERROR \*\*\* Method failed: (http://servername:port/hub.do?method=instance\_properties)HTTP/1.1 503 Service Unavailable with code: 503  
2017-06-07 10:09:43 (096) Default-thread-11 SESSIONID SEVERE \*\*\* ERROR \*\*\* java.lang.NullPointerException java.lang.NullPointerException  
2017-06-07 10:09:53 (120) Default-thread-11 SESSIONID WARNING \*\*\* WARNING \*\*\* Socket timeout  
2017-06-07 10:09:53 (120) Default-thread-11 SESSIONID SEVERE \*\*\* ERROR \*\*\* GetKeys failed (Socket timeout)  
2017-06-07 10:09:53 (184) Default-thread-11 SESSIONID #355448 /xmlhttp.do -- total transaction time: 0:01:09.520, tra   
\--localhost-----  
  

Cause

* * *

The _**glide.http.proxy\_host**_ system property is set but is not configured as servername. For more information about this property, see the product documentation topic [Basic proxy setup](https://docs.servicenow.com/).

Resolution

* * *

Instead of:

glide.http.proxy\_host = servername

Resolve the problem by using the following setting:

glide.http.proxy\_host = -empty- (blank)
