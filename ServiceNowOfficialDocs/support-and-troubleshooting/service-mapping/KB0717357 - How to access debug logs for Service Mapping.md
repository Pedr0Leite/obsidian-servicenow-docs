---
title: "How to access debug logs for Service Mapping"
aliases:
  - KB0717357
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717357
kb_number: KB0717357
last_modified: 2026-04-14
---

## How to access debug logs for Service Mapping

  

### Issue

Troubleshoot Service Mapping issues such as pattern execution failures, missing Business Service Map (BSM) nodes, or incomplete discovery results. This article describes where to locate the relevant debug logs for analysis.

### Release

All supported releases

### Cause

Service Mapping generates debug logs across multiple areas depending on the stage of discovery (pattern execution, node-level activity, or discovery messaging). Without knowing the correct log location, troubleshooting becomes difficult.

### Resolution

 Access Service Mapping debug logs using the following methods.

**View pattern logs (global)**

1.  Go to **Pattern Designer**.
2.  Select **Discovery Pattern Log**.
3.  Review logs for all Service Mapping pattern executions.

**View logs for a specific node**

1.  Open the BSM.
2.  Select the affected node.
3.  Select **Show discovery log**.
4.  Review logs specific to that node's discovery and pattern execution.

**View discovery error messages**

1.  Go to **Service Mapping** > **Administration** \> **Discovery Messages**.
2.  Review error messages generated during discovery. These messages correspond to those displayed in the BSM.

### Related Links

[CI relationships](https://www.servicenow.com/docs/r/it-business-management/cost-management/t_CIRelationships.html "CI relationships")

[Identify all configuration items affected by a security incident](https://www.servicenow.com/docs/r/security-management/security-incident-response/t_ViewBSMMap.html "Identify all configuration items affected by a security incident")
