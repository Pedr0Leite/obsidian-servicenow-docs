---
title: "JDBC/LDAP Data Source Imports can use a lot of MID Server Disk space"
aliases:
  - KB0813378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813378
kb_number: KB0813378
last_modified: 2025-06-26
---

## JDBC/LDAP Data Source Imports can use a lot of MID Server Disk space

  

### Issue

When an Import Set runs, that has a Data Source that uses JDBC to fetch the data via a MID Server, there is the possibility of using a huge amount of disk space on the MID Server.

This can cause problems because of a lack of available disk space of the server, or from limits set in MID Server parameters, and break the import and hold up any other jobs running in the same MID Server.

### Release

Any

### Cause

The cause of this issue is different network speeds between the MID Server and Database compared to between the MID Server and instance. The database and MID Server would normally both be within the fast company network, but the ServiceNow instance is in the cloud. This can result in a backlog of data building up in the MID Server that hasn't been passed on to the instance yet. The MID Server will temporarily store the data as XML files in the ECC Sender folder within the MID Server installation folder.

![](/sys_attachment.do?sys_id=cbfba97e47926a1cc2488d01426d43b2)

You can see if you have this happening by checking for a backlog in the MID Server's ECC Sender folder: 

1.  Open a list of MID Servers in the instance, and personalize the list view to add columns "Host Name" and "Home Directory", to find out exactly where the MID Server is installed.
2.  Log into that server and open the home directory.
3.  Navigate to agent\\work\\monitors\\ECCSender\\output\_s\\   
    Note: "output\_s" is for sequential inputs that need sending back in file name order, which is used by JDBC and LDAP. For other probes this may be be output\_2, output\_1 or output\_0 for inputs without a sequence value, or output\_oversize if the payload is too big to send back at all.
4.  See how many XML files are in there, and how much disk space they take up.

### Resolution

MID Servers have a Parameter "**glide.mid.max.sender.queue.size**" which places an upper limit on how large the queue is allowed to get. The MID Server starts deleting queued messages if this limit is exceeded, which is **"0.5 GB" by default**, and once that is reached the imports will end up being broken. Adding a parameter to the MID Server allows this to be overridden with a higher value, assuming you have the physical disk space available.

You should investigate if the import is correct, and whether so much data is expected. Perhaps more rows are being returned than expected, or certain columns have large data that needn't have been included in the query (e.g. User records containing Images).

To allow the backlog to clear, you could avoid sending more large import jobs to this MID Server for a while. 

The MID Server may have no connection with the instance at the moment, or a degraded connection, perhaps due to network issues. It may also be due to a performance issue with the ServiceNow instance, where API\_INT semaphores are not immediately available to handle the requests from the MID Server. That may need investigating. The MID Server agent log (agent/logs/agent0.log.0) is a good place to start.

If the import needs to be cancelled:

-   Do not simply restart the MID Server. This causes it to be run the whole import again as soon as the MID Server starts up.
-   You will need to error out the ECC Queue record for the import job:  
    -   Open the ECC Queue list (/ecc\_queue\_list.do)
    -   Filter for **Queue**\=Output, **Topic**\=JDBCProbe, **State**\=Processing. 
    -   The **Source** field value will be the Sys ID of the Data Source record \[sys\_data\_source\] used by the Import Set
    -   Update the State field value to Error.
-   Delete the XML records from the ECC Sender folder. You may need to limit this delete to only the XML records specific to the big import, to avoid breaking other things recently run in the MID Server that also have not been returned to the instance yet, and inspecting the contents for in order to identify those will be necessary. 
-   Then restart the MID Server service, from the Services Control Panel (run services.msc)

### Related Links

If the processing of xml records has completely stopped, and you are not simply experiencing a throughput issue, then in theory the ECCSender thread may be having problems inserting the ecc\_queue records in the instance. The MID Server agent log will confirm this if you see SOAP errors with Status 500:

[PRB1521761 / KB0995569 ECCSender can fail to insert inputs into the ECC Queue for many reasons, blocking all inputs from then on, leaving MID Server effectively Down](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995569 "PRB1521761 / KB0995569 ECCSender can fail to insert inputs into the ECC Queue for many reasons, blocking all inputs from then on, leaving MID Server effectively Down")
