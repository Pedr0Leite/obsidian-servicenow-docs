---
title: "[Service Portal]: Injection argument not found (newValue) error"
aliases:
  - KB0749991
  - "[Service Portal] Injection argument not found (newValue) error"
tags:
  - servicenow
  - support-kb
  - service-portal
  - client-scripts
  - catalog-client-script
  - glideajax
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749991
kb_number: KB0749991
last_modified: 2024-04-07
---

## \[Service Portal\]: Injection argument not found (newValue) error

  

### Issue

# Overview

When loading or submitting catalog items on Service Portal, there can be situations where you may end up encountering the following client-side error message:

(g\_env) \[SCRIPT:EXEC\] Error while running Client Script "<script>": Injection argument not found (newValue)

# Most Probable Cause

The most probable cause is trying to make an Ajax call from client-side scripting using a variable as a parameter that "**hasn't been populated yet**" (hence explaining the above error that newValue is not found - because the new value is not provided to the variable before the Ajax call)

In other words:

-   Let's say you have variable X (empty initially)
-   You made a Ajax call by using the above variable's value (empty still)

# Example

A perfect example would be our GlideForm's getReference() API which has the following syntax:

**g\_form.getReference(fieldName, Function callback);**

So let's say I have the following scenario:

-   A reference type variable on a catalog item that targets to User table. (Let's say: "user")
-   An on-load client script with the following script:

**var userName = g\_form.getReference('user', function(usr){**  
         **alert(usr.name);**  
**});  
**

The above script is just trying to get the user's name from the respective user record table.

Now when you load this catalog item on portal, you will get the above mentioned error (once the page load completes).

Why? As explained before: the above script will run and try to get reference of the user record which "**has not been populated**" with a value yet on the "User" variable.

# Additional Information

getReference API reference: [https://developer.servicenow.com/app.do#!/api\_doc?v=madrid&id=r\_GlideFormGetReference\_String\_Function](https://developer.servicenow.com/app.do#!/api_doc?v=madrid&id=r_GlideFormGetReference_String_Function)

## Related

- [[KB0745114 - Catalog client script is not hiding the container and the variables within the container]]
- [[KB0656003 - Redirecting Service Portal Catalog Items and Troubleshooting Submission & Search Issues]]
- [[KB0750068 - ServicePortal - Getting Failing Widget Ticket Conversations error and exception]]
