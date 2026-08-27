---
title: "SCCM Initial Setup - Login Failed for User"
aliases:
  - KB0546840
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546840
kb_number: KB0546840
last_modified: 2026-04-21
---

## SCCM Initial Setup - Login Failed for User

  

### Issue

 

When attempting to set up a new SCCM integration, testing of the SQL connection results in failure, even after verifying credentials.

When a user enters SQL credentials for the SCCM integration connection and attempts to test the new connection, a stack trace is returned indicating login failure for one or more data source. User is certain credentials are correct.  

-   Error: java.sql.SQLException: com.microsoft.sqlserver.jdbc.SQLServerException: Login failed for user 'xxxxxx'.

### Release

All

### Cause

SCCM Integration, by default, uses SQL based authentication (Standard Security) to connect to the SQL server and the company may have elected to use Windows NT based authentication (Integrated Security) for their SQL server. The login fails because the MID Server is using the wrong method to connect to the SQL server.

### Resolution

In order to successfully test and use the connection, the user must enable Integrated Authentication for each SCCM Data Source.  
  

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: The following should be done only if the SQL authentication mode has been verified to be Window NT (Integrated Authentication).</td></tr></tbody></table>

Verify MID Server credentials:

1.  Open **Services** in the **Windows Management Console.**
2.  Open the **ServiceNow MID Server** service.
3.  Verify the **Log On** account/password are a Windows user with access to the SQL SCCM tables.
4.  If updated, restart **MID Server**

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>:&nbsp;Restarting MID Server may cause delays and/or downtime in services.</td></tr></tbody></table>

Enable Integrated Authentication for each SCCM Data Source:

1.  Navigate to Integration - Microsoft SCCM 2012.
2.  Navigate to **Data Sources.**
3.  Open Data Source.
4.  Select **Use integrated authentication.**
5.  Update and repeat for remaining data sources.

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;If the <em>Use integrated authentication</em> is not available on the data source form, it must&nbsp;be added through <em>Personalize -&gt; Form Design</em>.</td></tr></tbody></table>

When finished, navigate back to the SCCM Setup and test the connection again.
