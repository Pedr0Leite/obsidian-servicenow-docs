---
title: Configuring Instance Clone
description: Register your instance for cloning and create a custom clone profile.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/configure-clone.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Instance Clone, Configure core features, Administer the ServiceNow AI Platform]
---

# Configuring Instance Clone

Register your instance for cloning and create a custom clone profile.

## Configuration overview

1.  [[configure-target-instance|Register an instance for cloning]] before requesting your clone.

    A clone target record specifies the instance URL and credentials used for cloning.

2.  [[configure-clone-profile|Create a custom clone profile]].

    Clone profiles enable you to select the correct exclusions and preservers for your clone.

3.  [[create-new-clone-preserver|Create a clone preserver]].

    Create clone preservers to protect data on the target instance from being overwritten.

4.  [[t_ExcludeATableFromCloning|Exclude a table from cloning]].

    Exclude a table to create an empty but usable table on the target instance.

5.  [[create-cleanup-script|Create cleanup scripts]].

    Use cleanup scripts to automate post-clone steps or to modify data after your clone.

## Related

- [[configure-target-instance|Register an instance for cloning]]
- [[configure-clone-profile|Create a custom clone profile]]
- [[create-new-clone-preserver|Create a clone preserver]]
- [[t_ExcludeATableFromCloning|Exclude a table from cloning]]
- [[create-cleanup-script|Create cleanup scripts]]
