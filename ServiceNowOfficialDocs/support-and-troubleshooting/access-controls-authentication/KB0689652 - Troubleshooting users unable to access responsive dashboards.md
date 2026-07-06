---
title: "Troubleshooting users unable to access responsive dashboards"
aliases:
  - KB0689652
tags:
  - servicenow
  - support-kb
  - dashboards
  - system-properties
  - cms
  - performance-analytics
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0689652
kb_number: KB0689652
last_modified: 2024-04-07
---

## Troubleshooting users unable to access responsive dashboards

  

### Issue

# Symptoms

* * *

Users cannot access responsive dashboards.

# Release

* * *

Jakarta Patch 6+ 

# Cause

* * *

-   Responsive dashboards are disabled
-   Responsive dashboards are dependent on the boolean variable glide.cms.enable.responsive\_grid\_layout  
    
-   glide.cms.enable.responsive\_grid\_layout is either set to false or it does not exist  
      
    

# Resolution

* * *

Enable Responsive Dashboards (Role required: Admin)

-   In the filter navigator enter "sys\_properties.list"  
    
-   Search the Name column for "glide.cms.enable.responsive\_grid\_layout"
    -   If the glide.cms.enable.responsive\_grid\_layout was found:
        -   Change the value from False to true.
    -   If the glide.cms.enable.responsive\_grid\_layout was not found:
        -   Create the glide.cms.enable.responsive\_grid\_layout system property.
        -   [https://docs.servicenow.com/bundle/istanbul-platform-administration/page/administer/reference-pages/task/t\_AddAPropertyUsingSysPropsList.htm](https://docs.servicenow.com/csh?topicname=t_AddAPropertyUsingSysPropsList.html&version=latest)l

-   All new and existing dashboards should now be responsive.

## Related

- [[domain-sep-pa-dashboards]] - official docs on Performance Analytics dashboards and domain separation
