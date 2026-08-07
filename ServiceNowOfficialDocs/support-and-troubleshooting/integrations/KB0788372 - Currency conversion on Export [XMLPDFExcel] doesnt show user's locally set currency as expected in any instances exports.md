---
title: "Currency conversion on Export [XML/PDF/Excel] doesnt show user's locally set currency as expected in any instances exports."
aliases:
  - KB0788372
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788372
kb_number: KB0788372
last_modified: 2024-04-08
---

## Currency conversion on Export \[XML/PDF/Excel\] doesnt show user's locally set currency as expected in any instances exports.

  

### Issue

Exported currency is always showing in $ though the current displayed currency in user's session is in Euro. Even though the below properties were set as follow.

glide.excel.fixed\_currency\_usd=false  
glide.excel.convert\_to\_user\_currency=true  
glide.i18n.single\_currency=false

### Release

All the releases 

### Resolution

Currency name is taken from the fx\_currency table and currency conversion will be done based on fx\_rate.  
  
Conversion rates are stored in the fx\_rate table. Each record contains the conversion rate from a given currency to the Euro. The rates are updated daily from the ECB website by a scheduled job called ECB Exchange Rate Load.  
  
A currency conversion from one currency to another involves two rates  
  
Rate to convert from the first currency to Euro  
Rate to convert from Euro to the second currency  
  
Below properties will control the currency export. If the user wants to export all the currency values in $ then set the "glide.excel.fixed\_currency\_usd" to true. If the user wants the currency displayed in user session then set the glide.excel.convert\_to\_user\_currency=true.

Country code set on user profile will also having control on which currency is applicable while exporting the currency fields. If the user country code is set to "null" then exported currency filed will be set to default currency $.

Inorder to export the currency field in other than $ then make sure that country code set in sys\_user record is set to respective country code.
