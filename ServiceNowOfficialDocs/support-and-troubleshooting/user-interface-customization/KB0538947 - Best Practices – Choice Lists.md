---
title: "Best Practices – Choice Lists"
aliases:
  - KB0538947
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538947
kb_number: KB0538947
last_modified: 2026-01-20
---

## Best Practices – Choice Lists

  

### Issue

A choice list is a type of field that allows users to select from a pre-defined set of options. Administrators and users with the personalize\_choices role can define the available options for choice lists. This article discusses best practices for setting up choice lists, including:

-   Using only letters, numbers, and underscores in choice list options and Variable Question Choices
-   Double-checking the Value field for special characters.
-   Referencing choice lists for repetitive options.

### Release

All Releases

### Resolution

### Best Practices Video

### Using Choice Lists

Use these best practices for setting up and referencing choice lists to avoid issues and time in maintenance.

#### Best Practice #1: Consider using only letters, numbers, and underscores in Choice list options.

To set up a choice list for a **Category** field:

1.  Navigate to **Incident > Create New**.
2.  Right-click the **Category** label and select **Personalize Choices**.
3.  In the **new item** field, add \[**new\_item**\] and press **Enter**. Avoid using spaces or other special characters.
4.  Click **Save**.
5.  To view, open the **Category** choice list and scroll down to the \[**new\_item**\] created.
6.  Right-click the **Category** label and select **Show Choice List**.

When a new item is created, the system generates its **Value** field automatically from the **Label** field. Using special characters in the name, such as a space, can generate other characters, such as %, in the **Value** field. These characters can cause filtering issues, for example, when setting up a user interface (UI) policy to hide a **Subcategory** field.

#### Best Practice #2: Choice field values should be limited and relatively static 

-   The choices should be relatively static.   Data that changes regularly are better suited to reference fields than choice lists.
-   The choices are limited.   Choice lists with large quantities of choices (arbitrary rule of thumb is > 15) are better suited to reference fields if only to leverage search ability and auto-complete.
-   Choices only need one property.   Any choices that have properties of their own should absolutely be a reference to a new table.
-   Choices should be unavailable anywhere else.   For example, if someone asks you for a choice list containing a subset of locations, its better to create a new reference field with a qualifier, because location data already exists. - [Uncle Rob (serviceNow community)](https://www.servicenow.com/community/in-other-news/practice-makes-perfect-choice-lists-best-practices/ba-p/2280312 "Community - Practice Makes Perfect: Choice Lists Best Practices")

* * *

#### 

#### Best Practice #3: Reference choice lists for repetitive options.

Referencing choice lists is a shortcut for implementing multiple, identical choice lists throughout an instance. For example, there may be 50 places where the same choice list is used. Rather than creating choice lists individually, create a choice list once, and then add it to other forms by referencing the original. Not only does this save time when creating choice lists, but it also simplifies choice list maintenance.

To customize the **Category** field from the incident form to the problem form:

1.  Open the **Category** list.
2.  Navigate to **Problem** > **Create New**. 
3.  To add the **Category** field, right-click the form header, and select **Personalize > Form Layout**.
4.  Under the **Create new** field in the **Name** field, enter **Category**.
5.  For **Type**, select **Choice**.
6.  Click **Add**.
7.  In the **Selected** list, select **Category** and move up below the **Work Notes** list.
8.  Click **Save**.

Personalize the dictionary by pulling the choices from the incident table **Category** choice list:

1.  Click the **Category** list.
2.  Select **Personalize Dictionary**.
3.  For **Choice table**, select **Incident**.
4.  For **Choice field**, select **Category**.
5.  Click **Update**.

Any updates to the **Category** choice list on the incident form should automatically go to the **Category** choice list on the problem form. 

#### Best Practice #4: Do not extent the sys\_choice table.

Please note that extending the **sys\_choice** table is not supported.

**Best Practice #5: Avoid Spaces, Commas, and Special Characters When Creating Variable Question Choices**

Variable Question Choices function similarly to Choice Lists. To ensure proper functionality and maintainability, follow these guidelines when creating them:

**1\. Avoid Long Texts and Special Characters:**

-   Do not use spaces, commas, or other special characters in the "value" field of a Variable Question Choice.
-   Instead, use simple numerical values like "1", "2", "3", etc.

**2\. Benefits of Using Numbers:**

-   Simplifies maintenance of variables.
-   Makes scripting easier, especially when scaling or expanding solutions.

**3\. Example of Incorrect Behavior:**

-   If a Variable Question Choice includes long text with a comma separator, it can lead to issues.
-   For instance, when such a choice is used in the Condition Builder with operators like "is one of" or "is not one of," the system may fail to save the condition correctly to the record.

**Reason:**  
Operators such as "is one of" or "is not one of" rely on the comma as a separator to distinguish between multiple values. Including a comma in the choice value interferes with this process, leading to incorrect behavior.

### Related Links

For more information, see [Customizing Choice Lists](https://docs.servicenow.com/csh?version=latest&topicname=c_ChoiceLists.html "Customizing Choice Lists").
