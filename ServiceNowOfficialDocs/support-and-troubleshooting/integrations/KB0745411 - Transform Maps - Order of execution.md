---
title: "Transform Maps - Order of execution"
aliases:
  - KB0745411
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745411
kb_number: KB0745411
last_modified: 2026-06-24
---

## Transform Maps - Order of execution

  

### Issue

It is very important to understand the order of execution of transform map and its scripts before creating one because incorrect assumptions about this order can cause major issues.

### Release

Applicable to all releases

### Resolution

1\. Run the onStart Script

-   onStart: This script runs once at the beginning of the import process, before any data rows are read. It is used for initialization tasks, such as setting up preconditions or sending notifications that an import has started. At this stage, you cannot access field values.

2\. Find the target record by evaluating all coalesce field maps/scripts

-   Before any other scripts are executed, the target record is found using the coalesce fields

3\. Run the onBefore Script

-   onBefore: This script executes before each row is transformed. It allows you to manipulate or validate the data before it is inserted or updated in the target table. You can set or alter values on the source table, validate data, or set the `ignore` variable to `true` to skip the record.

Note: Since this is executed after finding the target record, you need to make sure the coalesce scripts do not depend on any variables defined here in the onBefore script.

4\. Transform all field mappings

5\. Run the main transform Run Script

-   Run Script: the "Run Script" option is a powerful tool that allows you to execute custom scripts to manipulate data during the transformation process. This option is particularly useful when you need to perform complex data transformations that cannot be achieved through simple field mappings. By selecting the "Run Script" checkbox, you can write a script to map source table fields to target table fields, enabling you to alter or change the source field data before it is assigned to the target fields.

6\. Run the onAfter script

-   onAfter: This script runs after each row has been processed and the data has been transformed and inserted into the target table. It allows you to access the target record and perform additional actions, such as updating related records or sending notifications or any other operations that you would like to do only after data is been transformed and inserted in the target table

7\. Repeat 2-6 for all import set rows.

8\. Run the onComplete Script

-   This script runs once after all data rows have been read and transformed. It is used for final tasks, such as sending notifications or updating system properties, etc.
