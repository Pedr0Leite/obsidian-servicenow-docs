---
title: Create a resource generator in Recommended Actions
description: Create resource generators that you can use to provide resources for recommendations from Recommended Actions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/ra-csm-resource-generators-create.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring the Recommended Actions application, Recommended Actions configuration, Implement Intelligence, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a resource generator in Recommended Actions

Create resource generators that you can use to provide resources for recommendations from [[configure-nba|Recommended Actions]].

## Before you begin

The [[csm-task-intel-admin-center|Task Intelligence Admin Console]] \(com.sn\_ti\_admin\) plugin must be installed for selecting the Task [[intelligence-csm|Intelligence]] Classification resource generator type.

Role required: sn\_nb\_action.next\_best\_action\_author, sn\_nb\_action.resource\_generator\_author, admin

## Procedure

1.  Navigate to **All** &gt; **Recommended Actions** &gt; **Resource Generators**.

2.  Select **New** from the Resource Generators list.

3.  In the **Name** field, enter a name for the resource generator.

4.  In the **Context** field, select a context.

5.  In the **Generator type** field, select a generator type.

    Different types of generators are available that you can use. Some of the generator types require an additional selection in the **Generator** field.

    For example, if you choose flow as the generator type, you must also select the specific flow to use. Selecting the lookup icon opens a pop-up window that you can use to select the required flow.

    For more information, see [[ra-csm-resource-generators|Resource generator types]].

6.  If applicable, in the **Generator** field, select a generator.

7.  Save the record.

8.  On the Generator input form, fill in the fields.

    For a description of the field values, see [[ra-csm-resource-generator-form|Resource generator inputs form]].

    The fields that appear in this form section are determined by the selections in the **Generator type** and **Generator** fields.

9.  Select **Update**.

## Related

- [[ra-csm-resource-generators|Resource generators in Recommended Actions]]
- [[ra-csm-resource-generator-form|Resource generator inputs form]]
- [[configure-nba|Recommended Actions]]
- [[csm-task-intel-admin-center|Task Intelligence Admin Console]]
- [[intelligence-csm|Intelligence]]
