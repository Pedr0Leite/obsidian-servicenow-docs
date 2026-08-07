---
title: "Not able to update the edge encrypted column when Variable name on the catalog item is different than the field name"
aliases:
  - KB0787344
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787344
kb_number: KB0787344
last_modified: 2024-04-08
---

## Not able to update the edge encrypted column when Variable name on the catalog item is different than the field name

  

### Issue

Not able to update the edge encrypted column when Variable name on the catalog item is different than the field name

### Cause

Field name which is edge encrypted does not match with the variable name on the Catalog Item

### Resolution

1.  Create or Update an Edge Encryption Rule using Record Producer for the Service Catalog Item 
2.  In the Action for the EdgeEncryption Rule created, update it with the following . In this example 'comments' is the variablename in the Catalog Item , where as "description" is the field in the target table. In the code we are getting the name of variable sent in the request and mapping it to field on the table which is edge encrypted.

var jsonContent = request.getAsJsonContent();  
for (var jsonElementItr = jsonContent.getIterator('variables'); jsonElementItr.hasNext();) {  
var jsonElement = jsonElementItr.next();if (jsonElement.getName() == "comments") {  
jsonElement.valueFor(tableName, 'description');  
} else {  
jsonElement.valueFor(tableName, jsonElement.getName());  
}   
}
