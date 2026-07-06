---
title: "How Horizontal Discovery creates Virtualized By::Virtualizes relationships for cloud servers"
aliases:
  - KB0695229
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695229
kb_number: KB0695229
last_modified: 2026-03-09
---

## How Horizontal Discovery creates Virtualized By::Virtualizes relationships for cloud servers

  

### Issue

Understanding the Virtualized By::Virtualizes relationship

### Release

All Supported Releases

### Resolution

#### For Patterns

There is a post-processing script called "Create Relation Between Host To VM Instance" associated with 2 horizontal patterns << Linux Server & Windows OS - Servers >>

/nav\_to.do?uri=sa\_pattern\_prepost\_script.do?sys\_id=0341096adb457200c12ef9361d96193f

The created relationships will be based on the object id.

Moreover, In <Windows OS - servers & Linux Server> Patterns, < If host discovered by cloud discovery, set it as virtual > step sets the is\_virtual flag if the server is hosted on Azure or AWS. 

#### For Probes

The 'Windows Azure' probe is triggered from the windows classifiers. Here is the order in discovery terms for the relationship:

'Windows - Azure' probe -> 'Windows - Azure' sensor and with embedded script in the sensor:

if (related\_data.isAzure) {   
current.virtual = 'true';   
var p = SncProbe.get('Windows - Azure Relationship');   
\[...\]

This calls: 'Windows - Azure Relationship' probe to create the: Virtualized By::Virtualizes relationship between the servers and the virtual instances
