---
title: "How to search, group, and sort on a Glide List field in a list view"
aliases:
  - KB0596181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596181
kb_number: KB0596181
last_modified: 2026-02-25
---

## How to search, group, and sort on a Glide List field in a list view

  

### Issue

Learn about the limitations of interacting with a Glide List (glide\_list) field in a list view and how to work around them.

The following limitations apply to Glide List fields in a list view:

-   The search box at the top of the list is not available for Glide List fields, such as the Watch list field on Incident.

![](/sys_attachment.do?sys_id=73f33b9d47573254343d8b69736d4318)

-   The Group By option is not available for a Glide List field.
-   Alphabetical sorting is not available on a Glide List field.

![](/sys_attachment.do?sys_id=a7f33b9d47573254343d8b69736d4312)

### Release

All supported releases

### Cause

A Glide List (glide\_list) field stores the sys\_id values of referenced records, similar to a reference field. However, a Glide List field can store multiple sys\_id values and email addresses as a comma-delimited string in the database.

For example, a script that retrieves the value of the **Watch list** field on an incident record returns output similar to the following:

\*\*\* Script: 62826bf03710200044e0bfc8bcbe5df1,5137153cc611227c000bbd1bd8cd2007,sampleuser@test.com

Because the field stores sys\_id values rather than display values, searches using display values do not return results. For example, the query watch\_listLIKEAbel Tuter does not match the stored value `watch_listLIKE62826bf03710200044e0bfc8bcbe5df1`. For this reason, sorting is disabled on this field type.

This behavior also affects grouping. Grouping is based on the stored value, and no two records are guaranteed to have the same arrangement of referenced values. For example, one record might store Abel Tuter and David Loo in that order, while another record stores David Loo and Abel Tuter.

![](/sys_attachment.do?sys_id=b3f33b9d47573254343d8b69736d434d)

### Resolution

There is no resolution to these limitations because of how Glide List fields store data. However, the following workarounds are available depending on what you are trying to achieve.

**Searching** 

To search on a Glide List field in a list view:

1.  Expand the list filter.
2.  Select the Glide List field to search. Only the following operators are available: contains, does not contain, is empty, and is not empty.
3.  Select an operator.
4.  In the reference search box, select a referenced record using the Lookup icon.
5.  Run the search.

**Note**: If a Glide List field is displayed in the list view layout, the search results show all values stored in the Glide List field for each matching record, not just the value you searched for. The search is working as expected because it returns records where the Glide List matches the search criteria.

![](/sys_attachment.do?sys_id=7bf33b9d47573254343d8b69736d4335)

**Grouping** 

To enable grouping on a Glide List field, add the can\_group=true attribute to the field's dictionary entry. This makes the **Group By** option available.

**Note**: Because grouping is based on stored sys\_id values and their order, the grouped output may not appear to be logically organized. See the Cause section for details.  
  
![](/sys_attachment.do?sys_id=fff33b9d47573254343d8b69736d433a)

**Scripting** 

When working with Glide List fields in scripts, refer to the following product documentation:

-   [Referencing a Glide list from a script](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Referencing a Glide list from a script")

-   [Using indexOf("searchString")](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Using indexOf(\"searchString\")")

When filtering with addQuery or addEncodedQuery, search against the sys\_id value rather than the display value. You can create a helper function that looks up the display value and returns the sys\_id. The following example searches for incidents where Abel Tuter is on the Watch list:

var inc = new GlideRecord('incident');  
inc.addEncodedQuery('watch\_listLIKE' + getUserSID('Abel Tuter'));  
inc.query();

while (inc.\_next()) {  
  gs.print(inc.number + " | " + inc.watch\_list);  
}

function getUserSID(name) {  
  var user = new GlideRecord('sys\_user');  
  if (user.get('name', name)) {  
    return user.sys\_id;  
  }  
}

To display the referenced record names instead of sys\_id values, use the getDisplayValue function. For example, change:

gs.print(inc.number + " | " + inc.watch\_list);

to:

gs.print(inc.number + " | " + inc.watch\_list.getDisplayValue());

### Related Links

[Add users to a watch list](https://www.servicenow.com/docs/r/platform-user-interface/t_UseAWatchList.html)

[Lists in the classic environment](https://docs.servicenow.com/csh?topicname=c_UseLists.html&version=latest "Lists in the classic environment")

[Classic business rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Classic business rules")
