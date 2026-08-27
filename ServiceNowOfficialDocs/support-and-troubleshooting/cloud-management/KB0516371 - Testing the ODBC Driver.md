---
title: "Testing the ODBC Driver"
aliases:
  - KB0516371
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0516371
kb_number: KB0516371
last_modified: 2025-01-26
---

## Issue

**Testing the ODBC Driver**

The ODBC Driver is a convenient, simple way for a customer to get read-only access to their instances from the Windows environment for use in integrations with a plethora of products (e.g. Excel, SQL Server, Crystal Reports). Because of the diverse use of the driver, it is sometimes difficult to diagnose issues that customers experience. Here are the steps to better identify issues with the ODBC Driver:

  

1.  Read the product documentation on the [ODBC driver](https://docs.servicenow.com/csh?topicname=c_ODBCDriver.html&version=latest "ODBC driver"), to better understand its purpose and use
2.  Setup an ODBC Driver to connect to your demo instance by following the instructions on the wiki. (You will only need to do this once, then, you can just add a new System DSN, or update the url property for each new instance to which you wish to connect)
3.  Add a new System DSN for the customer instance. This will an exact copy of the default System DSN installed with the Driver, except with the property "url=<instance url>".
4.  From the System DSN, test connection to the Driver via the "Test Connect" button
5.  If you are able to connect, you can next try to connect with isql (included in ODBC Driver installation) and attempt to issue simple select queries to ensure that data is returned.

  

**NOTE**: The connect function that is part of isql is not very robust. You will not be able to connect with credentials that contain special characters (@, \\, /, etc.). If that is the case, you may run the Attached executable on the computer where the Driver is installed. This exe will allow you to select from the configured System DSNs, connect with username and password, and issue select queries with the option to display results in a grid.

Ultimately, if you are able to connect with the ODBC Driver and return the same data the customer is testing, with the same credentials they are using, the issue is with their configuration or their integration, and not with the Driver or Instance.

  

**Connecting to ODBC using iSQL when you have special characters in your user name and/or password:**

1.  In Windows, navigate to _Start > Programs > ServiceNow ODBC > Interactive SQL (ODBC)_.
2.  Enter the following command to connect to the ServiceNow instance: Customconnect "DSN=<System DSN>;UID=<username>;PWD=<password>"   
    1.  Don't actually include the angle brackets. Here is a connection string for a DSN named "demojm" for a set of time-sensitive credentials: Customconnect "DSN=demojm;UID=joey.mart@snc;PWD=kd}7\*d"
