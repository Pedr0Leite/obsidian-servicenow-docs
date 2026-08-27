---
aliases: [Other Applications Index]
area: other-applications-index
tags: [index, routing, erp, third-party]
---

# other-applications INDEX — third-party systems

Documentation for systems **we integrate with but do not own**. Distinct from
`Applications/` (things we build) and `ServiceNowOfficialDocs/` (ServiceNow's own
product documentation).

## unit4-erp

### `Unit4_ERP_Integration_Compendium_ServiceNow.md`
Internal Unit4 technical working document, compiled 17 August 2026.
**Classification: Business (TLP Green)** — internal material; review access
before wider distribution. Covers the implemented ServiceNow ↔ Unit4 ERP/ERPx
integrations.

| Section | Contents |
|---|---|
| 1–2 | Evidence boundary and caveats; executive architecture; MID Server distinction |
| 3 | **Endpoint and interface catalogue** — ERPx Discovery, Tracking, employee read/update, SOAP contract rows, inbound Scripted REST paths |
| 4 | **ServiceNow implementation inventory** — 23 IntegrationHub flows, 25 transform maps (9 named), script includes and scheduled jobs |
| 5–8 | Employee REST integration, JSON Patch updates, contract/rates SOAP, HR Letters and documents |
| 9 | ServiceNow ERP Integration Framework (`sn_fcms_intg`) roles and MID Server rule |
| 10 | **Zero Copy Connector for ERP** — remote tables + extraction tables, installation and entitlement |
| 11–12 | Unit4 cloud capabilities/constraints; **API and platform limits** (500 req/min, timeouts, concurrency) |
| 13 | **Security, authentication and operational concerns** — open findings |
| 14–15 | Migration services; **gaps, contradictions and validation backlog** |
| Appendix A–B | Payloads, field mappings, inbound API base paths, source register |

**Key facts** (cite the compendium, not this index):
- The ERP is **Unit4 ERPx**, with ERP CR / ERP7 as the legacy line
- Cloud-to-cloud REST; **no MID Server** on this path
- **IntegrationHub is in production** — 23 ERP-specific flows on `unit4dev1`
- Transform maps already populate `customer_account`, `service_entitlement`,
  `sn_install_base_m2m_installed_product`, `cmn_department` and `x_u4bsh_finance_le`
- Rate limits: 500 req/min per environment, HTTP 429 + `Retry-After`,
  recommended REST concurrency 10
- Inbound Scripted REST namespace is `/api/u4bsh/...`

**Evidence discipline:** the compendium preserves hedged wording ("likely",
"appears") as observations rather than facts, and §15 lists what it could not
confirm. Carry both forward — do not promote a flagged item to fact without
inspecting the instance.

## Related

- [[erp-crm-360|Applications/erp-crm-360/erp-crm-360-brief.md]] — the build brief
  that consumes this compendium; its §1A summarises the facts above and records
  which of its own earlier conclusions they overturned
