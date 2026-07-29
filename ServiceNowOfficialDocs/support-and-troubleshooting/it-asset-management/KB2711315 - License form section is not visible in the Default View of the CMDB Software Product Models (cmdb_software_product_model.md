---
title: "\"License\" form section is not visible in the Default View of the CMDB Software Product Models (cmdb_software_product_model) after upgrading to Zurich"
aliases:
  - KB2711315
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2711315
kb_number: KB2711315
last_modified: 2026-01-13
---

## "License" form section is not visible in the Default View of the CMDB Software Product Models (cmdb\_software\_product\_model) after upgrading to Zurich

  

### Issue

After upgrading the instance to Zurich, the “License” form section is no longer visible in the Default view of CMDB Software Product Models (cmdb\_software\_product\_model). 

### Symptoms

\- Log in to the instance.   
\- Navigate to Software Models.  
\- Open any record and switch to the Default view.  
\- Observe that the License section is not visible next to the General tab.

### Release

Zurich

### Cause

The License form section is delivered OOTB by the Model Management plugin (com.snc.model).

The section is defined in sys\_ui\_section (sys\_id: 32d6f87337a2100044e0bfc8bcbe5da1).

During the Model Management plugin upgrade, this UI section was removed from the Default form configuration.

During a family (platform) upgrade—for example, upgrading the instance to Zurich—ServiceNow not only updates the core platform but can also upgrade installed plugins that are part of the release baseline or required for compatibility.

### Resolution

The removal appears to be an intentional/expected OOTB change introduced by the plugin upgrade, which is why the section is no longer visible.
