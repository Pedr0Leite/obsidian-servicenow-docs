---
title: "Discovery of Cloud Datacenter failed with \"Method returned an object of type sys_script_68e502fa0a0a0aa9001fdd4619ef53b5_12 which is not allowed in scope sn_cmp\""
aliases:
  - KB0688231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688231
kb_number: KB0688231
last_modified: 2024-04-07
---

## Discovery of Cloud Datacenter failed with "Method returned an object of type sys\_script\_68e502fa0a0a0aa9001fdd4619ef53b5\_12 which is not allowed in scope sn\_cmp"

  

### Issue

# Symptoms

* * *

When going to **Cloud Account > Datacenter > Discovery Now**, immediately, client side is filled with the following errors:

"Method returned an object of type sys\_script\_68e502fa0a0a0aa9001fdd4619ef53b5\_12 which is not allowed in scope sn\_cmp"

# Release

* * *

Jakarta and newer

# Cause

* * *

The '_sys\_script_' record points to the '**getNextObjNumberPadded**' Business Rule. In older versions, this business rule was not accessible from the 'All Application Scope'. Some of the Cloud tables have a numbering column which uses the business rule to to get the next number in the sequence. Newer versions of this business rule has '**Accessible from**' field set to '**All application scopes**'. If this business rule is not upgraded properly (ie, the business rule was customized), the Cloud applications in the '**Cloud Management Application**' scope cannot access the business rule, resulting in the errors on the client side.

# Resolution

* * *

-   Go to the affected business rule: **getNextObjNumberPadded**
-   Under the '**Versions**' related list, right click the latest entry for the current instance and select '**Revert to this version**'
-   This will update the business rule to the latest base version, making it compatible with Cloud Management Application
