---
title: "How to increase debug logging for the Edge Encryption proxy"
aliases:
  - KB0621289
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621289
kb_number: KB0621289
last_modified: 2026-05-04
---

## How to increase debug logging for the Edge Encryption proxy

  

### Issue

There are currently three options for increasing debug logging on the Edge Encryption Proxy. You might want to increase the level of logging to debug issues with the proxy and interpret the logs yourself, or you might want to have technical support look into the issue with the benefit of more verbose log statements.

Depending on the issue being debugged, set up debug logging in one of three ways:

-   Debugging issues with SSL connectivity between the Edge Encryption Proxy and the instance
-   Debugging issues other than SSL connectivity
-   Logging timing metrics for requests through the proxy

For all debug cases, you may view and interpret the logs on your own or open an incident to get an interpretation from ServiceNow technical support providing the description of the issue and how it is reproduced.

**Note:** instructions use current log4j v2 configuration.  If your proxy is on an older version (pre-Paris) and does not have a $proxy\_installation\_location/conf/log4j2.properties file use the older, log4j v1, instructions at the end of the KB

### Release

All releases

### Resolution

### Debugging issues with SSL connectivity between the Edge Encryption Proxy and the instance

Use this method if you want to debug issues with SSL connectivity between the Edge Encryption Proxy and the instance (for example, you go to the URL of the proxy but access to the instance fails via the proxy). These steps increase logging and help find the verbose log statements.

1.  Stop the proxy.
2.  Add the following line to the file _$proxy\_installation\_location/conf/wrapper.conf_, which is a Java startup property:
    
    wrapper.java.additional._<next available number in sequence>_ = -Djavax.net.debug=all
    
    For example: wrapper.java.additional.4 = -Djavax.net.debug=all
    
