---
title: Create a dynamic namespace
description: Define categories and attributes once and reuse them across multiple tables and dynamic attribute store fields.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/create-dynamic-namespace.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Dynamic Schema, Administer, Field administration, Forms, fields, and lists, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Create a dynamic namespace

Define categories and attributes once and reuse them across multiple tables and dynamic attribute store fields.

## Before you begin

Role required: dynamic\_schema\_writer

## About this task

All dynamic categories and dynamic attributes belong to a dynamic namespace that you can associate with one or more dynamic attribute store fields.

A dynamic namespace is automatically created when you [[create-dynamic-attribute-store-field-transient|create a dynamic attribute store field]]. However, you can also create a dynamic namespace manually, and then associate it with one or more store fields. You might create a dynamic namespace this way in the following scenarios:

-   You created a dynamic attribute store field for storing transient attributes, which automatically created an associated namespace, but now you want to associate the store field with a different namespace that contains a different set of dynamic categories and dynamic attributes.
-   You created multiple dynamic attribute store fields on one or more tables, and you want them all to share the dynamic categories and dynamic attributes that you defined in a new namespace.

Note that changing the namespace associated with a dynamic attribute store field doesn't modify any saved data in the store field, but can affect how the system interacts with that data.

## Procedure

1.  Navigate to **All** &gt; **[[dynamic-schema|Dynamic Schema]]** &gt; **Dynamic Namespaces**.

2.  Select **New**.

3.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Label|Label used for displaying the dynamic namespace.|
    |Name|Internal name for the dynamic namespace.|
    |Description|A brief summary of what the namespace contains.|
    |Active|Option to activate the dynamic namespace.|


## Create a dynamic namespace for capturing everything about products in a department store

\[Omitted image "dynamic-namespace-example.png"\] Alt text: Creating a new namespace for Departments.

## What to do next

-   [[add-dynamic-attributes|Create a dynamic attribute]]
-   [[create-dynamic-category|Create a dynamic category]]
-   [[add-dynamic-attributes-dynamic-category|Include dynamic attributes in a dynamic category]]
-   [[create-choice-set|Create a dynamic choice set]]
-   [[update-dynamic-namespace-dynamic-attribute-store|Associate a dynamic attribute store with a different namespace]]

## Related

- [[add-dynamic-attributes|Create a dynamic attribute]]
- [[create-dynamic-category|Create a dynamic category]]
- [[add-dynamic-attributes-dynamic-category|Include dynamic attributes in a dynamic category]]
- [[create-choice-set|Create a dynamic choice set]]
- [[update-dynamic-namespace-dynamic-attribute-store|Associate a dynamic attribute store with a different namespace]]
- [[create-dynamic-attribute-store-field-transient|Create a dynamic attribute store field]]
- [[dynamic-schema|Dynamic Schema]]
