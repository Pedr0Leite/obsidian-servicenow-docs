---
title: "Linux MID server error \"java.lang.OutOfMemoryError: unable to create new native thread\"
aliases:
  - KB0784556
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784556
kb_number: KB0784556
last_modified: 2024-04-07
---

## Linux MID server error "java.lang.OutOfMemoryError: unable to create new native thread"

  

### Issue

Linux MID server error "java.lang.OutOfMemoryError: unable to create new native thread".

### Release

All currently supported releases.

### Cause

Users have a maximum number of processes/threads in linux operating systems. The user will not be able to create new threads once this limit is reached.

To check the maximum number of threads for the user:

1.  log into the server with the user which runs the MID server application.
2.  Run command:  
    ulimit -u

### Resolution

1.  Check the number of processes running for the user, this result should be less than the result from "ulimit -u":  
    ps -efL | grep "<user\_name>" | wc -l
2.  If greater than the number of processes allowed, reach out to your linux team which manages the MID server and request that the thread limit for the users be increased.

### Related Links

This could happen, if for example, there are multiple MID servers running on the same host all started by the same user. In such case each MID server would need its own account. If the issue keeps happening even once the max user processes is increased a "thread leak" could be the issue, if that is the case please open a support ticket for further investigation.
