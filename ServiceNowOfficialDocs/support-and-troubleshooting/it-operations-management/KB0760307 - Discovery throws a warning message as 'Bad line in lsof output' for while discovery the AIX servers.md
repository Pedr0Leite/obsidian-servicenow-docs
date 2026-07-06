---
title: "Discovery throws a warning message as 'Bad line in lsof output' for while discovery the AIX servers"
aliases:
  - KB0760307
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760307
kb_number: KB0760307
last_modified: 2024-04-08
---

## Discovery throws a warning message as 'Bad line in lsof output' for while discovery the AIX servers

  

### Issue

When you run discovery on some AIX devices, we will be seeing the following warning message in the discovery log.  
  
Bad line in lsof output, line 1:  
lsof: WARNING: compiled for AIX version XXXX; this is YYYY.  
Bad line in lsof output, line 1038:  
lsof: WARNING: /home/root/.lsof\_sftdpsdb3 was updated.

![](sys_attachment.do?sys_id=e7056734db0078d022e0fb24399619d4)

### Release

ALL

### Cause

The subset list for os level on AIX x.x seems to include at least two file sets, xlsmp.msg.en\_US.rte and xlsmp.rte, that do not install from AIX x.x media with a y.y level. Hence, os level reports x.x instead of the expected y.y. 

If either xlsmp.msg.en\_US.rte or xlsmp.rte is installed, lsof's Configure script and run-time tests will identify the AIX version incorrectly. The run-time test will issue a complaint message of this form:

 lsof: WARNING: compiled for AIX version xxx; this is yyy.

### Resolution

You can correct the Configure test by pre-defining the os level value, setting the correct value in the LSOF\_VSTR environment variable before running the Configure script

 e.g., to pre-define AIX y.y when using ksh, do this: 

$ LSOF\_VSTR= y.y Configure -n aix 

You can't affect os level output without uninstalling xlsmp.msg.en\_US.rte and xlsmp.rte. If you can't do that, you'll have to put up with the run-time complaint.
