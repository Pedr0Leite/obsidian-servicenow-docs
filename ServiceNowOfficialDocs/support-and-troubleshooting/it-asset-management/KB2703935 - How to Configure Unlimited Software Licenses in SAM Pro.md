---
title: "How to Configure Unlimited Software Licenses in SAM Pro"
aliases:
  - KB2703935
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2703935
kb_number: KB2703935
last_modified: 2026-01-05
---

## How to Configure Unlimited Software Licenses in SAM Pro

  

### Summary

In SAM Pro, unlimited licensing is configured on the Software Entitlement by selecting the "Unlimited license" option.

An unlimited entitlement provides unlimited allocations/rights, is prioritized during reconciliation over fixed entitlements (when applicable), and produces separate license metric results without marking covered installations as non-compliant.

**How it works:**  
  
\--> An unlimited license entitlement provides unlimited allocations and unlimited rights.  
  
\--> Installations covered by an unlimited entitlement are not classified as non-compliant in license metric results.  
  
\--> During reconciliation, unlimited entitlements are taken into account and are prioritized over fixed amount licenses (when an installation is licensed/matched).  
  
\--> License metric results are generated separately for unlimited licenses.  
  
**Supported options / key notes :**  
  
\--> Supported license metrics for unlimited licenses include: Per User, Per Device, Per Named User, Per Named Device, User Subscription, Named User Plus, Per Processor.  
  
\--> Supported license types include: Perpetual, Maintenance/Software Assurance, Perpetual + Maintenance/Software Assurance, Subscription.  
  
\--> For unlimited licenses, Purchased rights / Active rights / Allocations available fields are not displayed, and unit cost equals total cost.  
  
\--> An unlimited perpetual entitlement can be associated to only one unlimited maintenance entitlement.

### Release

Any release

### Instructions

\- Open the Software Entitlement record (or use Import Entitlement to create it). 

\- Select the “Unlimited license” check box on the Software Entitlement page (or Import Entitlement page).

\- Ensure you select a supported license metric for unlimited licenses (e.g., Per User, Per Device, Per Named User/Device, User Subscription, Named User Plus, Per Processor). 

\- Ensure you select a supported license type (Perpetual, Maintenance/Software Assurance, Perpetual + Maintenance/Software Assurance, Subscription). 

Note constraints: an unlimited perpetual entitlement can be associated with only one unlimited maintenance entitlement; for unlimited entitlements, certain rights/allocation fields are not shown and unit cost equals total cost.

### Related Links

[Unlimited software licenses](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/unltd-allocations-rights.html "Unlimited software licenses")
