---
title: "[SAMP] Why some of the important fields (like license type, purchase rights, etc) on software entitlement form are not editable after saving or once created"
aliases:
  - KB0859671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859671
kb_number: KB0859671
last_modified: 2025-01-02
---

## \[SAMP\] Why some of the important fields (like license type, purchase rights, etc) on software entitlement form are not editable after saving or once created

  

### Summary

While working with software entitlements, we might see that there are few fields like _**purchase rights**_, _**license type**_, etc that might be read-only after we create the new entitlement record. This will explain to you why it is like that and what is the enhancements around it.

**1\. How these are made as read-only?**  
There are a couple of client scripts and UI policies that make these fields as read-only once we submit the record.

_Example_: License Type  
Once the entitlement is saved then there is a client script "Set fields read-only when not new record" that makes few fields including "License Type" is made as read-only.

_Client Script_: Set fields read-only when not new record  
[https://instance](https://instance)\_name.service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=6ec9c6b767022200e85a87cb5685efde

**2\. Why these fields are kept these fields as read-only in existing releases?**  
As a recommended practice, entitlements are typically not edited throughout the entitlement lifecycle. As new purchases are made, they should be logged as new entitlement records and not updates to existing records. As entitlements are created, their settings and relationships to other records (metric attributes, downgrades, next version, allocations, etc.) can be impacted if attributes are changed within the reconciliation. Therefore many of the attributes are not-editable

**3\. Can we make changes so it's editable and if so will there be any implications?**  
Until Quebec release, the answer is No. Because. there are dependencies during the reconciliation engine processing and this could break the functionality.

**Enhancements**:  
Beginning from Quebec, we are adding the ability (new enhancement) to edit the entitlement field under specific circumstances. Error handling is added to ensure only changes that do not have a downstream impact are allowed. This error handling is not available in prior releases, so it's recommended customers re-create entitlements as opposed to making changes.
