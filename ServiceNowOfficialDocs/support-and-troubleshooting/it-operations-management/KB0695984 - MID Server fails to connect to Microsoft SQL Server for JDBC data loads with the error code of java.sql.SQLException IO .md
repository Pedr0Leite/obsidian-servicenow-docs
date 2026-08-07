---
title: "MID Server fails to connect to Microsoft SQL Server for JDBC data loads with the error code of java.sql.SQLException: I/O Error: Connection reset."
aliases:
  - KB0695984
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695984
kb_number: KB0695984
last_modified: 2024-04-07
---

## MID Server fails to connect to Microsoft SQL Server for JDBC data loads with the error code of java.sql.SQLException: I/O Error: Connection reset.

  

### Issue

# Symptoms

* * *

When a JDBC data source is configured to connect to a Microsoft SQL Server DB via MID Server, it might fail and give an error message of  `**java.sql.SQLException: I/O Error: Connection reset.**`

# Release

* * *

All MID Server releases

# Cause

* * *

This issue is might be caused by some firewall rules between MID Server and SQL Server, as well as an outdated Java Runtime Environment (JRE), which the MID Server is running within.

The JRE bug is explained here:

-   [https://bugs.java.com/bugdatabase/view\_bug.do?bug\_id=7103725](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=7103725)

# Resolution

* * *

-   MID Server should be using an updated version of the JRE 6.0 Update 30 and above.
-   If the above option is not possible, you can put this line in wrapper-override.conf to disable CBC:
    
     wrapper.java.additional.201=-Djsse.enableCBCProtection=false
    
    This flag will disable CBC protection in your SSL connection.
