---
title: "Setting the JVM memory in the wrapper-override.conf file causes the MID server to fail"
aliases:
  - KB0635200
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635200
kb_number: KB0635200
last_modified: 2024-04-07
---

## Setting the JVM memory in the wrapper-override.conf file causes the MID server to fail

  

### Issue

Setting the JVM memory in the wrapper-override.conf file causes the MID server to fail

# Issue

* * *

Customer set the JVM memory in the wrapper-override.config file and after that the MID Server fails to start successfully with the following error in the wrapper log:

Could not reserve enough space for X KB object heap

# Solution

* * *

This is usually caused by limitation of the memory address dictated by the platform the MID server is installed on and the MID server build itself. The maximum Java heap size is set to 1024 MB by default, if this setting is overridden and the MID Server architecture does not support the increased heap size, then the MID Server service does not start. Before increasing the heap size, make sure the server can accommodate this extra size:

1.  Check the server node's memory
2.  Check if the server is a 64-bit architecture
3.  Check if the Java JRE version installed in the \\agent\\jre\\bin directory is 64-bit platform
    
    java -version
    
    java version "1.8.0\_60"  
    Java(TM) SE Runtime Environment (build 1.8.0\_60-b27)  
    Java HotSpot(TM) **64-Bit Server VM** (build 25.60-b23, mixed mode)
4.   Check if the MID Server package is 64-bit platform. This is verified in the agent log, you should see a line similar to the one below in the logs. Notice that in a 64-bit MID Server package, its name ends with **x86-64.zip** indicating this is a 64-bit version, in a 32-bit system this ends as x86-32.zip:  
    StartupSequencer   Installed: \[mid-core.jakarta-05-03-2017\_\_patch1-hotfix2-07-19-2017\_07-20-2017\_0935.universal.universal.zip, mid-jre.jakarta-05-03-2017\_\_patch1-hotfix2-07-19-2017\_07-20-2017\_0935.windows.**x86-64.zip**\]
