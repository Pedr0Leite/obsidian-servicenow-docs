---
title: Working with Dynamic Schema
description: Extend Dynamic Schema capabilities by defining dynamic attributes and dynamic categories in a dynamic namespace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/working-with-dynamic-schema.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Dynamic Schema, Administer, Field administration, Forms, fields, and lists, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Working with Dynamic Schema

Extend [[dynamic-schema|Dynamic Schema]] capabilities by defining dynamic attributes and dynamic categories in a dynamic namespace.

After planning your metadata strategy, you can start building out your schema by creating dynamic attribute records in the dynamic namespace. Formally defining attributes provides several key benefits.

-   Ensure data integrity, optimize queries, and improve sorting by defining dynamic attributes with appropriate types. For example, you can define attributes as strings, integers, or dates to enforce type-specific behavior.
-   Organize dynamic attributes and enable inheritance by adding them to dynamic categories. For example, you can define dynamic attributes in a parent category, and automatically access them in child categories that inherit those attributes.
-   Define a fixed set of values for an attribute by creating a dynamic choice set. For example, you can control which values are available in an attribute, which categories or namespaces they appear in, and override the values in specific cases.
-   Reuse dynamic attributes across multiple dynamic attribute store fields. For example, you can define a dynamic attribute in a dynamic namespace, and then use that attribute in any store field that belongs to that namespace.

## Implementing Dynamic Schema

Implement Dynamic Schema using the following process.

1.  [[create-dynamic-attribute-store-field|Create a dynamic attribute store field]]

    Get started by creating a dynamic attribute field for storing your dynamic attributes.

2.  [[add-dynamic-attributes|Create a dynamic attribute]]

    Define one or more dynamic attributes in the dynamic namespace that's associated with the dynamic store field.

3.  [[create-dynamic-category|Create a dynamic category]]

    Define one or more dynamic categories in the dynamic namespace.

4.  [[add-dynamic-attributes-dynamic-category|Include dynamic attributes in a dynamic category]]

    Organize your dynamic attributes using the dynamic categories that you defined.

5.  [[create-choice-set|Create a dynamic choice set]]

    Define a fixed set of choices for an attribute and create choice overrides as needed.

6.  [[add-dynamic-attributes-record|Add dynamic attributes to a record]]

    Populate the dynamic attribute store field using the GlideRecord setValue\(\) method or by entering attributes and values as JSON.

## Related

- [[create-dynamic-attribute-store-field|Create a dynamic attribute store field]]
- [[add-dynamic-attributes|Create a dynamic attribute]]
- [[create-dynamic-category|Create a dynamic category]]
- [[add-dynamic-attributes-dynamic-category|Include dynamic attributes in a dynamic category]]
- [[create-choice-set|Create a dynamic choice set]]
- [[add-dynamic-attributes-record|Add dynamic attributes to a record]]
- [[dynamic-schema|Dynamic Schema]]
