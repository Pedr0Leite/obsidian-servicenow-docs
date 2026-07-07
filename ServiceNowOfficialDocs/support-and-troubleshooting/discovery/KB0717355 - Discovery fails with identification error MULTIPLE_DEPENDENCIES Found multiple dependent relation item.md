---
title: "Discovery fails with identification error \"MULTIPLE_DEPENDENCIES Found multiple dependent relation item\"
aliases:
  - KB0717355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717355
kb_number: KB0717355
last_modified: 2025-08-07
---

## Discovery fails with identification error "MULTIPLE\_DEPENDENCIES Found multiple dependent relation item"

  

### Issue

When running discovery, if discovery fails at identification stage, you will have entries similar to these in the identification engine log:

Error identification\_engine : MULTIPLE\_DEPENDENCIES Found multiple dependent relation items \[{"parent":4,"child":0,"type":"Contains::Contained by"}\] and \[{"parent":1,"child":0,"type":"Contains::Contained by"}\] in payload identification\_engine   
Error identification\_engine : DUPLICATE\_PAYLOAD\_RECORDS Found duplicate items in the payload (index 35 and 66), using className \[cmdb\_ci\_file\_system\] and fields \[name\]. Remove duplicate items from the payload  
Error identification\_engine : MULTIPLE\_DEPENDENCIES Found multiple dependent relation items \[{"parent":4,"child":0,"type":"Contains::Contained by"}\] and \[{"parent":1,"child":0,"type":"Contains::Contained by"}\] in payload: no thrown error

The discovery log for the "Windows OS - Servers" pattern will have an entry as follows:

In case the discovered CI is included CI (such as Tomcat WAR) check if there are multiple records with name 'Contains::Contained by' in cmdb\_rel\_type table.  
Missing identifier entry for ci type : cmdb\_ci\_nas\_file\_system . Go to 'CI Identifiers' from the navigation pane and add the needed entries.  
Missing identifier entry for ci type : cmdb\_ci\_win\_cluster\_node . Go to 'CI Identifiers' from the navigation pane and add the needed entries.  
Missing identifier entry for ci type : cmdb\_ci\_win\_cluster . Go to 'CI Identifiers' from the navigation pane and add the needed entries.  
Missing identifier entry for ci type : cmdb\_ci\_win\_cluster\_node . Go to 'CI Identifiers' from the navigation pane and add the needed entries.  
Missing identifier entry for ci type : cmdb\_ci\_win\_cluster . Go to 'CI Identifiers' from the navigation pane and add the needed entries.  
Found multiple dependent relation items \[{"parent":4,"child":0,"type":"Contains::Contained by"}\] and \[{"parent":1,"child":0,"type":"Contains::Contained by"}\] in payload

### Release

All

### Cause

There could be several reasons for duplication errors but one such cause is if the same drive letter is used for both Local Drive (cmdb\_ci\_file\_system) and Mapped Network Drive (cmdb\_ci\_nas\_file\_system). This causes identification to fail because these are thought to be duplicates due to same identifier rule being used for both.

### Resolution

Its an uncommon scenario to have the same letter being mapped to local drive and mapped network drive. The only workaround this would be to create an identifier for the NAS File System table to have an identifier entry on name and NAS\_hostname.  In order to do, please follow the steps below:

1.  Discovery Definition>CI identification>Identifiers. Create New
2.  Fill the following information:
    -   Name:NAS File System
    -   Applies to: NAS File System \[cmdb\_ci\_nas\_file\_system\]
3.  Under related record for Identifier Entries tab, click New with following information:
    -   Search on table:NAS File System \[cmdb\_ci\_nas\_file\_system\]
    -   Criterion Attributes:name, nas\_hostname
    -   Allow Null Attribute: false
