---
title: "Host detection fails when debugging pattern"
aliases:
  - KB0693353
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693353
kb_number: KB0693353
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

-   Run debug on any pattern, after filling in the connection information an error is thrown during host detection.
-   If you run discovery the pattern will run fine, it is just the debug that fails with the following error. 
-   Error: 
    -   Host Detection Failed for IP Address xx.xx.xx.xx

                              ![](sys_attachment.do?sys_id=861f7026db0ab450e515c2230596192b)

# Release

* * *

-   Any that are using patterns

# Cause

* * *

-   There is cmdb field called 'Operation Status'. This field has some choices, with the first choice called "Active". 
-   That choice has a value of "1"
-   If you customize the choices for that field and your active state is some other value other than 1 then when you run debug the error above will be thrown.
    -   Note: If you 'Show XML' on the CI record and check the value for operational status field, it should say '1' between the tags, where the corresponding display value for that value, on the form, is "Active".
-   Note: This is relative to what the host device's operational status in your cmdb is at the time of debugging. (See Additional Information below). 

# Resolution

* * *

-   Just be sure to use the out of box "Active" choice for the "Operational Status" field.
-   If you customize the choices, just be sure that your version of "Active" choice has a value of "1". 

# Additional Information (Example)

* * *

-   Lets says you have a linux server that hosts Apache.
-   You have also customized the Operation Status field on your cmdb\_ci table, such that the choice for "Active" state does not have a value of "1".
-   You go to the "Apache on Unix pattern" pattern and run debug.
-   The first thing it will do is to check that the host is in the cmdb, it will not look at any record that is not in an active operational state.  Since it does not look for CIs that are not active, it will never find it and hence the error is thrown.
