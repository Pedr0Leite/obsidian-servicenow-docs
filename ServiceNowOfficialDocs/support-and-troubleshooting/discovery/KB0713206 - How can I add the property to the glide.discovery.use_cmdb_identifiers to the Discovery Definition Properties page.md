---
title: "How can I add the property to the \"glide.discovery.use_cmdb_identifiers\" to the Discovery Definition > Properties page?"
aliases:
  - KB0713206
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713206
kb_number: KB0713206
last_modified: 2025-01-03
---

## How can I add the property to the "glide.discovery.use\_cmdb\_identifiers" to the Discovery Definition > Properties page?

  

### Issue

  
  

# Description

* * *

The property "glide.discovery.use\_cmdb\_identifiers" is not present in the sys\_properties table. This property is to be manually added if the instance was upgraded from a pre-Geneva version. Once it is manually added the property is not visible under Discovery Definition > Properties

# Procedure

* * *

1\. Once the "glide.discovery.use\_cmdb\_identifiers" property is manually created in the sys\_properties table with value as true similar to in link below:

/sys\_properties.do?sys\_id=86b227e2c3373100d8d4bea192d3ae7a&sysparm\_record\_list=nameSTARTSWITHglide.discovery.use\_cmdb\_identifiers^ORDERBYname&sysparm\_record\_target=sys\_properties&sysparm\_record\_row=1&sysparm\_record\_rows=1

2\. Under related tab "categories", add discovery.  
3\. On Discovery Definition>Properties page, search for keyword that you have entered in description field while creating the property in step 1.