3.  Save the change and restart the proxy.
4.  Reproduce the issue.
5.  Debug log statements related to the SSL exchange can be found in the _$proxy\_installation\_location/logs/wrapper\_<current date>.log_ file.
6.  When debugging is complete, stop the proxy and edit the file _$proxy\_installation\_location/conf/wrapper.conf_ again, removing or commenting out (adding a # at the beginning of the line) the following line:
    
    wrapper.java.additional._<next available number in sequence>_ = -Djavax.net.debug=all
    
7.  Save the change and restart the proxy.

### Debugging issues with the Edge Encryption application other than SSL-related issues

Use this method if you want to debug issues with the Edge Encryption application aside from SSL-related issues. These steps increase logging and help find the verbose log statements.

1.  In the _$proxy\_installation\_location/conf/log4j2.properties_ file, change the setting of the log from info to debug.  
    Change this:
    
    logger.edge.level=info  
      
    to this:  
      
    logger.edge.level=debug
    
2.  Save the change, the new logging level should be taken up automatically after about 60 seconds, no need to restart the proxy
3.  Reproduce the issue.
4.  Check for debug log statements related to the application in the _$proxy\_installation\_location/logs/edgeencryption.log_ file.
5.  When debugging is complete, restore the original log setting.  
      
    Change from:
    
    logger.edge.level=debug  
      
    back to:  
      
    logger.edge.level=info
    
6.  Save the change, the new logging level should be taken up automatically after about 60 seconds, no need to restart the proxy

### Logging timing metrics for requests through the proxy

Enabling timing metric logging will add a metric statement for each request handled by the edge proxy.  Each of these timing metric log statements has useful information about the request, such as processing times and which encryption rule was used. 

**Note:** The additional logging settings are added to the $_proxy\_installation\_location/conf/log4j2.properties_ file. Changes made are taken up by the proxy dynamically within about a minute after the changes to the file are made, so you do not have to restart the proxies.

1.  Modify the $_proxy\_installation\_location/conf/log4j2.properties_ file by adding the following lines at the end of the file:
    
    appender.timinglog.type=RollingFile  
    appender.timinglog.name=TimingLog  
    appender.timinglog.fileName=../logs/edgenetwork.log  
    appender.timinglog.filePattern=../logs/$${date:yyyy-MM}/edgenetwork-%d{yyyy-MM-dd-HH}-%i.log.gz  
    appender.timinglog.layout.type=PatternLayout  
    appender.timinglog.layout.pattern=%d \[%t\] %-5p %m%n  
    appender.timinglog.policies.type=Policies  
    appender.timinglog.policies.size.type=SizeBasedTriggeringPolicy  
    appender.timinglog.policies.size.size=500MB  
    appender.timinglog.strategy.type=DefaultRolloverStrategy  
    appender.timinglog.strategy.max=4  
      
    logger.timing.name=com.snc.edgeencryption.metrics.EdgeEncryptionTimingMetricCache  
    logger.timing.level=debug  
    logger.timing.additivity=false  
    logger.timing.appenderRef.rolling.ref=TimingLog
    
2.  After the log4j.properties file is saved, the following types of messages will be in the _$proxy\_installation\_location/logs/edgenetwork.log_ log file for network times:
    
    2022-07-21 12:56:15,783 \[qtp1971991758-7700\] DEBUG com.snc.edgeencryption.metrics.EdgeEncryptionTimingMetricCache -  request\_uri=/api/now/ui/presencesysparm\_auto\_request=true&cd=1658433375754 request\_method=POST client\_request\_received="2022-07-21 12:56:15,015" proxy\_request\_processing\_time=6 all\_rules\_processing\_time=0 rule\_executed="REST JSON" rule\_execution\_time=1 proxy\_instance\_round\_trip=14 proxy\_response\_processing\_time=1 total\_time\_from\_proxy=21 reponse\_code=201 glide\_user=SCv3\_1:BAz1ZK7ee9XoroG2nvMlixHpgTvsT4fY2bwQvnH2WdU=:y5HGsTTqo3Pjq6G0xk4LoazCwCiWRJk4/6SpbXuBzqg=:6816f79cc0a8016401c5a33be04be441 jsessionid\_suffix=037A66
    
    The values in the log messages are as follows:  
    
    request\_uri: The URI being requested  
      
    request\_method: The HTTP method being used, for example, GET, POST, PUT, PATCH, DELETE  
      
    client\_request\_received: The timestamp noting when the HTTP client request arrived at the Edge proxy  
      
    proxy\_request\_processing\_time: How long the Edge proxy took to process the request in milliseconds  
      
    all\_rules\_processing\_time: Total time it took to execute all of the Edge Encryption rules for the request in milliseconds  
      
    rule\_executed: The name of the encryption rule that was executed  
      
    rule\_execution\_time: How long it took to execute listed rule\_executed in milliseconds  
      
    proxy\_instance\_round\_trip: The time from when the Edge proxy sent the request to the instance until the instance sent the response and was received by the edge proxy in milliseconds  
      
    proxy\_response\_processing\_time: How long the Edge proxy took to process the response in milliseconds  
      
    total\_time\_from\_proxy: The total time from when the Edge proxy received the request from the client and returned the response to the client in milliseconds  
      
    response\_code: HTTP response code   
      
    glide\_user: The glide\_user cookie value  
      
    jsessionid\_suffix: The JSession cookie suffix associated with the request
    

### **Logging for the Jetty Application Server**

Jetty is the application server that hosts the Edge Encryption application.  Turning on this logger can give valuable information about the Jetty/Edge Encryption interactions.  

Additional logging has been introduced to the Edge Proxies. The additional logging settings are added to the $_proxy\_installation\_location/conf/log4j2.properties_ file. Changes made are taken up by the proxy dynamically within about a minute after the changes to the file are made, so you do not have to restart the proxies.

1.  Modify the $_proxy\_installation\_location/conf/log4j2.properties_ file by adding the following lines
    
    logger.jetty.name=org.eclipse.jetty  
    logger.jetty.level=debug
    

          it is recommended that this logger be kept on for a short a period as possible to collect the needed data as it creates a lot of logging.  
  

2.  Check for jetty debug log statements in the _$proxy\_installation\_location/logs/jetty.log_ file
3.  To revert the jetty logging to normal, you can either remove the 2 lines that were added (will require a proxy restart) or change the logging level back to warn using this line:

logger.jetty.level=warn

## Changing logging configuration for older releases that are still on log4j v1

All changes for log4j v1 are done in the _$proxy\_installation\_location/conf/log4j.properties_ file

### Changing edge encryption logging to debug level

Edge encryption log level is controlled by this line

log4j.logger.com.snc.edgeencryption.EdgeEncryptionLog=info

The default log level is info.  you can change it to debug to get additional debug logging messages

### Enabling Timing Metric Logging

Add these lines to enable timing metric logging:

log4j.appender.TimingLog=org.apache.log4j.RollingFileAppender  
log4j.appender.TimingLog.File=../logs/edgenetwork.log  
log4j.appender.TimingLog.MaxFileSize=500MB  
log4j.appender.TimingLog.MaxBackupIndex=4  
log4j.appender.TimingLog.layout=org.apache.log4j.PatternLayout  
log4j.appender.TimingLog.layout.ConversionPattern=%d \[%t\] %-5p %m%n

### Change jetty logging to debug level

log4j.logger.org.eclipse.jetty=debug, FileLog
