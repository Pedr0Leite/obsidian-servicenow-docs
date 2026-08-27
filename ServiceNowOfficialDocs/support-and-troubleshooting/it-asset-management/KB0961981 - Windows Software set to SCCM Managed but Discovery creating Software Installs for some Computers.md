---
title: "Windows Software set to SCCM Managed but Discovery creating Software Installs for some Computers"
aliases:
  - KB0961981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961981
kb_number: KB0961981
last_modified: 2024-04-13
---

## Issue

Computer records showing Software Install records updated by Discovery when property is set to have only SCCM update it.

  

Discovery property is set to Windows software is SCCM Managed, so the software installed for computers should only be coming in from SCCM.  [KB0696096](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696096 "KB0696096")

The Microsoft SCCM Integrations' can be set to exclusively manage Windows computer Software Installation records. If that is the case, Discovery will not update the cmdb\_sam\_sw\_install table for Windows computers and servers.

-   Check the **glide.discovery.software\_sccm\_managed system property**. If it is true, it probably should remain that way, and the solution is to re-run the SCCM Imports.

Search the documentation for topic "Discovery and SCCM together".

  

  

## Resolution

\[-\] In order for SCCM to be in the data source table, the device information should be coming from SCCM at least once to have an entry with SCCM name on "sys\_object\_source" table.

Run SCCM import once for this impacted Computer.
