---
title: Create a field recommendation for recommending assignment group field value
description: Create a field recommendation that you can select when configuring a recommended action. This field recommendation suggests an assignment group field value on a case record for a router issue.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/ex-create-field-recommendation-assg-grp.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Example: Recommend an assignment group for a router issue, Example configurations, Recommended Actions configuration, Implement Intelligence, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Create a field recommendation for recommending assignment group field value

Create a field recommendation that you can select when configuring a recommended action. This field recommendation suggests an assignment group field value on a case record for a router issue.

## Before you begin

Use the [[csm-default-record-page|CSM default record page]] or the [[csm-interaction-record-page|CSM Interaction record page]] to display field recommendations in [[csm-workspaces-configure|CSM Configurable Workspace]]. For setting the CSM default record page or the CSM Interaction record page as the default page, see [[config-csm-ws-set-record-page-order|Set record page order]].

Role required: sn\_nb\_action.next\_best\_action\_author, or admin

## About this task

Creating a field recommendation involves two main steps:

-   Creating inputs for the field recommendation.
-   Creating instructions about how to recommend values by configuring a definition for each field.

## Procedure

1.  Navigate to **All** &gt; **[[configure-nba|Recommended Actions]]** &gt; **Action Types** &gt; **Field Recommendations**.

2.  Select **New** on the Field Recommendations list.

3.  In the **Name** field, enter `Field recommendation for assignment group`.

4.  In the **Table** field, select `Case [sn_customerservice_case]` so that you can populate field recommendation for the **Assignment group** field on a case record.

5.  Save the record to display the related [[migration-lists|lists]].

6.  In the Field Recommendation Inputs related list, select **New** to create an input.

    1.  In the **Type** field, select Reference.

    2.  In the **Label** field, enter `Assignment group`.

        The **Column name** field is auto-filled.

    3.  In the Reference specification related list, configure the following fields.

        |Field|Action|
        |-----|------|
        |Reference|Select the `Group [sys_user_group] table.`|
        |Reference qual condition|Select the `Active | is | true` condition.|

    4.  Select **Update**.

7.  In the Field recommendation definitions related list, select **New** to create a definition.

    1.  In the **Name** field, enter `Assignment group for router issue definition`.

    2.  In **Field**, select the Assignment group field.

    3.  In the **Recommendation message** field, enter `You can assign this issue to` and use the pill-picker to add the recommended value **Field recommendation inputs** &gt; **Assignment group** as part of the message.

        \[Omitted image "ex-config-recommendation-message.png"\] Alt text: Recommendation message displaying the recommended value, specifically the assignment group in this case, as part of the message.

        **Note:** If the resource generator returns an empty field value, the recommendation message isn’t displayed.

    4.  In the **Recommendation Method** list, select Recommend only.

    5.  Select **Submit**.

## Related

- [[config-csm-ws-set-record-page-order|Set record page order]]
- [[csm-default-record-page|CSM default record page]]
- [[csm-interaction-record-page|CSM Interaction record page]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
- [[configure-nba|Recommended Actions]]
- [[migration-lists|Lists]]
