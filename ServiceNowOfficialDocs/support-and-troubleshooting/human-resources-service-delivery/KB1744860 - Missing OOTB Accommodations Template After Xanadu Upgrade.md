---
title: "Missing OOTB Accommodations Template After Xanadu Upgrade**"
aliases:
  - KB1744860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1744860
kb_number: KB1744860
last_modified: 2025-09-03
---

## Missing OOTB Accommodations Template After Xanadu Upgrade\*\*

  

### Issue

There is a Missing OOTB Accommodations (ER Scope App) template after Xanadu upgrade. We cloned our old environment to a non prod (HRSD) and template is there. When trying to reapply update sets in Xanadu environment missing OOTB template is causing error. ER Scope App plug in's are up to date in all environments.

### Release

Its not related to release or Environment specific

### Cause

The most probable cause of the problem is orphaned records. An orphan record is a record that has been disconnected from its parent record, causing a broken reference. In this case, the sysID: de11e647ff26201017e447cf793bf1cf on the parent table (sys\_template) is causing a duplicate entry error for the primary key.

### Resolution

1\. Export the record into XML from the instance where this file is available on child table.  
2\. Replace line#3 action="INSERT\_OR\_UPDATE" with "DETELE".  
3\. Save the XML file with a new file name.  
4\. Import the XML file, which will cascade delete the orphan record to avoid a duplicate when committing the update set.  
5\. Reimport the original XML file, which will restore the record.  
  
Note: To find the root cause for other orphan records, the customer should open a new case, and the platform team will review the cloning process and provide suggestions to avoid this in future cloning cycles.
