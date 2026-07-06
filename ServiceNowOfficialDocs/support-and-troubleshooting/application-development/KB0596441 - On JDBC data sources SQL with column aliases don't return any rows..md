---
title: "On JDBC data sources SQL with column aliases don't return any rows."
aliases:
  - KB0596441
tags:
  - servicenow
  - support-kb
  - jdbc
  - data-sources
  - import-sets
  - sql
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596441
kb_number: KB0596441
last_modified: 2024-04-07
---

## On JDBC data sources SQL with column aliases don't return any rows.

  

JDBC Data Sources with SQL Column Aliases Return 0 Rows 

Problem

* * *

When using a JDBC data source, if the SQL statement contains column aliases, no rows are returned.  

Symptoms

* * *

Steps to reproduce:  
  
Create a SQL JDBC data source  
Add a SQL query with column aliases, for example: select <column> as <aliasName> from <table>  
Test by loading 20 records. The query will run, but it will not return any rows.  
  
The same query without the column alias returns data back. (select <column> from <table>).  

Cause

* * *

This is due to PRB648117 - SQL Aliases do not work with JDBC Data Source imports.  

  
Workaround

* * *

Add the following property to the JDBC connection URL to enforce the old behavior:  
?useOldAliasMetadataBehavior=true  
  
  
1\. Personalize the form and add the connection URL  
2\. Open the data source  
3\. Append the property to the end of the connection URL. I.e. jdbc:mysql://localhost/glide?useOldAliasMetadataBehavior=true

## Related

- [[KB0756496 - Unable to connect to JDBC data source]] — general JDBC data source connectivity troubleshooting
- [[KB0635950 - On JDBC data sources, the fetch size is hard-coded and cannot be modified]] — another JDBC data source limitation
- [[configure-jdbc-driver]] — official docs on configuring JDBC drivers for data sources

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/ModelManufacture.README|ModelManufacture.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/README|Import sets overview]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/Import sets overview/TriggerDataSource.README|TriggerDataSource.README]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Import Sets/debug/README|debug]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0758037 - Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by security_admin Role|Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by \"security_admin\" Role]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0747613 - When importing data, some staging table records are duplicating or an Import set row is duplicating|When importing data, some staging table records are duplicating or an Import set row is duplicating]]
