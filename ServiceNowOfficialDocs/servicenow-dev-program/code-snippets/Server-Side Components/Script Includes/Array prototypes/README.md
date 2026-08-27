---
title: "Array prototypes"
aliases:
  - Array prototypes
tags:
  - servicenow-dev-program
  - code-snippet
  - array-prototypes
  - script-includes
---

# Add many helpful helper functions to array object

# How to use it?
Create a new Script Include
Copy and Paste the content of the JavaScript file here
Include the Script Include in your code: gs.include("VF_ArrayPrototypes");
Enjoy the extra utility functions


# Example 1: Joining two arrays

```

var countries = [
    { name: "USA", population: 300 },
    { name: "Canada", population: 200 },
    { name: "France", population: 100 }
];

var people = [
    { name: "John", country: "USA" },   
    { name: "Peter", country: "France" },
    { name: "Anna", country: "France" }
];

var res1 = countries.innerJoin(people,
    function (c) { return c.name },                                         // arr1 selector
    function (u) { return u.country },                                      // arr2 selector
    function (t, u) { return { country: t.name, person: u.name }});         // result selector

gs.log(JSON.stringify(res1));

```

# Example 2: Other helpful functions

```

var arr = [1, 2, 3, 4, 5];
var arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];

var first = arr.first(function(i){return i > 3;});
gs.log(first);


var last = arr.last();
gs.log(last); 


var dist = arr.distinct();
gs.log(dist);


var interSect = arr.intersect(arr2);
gs.log(interSect);


var except = arr.except(arr2);
gs.log(except);

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
