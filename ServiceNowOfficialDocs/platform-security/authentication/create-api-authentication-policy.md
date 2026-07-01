---
title: Create an API authentication policy
description: Authentication policies allow you to enforce access restrictions on the APIs based on the specified filter criteria.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/authentication/create-api-authentication-policy.html
release: australia
product: Authentication
classification: authentication
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [API Authentication Policies, API access policy, Authentication, Access Management]
tags:
  - platform-security
  - sso
  - oauth
  - saml
  - mfa
  - type-task
---

# Create an API authentication policy

[[authentication-policies|Authentication policies]] allow you to enforce access restrictions on the APIs based on the specified [[adaptive-auth-filter-criteria|filter criteria]].

## Before you begin

Role required: api\_service\_admin, adaptive\_auth\_policy\_admin

## Procedure

1.  Navigate to **All** &gt; **System Web Services** &gt; **[[api-authentication|API Authentication]] Policy**.

2.  Click **New**.

3.  On the form, fill in these fields.

    |Field|Description|
    |-----|-----------|
    |Name|Name to identify the policy.|
    |Description|Short description of the policy.|
    |Application|Scope of the application.|

4.  Right-click the form header and select **Save**.

5.  From the Policy Inputs tab, select **Edit** to add the existing Filter Criteria.

    You can also create a new Policy Input. For more information, see [Create policy inputs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/create-policy-input.md).

6.  Move one or more filter criteria from the Collections list to the Policy Inputs List.\[Omitted image "[[c_Authentication|authentication]]-filter-criteria.png"\] Alt text: Adding one or more filter criteria to an authentication policy.

7.  Select **Save**.

8.  From the Policy Conditions tab, select **New**.

9.  On the form, fill in these fields.

    |Field|Description|
    |-----|-----------|
    |Label|Name of the policy condition.|
    |Description|Short description of the policy condition.|
    |Application|Scope of the application.|
    |Condition|One or more conditions that are combined with **OR** filter.|

    \[Omitted image "policy-conditions-authentication.png"\] Alt text: Example policy condition with multiple criteria.

10. Select **Submit**.

## Related

- [[authentication-policies|Authentication policies]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[api-authentication|API Authentication]]
- [[c_Authentication|Authentication]]
