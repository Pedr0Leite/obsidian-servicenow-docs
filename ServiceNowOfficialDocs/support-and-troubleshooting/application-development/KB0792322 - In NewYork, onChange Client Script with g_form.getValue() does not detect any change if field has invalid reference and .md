---
title: "In NewYork, onChange Client Script with g_form.getValue() does not detect any change if field has invalid reference and hence not fired"
aliases:
  - KB0792322
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792322
kb_number: KB0792322
last_modified: 2024-04-08
---

## In NewYork, onChange Client Script with g\_form.getValue() does not detect any change if field has invalid reference and hence not fired

  

### Issue

In Madrid or older versions, onChange client script would fire even with invalid reference value populated in reference type field

Starting New York this behavior has changed and this is an intentional change where onChange client script would not fire with invalid reference value populated in reference type field.

For instance :

In New York, if there is onChange client script on the 'Assigned to' field  that sets the primary assignment group of the record based on the value populated in the 'Assigned to' field. then the onChange event does  fire when an invalid reference value is populated in the 'Assigned to' field, if there is already a value in the 'Assignment group' field. However, if the 'Assignment group' field is empty, any change to the 'Assigned to' field seems to trigger the onChange event. 

### Release

New York

### Cause

This is an intentional change in NY to match what we are actually seeing when we run g\_form.getValue()

For instance:

If you have an invalid value for assignment\_group and run "g\_form.getValue('assignment\_group');" you will see the value returned is an empty string "". This is the same value (empty string, "") returned as when you run "g\_form.getValue('assignment\_group');" with no value in the field, so script should not detect a change as the value of the field does not change and does not fire the script.

This is just for example, happens to all reference type fields.

### Resolution

This is an intentional change starting New York.
