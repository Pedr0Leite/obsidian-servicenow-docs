---
title: "When using Flow Designer, or GlideRecord to set the password of a newly created user record, the password does not work to log in"
aliases:
  - KB0815360
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815360
kb_number: KB0815360
last_modified: 2024-08-21
---

## When using Flow Designer, or GlideRecord to set the password of a newly created user record, the password does not work to log in

  

### Issue

-   If you use Flow Designer to create a new \[sys\_user\] record and set the password. When you try to log in as the newly created user, the password does not work
-   The same thing when you use GlideRecord to set the password, the password does not work

### Release

All

### Cause

-   When using Flow Designer or GlideRecord, the password is stored unencrypted on the \[sys\_user\] record.
-   The actual value that should be stored on the password field is a hash value of the password you're wanting to use.
-   When you try logging in, the password you input is encrypted, it's hash value is compared to the hash value being stored on the \[sys\_user\] record, since Flow Designer or GlideRecord did not encrypt the password, it's will fail the check. 

### Resolution

-   As a workaround, manually create a temporary \[sys\_user\] record, and set the password, save the record
-   On form reload, show XML, and copy the value stored in the user\_password field
-   this is the hash value of the password that was set
-   used this value, in FD, or GlideRecord

another alternative is to set the password via a flow script step

var gr = new GlideRecord("sys\_user");
gr.get("62826bf03710200044e0bfc8bcbe5df1"); // abel.tuter
gr.setDisplayValue("user\_password","c34V6e4r#E@W");
gr.update();  
  
the method setDisplayValue() will save the string as the hash value of the password
