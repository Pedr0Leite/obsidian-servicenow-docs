---
title: "Understanding the structure of forms in the ServiceNow platform"
aliases:
  - KB0656398
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656398
kb_number: KB0656398
last_modified: 2026-05-26
---

## Understanding the structure of forms in the ServiceNow platform

  

### Issue

Forms in the ServiceNow platform are built from a set of related database tables. Understanding how these tables connect helps administrators troubleshoot form issues and manage update sets correctly. The number of tables involved depends on how many sections a form contains. A single-section form uses four tables. A multi-section form uses six tables.

### Release

All

### Resolution

  The following explains the structure of multi-section and single section forms and the tables that are involved.

### Multi-Section Forms

A multisection form contains at least two sections, which might be displayed as tabs. These forms are comprised of the following tables:

-   sys\_ui\_view: The table of different views to which a form must be associated.
-   sys\_ui\_form: The parent that ties form sections together.
-   sys\_ui\_form\_section: A many-to-many relationship record required for forms with multiple sections. Relates each sys\_ui\_section record back to the sys\_ui\_form record.
-   sys\_ui\_section: The parent that ties the objects on a form to a particular section.
-   sys\_ui\_element: Defines the actual objects on the form. If you have 25 items in a section, 25 of these records will be tied to that section.
-   sys\_ui\_related\_list: Defines the related lists that appear on a particular table/view combination.

The following example shows how these tables are connected to each other:

![Multi form table structure](sys_attachment.do?sys_id=d7736bd697c5c310dfd73dae2153afce "Multi form table structure")

![Sys ui form structure in the platform form](sys_attachment.do?sys_id=a373abd697c5c310dfd73dae2153af12 "Sys ui form structure in the platform form")

### Single Section Forms

The number of tables involved with a single-section form is much lower:

-   sys\_ui\_view: The table of different views to which the single-form section must be associated.
-   sys\_ui\_section: The parent that ties the objects on a form to the single section.
-   sys\_ui\_element: Defines the actual objects on the form. If you have 25 items in a section, 25 of these records will be tied to that section.
-   sys\_ui\_related\_list: Defines the related lists that appear on a particular table/view combination.

There are no sys\_ui\_form or sys\_ui\_form\_section records in a single-section form. Once you add a second section to the form, entries will be created in those tables.

The following example shows how these tables are connected to each other in a single-section form:

![sys ui form for single section form](sys_attachment.do?sys_id=2773abd697c5c310dfd73dae2153af1b "sys ui form for single section form")

![single section form structure](sys_attachment.do?sys_id=eb73abd697c5c310dfd73dae2153af16 "single section form structure")

### Related Links

Product documentation on [Using Forms](https://docs.servicenow.com/csh?topicname=c_UsingForms.html&version=latest "Using Forms").
