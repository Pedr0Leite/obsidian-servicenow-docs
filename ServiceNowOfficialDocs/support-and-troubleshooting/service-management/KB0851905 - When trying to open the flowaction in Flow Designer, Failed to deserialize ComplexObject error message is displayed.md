---
title: "When trying to open the flow/action in Flow Designer, \"Failed to deserialize ComplexObject\" error message is displayed"
aliases:
  - KB0851905
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0851905
kb_number: KB0851905
last_modified: 2024-04-08
---

## When trying to open the flow/action in Flow Designer, "Failed to deserialize ComplexObject" error message is displayed

  

### Issue

When trying to open the flow/action in Flow Designer, "Failed to deserialize ComplexObject" error message is displayed.

Browser Console Error:  
Failed to load resource: the server responded with a status of 500 (Internal Server Error)  
js\_includes\_amb.jsx:3 amb.ServerConnection \[ERROR\] Connection broken

### Cause

-     
    

The issue might be:

\- Due to the max length problem (Somehow the complex object field was set to have a max length of 500 when changed it to 8000 it works).  

OR

\- Complex object data for Action Output was wrongfully saved as a wrong data type (Somehow complex data staying as Array.Object format where its type was updated to String type and therefore a type mismatch had occurred).  

OR

\- Users might have an input/output with the name "sys\_id" which is restricted and causes database issues.

  

### Resolution

We would recommend:

\- Changing the max length of the field and then disassociating the truncated complex object value from the flow should fix this issue. (Note: We now normally set complex objects to 65000 max length.)

OR

\- Updating the sys\_complex\_object table files to specify complex data as the correct object type should fix this issue.

OR

\- Users can use other words from reserved/restricted keywords (like sysid but not sys\_id) should fix this issue.
