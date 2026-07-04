---
title: "Flow designer has many updates in the update set"
aliases:
  - KB0719137
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719137
kb_number: KB0719137
last_modified: 2024-04-16
---

## Flow designer has many updates in the update set

  

### Issue

 

Large update sets when trying to transfer a flow from Flow Designer

#   

### Release

Kingston

### Cause

This is expected behavior because of the Flow Designer data model, there are a lot of different tables modified for each and every flow. This currently results in many files to be generated (many entries in the update set), and because all changes are tracked (creates/deletes/updates), this creates very large update sets. 

### Resolution

The recommended method to move Flow Designer flows is to use an Application Repo, however, update sets do work but they are very large.
