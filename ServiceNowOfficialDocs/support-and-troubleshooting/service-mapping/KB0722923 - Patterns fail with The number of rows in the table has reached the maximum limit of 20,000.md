---
title: "Patterns fail with \"The number of rows in the table has reached the maximum limit of 20,000\"
aliases:
  - KB0722923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722923
kb_number: KB0722923
last_modified: 2026-06-01
---

## Patterns fail with "The number of rows in the table has reached the maximum limit of 20,000"

  

### Issue

Pattern based discovery fails with the following error:

yyyy-mm-dd hh:mm:ss: The number of rows in the table has reached the maximum limit of 20,000. To adjust this use the glide property com.glide.closure\_max\_rows\_per\_table.

### Release

Any

### Cause

The amount of data collected in the table variable exceeds the default maximum number of rows per table.

### Resolution

There is not a definite figure for the **com.glide.closure\_max\_rows\_per\_table** system property. You can increase it gradually until the error is no longer seen. However increasing this property will allow more data to added to this variable and therefore, consume more heap memory. If the MID server's heap memory is not adjusted together with increasing the property, the MID server might crash with "OutOfMemory" errors.

This is a MID server property from \[**ecc\_agent\_properties\]** and not a system property from \[**sys\_properties\]**. So in order to increase it, you will need to implement one of the following methods:

**Method 1:**

-   Open this form to add a new property in "ecc\_agent\_property" table:   
    _https://<instance\_name>.service-now.com/ecc\_agent\_property.do_   
    **name:** com.glide.closure\_max\_rows\_per\_table   
    **value:** 100000  
    **mid server:** leave empty, if you want it to apply to all MID servers.
-   Restart the MID servers for the property to take effect.

**Method 2:**

-   Connect to the MID server host
-   Navigate to the MID server installation directory > agent > properties >  open glide.properties file with a text editor
-   Add the property: com.glide.closure\_max\_rows\_per\_table=100000
-   Save the file
-   Restart the MID server process for the property to take effect.

**NOTE**: If the property was added using the glide file, then it will be removed/cleared after any MID server upgrades. This is because the upgrade process overrides the glide file with the default values.

### Related Links

[MID Server received a large response that exceed the allowed number of rows 200,000 error shown in Service Mapping](https://support.servicenow.com/kb_view.do?sysparm_article=KB0827291 "MID Server received a large response that exceed the allowed number of rows 200,000 error shown in Service Mapping")
