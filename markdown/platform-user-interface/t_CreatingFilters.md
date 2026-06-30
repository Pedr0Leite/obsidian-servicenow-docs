---
title: Create a filter in List
description: You can create a filter to restrict what records appear in a list by providing a set of conditions. When you run the filter, only records that meet the specified conditions are listed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/t\_CreatingFilters.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Filters, Filters and breadcrumbs, Lists in the classic environment, Working in the classic environment, Working in Core UI, Configure UIs and portals, Configure user experiences]
---

# Create a filter in List

You can create a filter to restrict what records appear in a list by providing a set of conditions. When you run the filter, only records that meet the specified conditions are listed.

## Before you begin

Role required: none

## Procedure

1.  Open the condition builder by clicking the show/hide filter icon \(\[Omitted image "Icon-Condition\_builder\_UI15.png"\] Alt text: Show or hide filter icon\).

    If the icon is disabled and the breadcrumb has a related list condition in it, you must remove the related list condition to open the filter. The condition was created when the List v3 was enabled for this list. List v2 does not support related list conditions. For more information about related list conditions, see [[create-related-list-query|Add related list conditions]].

2.  Select a field from the list.

    The field type determines the available operators and values. For example, the **Active** field can have a value of **true**, **false**, or **empty**, while a text field can have many different values. Similarly, the **greater than** operator does not apply to the **Active** field, but it does apply to the **Priority** field. For more information, see [[c_ConditionBuilder|Condition builder]].

3.  Select an **operator** from the list.

4.  Select or enter a **value**, if appropriate.

5.  Add or remove conditions to construct the desired filter by completing one or more of the following steps.

<table id="choicetable_ll5_44w_tt"><tbody><tr><td id="d137631e135">

**To add a top-level condition**

</td><td>

Click **AND** or **OR** on the condition builder toolbar, above the conditions.

</td></tr><tr><td id="d137631e150">

**To add a dependent condition**

</td><td>

Click **AND** or **OR** beside the condition.

</td></tr><tr><td id="d137631e165">

**To remove a condition**

</td><td>

Click **x** beside the condition.

</td></tr></tbody>
</table>    **Note:** To find all records that do not contain the specified value, create a filter with two conditions: **\[field\] \[is not\] \[value\]** or **\[field\] \[is\] \[empty\]**.

6.  To specify the sort order of the results, click **Add Sort** and then select a field to sort by and a sort order.

7.  Click **Save** to keep the filter for future use.

    For more information, see [[t_SavingFilters|Save and use filters in a list view]].

8.  Click **Run** to apply the filter.


**Parent Topic:**[[c_Filters|Filters]]

**Related topics**  


[Add related list conditions]()

[OR conditions]()

[Filter on multiple string values]()

[Dynamic operators]()

[[c_DotWalking|Dot-walking to data in related tables]]

[Field types](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_FieldTypes.md)

[[r_OpAvailableFiltersQueries|Operators available for filters and queries]]

## Related

- [[create-related-list-query|Add related list conditions]]
- [[c_ConditionBuilder|Condition builder]]
- [[t_SavingFilters|Save and use filters in a list view]]
- [[c_Filters|Filters]]
- [[c_DotWalking|Dot-walking to data in related tables]]
- [[r_OpAvailableFiltersQueries|Operators available for filters and queries]]
