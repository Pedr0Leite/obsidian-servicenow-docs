---
title: "Resolving Date/Time Display Discrepancies in Web Services"
aliases:
  - KB0546240
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546240
kb_number: KB0546240
last_modified: 2024-04-30
---

## Resolving Date/Time Display Discrepancies in Web Services

  

### Issue

Date and time values have both a value and a display value. Inconsistencies between these values can lead to unexpected behaviour. The _value_ is the raw value within the database. The _display value_ represents the user-friendly value shown in the UI. Certain field types such as Encrypted text, DateTime, choice, and reference fields all also use a display value that differs from the raw value.

With DateTime fields, the raw value is always stored in the UTC timezone, while the display value appears in the timezone set for the current user record.

### Symptoms

-   Date and time values appear different than expected
-   Entering a date and time value using web services results in a different value appearing in the UI

### Cause

By default, web services use either the display value or the raw value depending on the operation.

-   SOAP Insert or Update operations treat request values as display values
-   SOAP retrieval operations return raw values
-   JSON operations all use raw values
-   REST Table API retrieval operations return raw values
-   REST Table API Insert or Update operations use display values for certain fields (you can force the REST API to always use a particular type of value using the '_**sysparm\_input\_display\_value**_' parameter

### Resolution

You can explicitly specify the format you want the operation to use by adding a parameter to the request URI.

1.  SOAP and JSONv2: add the display value parameter. Valid values are **true**, **false**, and **all**. For example, to use only the display values:  
    <instance>.service-now.com**/incident.do?SOAP&displayvalue=all  
      
    **
2.  REST retrieval operations: add the sysparm\_display\_value parameter for retrieval operationsValid values are **true,** **false,** and **all.** For example, to return only the display values:  
    <instance>.service-now.com**/api/now/table/incident?sysparm\_display\_value=true  
      
    **
3.  REST Insert or Update operations: add the sysparm\_input\_display\_value parameter for Insert or Update operations. Valid values are **true** and **false.** For example, to insert data using only raw values:  
    <instance>.service-now.com**/api/now/table/incident?sysparm\_input\_display\_value=false**
