---
title: "glide_list (e.g. watchlist) set with display values with a comma in it, are not parsed correctly"
aliases:
  - KB0622075
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622075
kb_number: KB0622075
last_modified: 2024-04-26
---

## glide\_list (e.g. watchlist) set with display values with a comma in it, are not parsed correctly

  

### Issue

glide\_list set with display values with a comma in it, are not parsed correctly

  
  

# Problem

* * *

When creating or updating a record that contains a glide\_list field (for example, watchlist), if the input value has a comma in any of the values, the API treats the input as two (2) different values instead of one name that contains the comma.

# Symptoms

* * *

1.  Create a new user with a name of "test, user one".
    
2.  Execute the following:
    
    test();
    function test() {
        **var** a = new GlideRecord("incident");
        a.setDisplayValue("watch\_list", "test, user one, abraham.lincoln");
        a.insert()
    };
    
    Note that watch\_list has **test, user\_one, abraham.lincoln** as three different entries.
    

# Cause

* * *

The glide\_list field parses values set as a comma-separated values.

# Resolution

* * *

There are several possible options:

-   Remove commas from the display name of the relevant records.
    
-   Set the glide\_list field with the relevant sys\_id of the target records.
    
-   Use a string field to populate the required value.
    
-   Use a custom separator for values with commas that is then processed using logic within the instance.
    
    glide\_list field parses values set as a comma-separated list. The display value from getDisplayValue() can be customized with a separator by setting the property **glide.ui.glide\_list.separator** to a string.
