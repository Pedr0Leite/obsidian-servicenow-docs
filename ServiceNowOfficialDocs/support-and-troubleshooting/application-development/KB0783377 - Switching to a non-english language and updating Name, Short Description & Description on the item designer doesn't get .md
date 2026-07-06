---
title: "Switching to a non-english language and updating Name, Short Description & Description on the item designer doesn't get updated on the respective Catalog Item. "
aliases:
  - KB0783377
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783377
kb_number: KB0783377
last_modified: 2024-04-08
---

## Switching to a non-english language and updating Name, Short Description & Description on the item designer doesn't get updated on the respective Catalog Item.

  

### Issue

Using item designer, create an item with some text in Description, Short description fields (ensure you are in EN language). Publish the item.  
Switch to another language which is non-english (like Chinese, Dutch or French). Unpublish the item and update the text present in Description, Short description fields.

Click on 'Publish' now. Go to the catalog item and observe the text in Description, Short description fields on the sc\_cat\_item record.

It doesn't show the updated text. These fields still show the text present when the user is in English language.

### Release

All releases till New York.

### Resolution

Here is the actual FIX which can be used to fix this issue:  
1) Navigate to script includes module and open the below script include:  
sc\_ic\_CatalogItem - https://<instance\_name>.service-now.com/sys\_script\_include.do?sys\_id=535f0c50eb3011003623666cd206fec5  
2) In the script, comment line no.47  
3) Add the below script after line no.53

> this.\_copyTranslations(item);

4) Save the changes.  
  
The issue should not be reproducible anymore.
