---
title: "Edge Proxy restart error:  \"java.lang.RuntimeException: Unable to obtain DB_ID\"   and message  \"The MySQL server is running with the --read-only option\"
aliases:
  - KB0813616
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813616
kb_number: KB0813616
last_modified: 2024-04-08
---

## Edge Proxy restart error: "java.lang.RuntimeException: Unable to obtain DB\_ID" and message "The MySQL server is running with the --read-only option"

  

### Issue

After apply simultaneously linux patches to Edge Proxy Servers and to the server hosting the order preserving encryption database, only one of four Edge Proxy servers was able to start.

The rest of the proxies shows the following error in the edgeencryption.log file:

2020-02-09 01:16:03,418 INFO Connected to database: jdbc:mysql://mycompanydb.mycompany.com as user dbuser  
2020-02-09 01:16:03,430 ERROR Error occured during proxy startup  
java.lang.RuntimeException: Unable to obtain DB\_ID  
...  
... 15 more  
Caused by: java.sql.SQLException: The MySQL server is running with the --read-only option so it cannot execute this statement  
Query is: CREATE DATABASE IF NOT EXISTS \`edgeencryption\`

### Release

A MySQL database is used along withe Edge Proxy in order to handle order preserving encryption.

### Cause

At some point during the OS patch process, the MySQL database changed to state read-only.  Once the Edge Proxies were restarted, only one of them was able to connect to the database just before the database state changed to read-only. The other Edge Proxy servers failed to start with error: java.lang.RuntimeException: Unable to obtain DB\_ID.

### Resolution

Return the database state to read-write so the  Edge Proxy can use the database tables.

Use the following SQL to check state. The following SQL statement must return value '0', meaning read-only = false:

mysql> SELECT @@global.read\_only;
