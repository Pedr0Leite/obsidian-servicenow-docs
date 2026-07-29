---
title: "Import Set API transform fails with Invalid table error"
aliases:
  - KB0813776
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813776
kb_number: KB0813776
last_modified: 2026-06-22
---

## Import Set API transform fails with Invalid table error

  

### Issue

  
When creating an import set using the Import Set API and testing it with the REST API Explorer, the transform fails with an Invalid table error. The import set is set to transform synchronously by default, but the transform does not complete successfully.

The following is an example of the REST API call and response:

Request:

```
POST https://<instance-name>.service-now.com/api/now/import/u_imp_cmdb
```

Request body:

```
{
  "u_service_id": "20",
  "u_service_name": "data",
  "u_description": "data",
  "u_category": "Cloud Storage",
  "u_subcategory": "Document Storage and Sharing",
  "u_web_address": "http://abc/en"
}
```

Response body:

```
{
  "import_set": "ISET022222",
  "staging_table": "u_imp_cmdb",
  "result": [
    {
      "transform_map": "",
      "status": "error",
      "error_message": "Invalid table "
    }
  ]
}
```

### Release

All

### Cause

Business Rule "Transform synchronously" is not active. 

### Resolution

1.  First check the import set record which created in the REST API call and verify the state of the data from the Import Set rows. Usually it will be in "Pending" state.
2.  Reprocess the import set and then transform it manually. This should be transformed successfully.
3.  Now, enable business rule "Transform synchronously" and then test the REST API call. It should get transformed successfully without an error.
