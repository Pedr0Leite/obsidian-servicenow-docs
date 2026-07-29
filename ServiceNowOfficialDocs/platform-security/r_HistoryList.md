---
title: History List
description: The history list displays each change as its own row in the change list.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/r\_HistoryList.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Knowing about History sets, Auditing]
tags:
  - platform-security
  - type-reference
---

# History List

The history list displays each change as its own row in the change list.

\[Omitted image "ViewHistoryList.png"\] Alt text: View History List

Click on a row item to view additional details about the change.

\[Omitted image "ViewListChange.png"\] Alt text: View List Change record

## Requirements

To view a history list, the following requirements must be met.

-   **[[c_AuditedTables|Auditing]]**

    Auditing for the table must be enabled to view a history list.

-   **ACLs**

    By default, the List history option is only available to [[users|users]] with the admin user role. To enable this option to non-admins, create a custom ACL rule granting read access to the Record History \[sys\_history\_set\] table.

-   **Roles**

    At least one of the roles that the user has must be included in the **glide.history.role** property, which includes the itil role by default.

## Related

- [[c_AuditedTables|Auditing]]
- [[users|Users]]
