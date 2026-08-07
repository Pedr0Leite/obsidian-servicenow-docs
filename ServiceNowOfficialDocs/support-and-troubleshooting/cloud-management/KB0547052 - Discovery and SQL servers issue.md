---
title: "Discovery and SQL servers issue"
aliases:
  - KB0547052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547052
kb_number: KB0547052
last_modified: 2024-04-30
---

## Issue

Discovery and SQL servers issue

Problem

* * *

When Discovery schedule is run on a SQL server or multiple SQL servers, the folliowing error occurs:

Not enough info for matching this SQL application

Details of the Discovery schedule shows another error logged by PowerShell for "Windows - MSSQL" under the ECC Queue tab of the details:  
  
Unable to load assembly Microsoft.SqlServer.Smo. The SMO library must be installed on the MID Server host  
  
These errors occur when Discovery does not have the necessary library to talk to the SQL server application because the MS SQL Server Management library (SMO) is missing or not installed.  

Solution

* * *

The SMO library is required on the MID Server for the Discovery to work. Installing the SMO library addresses these errors.  
  
For a list of requirements, see [Microsoft SQL Servers](https://docs.servicenow.com/csh?topicname=c_Software.html&version=latest "MIcrosoft SQL Serviers") in the product documentation.
