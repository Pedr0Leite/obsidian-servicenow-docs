---
title: "The Field Message/Notification will be cleared if we use Client Script to set value for the field on a form"
aliases:
  - KB0686723
tags:
  - servicenow
  - support-kb
  - client-scripts
  - g_form
  - catalog-client-script
  - glideform
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686723
kb_number: KB0686723
last_modified: 2024-04-07
---

## The Field Message/Notification will be cleared if we use Client Script to set value for the field on a form

  

### Issue

We can use 'g\_form.showFieldMsg()' to create Field Message/Notification poping up under the field(c1.png). This Field Message/Notification can be cleared by 'g\_form.setValue()' function.

Considering the following scenario:

-   The customer created a Catalog Client Script whose type is 'onChange'.
-   The functionality is checking if the selected date is 5 days later in the future.
-   If the selected date is earlier than the condition, the script will show an error Field Message and then set the value of the field to null.
-   The core scripts are listed as follows:  
    -   "g\_form.showFieldMsg('u\_due\_date','Due date must be at least 5 days in the future!','error');
    -   g\_form.setValue('u\_due\_date','')"
-   Actually, the Error Field Message never show.

### Release

Kingston Patch 5, Jakarta Patch 8, Istanbul Patch 11

  

### Cause

Function 'g\_form.setValue('u\_due\_date','')' cleares the Error Field Message of the Field .

### Resolution

Change the position of the two scripts:

1.  Clear the value of 'u\_due\_date'.
2.  Set the Error Field Message.

## Related

- [[KB0687687 - GlideAjax is working inconstantly]] — another client-scripting timing/ordering pitfall
- [[KB0783579 - How to do async validation in an onsubmit client script.]] — related catalog/onSubmit client script behavior
- [[c_GlideAjaxAPI]] — official client-side scripting API reference area

### Related Links

The documentation of '[g\_form.setValue()](https://developer.servicenow.com/dev.do#!/reference/api/paris/client/c_GlideFormAPI#r_GlideFormSetValue_String_String "g_form.setValue()")' and '[g\_form.showFieldMsg()](https://developer.servicenow.com/dev.do#!/reference/api/paris/client/c_GlideFormAPI#r_GlideFormShowFieldMsg_String_String_String "g_form.showFieldMsg()")'.
