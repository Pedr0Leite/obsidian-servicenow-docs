---
title: "How to repair Discovery Credentials not accessible after clone"
aliases:
  - KB0723549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723549
kb_number: KB0723549
last_modified: 2025-07-07
---

## How to repair Discovery Credentials not accessible after clone

  

### Issue

When you navigate to Discovery->Credentials on the cloned instance and click on a credential, the system displays "Record Not Found". Editing or deleting the record from a List won't work.

### Cause

Corruption of the credentials table data during the cloning process. Records are orphaned.

This is caused by: PRB1305469 [KB0717208 Excluding table-per-class (TPC) extended tables from a clone can cause orphaned Discovery Credentials with the 'Record not found' error when trying to open them](https://support.servicenow.com/kb_view.do?sysparm_article=KB0717208 "KB0717208 Excluding table-per-class (TPC) extended tables from a clone can cause orphaned Discovery Credentials with the 'Record not found' error when trying to open them")

### Resolution

Due to the orphaned records, the best practice is to use the table cleaner to purge the table. To do this, we must add an entry to sys\_auto\_flush table for the discovery\_credentials table to run the table cleaner against it. Afterwards we will need to remove that entry, otherwise the discovery\_credentials table will automatically be purged every hour. Finally we need to Import the credentials from the previous instance that we cloned into the new instance.

On the new instance, navigate to sys\_auto\_flush.list and add an entry for the discovery\_credentials table. Enter 0 for age in seconds. Do NOT check Cascade Delete. Click Update to add it.

![](sys_attachment.do?sys_id=e2d8286edb02b450e515c2230596190d)

To run the table cleaner against the discovery\_credentials table and remove all of the corrupted credential entries from the new instance, navigate to sys\_trigger.list. From there, search for name = Table Cleaner(no underscore). Choose Table Cleaner from the list and within the Table Cleaner utility click on "Execute Now" to purge the records in the discovery\_credentials table. You can check the Discovery Credentials list to verify that the entries have been purged.

\*keep in mind that all tables in the sys\_auto\_flush will be purged as well - this utility just makes it possible to run the process on demand as opposed to the once per hour schedule.

![](sys_attachment.do?sys_id=e6d8286edb02b450e515c22305961914)

Remove the entry for the discovery\_credentials table from the sys\_auto\_flush.list to ensure that the table does not get purged again during the hourly schedule.

On the previous instance (that was cloned), export the credentials to XML by right mouse clicking on the Discovery Credentials list between the column name values, and then click on Export ->XML. After the export you must choose Download to save a local copy.>

Import the Exported Credentials into the discovery\_credentials table on the new instance by right mouse clicking on the Discovery Credentials list between the column name values, and then click on Import XML and choose the exported  XML file that you downloaded from the previous step.

Optional:  
If there were any specific mid servers that were used by certain credentials that were only available to the cloned instance, and not available to the new instance, you will need to modify those mid servers in the new instance.
