---
title: "Error While Pulling Data from MSSQL Linked Server Using ODBC Driver:  Error un-initializing the cache for disk storage[10103] or Error opening disk cache file C:\ProgramData\ServiceNow\odbc\cache"
aliases:
  - KB0727041
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727041
kb_number: KB0727041
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Using MSSQL Linked Server with the ODBC driver got this error:

Querying for data from SQL Server (Linked Server using the ODBC driver fails with the error:  
\[SN\]\[ODBC ServiceNow driver\]\[OpenAccess SDK SQL Engine\]Error un-initializing the cache for disk storage\[10103\]".

Or this error:

SQLDRV : \[TID: 15F0\]:\[Tue Apr 30 16:48:40.174 2019\] sqlcache.c:223: dam\_exitCache():Error opening disk cache file C:\\ProgramData\\ServiceNow\\odbc\\cache\\xxxxxxx.dat  
SQLDRV : \[TID: 15F0\]:\[Tue Apr 30 16:48:40.190 2019\] sqlcache.c:243: Returning error from dam\_exitCache()  
SQLDRV : \[TID: 15F0\]:\[Tue Apr 30 16:48:40.190 2019\] sqlcache.c:386: Error un-initializing the cache for disk storage  
SQLDRV : \[TID: 15F0\]:\[Tue Apr 30 16:48:40.190 2019\] damdrv.c:3271: sqldrv\_fetch\_row() Error fetching result set

An example query that cause the error:

select \* from OPENQUERY (SERVICENOW, 'SELECT \* from incident)';

It may return some data or it returns data fine when the result set is small, but then one of the the errors above is seen.

When returning a small amount of data no issue will be seen.

# Release

* * *

Any release 

# Cause

* * *

The Windows user that runs the MSSQL Linked Server (the SQL Server Service user account) does not have permissions to read and/or write and/or delete data in the C:\\ProgramData\\ServiceNow\\odbc\\cache folder

# Resolution

* * *

-   **When you installed the ODBC driver you should have "...Run as Administrator to launch the installer" as documented here:**

[Download and install the ODBC driver](https://docs.servicenow.com/csh?topicname=t_DownloadAndInstallTheODBCDriver.html&version=latest "Download and install the ODBC driver")

If you did not do that in the initial installation, uninstall and reinstall the driver making sure to "Run as Administrator" to launch the installer and follow the documentation above to do the installation.

-   **Make sure that the MSSQL Linked Server user (the SQL Server Service user account) has read, write, and delete permissions on the C:\\ProgramData\\ServiceNow\\odbc\\cache folder.  The location of the folder can be seen in the ServiceNow ODBC Manager under Services -> SQL Engine Parameters in the ServiceSQLDiskCachePath Attribute, see the screen shot:**

![](sys_attachment.do?sys_id=3c9aa0a6db42b450e515c2230596196e)

Typically the %ALLUSERSPROFILE% environment variable is set to C:\\ProgramData.  You can verify it's actual setting by executing the following from a windows command terminal:

![](sys_attachment.do?sys_id=b49aa0a6db42b450e515c22305961974)

-   **If the issue still persists modify the Value of the ServiceSQLDiskCachePath as shown in the screen shot above - from its current Value (e.g. %ALLUSERSProfile%\\ServiceNow\\odbc\\cache) to a disk cache location under the SQL Server directory e.g.: ...MSSQLSVC\\cache that way the SQL Server Service user account should have all of the access it needs to act on that directory.  Once this change is made save it by closing the ServiceNow ODBC Manager and make sure to select to save the change.  Then reopen the ServiceNow ODBC Manager  and make sure the change is applied to the Value.  Also re-initialize the connection of the Linked Server to the driver to be sure the change is taken up.**
