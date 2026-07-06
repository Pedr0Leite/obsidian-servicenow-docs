---
title: "MSQL DB on windows Pattern does not populate certain attributes when using SQL authentication"
aliases:
  - KB0696550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696550
kb_number: KB0696550
last_modified: 2025-04-08
---

## Issue

# Description

* * *

MSQL DB on windows Pattern does not populate version name, edition name, number of CPU sockets, server properties using SQLCMD.

There are two ways to login to a SQL Server DB

 1) SQL account 

Applicative credentials need to be defined.

2) using a windows account. 

Some environments only allow windows authentication. In that case, please follow the below procedure

# Procedure

* * *

The OOTB "MSSQL DB on windows pattern " using the following sqlcmd commands format:

 1) Remove all occurrences of -U -P in the  MSSQL DB on windows pattern 

 sqlcmd -U 'username' -P '\*\*\*\*\*' 

This is used to connect to sql server database using sql server authentication.   In the case, where the customer's environment only allows windows authentication, the step fails with the following message "Login failed for user 'username'.."

 Follow the below steps for workaround:

By removing the -U -P , will result in using the windows authentication for connecting to the DB

# Applicable Versions

* * *

All releases

# Additional Information

* * *

[https://www.mssqltips.com/sqlservertip/2478/connecting-to-sql-server-using-sqlcmd-utility/](https://www.mssqltips.com/sqlservertip/2478/connecting-to-sql-server-using-sqlcmd-utility/)

[https://docs.microsoft.com/en-us/sql/relational-databases/scripting/sqlcmd-use-the-utility?view=sql-server-2017](https://docs.microsoft.com/en-us/sql/relational-databases/scripting/sqlcmd-use-the-utility?view=sql-server-2017)
