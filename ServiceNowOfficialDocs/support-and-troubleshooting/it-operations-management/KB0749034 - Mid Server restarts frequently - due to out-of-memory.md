---
title: "Mid Server restarts frequently - due to out-of-memory"
aliases:
  - KB0749034
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749034
kb_number: KB0749034
last_modified: 2026-05-12
---

## Mid Server restarts frequently - due to out-of-memory

  

### Issue

**Agent Log shows the below error**:  
  
/Downloads/log1/agent0.log.0:23443: 2019/05/14 16:57:24 (109) **StartupSequencer WARNING \*\*\* WARNING \*\*\* Encountered error: \[An active MID Server with a duplicate name detected.\]** in ensuring agent record on the instance. Retry... 

  
**Wrapper logs show the below error**:  
  
2019/05/14 16:57:24 | \[error occurred during error reporting (null), id 0xc0000005\]  
2019/05/14 16:57:24 |   
2019/05/14 16:57:24 | #  
2019/05/14 16:57:24 | # **There is insufficient memory for the Java Runtime Environment to continue**.  
2019/05/14 16:57:24 | # Native memory allocation (malloc) failed to allocate 32744 bytes for ChunkPool::allocate  
2019/05/14 16:57:24 | # An error report file with more information is saved as:  
2019/05/14 16:57:24 | # C:\\ServiceNow\\agent\\hs\_err\_pid23672.log  
2019/05/14 16:57:24 | #  
2019/05/14 16:57:24 | # Compiler replay data is saved as:  
2019/05/14 16:57:24 | # C:\\ServiceNow\\agent\\replay\_pid23672.log  
2019/05/14 16:57:24 | **JVM exited unexpectedly**.

### Release

All versions 

### Cause

By default, the mid server has **wrapper.java.maxmemory=1024** and max concurrent threads set to **25**, which may not be sufficient to carry out the transactions in the environment and once it reaches the max memory, the mid server goes down.

### Resolution

Validate if the mid server meets the minimum system requirements to carry out the transactions in your environment and increase the JVM memory or adjust the maximum threads to meet the requirements.

### Related Links

1.  [Set the MID Server JVM memory size](https://docs.servicenow.com/csh?topicname=t_MIDServerOptionalConfiguration.html&version=latest#t_MIDServerOptionalConfiguration "Set the MID Server JVM memory size")
2.  [Set MID Server thread use](https://docs.servicenow.com/csh?topicname=t_SetMIDServerThreadUse.html&version=latest "Set MID Server thread use")
3.  [MID Server system requirements](https://docs.servicenow.com/csh?topicname=r_MIDServerSystemRequirements.html&version=latest "MID Server system requirements")
