---
title: "Unable to connect to JDBC data source "
aliases:
  - KB0756496
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756496
kb_number: KB0756496
last_modified: 2024-04-07
---

## Unable to connect to JDBC data source

  

### Issue

When trying to test load 20 records from the data source, the error below is seen-

  
MID Server reported error: java.sql.SQLException: com.ibm.db2.jcc.am.SqlSyntaxErrorException: \[jcc\]\[t4\]\[10509\]\[13454\]\[4.21.29\] Connection to the data server failed. The IBM Data Server for JDBC and SQLJ license was invalid   
or was not activated for the DB2 for z/OS subsystem. If you are connecting directly to   
the data server and using DB2 Connect Unlimited Edition for System z, perform the   
activation step by running the activation program in the license activation kit.   
If you are using any other edition of DB2 Connect, obtain the license file,   
db2jcc\_license\_cisuz.jar, from the license activation kit, and follow the installation   
directions to include the license file in the class path. ERRORCODE=-4230, SQLSTATE=42968

### Release

All releases

### Resolution

Apply a DB2 Connect license by including the path to a license file db2jcc\_license\_cisuz.jar in the CLASSPATH of your application. For more information on how, please refer to-

[https://stackoverflow.com/questions/25630213/squirrel-db2-connection-to-the-data-server-failed-the-ibm-data-server-for-j](https://stackoverflow.com/questions/25630213/squirrel-db2-connection-to-the-data-server-failed-the-ibm-data-server-for-j)

[https://www-01.ibm.com/support/docview.wss?uid=swg1IC82094](https://www-01.ibm.com/support/docview.wss?uid=swg1IC82094)
