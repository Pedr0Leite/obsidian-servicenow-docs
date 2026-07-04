---
title: "Resolving ODBC Driver schema, table, or column not found errors."
aliases:
  - KB0595630
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0595630
kb_number: KB0595630
last_modified: 2024-04-16
---

## Resolving ODBC Driver schema, table, or column not found errors.

  

### Issue

  

The ODBC Driver may return an error stating that the schema, table, or column were not found  
The ODBC Driver returns one of the following errors:  

-   ERROR \[HY000\] \[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Exception retrieving tables schema: java.net.SocketTimeoutException: Read timed out\[1020\]
-   ERROR \[42S02\] \[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Base table:<a\_table> not found.\[10129\]
-   ERROR \[HY000\] \[SN\]\[ODBC ServiceNow driver\]\[OpenAccess SDK SQL Engine\]Cannot create schema.Cannot retrieve a DB schema. Please run <instance>?SCHEMA in your browser and try again. Also make sure that the table descriptor cache can hold all your tables and DB views. You can check the table descriptor stats runing <instance>/xmlstats.do in your browser.\[1050\]
-   ERROR \[HY000\] \[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Could not find any column information for table:<a\_table>.\[10131\]
-   Any other error that states the schema, table, or column was not found. 

### Cause

The ODBC Driver cannot retrieve the database schema from the instance due to the table descriptor cache being insufficient. The table descriptor cache is an in-memory object that stores information about database schema including the names and field names of all tables.

Another cause can be that the Data Source does not have the instance URL defined in the "Custom Properties".

### Resolution

Check if the table descriptor cache is large enough to hold all tables and database views. As an administrator, follow these steps:

1.  In your browser, navigate to <instance>.service-now.com/xmlstats.do.
2.  Look for the entry syscache\_tabledescriptor.
3.  Note the max\_entries attribute.
4.  Navigate to **System Definition > Tables** and note the number of records.
5.  Navigate to **System Definition > Database Views** and note the number of records.
6.  If the value of the max\_entries attribute is lower than the number of tables and database views, increase the value of the property glide.cache.size.syscache\_tabledescriptor to a value greater than the number of tables + the number of database views.
7.  Open the ODBC Data source Administrator -> System DSN tab -> General -> Be sure the "Custom Properties" point to the instance URL: url=https://<instance\_name>.service-now.com as in this screen shot - after setting this make a new connection to the data source and try the query again:

![](/sys_attachment.do?sys_id=67681cff1b04b4d07a5933f2cd4bcb21)
