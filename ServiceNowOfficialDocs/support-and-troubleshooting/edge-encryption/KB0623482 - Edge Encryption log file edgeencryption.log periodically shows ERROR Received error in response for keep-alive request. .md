---
title: "Edge Encryption log file edgeencryption.log periodically shows \"ERROR Received error in response for keep-alive request. Please check the connectivity between the Edge proxy and the ServiceNow instance. Result : java.util.concurrent.TimeoutException\" "
aliases:
  - KB0623482
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623482
kb_number: KB0623482
last_modified: 2024-04-07
---

## Edge Encryption log file edgeencryption.log periodically shows "ERROR Received error in response for keep-alive request. Please check the connectivity between the Edge proxy and the ServiceNow instance. Result : java.util.concurrent.TimeoutException"

  

### Issue

Edge Encryption log file edgeencryption.log periodically shows error: "ERROR Received error in response for keep-alive request. Please check the connectivity between the Edge proxy and the ServiceNow instance. Result : java.util.concurrent.TimeoutException: Total timeout elapsed"

  
  

# Issue

* * *

The Edge Encryption log file edgeencryption.log periodically shows the following error: "ERROR Received error in response for keep-alive request. Please check the connectivity between the Edge proxy and the ServiceNow instance. Result : java.util.concurrent.TimeoutException: Total timeout elapsed"

# Solution

* * *

1.  Modify the following property to each Edge Encryption proxy's /conf/edgeencryption.properties file (default value is 10):
    
    edgeencryption.proxy.keepalive.interval=17 
    
2.  Save the file and restart the proxies.
    
    Setting the keepalive interval from the default of 10 seconds to 17 seconds should help with eliminating this error. Should the error continue, change the interval to a higher prime number, such as 23, 47, ... until the error no longer occurs.
    
    Increasing this value gives the instance more time to reply to the proxy's "keep alive" request. A delay in response can happen if the instance is busy and the ten-second default time is exceeded.
