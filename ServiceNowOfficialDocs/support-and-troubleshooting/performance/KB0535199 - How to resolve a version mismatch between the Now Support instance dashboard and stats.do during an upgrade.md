---
title: "How to resolve a version mismatch between the Now Support instance dashboard and stats.do during an upgrade"
aliases:
  - KB0535199
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535199
kb_number: KB0535199
last_modified: 2026-05-04
---

## How to resolve a version mismatch between the Now Support instance dashboard and stats.do during an upgrade

  

### Issue

While upgrading your instance, the instance dashboard in the Now Support portal may show a different version than what appears on the stats.do page. If you experience upgrade problems, check the upgrade .war properties to verify the correct platform version is displayed. Incorrect property values indicate an unsuccessful upgrade. 

### Release

All supported releases

### Resolution

To check the upgrade .war properties: 

1.  Go to **System Properties** > **All Properties**.
2.  Search for the properties: glide.war or glide.war.assigned.
3.  Confirm that these values display the version that the platform is upgrading to.
4.  If the values displayed differ, update the values to the correct version, including the '.zip' extension. The following image is an example:  
    ![Screenshot of glide.war.assigned property](https://support.servicenow.com/ca40c20387d2aad057288519dabb352a.iix?t=large "Screenshot of glide.war.assigned property")
5.  Validate that the upgrade has completed successfully by checking the **Upgrade History** and **stats.do**.
