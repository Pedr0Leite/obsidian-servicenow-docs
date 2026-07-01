---
title: Grid-style fields and field collections
description: Learn about the various types of grid-style fields: the picklist extension, the field grid, the indexed set, the associated picklist set, and the product picker. Learn how best to choose a field type for your data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/what\_field\_type\_should\_i\_use\_for\_organizing\_field\_options\_and\_data.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Configure fields, CPQ app, Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Grid-style fields and field collections

Learn about the various types of grid-style [[fields|fields]]: the picklist extension, the field grid, the indexed set, the associated picklist set, and the product picker. Learn how best to choose a field type for your data.

In CPQ, although many grid-style fields and field collections look similar to an end user, they have different behaviors and uses for admins. This article explains the basic capabilities of each and their intended [[use-cases|use cases]]. It also provides the necessary resources for those who want to explore each option’s setup at a deeper level.

## Picklist extension

\[Omitted image "cpq-field-types-picklist-extension.png"\] Alt text: Picklist extension

A picklist extension is a field type that displays extended information. It may be used to show more option details or to show dynamic pricing options with the Picklist Extension Pricing enrichment. A picklist extension can include images and supports multi-select and single-select actions. It can send product information directly to the bill of materials \(BOM\).

A picklist extension uses exclusion [[rules_101|rules]] and option filters to populate what end users see. Only one field is editable out of the grid \(the selection\).

For an overview of the picklist extension feature, see [[cpq-picklist-extensions-ples|Picklist extensions]].

For a deeper understanding of the back end and how to display picklist extensions, see [[csv_layouts_how_do_i_display_a_picklist_extension|Displaying a picklist extension on a layout]].

For an overview of the Picklist Extension Pricing enrichment feature, see [[picklist-extension-pricing-scripts|The Picklist Extension Pricing enrichment]].

For information about using picklist extensions in rules, see [[cpq-picklists-and-picklist-extensions-in-rules|Picklists and picklist extensions in rules]].

## Field grid

\[Omitted image "cpq-field-types-field-grid.png"\] Alt text: Field grid

A field grid is a grid of independent fields in a format of rows and columns. It may be used to display similar and codependent fields in an easy-to-format pattern, when the number of fields to display is static, or when each field needs to be referenced outside of its own row and column.

Each field can be referenced and manipulated by any rule and must be independently defined. For example, a 3 x 3 row requires 9 fields.

For information about how to set up a field grid using the [[matrix_loader_table_of_contents|Matrix Loader]], see [Layouts: Field grid setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown).

## Indexed set

\[Omitted image "cpq-field-types-indexed-set.png"\] Alt text: Indexed set

An indexed set is a dynamic set of repeating identical fields. It can be used to display options for a component that can be changed per component, or to aggregate costs and quantities for simple product rules. It tends to require little setup and maintenance.

Each field can be cloned and edited separately depending on an outside number field. You only need to create the fields in each row, not one field per cell.

Each set field can only affect the fields in its row.

Each column can be aggregated into a field that can be referenced outside the set. It can be configured to display across tiers.

For more information about [[cpq-sets|sets]], set aggregates \(collections of sets\) and about how to use sets in [[layouts|layouts]], see:

-   [[sets|Configure sets]]
-   [[creating_set_aggregates|Creating set aggregates]]
-   [[layouts-sets|Using sets in layouts]]

## Associated Picklist set

\[Omitted image "cpq-field-types-associated-picklist-set.png"\] Alt text: Associated picklist set

An Associated Picklist set is a dynamic set of repeating fields based on the options of a picklist. It may be used to aggregate costs and work hours for distinct services, to limit the options of a configurable component, or to expand and use more field options for a picklist than a picklist extension.

Each field can be cloned and edited separately depending on an outside picklistʼs selections. You only need to create the fields in each row, not one field per cell.

Each set field can only affect the fields in its row.

Each column can be aggregated into a field that can be referenced outside the set. It can be configured to display across tiers.

For more information, see [[creating_an_associated_picklist_set|Creating an associated picklist set]].

## Product Picker

\[Omitted image "cpq-field-types-product-picker.png"\] Alt text: Product picket

The product picker field type is a product-based table of distinct options and qualities similar to the Associated Picklist set, but with built-in product rules. It may be used when product options need further information from the end user before being added to the BOM.

Each option is defined like a picklist, but every cell contains an editable field. You only need to define the options and fields, as shown in the row and column headers.

Value, Select, and Quantity are automatically added, and will automatically send end-user selections to the BOM. Field behavior in a product picker is determined by product picker bulk actions.

This field can affect fields outside the product picker by means of rules.

For more information, see:

-   [[product_picker_overview|Product pickers]]
-   [[product_picker_bulk_actions|Product picker bulk actions]]

**Related topics**  


[[system_fields_vs_partner_fields|CPQ fields, system fields, and partner fields]]

[[fields_101|Configure fields]]

## Related

- [[cpq-picklist-extensions-ples|Picklist extensions]]
- [[csv_layouts_how_do_i_display_a_picklist_extension|Displaying a picklist extension on a layout]]
- [[picklist-extension-pricing-scripts|The Picklist Extension Pricing enrichment]]
- [[cpq-picklists-and-picklist-extensions-in-rules|Picklists and picklist extensions in rules]]
- [[sets|Configure sets]]
- [[creating_set_aggregates|Creating set aggregates]]
- [[layouts-sets|Using sets in layouts]]
- [[creating_an_associated_picklist_set|Creating an associated picklist set]]
- [[product_picker_overview|Product pickers]]
- [[product_picker_bulk_actions|Product picker bulk actions]]
- [[system_fields_vs_partner_fields|CPQ fields, system fields, and partner fields]]
- [[fields_101|Configure fields]]
- [[fields|Fields]]
- [[use-cases|Use cases]]
- [[rules_101|Rules]]
- [[matrix_loader_table_of_contents|Matrix Loader]]
- [[cpq-sets|Sets]]
- [[layouts|Layouts]]
