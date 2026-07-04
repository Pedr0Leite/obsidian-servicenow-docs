---
title: "On receiving an asset via Purchase Order, the \"Reserved For\" field is auto-populated, even if no one is chosen in the \"Reserve\" toggle in Receive order page."
aliases:
  - KB2473493
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2473493
kb_number: KB2473493
last_modified: 2025-08-28
---

## On receiving an asset via Purchase Order, the "Reserved For" field is auto-populated, even if no one is chosen in the "Reserve" toggle in Receive order page.

  

### Summary

-   When the "Requested For" field is populated on the "Purchase Order Line Item," the asset is reserved for that specific user. In this case, the "Reserve" toggle switch is ineffective. Therefore, the automatic population of the "reserved\_for" field when a user is assigned to the "requested\_for" field is the expected behavior.
-   The "Reserve" toggle will be useful only when the "Requested For" field on the "Purchase Order Line Item" is not populated. In the out-of-the-box (OOB) configuration, the "Requested For" field is not available on the form.
-   The "ProcurementUtils" script include is responsible for creating the asset and populating the "reserved\_for" field on the asset.

![](/sys_attachment.do?sys_id=e72b81d7836b6e14cdbbc430feaad39f)

### Related Links
