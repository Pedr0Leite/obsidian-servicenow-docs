---
title: "Choice Field Validator"
aliases:
  - Choice Field Validator
tags:
  - servicenow-dev-program
  - code-snippet
  - choice-field-validator
  - transform-map-scripts
---

# **Choice Field Validator**

Function that returns the value of a choice by its display value. Initially created to be used in field map scripts.
Used to return the choice even if the instance is in different language.


## *Important points*
- It is imperative that the display value in the transform map table exists in the instance
- It is possible to validate the values of choices dependent on other choices
- To get the dependent choice you need set and static value or run the function for the first choice and then with the dependent choice (as in the second example).


## **Example configuration**

1. Category validation:
![categoryvalidation](choice_validador1.png)

2. Category and subcategory validation:
![categorysubcategoryvalidation](choice_validador1.png)


In these previous cases we used the validator because some users use Portuguese language and all options in the excel are in English. With the functions we don't need to worry about the different languagues.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Check if the Import file is valid/README|Check if the Import file is valid]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Conditional Coalesce/README|Conditional Coalesce]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Email Formatter/README|Email Formatter]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Global Variable in Transform Map/README|Global Variable in Transform Map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Incident Priority Set on Insert Only/README|Incident Priority Set on Insert Only]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Transform Map Scripts/Verify headers of a CSV attached file/README|Verify headers of a CSV attached file]]
