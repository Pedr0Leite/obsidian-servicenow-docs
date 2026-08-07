---
title: "Configure form layout displays 'label' as section name"
aliases:
  - KB0635235
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635235
kb_number: KB0635235
last_modified: 2025-07-28
---

## Configure form layout displays 'label' as section name

  

### Issue

## Table of Contents

-   [Identifying the issue](#mcetoc_1fp76b510k)
-   [How Forms Work](#mcetoc_1fp76b510l)  
    -   [Case #1: Single Form Section](#mcetoc_1fp76h95l1p)
    -   [Case #2: Multiple Form Sections](#mcetoc_1fp76h95l1q)
-   [How to Troubleshoot](#mcetoc_1fp76b510n)  
    -   [Case #1: Single Form Section](#mcetoc_1fp76h95l1r)
    -   [Case #2: Multiple Form Sections](#mcetoc_1fp76h95l1s)

## Identifying the issue

When configuring forms, occasionally all the fields and form sections are missing, as shown in the following figure.

![](sys_attachment.do?sys_id=d53467bcdb818d10e2adc22305961986)

If this situation occurs, the form layout has a problem that needs to be addressed.

## How Forms Work

A form consists of the collaboration of multiple tables:

-   sys\_ui\_view – Holds the record for the View where the form lives
-   sys\_ui\_form – Holds the container for when a form has Multiple Form Sections
-   sys\_ui\_form\_section – A container for the section and its elements
-   sys\_ui\_section – The form section as displayed on tabs in the form
-   sys\_ui\_element - Contains the relationship to the fields on the form

When you configure the form layout, all of these tables are updated in the backend to reflect the changes made.

There are two different use cases for how forms are built. The following diagrams show how these tables work together, followed by an explanation.

### Case #1: Single Form Section

![](sys_attachment.do?sys_id=593467bcdb818d10e2adc22305961991)

For a form with a single form section, the relationship between the View and the Section is established directly without needing to reference the Form or Form Section records. The section itself is tied to multiple elements.

The view, which in many cases is the base system Default view, will be tied directly to the Section. A section for this use case tends to not contain a Caption and is not accompanied by any Tabs or additional division of sections below it. (NOTE: Sections should not be confused with related lists, which tend to be below Related links on forms.) The single section tends to inherit the name of the table. The following example shows a sample.

![](sys_attachment.do?sys_id=193467bcdb818d10e2adc2230596198c)

### Case #2: Multiple Form Sections

![](sys_attachment.do?sys_id=153467bcdb818d10e2adc22305961993)

For a form with multiple form sections, two additional tables join the schema, sys\_ui\_form, and sys\_ui\_form\_section. The sys\_ui\_form record acts as an invisible container to all the form sections and their corresponding elements. The sys\_ui\_form\_section sections are contained inside the Form record and act as containers for all the individual sections.

This schema enables you to easily modify your sections across the platform, without having to repeat the same steps on each individual view, of which there can be several, for which it would be tedious to repeat the modifications individually. It also provides a way to domain-separate the form sections if the instance is domain separated.

Keep in mind that the Form and Form Sections are containers that are not explicitly visible on the form. The following example shows this schema and how it is presented.

![](sys_attachment.do?sys_id=d13467bcdb818d10e2adc2230596198e) 

Note that even though the Form Sections are highlighting the tabs, they are just representing a container of the section inside and are not the section itself.

## How to Troubleshoot

To troubleshoot, identify which of the blocks depicted in the examples is missing, then replace it by bringing it in from another instance where the issue is not present.

### Case #1: Single Form Section

1.  Identify the view you are working on.
    
2.  Navigate to System UI > Views.
    
3.  Find and open the record for the view identified in step 1.
    
4.  Go to the Sections tab in the related records and look for the affected section by searching for it using the table name.
    
    If one is not found, then you need to address the issue. If you have another instance where the section exists, you can export the XML file for that one and import it in the affected environment. To ensure that you have the right form section, verify the sys\_id by going to the form, bringing up your browser developer tools, and, in the elements section, look for an element where the ID starts with section\_tab. The sys\_id for the corresponding section will follow the section\_tab text, for example, section\_tab.bfb81dc9c0a8000900127627db594210.
    
    The following figure shows an example.
    
    ![](sys_attachment.do?sys_id=9d3467bcdb818d10e2adc2230596198f)
    
5.  Import the XML file from your other instance.
    
    If none exist, contact Customer Support for further troubleshooting.
    
6.  Run cache.do in your instance to clear the instance cache and reflect the changes.
    

### Case #2: Multiple Form Sections

1.  Identify the view you are working on.
    
2.  Navigate to System UI > Views.
    
3.  Find and open the record for the view identified in step 1.
    
4.  Go to the Forms tab in the related records and look for the affected section by searching for it using the table name.
    
    If one is not found, you need to address the issue. If you have another instance where the section exists, you can export the XML file for that one and import it in the affected environment.
    
5.  If the form exists, open the record and review every related form section record to ensure it exists.
    
    If one does not exist, import it from an instance where the issue is not present. Ensure that the sys\_id's for the missing section match the instance where the issue is not present. Repeat this for any missing Form, Form Section, Section, or Element that you find is missing.
    
6.  Run cache.do in your instance to clear the instance cache and reflect the changes.
    

The following video provides a live example of how to fix multiple form sections (with audio).

Once you are finished, your form layout should be back to normal and you should be able to configure it in the conventional ways.

### Release

All Releases

### Resolution

#### Case 1: Single Form Section

1.  Identify the view:  
    Navigate to System UI > Views, and locate the one in use.
2.  Check Section record:  
    In the Sections related list, find the section associated with the table.  
    If missing, locate a working version in another instance, export the XML, and import it.
3.  Find Section sys\_id (optional):  
    Open the form in your browser, use DevTools, and search for elements with ID **section\_tab.<sys\_id>** to confirm.
4.  Run **cache.do**:  
    Refresh your instance’s cache to apply changes.

* * *

#### Case 2: Multiple Form Sections

1.  Identify the view:  
    Navigate to System UI > Views.
2.  Check Form and Sections:
    -   In the Forms related list, find the **sys\_ui\_form** for the table/view.
    -   Review all related Form Section, Section, and Element records.
    -   If any are missing, export/import from a working instance or rebuild manually.
3.  Verify sys\_id consistency:  
    Ensure that sys\_ids match when copying from another instance to avoid broken references.
4.  Run **cache.do**:  
    Clear cache to apply the updates and verify form renders correctly.

* * *
