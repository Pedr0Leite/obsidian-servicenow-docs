---
title: "Data Source Test Load 20 Records Fails with Did Not Get a Response From the MID Server error"
aliases:
  - KB0725213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725213
kb_number: KB0725213
last_modified: 2024-04-07
---

## Data Source Test Load 20 Records Fails with Did Not Get a Response From the MID Server error

  

### Issue

# Symptoms

* * *

When using the related link called "Test Load 20 Records" from a Data Source, the test does not complete and the page will refresh until the timeout is reached. (_See additional information below about the timeout setting.)_

Once the timeout is reached you may see the following error "Did not get a response from the MID Server"

 ![](sys_attachment.do?sys_id=657aa866db42b450e515c22305961929)

If you view the ECC queue during the time of your test, you can see the JDBCProbe output record, but will not see an input record immediately or even minutes later. It may take over 15 mins or possibly hours to get an input.

[https://YOUR\_INSTANCE.service-now.com/ecc\_queue\_list.do?sysparm\_query=topicLIKEJDBCProbe](https://YOUR_INSTANCE.service-now.com/ecc_queue_list.do?sysparm_query=topicLIKEJDBCProbe)

If you set your MID Server to "debug" logging level, run the test again, and check the MID Server agent log, you may see the following "Socket closed" error below:

<results error="com.microsoft.sqlserver.jdbc.SQLServerException: **Socket closed**&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerConnection.terminate(SQLServerConnection.java:1667)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerConnection.terminate(SQLServerConnection.java:1654)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.TDSChannel.read(IOBuffer.java:1789)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.TDSReader.readPacket(IOBuffer.java:4838)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.TDSCommand.startResponse(IOBuffer.java:6150)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement.doExecuteCursored(SQLServerStatement.java:1877)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement.doExecuteStatement(SQLServerStatement.java:766)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement$StmtExecCmd.doExecute(SQLServerStatement.java:689)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.TDSCommand.execute(IOBuffer.java:5696)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerConnection.executeCommand(SQLServerConnection.java:1715)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement.executeCommand(SQLServerStatement.java:180)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement.executeStatement(SQLServerStatement.java:155)&#13;&#10;&#9;at com.microsoft.sqlserver.jdbc.SQLServerStatement.executeQuery(SQLServerStatement.java:616)&#13;&#10;&#9;at com.service\_now.monitor.jdbc.JDBCRowSet.query(JDBCRowSet.java:64)&#13;&#10;&#9;at com.service\_now.mid.probe.JDBCProbe.doSelect(JDBCProbe.java:312)&#13;&#10;&#9;at com.service\_now.mid.probe.JDBCProbe.doQuery(JDBCProbe.java:198)&#13;&#10;&#9;at com.service\_now.mid.probe.JDBCProbe.probe(JDBCProbe.java:123)&#13;&#10;&#9;at com.service\_now.mid.probe.AProbe.process(AProbe.java:96)&#13;&#10;&#9;at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:125)&#13;&#10;&#9;at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)&#13;&#10;&#9;at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)&#13;&#10;&#9;at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)&#13;&#10;&#9;at java.lang.Thread.run(Unknown Source)&#13;&#10;" probe\_time="1808105" result\_code="900000"><result/>

# Cause

* * *

The message above "Did not get a response from the MID Server" may lead some to believe there is a MID Server issue when there is not. The MID Server sent out the SQL statement but the socket was closed. 

A "s_ocket closed_" error indicative that the connection has been terminated, however, no specific reason was provided/returned. There can be a number of reasons such as:

-   Network failure
-   Firewall ACLs and/or timeouts
-   The database unexpectedly terminated the connection
-   Account permissions
-   Physical proximity of the MID Server host and the SQL Server

# Resolution

* * *

Check that the MID Server is UP   [https://YOUR\_INSTANCE.service-now.com/ecc\_agent\_list.do](https://YOUR_INSTANCE.service-now.com/ecc_agent_list.do "https://YOUR_INSTANCE.service-now.com/ecc_agent_list.do")

Install Microsoft SQL Server Management Studio (SSMS) or equivalent tool on the MID Server and run the same SQL statement that is in your Data Source then analyze the results. 

# Additional Information

* * *

By default the JDBC request times out after five minutes due to these default settings for these system properties:

glide.jdbcprobeloader.retry = 60

and 

glide.jdbcprobeloader.retry\_millis = 5000

Those system properties do not exist in the sys\_properties table by default, the default values are set in the platform code.

The five minute timeout is calculated as follows:

glide.jdbcprobeloader.retry (60 retries) x glide.jdbcprobeloader.retry\_millis (5000 milliseconds (5 seconds)) = 300 seconds or 5 minutes

NOTE: 

If you have set your MID Server logging to DEBUG, don't forget to remove the MID Server Configuration Parameter or set it from DEBUG to INFO.

[https://docs.servicenow.com/csh?topicname=c\_MIDServerConfiguration.html&version=latest](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest)
