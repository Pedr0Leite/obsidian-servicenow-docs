---
title: "getDependent"
aliases:
  - getDependent
tags:
  - servicenow-dev-program
  - code-snippet
  - getdependent
  - glideelement
---

GlideElement API provides different functions to work with the fields, attribute, values, etc.,
getDependent function on GlideElement API - helpful in validating the dependent field values if any for the given field. 

Used subcategory field in incident table as an example so that it will print "category" as result.
If we update the field_name variable to some other field that is not dependent on another field then the method prints null as result.

Link to documentation - https://developer.servicenow.com/dev.do#!/reference/api/paris/server_legacy/c_GlideElementAPI#r_GlideElement-getDependent

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideElement/Display available choices/README|Display available choices]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideElement/Display base table for each field/README|Display base table for each field]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideElement/Smart Field Validation and Dependent Field Derivation Using getError() and setError()/README|Smart Field Validation and Dependent Field Derivation Using getError() and setError()]]
