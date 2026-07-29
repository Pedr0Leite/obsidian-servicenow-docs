---
title: "Types of Service Catalog variables that support advanced reference qualifier"
aliases:
  - KB0686862
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686862
kb_number: KB0686862
last_modified: 2026-05-01
---

## Types of Service Catalog variables that support advanced reference qualifier

  

### Issue

 

Reference qualifiers are used to filter records of the target table that gets referenced on.

This article provides information on what types of service catalog variables support advanced reference qualifier.

### Release

Any

Environment: UI16

### Resolution

  The functionality depends on whether the field show up on the variable form (item\_option\_new table).

If the field doesn't show up (though present in the Form Layout) when a variable's type is selected, it's understood that this field won't function (even if you try other ways to make it visible).

The following are the types of variables that advanced reference qualifier field functions on:

-   Reference (if Use reference qualifier is "Advanced")
-   List Collector
-   Lookup Multiple Choice
-   Lookup Select Box

This indeed is controlled via a UI Policy defined at "item\_option\_new" table called "Advanced ref qual" that controls the visibility of this field (reference\_qual).

### Related Links

[Types of service catalog variables](https://www.servicenow.com/docs/r/servicenow-platform/service-catalog/r_VariableTypes.html)

[Reference qualifiers](https://www.servicenow.com/docs/r/platform-administration/c_ReferenceQualifiers.html)
