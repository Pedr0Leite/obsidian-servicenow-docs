---
title: "List fields do not support choices"
aliases:
  - KB0656550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656550
kb_number: KB0656550
last_modified: 2025-10-16
---

## List fields do not support choices

  

### Issue

A configuration that is becoming more and more common is using a List type field (like watch\_list) with choices. This is being done to create a sort of "multiple choice" field but it is not a supported configuration and can lead to problems.  

Some of the problems that this can cause are:

-   Choices in the list may show their value instead of their label.
-   Scripted logic performing operations against the mis-configured field do not function as expected.
-   Choices are not translated properly.
-   Unable to set the field value via template.

### Cause

These issues come up because the List field type was not designed to be used in this way. It is a reference field and the only supported configuration is that it is set up as a reference field.

### Resolution

Make sure the field is configured properly in the the system dictionary.

1\. List fields are reference fields so make sure you have a valid reference configured.

![](https://support.servicenow.com/sys_attachment.do?sys_id=8e8ebdffdba28d10e515c22305961954)

2\. Make sure there are no choices defined in the Choices related list.

![](https://support.servicenow.com/sys_attachment.do?sys_id=828ebdffdba28d10e515c22305961952)

3\. Make sure that the choice list specification is set to "none".

![](https://support.servicenow.com/sys_attachment.do?sys_id=8e8ebdffdba28d10e515c2230596197b)

If you're used to using these fields as "multiple choice" fields, the best way to accomplish this without going against the design of the data type is to create a choice table and define the choices you need there. Then, configure the field so that it references that table and remove your old choice configurations.
