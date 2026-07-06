---
title: "Windows MID Server Goes Down For Unknown Reason \"Comparison method violates its general contract!\"
aliases:
  - KB0696845
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696845
kb_number: KB0696845
last_modified: 2024-04-07
---

## Issue

1\. Windows MID server goes down for unknown reason.

2\. Stopping and starting the service does not resolve the issue.

3\. You can see the following in the agent log:

  

08/15/18 22:59:09 (558) ECCSender.1 SEVERE \*\*\* ERROR \*\*\* Comparison method violates its general contract!  
java.lang.IllegalArgumentException: Comparison method violates its general contract!  
at java.util.TimSort.mergeHi(TimSort.java:899)  
at java.util.TimSort.mergeAt(TimSort.java:516)  
at java.util.TimSort.mergeForceCollapse(TimSort.java:457)  
at java.util.TimSort.sort(TimSort.java:254)  
at java.util.Arrays.sort(Arrays.java:1512)  
at java.util.ArrayList.sort(ArrayList.java:1462)  
at java.util.Collections.sort(Collections.java:175)  
at com.glide.util.FileUtil.getFilesSortedListing(FileUtil.java:372)  
at com.glide.util.FileUtil.getFilesSortedByDateAsc(FileUtil.java:327)  
at com.service\_now.monitor.ECCSenderCache.getFilesSorted(ECCSenderCache.java:683)  
at com.service\_now.monitor.ECCSenderCache$DirectoryCache.getFiles(ECCSenderCache.java:758)  
at com.service\_now.monitor.ECCSenderCache.sendFiles(ECCSenderCache.java:190)  
at com.service\_now.monitor.ECCSender.run(ECCSender.java:97)  
at com.service\_now.monitor.AMonitor.runit(AMonitor.java:145)  
at com.service\_now.monitor.AMonitor.access$200(AMonitor.java:39)  
at com.service\_now.monitor.AMonitor$MonitorTask.runMonitor(AMonitor.java:135)  
at com.service\_now.monitor.AMonitor$MonitorTask.run(AMonitor.java:115)  
at java.util.TimerThread.mainLoop(Timer.java:555)  
at java.util.TimerThread.run(Timer.java:505)

#   

#   

## Resolution

Check Windows Services and determine if two services are registered for the same MID server and delete the duplicate service.

1) Open Windows Services by going to Start>>Run>>cmd>>services.msc

2) Review all MID Server services and determine if there is a duplicate "ServiceNow MID Server" service. You can do this by opening the properties of each services under review and checking the path to executable. (see below images)

Here you can see 2 MID Server services:

 ![](sys_attachment.do?sys_id=1f2dac62db82b450e515c223059619af)

  

Here we are checking the path to executable:

![](sys_attachment.do?sys_id=132dac62db82b450e515c223059619b5)

  

3) Once you've determined the service to delete, make sure it is stopped.

4) Using the "Service name" of the service to be deleted, run "sc delete". For example, to delete the service above, we would type "sc delete snc\_mid"

5) Make certain that the remaining MID Server service is started. 

  

#
