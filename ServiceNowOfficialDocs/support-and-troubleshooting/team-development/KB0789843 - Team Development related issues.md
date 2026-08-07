---
title: "Team Development related issues"
aliases:
  - KB0789843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789843
kb_number: KB0789843
last_modified: 2025-08-28
---

## Issue

This document contains some frequently faced Team Development related issues. ServiceNow no longer updating/enhancing the team development application.  But we do support the existing application.  Until ServiceNow completes the process of replacing Team Development with source control and continuous integration features, if you can't use [Update set batching](https://docs.servicenow.com/csh?topicname=us-hier-overview.html&version=latest "Update set batching") and/or the  [ServiceNow application repository,](https://docs.servicenow.com/csh?topicname=app-repo.html&version=latest "ServiceNow application repository") the following procedures may help to get more value out of TeamDev.

## Resolution

 Even though the following problems have been fixed in older releases (like Geneva and Jakarta), the workarounds suggested in the corresponding knowledge articles are still valid.

[KB0547554 - Pushes can terminate in a state where no further pushing and pulling can be done (PRB625974)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547554 "KB0547554 - Pushes can terminate in a state where no further pushing and pulling can be done (PRB625974)")

[KB0598987 - Team Development pushes appear successful, but Stage is not set to Completed (PRB730569)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598987 "KB0598987 - Team Development pushes appear successful, but Stage is not set to Completed (PRB730569)")

[KB0622987 - Avoiding long Team Development Reconciles After Cloning (PRB1032308)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0622987 "KB0622987 - Avoiding long Team Development Reconciles After Cloning (PRB1032308)")

Here are some useful definitions:

-   **Reconcile changes:** Reconciling first compares the local instance to the parent, and then generates the list of local changes and calculates the number of changes that are ready to pull from the parent.
-   **Compare to peer instances:** It initiates a full comparison of all changes on the remote instance and all changes on the local instance, and then reports which customized records have different current versions. You can selectively commit a version from the remote instance or compare it with the version on your local instance.
-   **Pull a version:** Pulling retrieves all versions for changes made by users that have not already be pulled onto the development instance, and you cannot choose which versions to pull. The first time you pull from a parent instance, the pull retrieves all versions for changes made by users. Subsequent pulls retrieve the new versions since your last pull.
-   Reconcile & Compare to peer are done on all the changes in the instances.
-   Each pull is recorded in the Push or Pull \[sys\_sync\_history\] table on the development instance. So when you pull from a parent, it will verify this table and gets the changes that are not previously pulled.

## Additional Information

[Team Development](https://docs.servicenow.com/csh?topicname=c_UsingTeamDevelopment.html&version=latest "Team Development")

[Achieve your process goals with Team Development, Update Sets, & Applications](https://community.servicenow.com/community?id=community_blog&sys_id=8f1e626ddbd0dbc01dcaf3231f96196f "Achieve your process goals with Team Development, Update Sets, & Applications")

[Properly deploy changes using Team Development](https://community.servicenow.com/community?id=community_blog&sys_id=c79dae69dbd0dbc01dcaf3231f96192a "Properly deploy changes using Team Development")
