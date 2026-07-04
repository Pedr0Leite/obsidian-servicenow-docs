---
title: "How choice updates behave differently in scoped applications versus update sets"
aliases:
  - KB0657356
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657356
kb_number: KB0657356
last_modified: 2026-04-01
---

## How choice updates behave differently in scoped applications versus update sets

  

### Issue

Understand how choice updates behave differently in scoped applications compared to update sets, and how to manage large choice sets to avoid long application install times.

The most common way to move choice changes is through update sets. However, capturing and applying choice changes in a scoped application behaves differently than applying the same changes through an update set. Understanding this difference is important when working with large choice sets.

### Release

All supported releases

### Resolution

### Choices in an update set

When choice changes are made and applied through an update set, the system applies the changes as a single complete `sys_choice_set` snapshot — only one update is applied, containing the latest version of the entire choice set.

![Screenshot of Choice Set record incident\_state](https://support.servicenow.com/sys_attachment.do?sys_id=19636eec4704471030fba325126d43d5 "Screenshot of Choice Set record incident_state")

For example, if two new choices are added to the `incident_state` element on the Incident `[incident]` table, the Customer Updates `[sys_update_xml]` table shows only a single update to `sys_choice_incident_incident_state`, even though two choices were added.

![Screenshot showing list view of customer updates of sys\_choice\_incident\_incident\_state record](https://support.servicenow.com/sys_attachment.do?sys_id=616322204744471030fba325126d430b "Screenshot showing list view of customer updates of sys_choice_incident_incident_state record")

This behavior is the same whether the changes are captured in the default update set or a local update set. When the update set is applied to another instance, the existing choice set on the target is overwritten — but only one update to the choice set is applied.

For more information about how choices work in update sets, see [KB0656146](https://support.servicenow.com/kb_view.do?sysparm_article=KB0656146).

### Choices in a scoped application

On initial installation of a scoped application, choices are loaded as a single update — the same behavior as an update set. However, when subsequent changes are made to a choice set and the scoped application is updated, the system applies one update for every individual change that was made, rather than applying only the latest version of the choice set.

This is different from update set behavior, where only the latest version of the choice set is applied regardless of how many changes were made.

For example, if a scoped application has choices for Incident State and two new choices are added, the `localhost` logs show two updates on the next application install — one for each change — rather than a single update.

### Performance impact of large choice sets in scoped applications

When a scoped application with a large choice set is updated, the install process can take a long time because the system applies one update per change rather than a single snapshot.

For example, if a choice set has 500 or more choices and 600 new choices are added, the `localhost` logs show 600 updates on the next application install. Each update loads the entire choice set at that point in time — the existing choices plus the one new choice added in that update. Only the final update contains the complete choice set with all new additions.

### General guidelines for large choice sets in scoped applications

The following guidelines apply only to instances affected by [PRB1240837](https://support.servicenow.com/now?id=form&sys_id=aecac800db3e07c47fc27c541f961918&table=problem&view=ess_sp "PRB1240837"), which causes long application install times when a scoped application contains a large number of choices.

-   If the choice set is small and the number of updates is low, continue using the application repository to move choice changes.
-   If the choice set is large and has a high number of updates, create a local update set within the scoped application to capture the changes and use the update set method to move those changes as needed.

Note: If you are already using the application repository to publish your scoped application, do not use update sets to migrate changes. Using update sets and the application repository together causes conflicts in the upgrade engine when downloading updates to the scoped application. This results in changes not being applied to the target instance until the conflicts are resolved. If you use an update set as a workaround, check for skipped changes during your next installation. See [Resolve a skipped update](https://docs.servicenow.com/csh?topicname=t_ResolveASkippedUpdate.html&version=latest "Resolve a skipped update").
