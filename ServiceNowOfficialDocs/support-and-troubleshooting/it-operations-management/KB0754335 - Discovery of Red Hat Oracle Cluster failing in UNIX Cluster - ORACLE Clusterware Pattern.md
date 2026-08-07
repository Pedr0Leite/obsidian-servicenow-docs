---
title: "Discovery of Red Hat Oracle Cluster failing in \"UNIX Cluster - ORACLE Clusterware\" Pattern"
aliases:
  - KB0754335
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754335
kb_number: KB0754335
last_modified: 2024-04-07
---

## Issue

# Symptoms

Discovery of Red Hat Oracle Cluster failing in 'UNIX Cluster - ORACLE Clusterware'

\- Failing in Step 60 ( not able to create reference & relation between cmdb\_ci\_unix\_cluster\_node to cmdb\_ci\_unix\_cluster)

# Release

ALL

# Cause

Set Oracle CRS cluster name should get the name and insert it in a variable. Instead it received the name with junk that includes error, information, more errors and then the name. This means that instead of variable the pattern created a list. That caused an issue since pattern expected a variable and not a list.

# Resolution

The solution is to change the step to filter the junk. In the pattern - UNIX Cluster - ORACLE Clusterware at Step 9 change:

From:  
$oracle\_home + "/bin/olsnodes -c | egrep -v 'error|return code'"  
To:  
$oracle\_home + "/bin/olsnodes -c | egrep -v 'error|return code|information|err|DIA-|Error|ADR'"
