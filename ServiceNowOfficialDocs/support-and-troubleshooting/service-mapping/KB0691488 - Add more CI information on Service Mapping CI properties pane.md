---
title: "Add more CI information on Service Mapping CI properties pane"
aliases:
  - KB0691488
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691488
kb_number: KB0691488
last_modified: 2025-01-03
---

## Issue

On the Service Mapping map display, on the right pane there is information about the CI you are viewing.

This information is about the CI and is relative to the data in the record fields of that CI

This KB will go over how to add/remove what fields will show in that pane of a specific 

  

#   

  

## Resolution

1.  Open any CI from the class you want to modify the properties display for.
2.  Right-click on the grey header banner and select Configure > Form Layout.
3.  There is a field called 'Views' and select the view called 'sa\_map\_properties'.  
    -   If it does not exist then create the new one and give it that name (case sensitivity might apply so make sure it is exactly as you see in the previous line).
4.  In that view add the fields you want to see for that class.
5.  It is recommended not to add more than 4 or 5 fields.  
    -   Note: Not all fields might appear on that properties pane even if you add them.
    -   Note: Some fields, even if you add or remove from the view may or may not appear.

  

## Additional Information

This is a very limited customization.

It is not a perfect process and this method is not officially supported so if there are issues with adding fields then there is not much else that can be done at this time.
