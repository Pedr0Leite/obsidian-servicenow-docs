---
title: "SQL Server JDBC connection fails with \"Login failed for user\" error"
aliases:
  - KB0719341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719341
kb_number: KB0719341
last_modified: 2025-12-22
---

## SQL Server JDBC connection fails with "Login failed for user" error

  

### Issue

Resolve SQL Server JDBC connection errors that occur when the database requires Windows Integrated Authentication but the MID Server service is not configured to use the correct domain account.

When retrieving data from a Microsoft SQL Server database using a JDBC data source, the connection may fail with a "Login failed for user" error even when the data source record contains correct credentials.

### Symptoms

The following error appears in the MID Server logs:

java.sql.SQLException: com.microsoft.sqlserver.jdbc.SQLServerException: Login failed for user 'DOMAIN\\username'. ClientConnectionId:76194d006-988f-4814-aec1-366o28bfb62c

### Release

All supported releases

Affected integrations:

-   Service Graph Connector for SCCM
-   SCCM 2016 integration (deprecated)
-   Any integration that connects to Microsoft SQL Server via JDBC

### Cause

The SQL Server database requires Windows Integrated Authentication. When this is enabled, the database uses the credentials of the Windows account running the MID Server service rather than the user name and password specified in the data source record.

If the MID Server service is not running as a domain account with access to the SQL Server database, the connection fails even when the data source credentials are correct.

### Resolution

### Configure the MID Server service

1.  On the MID Server host, open **Windows Services**.
2.  Locate the ServiceNow MID Server service.
3.  Right-select the service and select **Properties**.
4.  Select the **Log On** tab.
5.  Select **This account** and enter the domain account credentials (for example, DOMAIN\\svc-account).
6.  Enter the password.
7.  Select **OK**.
8.  Restart the service.

### Configure the data source

1.  In ServiceNow, go to **System Import Sets** > **Administration** \> **Data Sources**.
2.  Open the data source record.
3.  Set **Use integrated authentication** to **true**.
4.  Select **Save**.

### Update the JDBC connection string (if required)

If the connection still fails, add the integratedSecurity parameter to the JDBC connection string:

jdbc:sqlserver://database-server.example.com:1433;selectMethod=cursor;databaseName=exampledb;integratedSecurity=true

### Additional considerations

**Multiple integrations requiring different service accounts**

The MID Server Windows service can only run as a single user account. If you have multiple SQL Server connections that require Integrated Authentication with different user accounts, you must use a separate MID Server for each account. For integrations that do not require integrated authentication, you can use the same MID Server regardless of the service account.

**"Login is from an untrusted domain" error**

When using integrated authentication, you may see this error:

java.sql.SQLException: com.microsoft.sqlserver.jdbc.SQLServerException: Login failed. The login is from an untrusted domain and cannot be used with Windows authentication.

This error typically occurs when setting up a new MID Server in a different network location, such as an AWS EC2 instance when the existing MID Server is on-premises. This is an Active Directory trust issue, not a ServiceNow issue. Work with your Active Directory and SQL Server administrators to resolve domain trust configuration.

### Related Links

[MID Server system requirements](https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/mid-server/reference/r_MIDServerSystemRequirements.html)

[Create a JDBC type data source](https://www.servicenow.com/docs/bundle/zurich-integrate-applications/page/administer/import-sets/task/create-jdbc-type-data-source.html)

[Service Graph Connector for Microsoft SCCM](https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/configuration-management/concept/cmdb-integration-sccm.html)
