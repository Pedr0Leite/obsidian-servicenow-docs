---
title: "How to define a currency when importing software entitlements in Software Asset Management"
aliases:
  - KB1648108
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1648108
kb_number: KB1648108
last_modified: 2025-02-20
---

## How to define a currency when importing software entitlements in Software Asset Management

  

### Summary

When importing entitlements the assumed currency for fields such as unit\_cost is the user's session currency, depending on your business requirements you might need to define different currencies in the same import or you may want to divert from the assumed currency during import, if so, please follow the instructions below.

### Release

All current releases

### Instructions

As per [Default currency values in import and export](https://docs.servicenow.com/csh?topicname=currency-import-export.html&version=latest "Default currency values in import and export"), ServiceNow will interpret currency fields as so:

-   A number formatted in the user’s locale. The number is taken as a value in the user's session currency.
-   The number prefixed by the three-letter currency code separated by a semicolon, for example, 'EUR; 1.234,56'.

### Related Links

Example where the prefix is used to set "Widget Ware v2"'s unit cost to A$700 using the string 'AUD; 700'

![](/sys_attachment.do?sys_id=6634b39247bf1210b7832920326d4396)
