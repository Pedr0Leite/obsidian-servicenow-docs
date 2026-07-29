---
title: "JVM crashing. Creating large hs_err_pid<pid>.mdmp files and rapidly fills disk space"
aliases:
  - KB0727261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727261
kb_number: KB0727261
last_modified: 2024-04-07
---

## Issue

hs\_err\_pid<pid>.mdmp files accumulating on the host machine of the MID server service and filling up disk space rapidly.

## Resolution

Look for corresponding hs\_err\_pid<PID>.log files for hints regarding the crash.

The following is a sample snippet from a core log file:

#  
\# A fatal error has been detected by the Java Runtime Environment:  
#  
\# EXCEPTION\_ACCESS\_VIOLATION (0xc0000005) at pc=0x0000000072d8d195, pid=1372, tid=0x0000000000000ce4  
#  
\# JRE version: (8.0\_152-b16) (build )  
\# Java VM: Java HotSpot(TM) 64-Bit Server VM (25.152-b16 mixed mode windows-amd64 compressed oops)  
\# Problematic frame:  
\# V \[jvm.dll+0x22d195\]  
#  
\# Core dump written. Default location: D:\\Mid Server\\Dev\\agent\\hs\_err\_pid1372.mdmp  
#  
\# If you would like to submit a bug report, please visit:  
\# http://bugreport.java.com/bugreport/crash.jsp  
#  
  
\--------------- T H R E A D ---------------  
  
Current thread (0x0000000000c3e800): JavaThread "main" \[\_thread\_in\_vm, id=3300, stack(0x0000000001450000,0x0000000001550000)\]  
  
siginfo: ExceptionCode=0xc0000005, reading address 0xffffffffffffffff  
  
 \*\*\*SNIPPED\*\*\*

The text highlighted in red above are keywords that can be used as research. Google for those messages, to see if this a known JVM bug, OS bug, or third party bug in the native code.

**NOTE**: Be extra careful when googling, as there could be many invalid answers.
