---
title: "Best Practices – System Properties"
aliases:
  - KB0538866
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538866
kb_number: KB0538866
last_modified: 2025-01-28
---

## Best Practices – System Properties

  

### Issue

This article describes how system administrators can manage script behavior by creating system properties to use in scripts. Best practices include:

## Table of Contents

-   [Best Practices Video](#mcetoc_1foi1u9i3ji)
-   [Using System Properties](#mcetoc_1foi1u9i3jj)
-   [1\. Using system properties instead of hard-coded values](#mcetoc_1foi1u9i3jk)
-   [2\. Defining and using a naming convention](#mcetoc_1foi1u9i3jl)
-   [3\. Grouping properties into categories](#mcetoc_1foi1u9i3jm)
-   [4\. Creating a Properties page to display properties](#mcetoc_1foi1u9i3jn)

### Best Practices Video

### Using System Properties

System properties are maintained in the **System Property** table \[sys\_properties\]. You can access this table via the module navigator, or directly typing sys\_properties.list in the **Navigator Filter**.

 **Warning:** System properties store configuration information that rarely or never changes. Each time you change or add a system property, the system flushes the cache to keep all nodes in the cluster in sync. This cache flush might cause temporary performance issues to the instance if done excessively. As an alternative to a system property to store configuration information that changes more than once or twice a month, you can use instead a custom table to store regularly changing configuration information.

### Release

  All Releases

### Resolution

### 1\. Using system properties instead of hard-coded values

When required values are hard-coded into the server-side scripts, changes to these values must be manually adjusted in every script where they appear. To save time and maintenance, create system properties so that your scripts can use the values contained in those properties. When a system change is required, changes made to a single system property can be implemented system-wide.

### 2\. Defining and using a naming convention

Define and use a naming convention that makes the property easy to manage. This allows users to filter custom properties from the hundreds in the system properties list.

To define a property:

1.  Create a property name with the company name.
2.  Add the application or process name (or both) using a _dot notation_ to separate the elements.
3.  Add a description that is short and meaningful. If the property refers to a script, include the script name. For example, _cd.default.assignment\_group_.
4.  To create system properties for the values:  
    1.  Navigate to **System Properties**
    2.  Check for an existing property with the needed functionality before creating a new one.
    3.  Click **New**
    4.  In the **Name** field, enter cd.default.assignment\_group (for example).
    5.  In the **Description** field, enter the default assignment group description.
    6.  From the **Type** choice list, select **String**.
    7.  In the **Value** field, enter the corresponding value for the default assignment group.
    8.  **Submit**

### 3\. Grouping properties into categories

To create a category to group properties:

1.  Navigate to **System Properties > Categories**.
2.  Click **New**
3.  In the **Name** field, enter the new category.
4.  In the **Description** field, enter the category description.
5.  Right-click the form header and select **Save**.  
    The properties-related list is now displayed.
6.  Click **Edit**.
7.  Select the properties and add them to the new category.

### 4\. Creating a Properties page to display properties

The Properties page gives easy access to all of the properties in one place. To display properties, create a new module under the appropriate application menu.

1.  Right-click the application and select **Edit Application Menu**.
2.  In the modules-related list, click **New**.
3.  In the **Title** field, enter **Properties**.
4.  In the **Link type** field, select **URL** (from Arguments).
5.  In the **Roles** field, select **admin**.
6.  In **Order**, use the number where this should appear on the application menu.
7.  Click the image icon.
8.  Select the **Properties** icon.
9.  For **Arguments**, use the system properties UI page.
10.  **Submit**

The property page now appears in the application menu.
