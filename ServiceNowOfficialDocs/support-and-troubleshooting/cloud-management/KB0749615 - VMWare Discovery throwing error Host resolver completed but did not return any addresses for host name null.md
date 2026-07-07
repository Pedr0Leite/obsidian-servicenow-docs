---
title: "VMWare Discovery throwing error \"Host resolver completed but did not return any addresses for host name: null\"
aliases:
  - KB0749615
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749615
kb_number: KB0749615
last_modified: 2024-04-07
---

## Issue

# Symptoms

When discovering Vmware Vcenter Datacenters from the Cloud account , discovery fails with the below error :

Host resolver completed but did not return any addresses for host name: null

# Release

All

# Cause

\- The reason we are seeing the error is because the datacenter URL field on the service account as well as on the datacenter record might be empty.

# Resolution

\- Populate the datacenter URL field on the correlating Could Service Account service account.   
  
\- Run discover datacenter   
  
\- Run Cloud account discovery
