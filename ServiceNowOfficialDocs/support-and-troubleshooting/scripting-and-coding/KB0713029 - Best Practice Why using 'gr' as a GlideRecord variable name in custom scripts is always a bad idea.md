---
title: "Best Practice: Why using 'gr' as a GlideRecord variable name in custom scripts is always a bad idea"
aliases:
  - KB0713029
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713029
kb_number: KB0713029
last_modified: 2026-02-06
---

## Best Practice: Why using 'gr' as a GlideRecord variable name in custom scripts is always a bad idea

  

### Issue

Any script in the instance could have unexpected behaviour.

### Release

Any

### Cause

It is very common to see "gr" used as a variable name in scripts in a ServiceNow instance, in examples in the official documentation, community forums, and other places, and of course AIs fed on those sources. e.g.

var gr = new GlideRecord('incident');

**This is a bad idea!**

The platform is JavaScript and a lot of code is run in a Global Variable Scope.

**A "gr" defined in one business rule can clobber another "gr" defined in some other script**, which happens to be running as part of the same update or transaction. One 'gr' can be replaced by the other 'gr' for something completely unrelated, and your script will continue running subsequent lines thinking it is the one it defined.

Your script could end up returning no query result, or updating a different record, from even a different table, than the one you have just queried for in your script. That can clearly have serious implications.

A real world example:

-   In a customer's incident, a simple gr.get(); query of the incident table from a script in a workflow returned no records returned because the Requested Item table was actually what was unknowingly being queried.
-   That was due to a requested item query business rule running, for a linked related record being run in the same transaction, that happened to also use 'gr' for the sc\_req\_item table.
-   The custom script in the workflow assumed a record was returned, but did not actually check. It used the gr.assigned\_to value, which was null, and did not check it had a real value.
-   The 'null' result was then used for another query on the user table for a Notification, resulting in every employee in the company receiving the email.
-   Ouch!

In this kind of situation debugging to figure out what other code is breaking your code is also almost impossible, as you have to take everything running as part of the complete transaction into account. Adding lots of gs.info() messages into the code to double check all the values.

### Resolution

General good javascript coding practice would avoid most of these issues.

You could wrap your scripts in a function to avoid your script clobbering another gr, which is why new business rules, calculated fields, etc. mostly now have a default script added to wrap the code to protect the variables within the function, but most scripts and including older business rules don't require this. **Wrapping your code in a function is good coding practice**, so always do this.

When using more than one GlideRecord in your script, you may also accidentally re-use the gr name. The best practice is to **use your own unique variable names, relevant to the table you are using, and never use 'gr'**. e.g. 

function updateOpenIncidents() {
    var **openIncidentGr** = new GlideRecord('incident');
    ....
}
updateOpenIncidents(); // runs the above function

So, **just don't do it**, and you will reduce the chances of this happening.

### Related Links

This doesn't just apply to "gr". **Using "i" as a for loop counter everywhere is also bound to cause trouble sooner or later**. Symptoms would be for loops that end early or go infinite.

The platform has reserved names, which should also never be used for your own variables: **answer, current, previous etc**.

Problem tickets directly related to this cause:

-   [PRB1320166 MID Server Business rule 'Probe - All MIDs' isn't protecting its global scope javascript variables from being clobbered (MID Servers wrongly reported as DOWN)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0721229 "PRB1320166 MID Server Business rule 'Probe - All MIDs' isn't protecting its global scope javascript variables from being clobbered (MID Servers wrongly reported as DOWN)")
-   PRB612498 Use of "answer" variable (or other same variable name) in script & calculated dictionary fields, will cause "answer" variable in script overwritten by calculated field values
-   [PRB1351676 Publish to Hardware Catalog redirects to Record Not Found, caused by the "gr" in global scope in the publish\_to\_product\_catalog UI Page Processing Script](https://support.servicenow.com/kb_view.do?sysparm_article=KB0755786 "PRB1351676 Publish to Hardware Catalog redirects to Record Not Found, caused by the \"gr\" in global scope in the publish_to_product_catalog UI Page Processing Script")
-   [PRB1508005 Clear MID Environment Cache business rule uses variable name "gr" in global variable scope, risking the variable being clobbered/clobbering other variables, and breaking updates of cmdb\_ci\_ip\_address records](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966071 "PRB1508005 Clear MID Environment Cache business rule uses variable name \"gr\" in global variable scope, risking the variable being clobbered/clobbering other variables, and breaking updates of cmdb_ci_ip_address records")

[W3 Schools: JavaScript Scope](https://www.w3schools.com/js/js_scope.asp)  
[Rhino: Scopes and contexts](https://rhino.github.io/docs/scopes_and_contexts/)
