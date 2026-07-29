---
title: "[SAMP\Downgrade Rights] Downgrade rights configured for the Software Model \"Oracle DB Server 19c Enterprise\" are not honored during the reconciliation"
aliases:
  - KB0855569
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855569
kb_number: KB0855569
last_modified: 2024-04-08
---

## \[SAMP\\Downgrade Rights\] Downgrade rights configured for the Software Model "Oracle DB Server 19c Enterprise" are not honored during the reconciliation

  

### Issue

-   There is an entitlement created for "Oracle DB Server 19c Enterprise" software model. The other discovered versions of this product are added as downgrade rights to "Oracle DB Server 19c Enterprise".

![](sys_attachment.do?sys_id=1ffdf009dbccb4d0471f9c41ba9619cc)

-   But reconciliation does not recognize this setup, thus resulting in "Non Complaint" entries in the license position report.

![](sys_attachment.do?sys_id=93fdf009dbccb4d0471f9c41ba9619cb)

### Release

-   Instance with Software Asset Management Professional plugin enabled. (Orlando & prior release)

### Cause

-   The Downgrade rights support for "Per Processor" License Metric for Oracle DB Server installs is available from Paris and later releases.

### Resolution

-   As per the downgrades defined on the "Oracle DB server 19c Enterprise" entitlement if one wants to cover all the Oracle DB Server installs using this entitlement a probable solution would be leaving both "Version" and "Edition" as  "empty" in the discovery map.
-   So that it will cover all the versions and Editions based on the downgrades defined and Software model will be just "Oracle DB server". Now this will be tied to the Entitlement to cover all the installs.
