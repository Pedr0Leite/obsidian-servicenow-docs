---
title: "Custom workflow activity JDBC"
aliases:
  - KB0719103
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719103
kb_number: KB0719103
last_modified: 2024-04-07
---

## Custom workflow activity JDBC

  

### Issue

# Symptoms

* * *

Create a new custom JDBC workflow activity, in the sql command field enter ‘alter’ then the error shows up:

Given SQL statement is not allowed to be executed at this time.  
The query: alter group xxx add user xxxxx

# Release

* * *

All Releases

# Cause

* * *

There is a mid server property called mid.property.jdbc\_operations that tells the JDBCOrchestrationProbe what JDBC operations are allowed to execute, **alter** operation is not included by default.

# Resolution

* * *

Edit the mid server property mid.property.jdbc\_operations and include the **alter** keyword

# Additional Information

* * *

[MID Server property](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest#r_MIDServerProperties "MID Server property")
