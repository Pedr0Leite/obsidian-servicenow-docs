---
title: "[SAMP] Create multiple entitlements for same Software Model"
aliases:
  - KB0824137
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824137
kb_number: KB0824137
last_modified: 2025-01-03
---

## \[SAMP\] Create multiple entitlements for same Software Model

  

### Summary

If we create an entitlement for a product as a subscription and map to the agreement type ‘Enterprise’ and create another entitlement with perpetual license for the same product the status for the product will always be a complaint.

  
E.g; Photoshop has subscriptions and also separate perpetual licenses.

There is an Enterprise Term Level Agreement (ETLA) entitlement covering Adobe Systems Photoshop that expires in 2020. There is also a perpetual generic agreement type for 5 rights covering 5 rights. It is not possible to produce different reconciliation results for the same software model with overlapping entitlements. Reconciliation will ignore the weaker entitlement, generic for 5 rights, until the ETLA/unlimited entitlement expires.

Reconciliation picks the more powerful entitlement, ETLA, for Adobe System Photoshop software model and produces a compliant product result.

The product result being complaint is expected as called out here:

[https://docs.servicenow.com/csh?topicname=t\_ViewSWModelResults.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ViewSWModelResults.html&version=latest)

If an ELA entitlement is associated with a software model, that the software model will be considered compliant regardless of unlicensed installs.
