---
aliases: [ERP CRM 360, ERP/CRM 360]
area: entity
tags: [entity, scoped-app, erp, csm, integration]
---
Proposed in-house scoped app (`x_u4bsh_erpcrm`) surfacing Unit4 ERP financial context inside CSM/ITSM records, plus an ERP integration control tower. **Status: brief only, not built.** Wiki entity page — a pointer + summary, not a copy. Source of truth is `Applications/erp-crm-360/`.

## Source notes
- [[erp-crm-360-brief|ERP/CRM 360 build brief]] (`Applications/erp-crm-360/erp-crm-360-brief.md`) — licensing map, five-layer architecture, data model, React UI, phase gates, now-sdk setup.
- `other-applications/unit4-erp/Unit4_ERP_Integration_Compendium_ServiceNow.md` — the ERP-side evidence the brief is built on.

## Shape of it
Not a CRM: ServiceNow already ships Sales CRM / CSM / FSM on a shared foundation. The app builds the **ERP join** that is missing — financial and entitlement context on the Account and Case, via remote tables (rows in memory, never stored), fronted by a control tower registering ERP connections, object maps and account cross-references.

Two questions gate the build: whether **Zero Copy Connector for ERP** is entitled and Unit4-compatible (it may replace two whole layers), and whether `customer_account` already carries the Unit4 customer key.

## Related concepts
- [[scoped-apps]]
- [[integrations]]
- [[acls]]

## Related
- [[wiki/index|Wiki Index]]
