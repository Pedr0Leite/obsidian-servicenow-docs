---
title: Exclusion policies
description: You can exclude certain files from change tracking by creating an exclusion policy.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/team-development/c\_ExclusionPolicies.html
release: australia
product: Team Development
classification: team-development
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Administer, Team Development, Planning your application, Building applications]
tags:
  - application-development
  - team-dev
  - collaboration
  - branching
  - source-control
  - type-concept
---

# Exclusion policies

You can exclude certain files from change tracking by creating an exclusion policy.

When a change matches an exclusion policy, the change does not generate records in the [[c_LocalChanges|local changes]] list. The change still generates local [[r_VersionRecords|version records]] and Update Set records as normal. See [Creating an Exclusion Policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/team-development/t_CreateAnExclusionPolicy.md).

**Note:** The exclusion policy applies to changes identified during a reconciliation operation. If you [[t_CreateAnExclusionPolicy|create an exclusion policy]] after a reconciliation, [[team-development-landing|Team Development]] still tracks the changes until the next reconciliation.

## Related

- [[c_LocalChanges|Local changes]]
- [[r_VersionRecords|Version records]]
- [[t_CreateAnExclusionPolicy|Create an exclusion policy]]
- [[team-development-landing|Team Development]]
