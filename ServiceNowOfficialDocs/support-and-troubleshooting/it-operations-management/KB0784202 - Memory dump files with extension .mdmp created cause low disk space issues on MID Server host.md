---
title: "Memory dump files with extension .mdmp created cause low disk space issues on MID Server host"
aliases:
  - KB0784202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784202
kb_number: KB0784202
last_modified: 2024-04-08
---

## Memory dump files with extension .mdmp created cause low disk space issues on MID Server host

  

### Issue

Memory dump files are created in the agent folder of the MID Server. These are not manually created or part of any debug logging for troubleshooting. The size of these memory dump files are in GigaBytes and depending on the number of times MID Server runs into JVM issues, the service can create a dump file for every occurrence. As a result the host running the MID Server service will start to run out of disk space.

Agent log files will seem to report errors as

\# There is insufficient memory for the Java Runtime Environment to continue.&#13;  
 | # Native memory allocation (malloc) failed to allocate 1779920 bytes for Chunk::new&#13;  
 | # An error report file with more information is saved as:&#13;  
 | # <MID SERVER PATH>\\agent\\hs\_err\_pid18796.log&#13;  
 | #&#13;  
 | # Compiler replay data is saved as:&#13;  
 | # <MID SERVER PATH>\\agent\\replay\_pid18796.log&#13;  
 | JVM exited unexpectedly.&#13;  
 | There were 5 failed launches in a row, each lasting less than 300 seconds. Giving up.&#13;  
 | There may be a configuration problem: please check the logs.&#13;

### Cause

This is usually caused by the host machine not having enough virtual/physical memory to allocate to JRE, and JVM crashes because of this. In order to confirm the cause, if we inspect the memory dump file(s) we should see something along the lines of

#  
\# There is insufficient memory for the Java Runtime Environment to continue.  
\# Native memory allocation (malloc) failed to allocate 1779920 bytes for Chunk::new  
\# Possible reasons:  
\# The system is out of physical RAM or swap space  
\# The process is running with CompressedOops enabled, and the Java Heap may be blocking the growth of the native heap  
\# Possible solutions:  
\# Reduce memory load on the system  
\# Increase physical memory or swap space  
\# Check if swap backing store is full  
\# Decrease Java heap size (-Xmx/-Xms)  
\# Decrease number of Java threads  
\# Decrease Java thread stack sizes (-Xss)  
\# Set larger code cache with -XX:ReservedCodeCacheSize=  
#

### Resolution

-   Head into, MID Server -> Dashboard, under the average percentage of CPU used in the last 30 days, check if the average CPU consumption is unusually high.
-   How many MID Server's are running on the same host?
-   Check wrapper-override.conf for each MID Service. For example, Let us consider a host having 16GB RAM allocated to it. If there are 3 MID Servers running on the same host and if each MID Server has an allocation of 4 GB for it's own JVM, that constitues to 12GB of memory just for the JVMs across the three MID Servers. And if we were to factor in other processes running on the OS, and the memory consumption for the OS itself, 16GB of memory might not be adequate.  
      
    So we now have two options going forward.
    -   Check the agent0 log file on the MID for the line containing  
        (349) LogStatusMonitor.60 stats threads: 110, memory max: 3641.0mb, allocated: 1584.0mb, used: 117.0mb  
        we can look at reducing the JVM memory allocation from 4 GB to around 2 GB based on the used memory reported above.
    -   The other option here is to increase the memory for the host on which these MID Servers are running. If choosing this option, double the exisiting memory, in our example from 16GB to 32GB.
