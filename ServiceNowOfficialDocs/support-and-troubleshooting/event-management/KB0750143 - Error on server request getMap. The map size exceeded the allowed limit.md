---
title: "Error on server request getMap. The map size exceeded the allowed limit"
aliases:
  - KB0750143
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750143
kb_number: KB0750143
last_modified: 2024-04-07
---

## Error on server request getMap. The map size exceeded the allowed limit

  

### Issue

# Symptoms

-   Go to service mapping ->applications and access any application.
-   Click view map, the map will load for some time and will show the error "`Error on server request getMap. The map size exceeded the allowed limit`".

                 ![](sys_attachment.do?sys_id=80dc6ceedb42b450e515c22305961992)

  

  

### Release

All

### Cause

-   The system property "sa.map.LIMIT\_MAX\_GRAPH\_SIZE" by default it has true value. If this is true, it will control the maximum size of the map size to improve the performance.
-   Open the system property by using URL below.

            https://<instancename>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=5dc5ac2e87111200b5bea18dd0e3ece2

  

                    ![](sys_attachment.do?sys_id=44dc6ceedb42b450e515c22305961997)

### Resolution

-   Select the property by clicking the URL below and set the property"sa.map.LIMIT\_MAX\_GRAPH\_SIZE" to false.

            https://<instancename>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=5dc5ac2e87111200b5bea18dd0e3ece2

                   ![](sys_attachment.do?sys_id=d4dc6ceedb42b450e515c2230596199c)

  

#### Note: Setting this property to false may reduce performance in maps for large services.
