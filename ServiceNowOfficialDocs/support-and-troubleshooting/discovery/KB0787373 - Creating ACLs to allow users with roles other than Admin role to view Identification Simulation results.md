---
title: "Creating ACLs to allow users with roles other than Admin role to view Identification Simulation results"
aliases:
  - KB0787373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787373
kb_number: KB0787373
last_modified: 2024-04-08
---

## Creating ACLs to allow users with roles other than Admin role to view Identification Simulation results

  

### Issue

Out of the box, only users with "Admin" role can view the result of Identification Simulation.

### Resolution

Please create read access control rule for both cmdb\_ie\_run and cmdb\_ie\_context table:

\> Create an Access Control rule that is on cmdb\_ie\_run table (name: cmdb\_ie\_run, fields --None--), and pick the role you need.  
\> Create an Access Control rule that is on cmdb\_ie\_context table (name: cmdb\_ie\_context, fields --None--), and pick the role you need.
