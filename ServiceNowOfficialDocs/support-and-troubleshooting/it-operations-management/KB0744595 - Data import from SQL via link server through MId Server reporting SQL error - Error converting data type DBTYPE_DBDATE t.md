---
title: "Data import from SQL via link server through MId Server reporting SQL error - Error converting data type DBTYPE_DBDATE to date"
aliases:
  - KB0744595
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744595
kb_number: KB0744595
last_modified: 2024-04-07
---

## Data import from SQL via link server through MId Server reporting SQL error - Error converting data type DBTYPE\_DBDATE to date

  

### Issue

# Overview

This KB talks about a SQL exception which may appear when a customer is trying to import data using JDBC Data Source through MID server from SQL via Link server. 

# Subject

Let's say a data source is defined to import data by connecting to the SQL server via link server. Assume you needed to import null values as well, so you've ticked 'Copy empty fields' on the transform map mapped to this data source. MID Server is involved in this import.

Now when the import is executed , you might receive the following error message:  
  
"MID Server reported error: com. microsoft. sql server. jdbc. SQL ServerException: Error converting data type DBTYPE\_DBDATE to date.  
at com. microsoft. sql server. jdbc. SQL ServerException. make FromDatabaseError(SQL Server Exception. java: 216)" 

This error has nothing to do with our platform nor the MID Server and is something that the SQL admins to deal with. This is completely an SQL exception.

Please reach out to the Database Admins and fix the error at the DB level 

# Additional Information

Here are few links from google on this SQL exception

   - [https://knowledgebase.progress.com/articles/Article/000044844](https://knowledgebase.progress.com/articles/Article/000044844)  
   - [https://www.tek-tips.com/viewthread.cfm?qid=1087756](https://www.tek-tips.com/viewthread.cfm?qid=1087756)
