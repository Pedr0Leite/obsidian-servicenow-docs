---
title: "Determining if client script settings are incorrectly configured"
aliases:
  - KB0538917
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538917
kb_number: KB0538917
last_modified: 2024-05-01
---

## Determining if client script settings are incorrectly configured

  

### Issue

Determining if client script settings are incorrectly configured

Symptoms

* * *

-   No variables on form
-   Variables values wiped out
-   Mandatory value not mandatory
-   Not mandatory is actually mandatory
-   Variable not visible
-   Variable is read-only
-   Variable is not read-only

  
Resolution

* * *

Client scripts run after the original variable configurations are rendered, so it is possible that the client scripts override the behaviors with which the variables are configured.

To determine if client script settings are incorrectly configured:

1.  Navigate to **Self-Service > Service Catalog**.  
      
    
2.  Open the item that is behaving incorrectly.  
      
    
3.  On the item page, right-click the header bar and open a client script.  
      
    

![](/sys_attachment.do?sys_id=82fce822db82b450e515c22305961913)  
  
-   Try the following troubleshooting steps:  
      
    

-   If a sub-production environment is available for testing, a simple way to test if the client script could be causing issues is to turn them off (**active=false**) in the sub-production environment and check if the issue still occurs.
-   Check lines in scripts such as ...setReadOnly(..) or ...setMandatory(...).
-   Client scripts can also be used to set Values in variables or remove invalid values. If these are used, it is possible that the created records have unexpected values.
-   Client scripts can be defined on the catalog item and also on the target record. For example, the requested item record where the variables are placed. The two client scripts may be clashing.
-   If there is a same named field on requested item and variable on the catalog item, a client script that does something like:

1.  -   g\_form.setMandatory('same\_name\_field',true) may have unexpected response
    -   It is recomended you explicitly call out variable names by using the variables. prefix. For example, the above script, if it was for the variable, should be:
    -   -   g\_form.setMandatory('variables.same\_name\_variable',true)
    -   This would remove any confusion about which element you wish to target

-   The example above shows one example of conflicts that client scripts may create. Other conflicts may occur:

1.  -   between multiple client scripts on a catalog item
    -   between client script on a catalog item and client script on the target record
    -   between client scripts and UI policies

-   In most of these cases, a good experiment is to use a sub-production instance, turn off potentially problematic client scripts, and try to narrow down the conflicting scripts.
