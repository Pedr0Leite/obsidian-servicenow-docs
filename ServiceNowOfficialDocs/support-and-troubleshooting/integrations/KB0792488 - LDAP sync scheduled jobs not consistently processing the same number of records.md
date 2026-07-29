---
title: "LDAP sync scheduled jobs not consistently processing the same number of records"
aliases:
  - KB0792488
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792488
kb_number: KB0792488
last_modified: 2024-04-08
---

## LDAP sync scheduled jobs not consistently processing the same number of records

  

### Issue

This article is based on an issue which was reported where an LDAP related data source is being used with daily job schedule.

it is expected that the same number of records should get processed.

It was noted that on a given day/job run, some 30K records were processed and then another day, only 20K would be processed and sometimes, no records were processed at all

  

### Release

Any

### Cause

The root cause was identified based on this error in the logs, it is a timeout.

2020-01-15 05:00:30 (144) worker.6 worker.6 txid=fda00689dbse WARNING \*\*\* WARNING \*\*\* LDAP API - LDAPLogger : **LDAP query timed out** waiting for a response:\[Data source Name\]

\[Data source Name\] will be the name of the LDAP data source

  

### Resolution

A solution we recommend consists in increasing the time out of the LDAP server as follows

  

STEPS

1 - Open the LDAP server record (see screen print)

2 - Edit the field 'Connect timeout' and set it to 180

3 - Edit the field 'Read timeout' and set it to 180

  

Sample LDAP server screen print below:

![](sys_attachment.do?sys_id=de51e0c9dbc838d0fec4fb2439961990)
