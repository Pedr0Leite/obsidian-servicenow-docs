---
title: "One of the dispatchers has a different settings configuration on Central Dispatch"
aliases:
  - KB0997322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997322
kb_number: KB0997322
last_modified: 2024-08-28
---

## One of the dispatchers has a different settings configuration on Central Dispatch

  

### Issue

As admin, the Central Dispatch has been configured as follows:

Navigate to Central Dispatch Configuration and on the Task Display Fields select:

-   Number
-   Parent
-   Short Description
-   Location

When the admin or other dispatcher/agent access Central Dispatch, they can configure those fields to be enable or disable except one dispatcher who can see different field, for example:

-   Number
-   Assignment Group
-   Short Description

### Cause

Each Central Dispatch user can create its own configuration. This configurations are stored on table central\_dispatch\_config

When a user opens Central Dispatch, the script include CentralDispatchConfigRESTHelper gets the user ID and checks if said user has a configuration stored. In case the user has one, it updates the configuration on Central Dispatch to show the user preferences.

If the user does not have a configuration, the system uses the admin configuration instead.

### Resolution

If a user has a different configuration than the desired one, navigate to central\_dispatch\_config table, check if there is a configuration for that user and update or delete that record to meet the dispatcher needs.
