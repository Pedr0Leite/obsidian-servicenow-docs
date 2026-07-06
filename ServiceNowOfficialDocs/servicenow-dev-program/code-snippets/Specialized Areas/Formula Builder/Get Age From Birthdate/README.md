---
title: "Get Age From Birthdate"
aliases:
  - Get Age From Birthdate
tags:
  - servicenow-dev-program
  - code-snippet
  - get-age-from-birthdate
  - formula-builder
---

## Formula builder to calculate the Age from birthdate

This Formula calculates at the beginning of Today to calculate the exact age from Birthdate.

IF(
  OR(
    MONTH(birthdate) < MONTH(TODAY()), 
  AND(MONTH(birthdate) = MONTH(TODAY()), DAY(birthdate) < DAY(TODAY()))),  
    SUBTRACT(YEAR(TODAY()), YEAR(birthdate)),  
    SUBTRACT(SUBTRACT(YEAR(TODAY()), 1) ,YEAR(birthdate)))

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Formula Builder/Formula builder overview/README|Formula builder overview]]
