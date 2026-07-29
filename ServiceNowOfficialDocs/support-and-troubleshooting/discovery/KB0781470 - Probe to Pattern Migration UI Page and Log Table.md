---
title: "Probe to Pattern Migration: UI Page and Log Table"
aliases:
  - KB0781470
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781470
kb_number: KB0781470
last_modified: 2025-04-23
---

## Additional Information

**Troubleshooting**

1) After running the prerequisite script, some of the migrate buttons are faded out and not clickable.

Once a migration has been completed and the classifier probes for the migration have been updated, that migrate button should no longer be runnable.  
Also, when running individual migrations, if some migrations have been completed and others are not yet ran, you should see that the Migrate ALL button will be disabled, like below.

![](/sys_attachment.do?sys_id=dcfe8bf8dbc434d0471f9c41ba96199d)

This is expected, since the Migrate ALL button will only be available if all the migrations are not completed. 

  

2) Additional pop-up windows are occurring when trying to run a migration.

When running a migration you may see these additional pop-up windows

a)

![](/sys_attachment.do?sys_id=d0fe8bf8dbc434d0471f9c41ba9619a1)

This means that this migrations has already been previously completed, but likely someone has manually deactivated running patterns on one of the classifiers, so the migration is available to run again.

It is typically not recommended to run the migration process more than once unless under certain circumstances.

b)

![](/sys_attachment.do?sys_id=58fe8bf8dbc434d0471f9c41ba9619cd)

This message occurs if you are trying to trigger an individual migration while another migration of a different type is still in progress.

It is typically recommended to run only one migration at a time (unless running the ALL migration) unless under certain circumstances.

3) Error messages while trying to run a migration

When triggering to run a migration you may see these error messages occur.

a) xxxxx migration FAILED. See log record for more details

This message occurs when trying to run a migration and the migration fails.

Most likely this would occur if there is some issue with the prerequisite check.

b) Migration has been cancelled. Please check log table for migrations that are still in progress

This message occurs when clicking on the Cancel button from one of the pop-ups mentioned above.

c) Migration is already in progress. Please check log table for migrations that are still in progress

This message occurs when trying to run a migration that is already in progress (likely started from another tab or browser window).

This helps to prevent running multiple of the same migration simultaneously.
