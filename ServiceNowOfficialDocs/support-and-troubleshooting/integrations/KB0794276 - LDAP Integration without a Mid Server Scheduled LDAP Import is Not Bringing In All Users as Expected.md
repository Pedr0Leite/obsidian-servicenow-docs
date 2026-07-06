---
title: "LDAP Integration without a Mid Server:  Scheduled LDAP Import is Not Bringing In All Users as Expected"
aliases:
  - KB0794276
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794276
kb_number: KB0794276
last_modified: 2024-04-29
---

## LDAP Integration without a Mid Server: Scheduled LDAP Import is Not Bringing In All Users as Expected

  

### Issue

LDAP Integration without a Mid Server.

The Scheduled LDAP Imports are running as expected, but there are users missing in the instance.

Checking the import sets shows that the imports complete successfully, but there is a lower number of total rows brought into the instance than expected for the respective import sets.

### Release

Applies to any release.

### Cause

Checking the node logs during the import shows the following when doing a tail and grep on the worker thread that is doing the import, for example:

\[app135153.ytz3:/glide/nodes/instance001\_16002/logs\]$ tail -f localhost\_log.2020-01-23.txt | grep worker.4  
2020-01-23 10:09:53 (090) worker.4 worker.4 txid=49ad20dd1bae LDAP SEARCH: >>Next Page  
2020-01-23 10:10:03 (514) worker.4 worker.4 txid=49ad20dd1bae LDAP SEARCH: >>Next Page  
2020-01-23 10:10:21 (572) worker.4 worker.4 txid=49ad20dd1bae LDAP SEARCH: >>Next Page  
2020-01-23 10:11:18 (009) worker.4 worker.4 txid=49ad20dd1bae WARNING \*\*\* WARNING \*\*\* LDAP SEARCH: Next Page: Exception : 255.255.255.255:636; socket closed  
2020-01-23 10:11:18 (218) worker.4 worker.4 txid=49ad20dd1bae \[0:00:00.010\] Compacting large row block (file.write: ldap\_import 10000 rows 160000 saveSize)  
2020-01-23 10:11:18 (238) worker.4 worker.4 txid=49ad20dd1bae \[0:00:00.009\] Compacting large row block (file.write: ldap\_import 10000 rows 160000 saveSize)  
2020-01-23 10:11:18 (258) worker.4 worker.4 txid=49ad20dd1bae \[0:00:00.008\] Compacting large row block (file.write: ldap\_import 10000 rows 160000 saveSize)  
2020-01-23 10:11:18 (265) worker.4 worker.4 txid=49ad20dd1bae WARNING \*\*\* WARNING \*\*\* Large Table: Table handling an extremely large result set: 35000

Notice:

\*\*\* WARNING \*\*\* LDAP SEARCH: Next Page: Exception : 255.255.255.255:636; socket closed

The socket between the instance and the LDAP server has been closed and the rows to be processed is at 35000 as shown in the log:

\*\*\* WARNING \*\*\* Large Table: Table handling an extremely large result set: 35000

In this example there are over 40k rows that should have been brought into the instance.

The import will process the 35000 rows that were brought in, but the other missing rows will never be accounted for or processed during this import.

The is most likely caused by the LDAP server not having enough time to process all of the data and send it to the instance causing the "Read Timeout" configured in the LDAP server to be exceeded and the connection socket is closed.  The LDAP server may be having resource/performance issues that cause it to take longer to respond.  This could be confirmed by the LDAP administrator.

In the log above the "Read Timeout" was set to 60 seconds in the LDAP server, notice the timing of the "Next Page" logging and the "socket closed" after it:

2020-01-23 10:10:21 (572) worker.4 worker.4 txid=49ad20dd1bae LDAP SEARCH: >>Next Page  
2020-01-23 10:11:18 (009) worker.4 worker.4 txid=49ad20dd1bae WARNING \*\*\* WARNING \*\*\* LDAP SEARCH: Next Page: Exception : 255.255.255.255:636; socket closed

This is about 57 seconds which is very closed to the 60 second configured Read Timeout.

### Resolution

(1) If the LDAP server has paging enabled be sure that the paging is not set above 1000.  One-thousand is the default value.  Check the value by looking at this system property to see if it is above 1000:

glide.ldap.max\_results   
  
Set this to 1000 if it is set to a higher value.  
  
(2) Increase the LDAP server record's "Read Timeout" from its setting its current value (defaut is 30 seconds) to 120 seconds:  
  
Read Timeout = 120

This will give the LDAP server more time to send up the data and should avoid the "socket closed" error

You may need to set this above 120 seconds if the "socket closed" issue still happens.

(3) Retry the import after these changes, confirm that the "socket closed" is gone from the logs and that all expected rows are imported.
