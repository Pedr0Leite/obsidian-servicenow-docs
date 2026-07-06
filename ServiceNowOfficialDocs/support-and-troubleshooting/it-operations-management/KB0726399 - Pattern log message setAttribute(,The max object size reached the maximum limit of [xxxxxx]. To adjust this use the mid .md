---
title: "Pattern log message \"setAttribute(<<>>,The max object size reached the maximum limit of [xxxxxx]. To adjust this use the mid property mid.sm.discolog.max_object_size.)\""
aliases:
  - KB0726399
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726399
kb_number: KB0726399
last_modified: 2026-05-21
---

## Pattern log message "setAttribute(<<>>,The max object size reached the maximum limit of \[xxxxxx\]. To adjust this use the mid property mid.sm.discolog.max\_object\_size.)"

  

### Issue

Discovery Pattern logs messages similar to:

setAttribute(<<>>,The max object size reached the maximum limit of \[xxxxxx\]. To adjust this use the mid property mid.sm.discolog.max\_object\_size.)

### Release

All currently supported versions

### Cause

Property "mid.sm.discolog.max\_object\_size" control how much logging Pattern Engine adds to Pattern log for EACH pattern step. Default value is 1000 characters. This property has no impact on how much data is collected by Pattern discovery. The value of the property does not impact Discovery, ie, doesn't cause it to succeed or fail.

In a Pattern Discovery execution, there can be many steps and results for each steps are appended altogether in a Pattern log. This log contains each step command and result. These logs can be huge and the Pattern Engine will log the message instead of the actual data values.

When the property is increased higher, if a step data size is less than property value, data will be added to Pattern log for that step. Increasing the property value will increase the log size for the pattern.

After Pattern Discovery is completed, the pattern logs are transferred to the instance per discovered device/application and the user can view it on the instance. If the property value is set to very high value, the total Pattern log built can be very large in size (tens of MBs). When Instance is processing this large amount of logging, it can cause high memory consumption and even OutOfMemoryError.

### Resolution

These messages can be safely ignored. Discovery is not impacted.

In the case of infrastructure patterns, we are creating tables with multiple CI's and relation and doing manipulation for each step. The table size or step result can be very large and will influence on memory and view experience.   
  
In order to decrease Mid memory usage and the size of Pattern log, **mid.sm.discolog.max\_object\_size** was added.

**WARNING: If there is a need to debug the pattern, this property should be set temporarily and setting a higher value to the property can sometimes help and should only be use on sub production instances. As soon as debugging is finished, the property should be either deleted or set back to original value.**

Note: In case the mid server property is added, make sure to restart the mid server.
