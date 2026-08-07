---
title: "Mid server service restarts frequently due to \"mdmp\" files accumulating the MID installation folder"
aliases:
  - KB0753178
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753178
kb_number: KB0753178
last_modified: 2025-02-14
---

## Mid server service restarts frequently due to "mdmp" files accumulating the MID installation folder

  

### Issue

MID server service goes down frequently due to "hs\_err\_pid<pid>.mdmp" files accumulating on the host machine of the MID server service and filling up disk space rapidly.

### Release

Windows MID server JVM

### Cause

There are multiple reasons for the cause of this JVM crash and an initial investigation can be started from [KB0727261.](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727261 "KB0727261")

### Resolution

1\. Analyze the wrapper.log during the time "hs\_err\_pid<pid>.mdmp" created.

2019/05/28 11:01:15 | #   
2019/05/28 11:01:15 | # A fatal error has been detected by the Java Runtime Environment:   
2019/05/28 11:01:15 | #   
2019/05/28 11:01:15 | # **EXCEPTION\_STACK\_OVERFLOW (0xc00000fd) at pc=0x0000000064643e27**, pid=19624, tid=0x0000000000002058   
2019/05/28 11:01:15 | #   
2019/05/28 11:01:15 | # JRE version: Java(TM) SE Runtime Environment (8.0\_152-b16) (build 1.8.0\_152-b16)   
2019/05/28 11:01:15 | # Java VM: Java HotSpot(TM) 64-Bit Server VM (25.152-b16 mixed mode windows-amd64 compressed oops)   
2019/05/28 11:01:15 | # Problematic frame:   
2019/05/28 11:01:16 | # **V \[jvm.dll+0x213e27\]**   
2019/05/28 11:01:16 | The JVM process terminated due to an uncaught exception: EXCEPTION\_ACCESS\_VIOLATION (0xc0000005)   
2019/05/28 11:01:16 | JVM exited unexpectedly.   
2019/05/28 11:01:21 | Launching a JVM...   
2019/05/28 11:01:22 | WrapperManager: Initializing...   
2019/05/28 11:01:23 | Logger for 'glide' has not been configured by the container, configuring now:   
2019/05/28 11:01:23 | Configuring log handler: java.util.logging.FileHandler   
2019/05/28 11:01:23 | Setting useParentHandlers=false for Logger 'glide'   
2019/05/28 11:01:23 | Overriding formatter to: com.glide.util.DefaultLogFormatter (for handler: java.util.logging.FileHandler)   
2019/05/28 11:11:40 | \[ECCQueueMonitor.40\] WARN org.eclipse.jetty.util.thread.QueuedThreadPool - 4 threads could not be stopped   
2019/05/28 11:57:50 |   
2019/05/28 11:57:50 | \[error occurred during error reporting (null), id 0xc0000005\]   
2019/05/28 11:57:50 |   
2019/05/28 11:57:50 | #   
2019/05/28 11:57:50 | # There is insufficient memory for the Java Runtime Environment to continue.   
2019/05/28 11:57:50 | # Native memory allocation (malloc) failed to allocate 1048592 bytes for Chunk::new   
2019/05/28 11:57:50 | # An error report file with more information is saved as:   
2019/05/28 11:57:50 | # **C:\\ServiceNow\\agent\\hs\_err\_pid18532.log**   
2019/05/28 11:57:50 | #   
2019/05/28 11:57:50 | # Compiler replay data is saved as:   
2019/05/28 11:57:50 | # C:\\ServiceNow\\agent\\replay\_pid18532.log   
2019/05/28 11:57:50 | JVM exited unexpectedly.   
2019/05/28 11:57:56 | Launching a JVM...   
2019/05/28 11:57:57 | WrapperManager: Initializing...   
2019/05/28 11:57:57 | Logger for 'glide' has not been configured by the container, configuring now:   
2019/05/28 11:57:57 | Configuring log handler: java.util.logging.FileHandler   
2019/05/28 11:57:57 | Setting useParentHandlers=false for Logger 'glide'   
2019/05/28 11:57:57 | Overriding formatter to: com.glide.util.DefaultLogFormatter (for handler: java.util.logging.FileHandler)   
2019/05/28 12:34:14 | The JVM process terminated due to an uncaught exception: EXCEPTION\_ACCESS\_VIOLATION (0xc0000005)   
  

2\. Analyze the "**C:\\ServiceNow\\agent\\hs\_err\_pid18532.log**" what error was logged,

\# There is insufficient memory for the Java Runtime Environment to continue.   
\# Native memory allocation (malloc) failed to allocate 32744 bytes for ChunkPool::allocate   
\# Possible reasons:   
\# The system is out of physical RAM or swap space   
\# In 32 bit mode, the process size limit was hit   
\# Possible solutions:   
\# Reduce memory load on the system   
\# Increase physical memory or swap space   
\# Check if swap backing store is full   
\# Use 64 bit Java on a 64 bit OS   
\# Decrease Java heap size (-Xmx/-Xms)   
\# Decrease number of Java threads   
\# Decrease Java thread stack sizes (-Xss)   
\# Set larger code cache with -XX:ReservedCodeCacheSize=   
\# This output file may be truncated or incomplete.   
#   
\# Out of Memory Error (allocation.cpp:273), pid=18532, tid=0x0000000000003640   
#   
\# JRE version: Java(TM) SE Runtime Environment (8.0\_152-b16) (build 1.8.0\_152-b16)   
\# Java VM: Java HotSpot(TM) 64-Bit Server VM (25.152-b16 mixed mode windows-amd64 compressed oops)   
\# Failed to write core dump.   
#   
  
\--------------- T H R E A D ---------------   
  
Current thread (0x00000000158f7800): JavaThread "C2 CompilerThread1" daemon \[\_thread\_in\_native, id=13888, stack(0x0000000017030000,0x0000000017130000)\]   
  
Stack: \[0x0000000017030000,0x0000000017130000\]   
\[error occurred during error reporting (printing stack bounds), id 0xc0000005\]   
  
Native frames: (J=compiled Java code, j=interpreted, Vv=VM code, C=native code)   
  
  
Current CompileTask:   
C2: 1160 146 4 sun.nio.cs.UTF\_8$Encoder::encode (359 bytes) 

3\. Apart from the above logs, in order to confirm why the JVM crash has happened, follow the below steps for additional info,

-   which installer MID server is using. (32bit or 64bit)
-   check the "agent.log" to see how much JVM memory was used by MID when the ".mdmp" log was filed. 
-   Further to it execute the command "system info" on the MID server Windows host,

![](sys_attachment.do?sys_id=da6a4124dbdac990da1999ead39619af)

-   The above command output gives detailed info on how much RAM is allocated, available RAM size, and especially the MID is hosted in a physical server or VM.
-   In this case, the MID Server is running on "Xen" Manufacturer and the Model name "HVM domU", Which is then a Hypervisor.
-   This VM was configured with dynamic RAM allocation, where the virtual RAM will go up and down based on the load in other VM's.
-   Depending on the load from other VMs on the same hardware, there might be a cause of the JVM being Out of memory and thus creating ".mdmp" files.

**Note: Further to avoid JVM crashes, the virtual memory for the affected MID hosts has to be increased (probably double the available size).**
