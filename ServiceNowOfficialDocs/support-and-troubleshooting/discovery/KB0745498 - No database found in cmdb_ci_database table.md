---
title: "No database found in cmdb_ci_database table"
aliases:
  - KB0745498
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745498
kb_number: KB0745498
last_modified: 2024-04-07
---

## Issue

# Overview

We see the cmdb\_ci\_database table but there is not database listed there.

# CMDB\_CI\_Database is not used by Discovery

We do not use this "cmdb\_ci\_database" table by default for populating databases like MSSQL, Oracle, MySQL, etc.   
Now, as far as why we don't populate this table and why this exists, there are a couple of likely explanations for this.   
  
First, it's likely that this table was initially created a long time back for populating these Databases.   
However, it looks like based on common naming conventions that it's more proper to refer to the Database installations themselves as "Database Instances" and the containers of information about these instances as "Database Catalogs".   
You can read some reference on this as it pertains to MSSQL below.   
\- [https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/database-engine-instances-sql-server](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/database-engine-instances-sql-server)   
\- [https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql)   
  
Here are also some articles that explain about "Instances" and "Catalogs" on a broader scale as well you can reference.   
\- [https://www.lifewire.com/database-instance-1019612](https://www.lifewire.com/database-instance-1019612)   
\- [http://www.dbta.com/Columns/DBA-Corner/The-Importance-of-the-Relational-System-Catalog-116713.aspx](http://www.dbta.com/Columns/DBA-Corner/The-Importance-of-the-Relational-System-Catalog-116713.aspx)   
  
So, therefore, this is why now we are using the tables like "cmdb\_ci\_db\_mssql\_instance" and "cmdb\_ci\_db\_mssql\_catalog" instead.   
  
We also have an enhancement request FTASK36613 to remove the module since it's not used by discovery. 

# Example

This section is optional.

# Additional Information

This section is optional.
