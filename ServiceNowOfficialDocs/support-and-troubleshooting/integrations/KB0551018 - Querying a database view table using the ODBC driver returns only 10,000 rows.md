---
title: "Querying a database view table using the ODBC driver returns only 10,000 rows"
aliases:
  - KB0551018
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551018
kb_number: KB0551018
last_modified: 2024-04-07
---

## Querying a database view table using the ODBC driver returns only 10,000 rows

  

### Issue

Database view tables limit the number of records you can query at one time.

### Symptoms

Querying a database view table using the ODBC driver returns only 10,000 records at most, even if the query should return more.

### Cause

The system property '_**glide.db.max\_view\_records'**_ limits the maximum number of database view records you can query at one time.

### Resolution

Set the property '_**glide.db.max\_view\_records'**_ to a value greater than 10,000.
