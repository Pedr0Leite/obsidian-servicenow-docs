---
title: "Suite components are missing or inconsistent on a software model"
aliases:
  - KB0748712
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748712
kb_number: KB0748712
last_modified: 2026-06-30
---

## Suite components are missing or inconsistent on a software model

  

### Issue

When the Software Asset Management Professional plugin is active and you create or update a software model, the Suite Components section may show an inconsistent number of records — or no records at all — after changing the Discovery Map (DMAP) on the form.

### Symptoms

-   The Suite Components section on a software model shows fewer records than expected
-   The Suite Components section is empty after changing the DMAP
-   Suite component records appear inconsistently across different software models

### Release

  Beginning with Kingston

### Cause

Suite component population depends on two conditions being met:

1\. The DMAP selected on the software model must have the Suite Defined field set to true, indicating it is a parent suite with child components defined.  
2\. A matching entry must exist in the Suite Definitions table (samp\_m2m\_suite\_entitlement\_def), which is populated by the content service and is read-only.

When you save a software model after changing the DMAP, a business rule named Create pre-built suite components runs. This business rule calls a script include that checks whether the selected DMAP has suite components defined in the Suite Definitions table. If both conditions are met, the child suite components are built and displayed in the Suite Components section. If either condition is not met, the section remains empty or incomplete.

### Resolution

**Understanding the Suite Definitions table**

The Suite Definitions table (\`samp\_m2m\_suite\_entitlement\_def\`) contains suite parent and child relationships. This data is provided by the content service and cannot be edited directly. Each parent DMAP can have multiple child components defined.

To view suite definitions for a DMAP, navigate to the Suite Definitions table on your instance:   
https://<instance-name>.service-now.com/samp\_m2m\_suite\_entitlement\_def\_list.do?sysparm\_query=suite\_parent.name%3D<DMAP-name>

**Option 1: Use a custom DMAP to manage suite components**

If the base system DMAP does not meet your requirements, create a custom DMAP and attach the required suite components to it, including any custom components. Custom DMAPs are not read-only and can be managed directly.

1\. Navigate to the Discovery Maps table in your instance.  
2\. Create a new DMAP record.  
3\. Set the Suite Defined field to true if this DMAP is a parent suite.  
4\. Add the required child suite components to the new DMAP.  
5\. Attach the custom DMAP to the relevant software model and save.

The Create pre-built suite components business rule runs on save and builds the Suite Components section based on the custom DMAP definition.

**Option 2: Request a DMAP through the content service**

To have a DMAP added as a base system product, submit a request through the [Software Asset Management content service.](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/c_SAMContentService.html) Requests are reviewed and added if approved.

**Option 3: Contact ServiceNow Technical Support**

If an urgent update is required, create a support case with ServiceNow Technical Support for review.

### Related Links

[Software Asset Management content service](https://docs.servicenow.com/csh?topicname=c_SAMContentService.html&version=latest) 

[Add software model](https://docs.servicenow.com/csh?topicname=c_SoftwareAssetMgmt.html&version=latest)
