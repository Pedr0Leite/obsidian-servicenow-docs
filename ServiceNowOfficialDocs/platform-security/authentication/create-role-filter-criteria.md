---
title: Create role filter criteria
description: Role filter criteria allows you to filter users based on the roles. You can configure an authentication policy to allow or deny access to a list of user roles.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/create-role-filter-criteria.html
release: australia
product: Authentication
classification: authentication
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Role Filter, Filter criteria, Adaptive authentication, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-task
---

# Create role filter criteria

[[role-filter|Role filter]] criteria allows you to filter [[users|users]] based on the roles. You can [[configure-allow-access-policy|configure an authentication policy]] to allow or deny access to a list of user roles.

## Before you begin

Role required: adaptive\_auth\_admin

## Procedure

1.  Navigate to **All** &gt; **[[adaptive-authentication|Adaptive Authentication]]** &gt; **[[adaptive-auth-filter-criteria|Filter Criteria]]** &gt; **Role Filter Criteria**.

2.  Click **New**.

3.  On the form, fill in these fields.

    |Field|Description|
    |-----|-----------|
    |Name|Name to identify the role.|
    |Application|Scope of the application.|
    |Description|Short description of the role.|

    \[Omitted image "role-filter-criteria-2.png"\] Alt text: Role filter criteria form

4.  From the **Roles for criteria**, double-click **Insert a new row**.

5.  Create a condition for a specific role using the Condition Builder.

    For example, you can create a condition that allows only users with admin, itil, or snc\_internal roles. For more information about Condition Builder, see [Create a condition statement using the condition builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/create-cond-state-using-cond-build.md).

    **Note:**

    -   Currently, Dot-walking is not supported in role filter criteria.
    -   Following operators are not supported for role filter criteria:
        -   Is not
        -   Does not contain
        -   Is different from
        -   Is empty
        -   Is same as
        -   Is not empty
        -   Is empty string
    \[Omitted image "role-filter-criteria.png"\] Alt text: Role filter criteria sample

## Related

- [[role-filter|Role Filter]]
- [[users|Users]]
- [[configure-allow-access-policy|Configure an authentication policy]]
- [[adaptive-authentication|Adaptive authentication]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
