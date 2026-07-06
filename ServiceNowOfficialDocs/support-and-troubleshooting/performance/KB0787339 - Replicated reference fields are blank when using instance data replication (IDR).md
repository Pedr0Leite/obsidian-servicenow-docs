---
title: "Replicated reference fields are blank  when using instance data replication (IDR)"
aliases:
  - KB0787339
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787339
kb_number: KB0787339
last_modified: 2024-08-12
---

## Replicated reference fields are blank when using instance data replication (IDR)

  

### Issue

You may notice that fields on replicated records can be blank on the consumer instance side after replication. For example: You may be replicating all the fields from the sys\_user table and see that the department field is blank on the consumer instance side but populated on the source instance side.

### Cause

This is by design, reference fields only contain sys\_id's from the referenced table. If the platform is unable to locate that sys\_id in the reference table, then the field appears blank. 

### Resolution

Make sure that you are including records from related tables in your producer replication sets. 

**Example:** User replication set is missing the users department.

1.  Reviewing the dictionary record for department on the user table shows that it is a reference field to the cmn\_department table.
2.  Navigate to Instance Data Replication -> Producer Replication Sets
3.  Select my current user replication set
4.  Go to related lists and select the list 'Replication Entries'
5.  Create a new entry for my missing reference table. In this example: cmn\_department
6.  The system warns me about creating a new replication set as it will pause the replication until we sync the new configuration.
7.  Confirm the new settings and let the instance create the replication entry.  
      
    All steps below take place on the consumer side.
8.  On the **consumer** instance, navigate to Instance Data Replication -> Consumer Replication Sets
9.  Select the replication set you modified in step 5.
10.  Under 'Related Links' select "Synchronize Replication Configuration" (Wait for this to finish)
11.  The page should refresh and you will see your replication set under the 'Consumer Replication Entries' related list.
12.  Select the check box next to the new entry or entries and select "Activate with Seeding" or "Activate with Seeding (Include History)"
13.  Your instances should seed the new set and once that is complete, you should see the reference record show up.
