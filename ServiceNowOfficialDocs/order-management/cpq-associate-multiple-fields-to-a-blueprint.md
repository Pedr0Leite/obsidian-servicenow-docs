---
title: Associate multiple fields to a blueprint
description: You can associate any number of fields to a blueprint by using the Blueprint Import function in the Matrix Loader.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/cpq-associate-multiple-fields-to-a-blueprint.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Set up blueprints, CPQ app, Configure, price, quote apps, Configure, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Associate multiple fields to a blueprint

You can associate any number of [[fields|fields]] to a blueprint by using the Blueprint Import function in the [[matrix_loader_table_of_contents|Matrix Loader]].

## Before you begin

Role required: Admin

## Procedure

1.  Create or edit a blueprint.yaml file and define the blueprint variable name and name in the following format \(removing the angle brackets around the variable names\).

    ```
    [[blueprints|blueprints]]:
    -variableName: <variableNameOfBlueprint>
    	relatedFields:
    	-<fieldVariableName1>
    	-<fieldVariableName2>
    	-<fieldVariableName3>
    	-<etc...>
    name: <Name of Blueprint>
    ```

2.  Add the variable names of the desired fields.

3.  Import the YAML file into the Matrix Loader.

    Choose Blueprint as the upload type.

    **Note:** Any existing fields or [[configurable-products-explore|configurable products]] in the blueprint will be disassociated from it unless they are also defined in the YAML file.


**Related topics**  


[[enable-markdown-in-text-fields|Enable Markdown in text fields]]

## Related

- [[enable-markdown-in-text-fields|Enable Markdown in text fields]]
- [[fields|Fields]]
- [[matrix_loader_table_of_contents|Matrix Loader]]
- [[blueprints|Blueprints]]
- [[configurable-products-explore|Configurable products]]
