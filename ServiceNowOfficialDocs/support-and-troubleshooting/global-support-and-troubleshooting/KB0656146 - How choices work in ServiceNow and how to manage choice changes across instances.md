---
title: "How choices work in ServiceNow and how to manage choice changes across instances"
aliases:
  - KB0656146
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656146
kb_number: KB0656146
last_modified: 2026-04-01
---

## How choices work in ServiceNow and how to manage choice changes across instances

  

### Issue

Understand how choices work in ServiceNow, how they are captured in update sets, and how to manage choice changes across instances.

In ServiceNow, choices are stored and managed as a special data type called a `sys_choice_set`. When a new choice is added to an existing field element, that choice is captured in the `sys_choice_set` for that element. This is important to understand because it affects how choices behave when changes are moved between instances.

![Screenshot of Customer Updates list](Screen%20Shot%202017-11-10%20at%2012.03.28%20PM.pngx "Screenshot of Customer Updates list")

When a choice is added or updated, the Customer Updates `[sys_update_xml]` table records a change entry for the `sys_choice` table. The payload of that `sys_update_xml` record contains not just the individual change, but all choices for that element on that table — because the change is captured as a complete `sys_choice_set` snapshot.

![Screenshot highlighting sys\_choice\_set xml](sys_attachment.do?sys_id=68bfdaac4740471030fba325126d43c9 "Screenshot highlighting sys_choice_set xml")

### Release

All supported releases

### Resolution

### How choices behave when moved between instances

Because choices are captured as a complete `sys_choice_set` snapshot, applying a choice change to an instance always overwrites the existing choice set on the target instance. Choices are not appended or merged — the entire choice set is replaced. This is a common source of unintentional overwrites when moving choice changes between instances via update sets or scoped applications.

### Example

_Instance 1:_ Two new choices — Happy (9) and Sad (10) — are added to the Incident `[incident]` table where the element is State. The choice set for that element now has eight choices total. These changes are captured in a local update set called Choices.

![Screenshot of Choices list](sys_attachment.do?sys_id=e0bf1eac4740471030fba325126d430d "Screenshot of Choices list")

_Instance 2:_ Two new choices — Bashful (14) and Grumpy (12) — are added to the same element on the Incident `[incident]` table. The choice set also has eight choices total. These changes are captured only in the default update set.

![Screenshot of Choices list filtered where table is incident and element is state](sys_attachment.do?sys_id=60bf1eac4740471030fba325126d4312 "Screenshot of Choices list filtered where table is incident and element is state")

When the update set from instance 1 is applied to instance 2, the Bashful and Grumpy choices are no longer present because the choice set from instance 1 replaces the choice set on instance 2.

In this scenario, a warning may be generated if the changes in the update set are older than the existing changes on the target instance. In practice, when choices are added directly to an instance, the last updated date on the target is typically newer than the update set change being applied — which means no preview errors are generated, and the overwrite may go unnoticed.

### How to restore overwritten choices

When a choice set is overwritten after applying an update set, you can restore the previous version using the Update Versions `[sys_update_version]` table. A `sys_update_version` record is created each time a choice is modified, which makes it possible to revert to any previous state.

> Note: This remediation approach also applies to other ServiceNow artifacts. Always test version reverts in a non-production environment before applying them to production.

The following steps use the earlier example where the Bashful and Grumpy choices were overwritten and need to be restored.

1.  Go to the Customer Updates `[sys_update_xml]` table and locate the update record for the choice change. Copy the value from the Name field — for example, `sys_choice_incident_state`.
2.  Go to `/sys_update_version_list.do`.
3.  Filter the list where Name contains the value copied in step 1.
4.  Find the record where State is Current. This identifies the version currently applied for this artifact. If the changes were applied from an update set called Choices, the Source field reflects this.
5.  Sort the list by Created and locate the version that was current before the update set was applied.
6.  Open that record and select Compare to Current in the related links. A diff view opens showing the differences between the current version and the earlier version.
7.  Review the earlier state of the choice set, then select Revert to this Version.
8.  The choice set for the Incident `[incident]` table where the element is State is now restored to its state before the update set was applied.  
    _![Screenshot of Update Versions list](sys_attachment.do?sys_id=ecbf1eac4740471030fba325126d4316 "Screenshot of Update Versions list")__  
    ![Screenshot of Compare to Current](sys_attachment.do?sys_id=68bf1eac4740471030fba325126d434d "Screenshot of Compare to Current")_

You can revert to any version in the Update Versions table using these steps. To restore the update set version specifically, follow the same steps and select the update set version of the `sys_choice` record.

### General guidelines for managing choices

Follow these guidelines to reduce the risk of unintentional choice overwrites across your instances:

-   Modify choices in one instance only, then move those changes to other environments as needed.
-   Do not manually create choices on separate instances.
-   Clone down from production to all environments regularly to keep choice sets synchronized across your instance pipeline.
-   Follow the standard development cycle — development, test, production — for all choice additions and modifications. This reduces the risk of unintentionally overwriting choices when applying update sets or scoped applications.
