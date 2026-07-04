---
title: "Hardware Asset Management | Duplicate Model Clean Up Script"
aliases:
  - KB2543671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2543671
kb_number: KB2543671
last_modified: 2026-05-12
---

## Hardware Asset Management | Duplicate Model Clean Up Script

  

### Issue

Duplicate records with same Name, Model Number, and Manufacturer on the cmdb\_model table.

The sets of duplicates may have CI's and Asset records referencing more than one of the duplicate records making it complicated to identify which model to keep and which to delete.

### Release

All Releases

### Resolution

1\. Download the attached Scheduled Job file sysauto\_script\_HAM\_DuplicateModelCleanup.xml

2\. Import the XML file to your instance.

3\. Open the Scheduled Job and set it to Active = true.

4\. The job will run every 10 minutes and process the sets of duplicates in batches of 10.
