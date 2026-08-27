---
title: ERP/CRM 360 — build brief and session prompt
status: brainstorm
last_updated: 2026-08-18
scope: x_u4bsh_erpcrm (proposed)
---

# ERP/CRM 360 — build brief for a fresh Claude session

> [!info] What this file is
> A self-contained prompt. Paste it whole, or point a session at this path.
> Every platform claim carries a `rel_path` from **sn-rag** retrieval over
> `obsidian-servicenow-docs`. Claims sourced from GitHub or from the ServiceNow
> Store are labelled as such. Anything uncited is an assumption to be tested,
> not a fact.

---

## 0. Mission

Build a **custom scoped ServiceNow application** that surfaces ERP financial and
commercial context inside the CSM/ITSM records where agents already work, plus a
**control tower** for configuring and monitoring the ERP integrations behind it.

Two decisions are already made and are **not** open for re-litigation:

1. **Custom build, not the ServiceNow Store ERP Integration Framework.** The
   product owner has confirmed there is **no Source-to-Pay / Finance entitlement**.
   The Store app (`77992f221b246a50a85b16db234bcb74`, publisher ServiceNow) is
   the ERP Integration Framework, scope `sn_fcms_intg`, and it sits inside a
   licensed install chain — Finance Common Architecture `sn_fin` → ERP
   Integration Framework `sn_fcms_intg` → Common Service Delivery → …
   (`ServiceNowOfficialDocs/source-to-pay-operations/sourcing-and-procurement-operations/activate-finance-spend-central.md`).
   Unavailable means unavailable. Build the equivalent.
2. **The UI is React.** This is officially supported — see §4.

Read §1 and **§1A** before designing anything. §1 sets the licensing constraints;
**§1A carries the Unit4 ERPx facts and overturns one of §1's conclusions**, names
the first ERP, and identifies a Store app that may replace two whole layers.

---

## 1. Hard constraints — the licensing map

This is the single most load-bearing section. Every plugin below was checked
against the corpus.

| Component | Plugin / scope | Status | Verdict |
|---|---|---|---|
| Remote Tables | `com.glide.script.vtable` | **"Active on the base instance"** | ✅ **Use freely** |
| OAuth 2.0 | `com.snc.platform.security.oauth` | **"Active on the base instance"** | ✅ **Use freely** |
| Transformation Service | `com.glide.transform` | auto-activated with Remote Tables | ✅ Use |
| IntegrationHub | `com.glide.hub.integrations` | *"requires subscription"* — **but this org has it and uses it** (§1A) | ✅ **Available. Prefer it for outbound.** |
| ERP Integration Framework | `sn_fcms_intg` | licensed (S2P chain) | ❌ Replacing it |
| Customer Service | `com.sn_customerservice` | licensed — **assumed present** | ⚠️ Confirm, see below |
| Now Assist for App Engine | — | licensed | ⚠️ Gates the agentic layer |

Sources:
`ServiceNowOfficialDocs/customer-service-management/csm-third-party-data-integration.md`
lists all four plugins for third-party data integration with exactly those
annotations — Remote Tables *"Active on the base instance"*, OAuth 2.0
*"Active on the base instance"*, and IntegrationHub *"requires subscription and
is available in several subscription packages"*.
`ServiceNowOfficialDocs/servicenow-platform/remote-tables/activate-remote-tables-plugin.md`
confirms Remote Tables `com.glide.script.vtable` auto-activates
Transformation Service `com.glide.transform`.

### If IntegrationHub were unavailable — what `RESTMessageV2` costs

> [!warning] Superseded in part by §1A
> This subsection was written assuming IntegrationHub was out of reach. The Unit4
> compendium shows **23 ERP-specific IntegrationHub flows already running on
> `unit4dev1`**, so the REST Step *is* available. Keep this table as the fallback
> analysis and as the reference for anything that must stay scripted — but the
> default for new outbound calls is now the REST Step, not `RESTMessageV2`.

Outbound calls must use the **`RESTMessageV2` scripted API**, not the REST Step.
`ServiceNowOfficialDocs/api-reference/web-services/c_OutboundRESTAuth.md`
enumerates precisely what is lost:

| Limitation | Consequence for this build |
|---|---|
| **Retry policy for outbound calls** — *"Built-in configurable retry policies for automatic retries on transient failures are not available. Custom retry logic must be implemented in script."* | **Write our own retry/backoff.** Non-optional. A remote table query that fails on a transient blip must not render as "no invoices". |
| Mutual authentication on MID Server — mTLS *"not supported when routing REST calls through a MID Server"* | If the ERP demands mTLS, it must be a direct instance call, not via MID |
| Multipart with attachments | No file push to ERP. Out of scope anyway |
| Custom authentication (Authentication Algorithm framework) | Rules out exotic ERP auth schemes |
| AWS Signature v4 | Rules out direct AWS-signed endpoints |

Supported auth (same doc): **basic**, **OAuth 2.0 via provider and profile**, and
**mutual authentication via protocol profiles** (direct calls only).

Scripting notes:
- *"When scripting new REST messages configured with authentication you must use
  the RESTMessageV2 API. The legacy RESTMessage APIs do not support current
  authentication formats."*
- `RESTMessageV2.setAuthenticationProfile(type, profileId)` — `'basic'` takes the
  sys_id of a `sys_auth_profile_basic` record; `'oauth2'` takes an
  `oauth_entity_profile` sys_id
  (`ServiceNowOfficialDocs/api-reference/server-api-reference/c_RESTMessageV2API.md`).
- OAuth 2.0 JWT Bearer grant is workable from script — worked example at
  `ServiceNowOfficialDocs/support-and-troubleshooting/integrations/KB0718030 - How to configure Outbound Rest Message with oAuth 2.0 JWT Bearer grant flow.md`.
- A REST message configured with OAuth must not be configured to use a MID Server
  (`ServiceNowOfficialDocs/api-reference/web-services/t_ConfigureARESTMessageWithOAuth.md`).

**Even with IntegrationHub available, a retry/backoff layer is still required** —
not because of a licensing gap, but because Unit4 enforces hard rate limits and
returns HTTP 429 with `Retry-After` (§1A.4). The reason changed; the requirement
did not.

### Confirm before Phase 1

- **Is `com.sn_customerservice` active?** The whole "CSM side" of the value
  proposition assumes it. (Working assumption: yes — the org already runs Now
  Assist AI Agents inside CSM, per the PCCC work in
  `ServiceNowOfficialDocs/custom-solutions/proactive-customer-case-communicator/`.)
- **Is a MID Server available?** Changes whether ERP endpoints can be reached
  on-prem at all.
- **Is Now Assist for App Engine licensed?** Gates Phase 5 entirely.

---

## 1A. The ERP is Unit4 ERPx — and a lot already exists

Source for this entire section:
`other-applications/unit4-erp/Unit4_ERP_Integration_Compendium_ServiceNow.md`
(internal Unit4 technical working document, compiled 17 August 2026, **Business /
TLP Green** — treat as internal, review before wider distribution).

It carries its own evidence discipline, which this brief inherits: *"Where a
source itself uses words such as 'likely', 'appears', or flags a concern, that
wording is preserved as an observation rather than converted into a confirmed
fact."* Do the same. Several items below are flagged as unconfirmed and must not
be promoted to fact without instance inspection.

### 1A.1 What this answers

Four of the §10 open questions are now answered, and one §1 conclusion is
overturned.

| Question | Answer |
|---|---|
| Which ERP first? | **Unit4 ERPx** (with ERP CR / ERP7 as the legacy line) |
| Does it expose REST? | **Yes.** Outbound REST + inbound Scripted REST APIs are live |
| MID Server? | **Not used on this path.** *"no MID Server is used for this cloud-to-cloud path"* |
| IntegrationHub? | **Available and in production** — see 1A.2 |

> [!danger] Correction to §1
> The brief originally concluded IntegrationHub *"must not be depended on"*,
> reasoning from the platform doc's *"requires subscription"*. That reasoning was
> sound but the premise was wrong for this org: **23 ERP-specific IntegrationHub
> flows are documented as running on `unit4dev1`**. The REST Step, its retry
> policies, and spokes are all on the table. The `RESTMessageV2` fallback analysis
> in §1 remains useful, but it is no longer the constraint.

### 1A.2 What is already built on `unit4dev1`

Architecture, per the compendium: *"connects ServiceNow to Unit4 ERPx using
outbound REST messages, inbound Scripted REST APIs and Integration Hub flows."*

| Direction | Mechanism | Documented use |
|---|---|---|
| ServiceNow → ERPx | Outbound REST | Discovery, user tracking, employee reads/updates, document operations |
| ERPx → ServiceNow | Scripted REST APIs | Attachments, change requests, customer contact management, customer emails |
| Orchestration | IntegrationHub / Flow Designer | Provisioning, tracking, operations, support, release, decommissioning |
| Bulk/external → ServiceNow | Import Sets + Transform Maps | Entitlements, accounts, departments, legal entities, install base, services, Salesforce cases |
| ServiceNow → Unit4 Business World | SOAP | Add/update employee contract/rates flexi-field rows |

**23 ERP-specific flows** are stated to exist; the compendium names ~21 and flags
that *"the source groups several names and does not expose full definitions"* —
trigger tables, conditions, inputs, outputs and error handling are incomplete.

**Inbound Scripted REST base paths** — note the `u4bsh` namespace, which confirms
the `x_u4bsh_` scope prefix chosen in §3:

```
/api/u4bsh/unit4_attachments
/api/u4bsh/unit4_change_request
/api/u4bsh/ccm
/api/u4bsh/unit4_customers_emails
```

### 1A.3 Master data is already flowing — this changes the data model

**25 transform maps** are stated to exist; 9 are named. The named ones land
directly on the CSM objects this app was going to join against:

| Transform map | Target table |
|---|---|
| Unit4 Entitlement V3 | `service_entitlement` |
| Unit4 - Cutomer Account *(sic)* | `customer_account` |
| Unit4 Populate departments | `cmn_department` |
| Unit4 - imp Legal Entity | **`x_u4bsh_finance_le`** |
| Unit4-Installbase-Sold Products | `sn_install_base_m2m_installed_product` |
| Unit4 Application Services V2 | `cmdb_ci_service_discovered` |
| Unit4 - Transform Sales Force Cases | `sn_customerservice_case` |
| Unit4 - Import SF case Comments & Worknotes | `sn_customerservice_case` |
| Unit4 - product/version | CSM Data Lookup |

Consequences for §3:

1. **A legal entity table already exists: `x_u4bsh_finance_le`.** The proposed
   `u_legal_entity` field on `x_u4bsh_erpcrm_erp_system` must be a **reference to
   it**, not a free-text string. Do not create a second legal-entity table.
2. **Accounts are already imported from Unit4.** Before building
   `x_u4bsh_erpcrm_account_xref`, inspect `customer_account` — the `Unit4 -
   Cutomer Account` map may already carry the ERP customer key, which would make
   the cross-reference a lookup rather than a data-entry exercise. **This is the
   single highest-value thing to check in Phase 0.**
3. **Install base and entitlements are populated.** The "what do they own / what
   are they entitled to" half of the 360 view may already be answerable from local
   data, narrowing this app's job to the financial half.
4. Only 9 of 25 maps are named — *"Field-level and transformation-script
   completeness cannot be confirmed."* Enumerate the rest on the instance.

> [!note] This does not contradict "never store ERP financial data"
> Master data (accounts, departments, entitlements, install base) is legitimately
> replicated by these transform maps. The §9 rule is about **transactional
> financial data** — invoices, POs, balances, credit status. Those stay in remote
> tables. Keep the distinction explicit.

### 1A.4 Unit4 rate limits and timeouts — the retry layer is now specified

These turn the hand-wavy "write our own retry" into concrete numbers.

**API limits (general Unit4 SaaS, excluding ERPx):**

| Limit | Environment | Value |
|---|---|---|
| HTTP requests/minute | PROD, PREV, ACPT01, ACPT02 | **500/min per environment** |
| HTTP requests/minute | ACPT03-11 | 1,500/min shared |
| Inbound/outbound API size | All | 350 MB/min |

On breach: *"subsequent requests are suspended for one minute"*, with documented
responses of **HTTP 429, `Retry-After`, connection closure request and TCP
termination**. Unit4's own recommended handling: *"usage monitoring, batching,
caching, throttling, exponential backoff and honoring Retry-After."*

**Timeouts that bound the UI:**

| Limit | Value |
|---|---|
| ERPx web application request timeout | 110 s |
| ERPx Public API Gateway request timeout | 240 s |
| ERP CR/ERP7 Web REST API timeout | 120 s |
| ERP CR/ERP7 SOAP API timeout | 120 s |
| Recommended REST API concurrency | **10** |
| Recommended SOAP call frequency | 60/min |

**Design consequences, non-negotiable:**

- The connector **must honour `Retry-After`**, not just back off on its own
  schedule. A fixed backoff that ignores the header is a wrong implementation.
- **Concurrency cap of 10** — a remote table query fanning out per row breaches
  this immediately. This is the hard evidence behind §9 rule 5 ("batch, never
  loop").
- A remote table with `Cache TTL = 0` on a busy list view is a rate-limit
  incident waiting to happen. **Set a non-zero TTL for invoices and POs.** Reserve
  TTL=0 for credit status, and even there, consider a short TTL.
- 500 req/min sounds generous until a 50-row list refreshes per user. Model the
  worst case before choosing TTLs.

**Connectivity:** TLS 1.2 minimum, HTTPS on 443, WebSockets required for SignalR,
firewall must allow `unit4cloud.com` and subdomains.

> [!warning] Environment matching is a hard Unit4 rule
> *"PROD ↔ PROD; matching non-production types; non-production ↔ production is not
> supported or allowed."* Enforce this in the Connection Alias configuration —
> a dev ServiceNow instance must never point at Unit4 PROD.

### 1A.5 Authentication — use Connection Aliases, not raw profile sys_ids

The existing implementation authenticates through **Connection Aliases**:
*"Password (2-Way) through Connection Alias"* for employee reads, with endpoints
built from `{Connection Alias base URL}`.

**Amend §3:** `x_u4bsh_erpcrm_erp_system.u_auth_profile` should reference a
**Connection Alias**, not a `sys_auth_profile_basic` / `oauth_entity_profile`
sys_id directly. That matches the house pattern, keeps environment separation in
one place, and makes the PROD/non-PROD rule enforceable.

Documented endpoint shapes, for reference:

```
GET   {baseUrl}/objects/employees?companyId={companyId}&filter=personId eq {employeeId}&select={select}
PATCH {baseUrl}/employees/{employeeId}?companyId={companyId}
      Content-Type: application/json-patch+json
```

### 1A.6 Open security findings — inherit these, do not repeat them

The compendium's §13 lists live concerns in the existing integration. Treat them
as both risk context and a standard this app must not fall below:

| Finding | Evidence status |
|---|---|
| ERPx Tracking has OAuth 2.0 selected but **no OAuth profile assigned** | *"Explicitly stated in integration summary"* |
| ERPx Discovery endpoint has **no authentication configured** | *"Explicitly stated"* |
| Credentials passed **in the SOAP body** (Username, Client/Company ID, Password) | *"Explicitly shown in envelope"* |
| Employee REST uses **Password (2-Way)** | *"Explicitly stated"* |
| `ERPxAppFilter` script include is **inactive**; purpose described as *likely*; possible routing/filtering side effects | Functional purpose presented as *likely* |
| **Employee endpoints carry HR / identity / bank fields** | Recommendation: least privilege, field minimisation, safe logging |

That last row matters for §9 rule 8. This app deals in financial data about
customers; the existing integration deals in **personal data about employees**.
If any employee-facing endpoint is reused, the ACL and logging bar is higher, not
equal.

### 1A.7 Zero Copy Connector for ERP — evaluate before building L2/L3

This is the biggest build-vs-buy question and it did not exist in the brief before.

**Zero Copy Connector for ERP** (formerly ERP Data Hub / ERP Canvas) is a
ServiceNow scoped application that:

- *"Creates models containing ERP data in remote tables and extraction tables"*
- Supports **read, update and create** through ERP models
- *"Remote tables run an associated script against an external data source"*
- *"Extraction tables use scheduled queries and transform tables for larger
  datasets and refresh needs"*
- *"mirrors ERP data and does not replicate it into the ServiceNow AI Platform"*
- Is consumable from **UI Builder and Workspace Builder** (and Studio, Creator
  Studio, Workflow Studio, Table Builder)
- Ships **content packs** with predefined models and process extensions

**That is L2 and most of L3, bought rather than built.** If it is entitled, large
parts of this brief become configuration.

Installation facts: ServiceNow Store, admin role required; *"Confirm product and
dependent-application entitlements before requesting installation"*; property
`sn_erp_integration.enableModelModification` must be enabled in the correct scope
to edit/clone models; role `sn_erp_integration.erp_admin` configures the
system-of-record connection; connections may be direct or via load balancer.

**Two blockers, both explicit:**

1. **Entitlement is unconfirmed** — same class of question as the S2P framework.
   Check it in Phase 0.
2. **Domain separation is documented as unsupported.**
3. The compendium's own gap list flags: *"Zero Copy documentation is generic and
   SAP-oriented. No retrieved source explicitly confirms a Unit4 ERP content pack
   or connection implementation."*

**Do not assume it works with Unit4.** But do not build L2/L3 by hand before
answering the question either — that is potentially weeks of avoidable work.
**Phase 0 must produce a yes/no on Zero Copy entitlement and Unit4 compatibility.**

### 1A.8 Gaps the compendium itself flags

Do not treat the inventory above as complete. Verbatim from its §15:

- Only 9 of 25 transform maps named — field-level completeness unconfirmed
- Flow count says 23, definitions not exposed — trigger tables, conditions,
  inputs/outputs and error handling incomplete
- *"Inbound Scripted REST APIs lack resource/method/schema detail"* — request and
  response JSON, version paths, ACLs and error models unavailable
- Document-send action lacks endpoint and payload
- Employee rates documentation differs between REST read and SOAP contract write
- SOAP endpoint is dynamic — actual host/path and MID Server routing not shown

Every one of those needs instance inspection. `sn-instance-scan` exists in this
vault and may be the right tool for enumerating the flows, maps and Scripted REST
APIs rather than reading them by hand.

---

## 2. Target architecture — five layers

```
┌─────────────────────────────────────────────────────────────┐
│ L5  Agentic layer (OPTIONAL, gated on Now Assist for AE)     │
│     AI Agent Studio agents · evidence ledger · suggestions   │
├─────────────────────────────────────────────────────────────┤
│ L4  Presentation — React UI Page (Fluent UiPage) +           │
│     UI Builder panels on Account / Case                      │
├─────────────────────────────────────────────────────────────┤
│ L3  Remote tables — invoice, PO, receipt, balance            │
│     schema in ServiceNow, rows in memory, never stored       │
├─────────────────────────────────────────────────────────────┤
│ L2  Connector runtime — RESTMessageV2 + OAuth2/basic         │
│     + our own retry/backoff/circuit-breaker + telemetry      │
├─────────────────────────────────────────────────────────────┤
│ L1  ERP Control Tower — connection registry, object maps,    │
│     account cross-reference, health                          │
└─────────────────────────────────────────────────────────────┘
```

Build order is strictly **L1 → L2 → L3 → L4 → L5**. Each layer has a gate (§8).

### L3 is the core idea — remote tables

`ServiceNowOfficialDocs/servicenow-platform/remote-tables/remote-tables.md`:

> *"You can then view and update the external data without importing or storing
> it. You view the external data in lists or forms in the same way that you view
> internally stored data. You can manipulate this data by using standard Glide
> records, business rules, remote APIs, scripting, table reference fields,
> services, and development tools in the ServiceNow AI Platform."*

> *"You create remote tables to describe the schema for the data that you want to
> retrieve from an external source. The table definition is in the ServiceNow AI
> Platform, but its rows, or external records, live in memory."*

The Remote Tables plugin *"Adds the Remote Table Script Definition table
(`sys_script_vtable`) and adds the **Remote Table** flag to the Tables
(`sys_db_object`) table"*
(`ServiceNowOfficialDocs/customer-service-management/csm-third-party-data-integration.md`).

**Query script contract** — from
`ServiceNowOfficialDocs/servicenow-platform/remote-tables/create-remote-table-script.md`:

```javascript
(function executeQuery(v_table, v_query) {
    // v_table.addRow({ ... }) — adds a row to the result set.
    //   keys are the column names of the table definition.
    //   sys_id must be non-empty and uniquely identify each row.
    //   strictly enforced for editable tables; warnings for read-only tables.
    //   sys_id is supplied to the Update and Delete scripts to identify the row.
    // v_query.getEncodedQuery()  — encoded query string
    // v_query.getCondition(field) — ...
})(v_table, v_query);
```

*"Every time a list that contains external data from a remote table is refreshed,
the associated query script runs."*

**Performance controls on the script definition record** (same doc) — these are
the difference between a usable panel and a hanging one:

| Field | Meaning |
|---|---|
| **Cache TTL** | Seconds cached in memory. Default `0` = no caching, fetched every time. **Max 3600** (60 min). |
| **Cache Isolation Level** | *Cache per user* (default) or *System Shared Cache* |
| **Enhanced Capacity** | Required to exceed **1000 rows**. Doc advises leaving off for small result sets |

APIs available: `v_table`, `v_query`
(`ServiceNowOfficialDocs/api-reference/server-api-reference/v_queryAPI.md`) and
`v_record` for insert/update/delete
(`.../v_recordAPI.md` — *"insert, update, and delete methods are used in a script
with no changes to workspaces or lists and forms"*). Both require
`com.glide.script.vtable`.

Setup sequence is documented end-to-end at
`ServiceNowOfficialDocs/financial-services-operations/setting-up-a-remote-table-integration.md`
(activate plugin → inspect source data → create remote tables → …) and worked
examples at `.../remote-tables/remote-table-script-def-example1.md` (query all
records) and `.../remote-table-script-def-example3.md` (insert into external
source). **Read all three before writing L3.**

### Why this shape is right

`ServiceNowOfficialDocs/customer-service-management/csm-third-party-data-overview.md`
describes the identical pattern with Salesforce standing in for the ERP:

> *"When an agent accesses an account in Agent Workspace for CSM, a list of
> related opportunities for this account is retrieved from Salesforce in
> real-time and presented to the agent."*

and — critically for L1 — how correlation was solved:

> *"The ServiceNow account record is updated with the Salesforce account ID
> attribute that holds the reference to the Salesforce account record. The
> Salesforce account ID is later used to match account records between ServiceNow
> and Salesforce"*

A shipped precedent for the same architecture in another vertical:
`ServiceNowOfficialDocs/financial-services-operations/financialservices-remote-tables.md`
— *"enables real-time record lookup into external financial applications without
the need to store the data permanently."*

---

## 3. Data model

Scope: **`x_u4bsh_erpcrm`** (proposed — reuses the `x_u4bsh_` vendor prefix
already established by `x_u4bsh_capmgmt`).

### Stored tables (L1)

**`x_u4bsh_erpcrm_erp_system`** — the connection registry. One row per ERP
instance. This is our replacement for the framework's *ERP Source* concept, which
the vendor doc defines as *"a specific ERP instance from which data is imported
and to which data is exported... each ERP source mapped to a legal entity"*
(`ServiceNowOfficialDocs/source-to-pay-operations/source-to-pay-integration-framework/erp-integration-framework.md`).

| Field | Type | Notes |
|---|---|---|
| `u_name` | string, unique | Display field |
| `u_vendor` | choice | `sap_ecc`, `sap_s4`, `oracle_ebs`, `oracle_fin_cloud`, `dynamics`, `other` |
| `u_legal_entity` | string or reference | Mirrors the framework's legal-entity mapping |
| `u_base_url` | url | |
| `u_auth_type` | choice | `basic` \| `oauth2` \| `mutual` |
| `u_auth_profile` | string (sys_id) | `sys_auth_profile_basic` or `oauth_entity_profile` |
| `u_use_mid` | boolean | Mutually exclusive with OAuth — enforce in a BR |
| `u_mid_server` | string | |
| `u_timeout_ms` | integer | |
| `u_max_retries` / `u_backoff_ms` | integer | We own retry; IntegrationHub would have |
| `u_circuit_open_until` | glide_date_time | Breaker state |
| `u_read_only` | boolean, default **true** | Write-back is opt-in per system |
| `u_active` | boolean | |

**`x_u4bsh_erpcrm_object_map`** — the abstraction layer. One row per
(ERP system × logical object). **This table is the whole "prepared for other
ERPs" claim.** The vendor framework describes its own equivalent as an
*"abstraction layer... [that] shields Source-to-Pay workflows and data models
from backend-specific integration components and data structures"* — same intent.

| Field | Notes |
|---|---|
| `u_erp_system` | reference → `x_u4bsh_erpcrm_erp_system` |
| `u_object` | choice: `invoice`, `purchase_order`, `receipt`, `balance`, `credit_status` |
| `u_remote_table` | which remote table this feeds |
| `u_endpoint_path` / `u_http_method` | |
| `u_field_map` | JSON: ERP field → remote-table column |
| `u_response_root` | JSON path to the record array |
| `u_active` | |

Adding an ERP = new `erp_system` row + N `object_map` rows. **No new code.** If a
new ERP requires new code, the abstraction failed — treat that as a design bug.

**`x_u4bsh_erpcrm_account_xref`** — solves the correlation-key problem, per-ERP.

| Field | Notes |
|---|---|
| `u_account` | reference → `customer_account` |
| `u_erp_system` | reference → `x_u4bsh_erpcrm_erp_system` |
| `u_external_id` | ERP customer master key |
| `u_verified_on` / `u_verified_by` | |

Unique index on (`u_account`, `u_erp_system`). Deliberately a table, not a field
on `customer_account`: one account can exist in several ERPs (different regions
or lines of business — the vendor doc confirms this is normal:
*"supports multi-ERP integration that enables you to use different ERP systems for
different regions or lines of business"*,
`ServiceNowOfficialDocs/source-to-pay-operations/sourcing-and-procurement-operations/erp-source-val-spo-objects.md`).

**`x_u4bsh_erpcrm_call_log`** — per-call telemetry: erp_system, object, started,
`u_duration_ms`, status, http_code, error, rows returned, cache hit. Feeds both
the control tower and the transparency panel in §4.

### Remote tables (L3) — schema only, no stored rows

`x_u4bsh_erpcrm_rt_invoice`, `_rt_purchase_order`, `_rt_receipt`, `_rt_balance`.
The four object families are exactly those the vendor framework names as in
scope: *"primary data, transactional data (purchase orders, receipts, invoices),
fixed assets, and tax information"*.

Each needs an **external primary key** —
`ServiceNowOfficialDocs/servicenow-platform/remote-tables/create-remote-table.md`:
*"A remote table needs an external primary key to relate its temporary data to the
data that is stored in the external source."*

### CSM join keys — reuse, never recreate

From `ServiceNowOfficialDocs/customer-relationship-management/customer-relationship-management/crm-data-models.md`
and `.../customer-service-management/csm-use-case-tables.md`:

| Object | Table |
|---|---|
| Case | `sn_customerservice_case` |
| Account | `customer_account` |
| Contact | `customer_contact` |
| Consumer | `csm_consumer` |
| Sold Product | `sn_install_base_sold_product` |
| Install Base Item | `sn_install_base_item` |
| Work order (FSM) | `wm_order` |

CSM's own framing — *"Who is the customer? What do they own? What are they
entitled to?"*, with Case connecting *"Who (Account/Contact/Consumer) + What
(Product/Asset) + What's Owed (Contract/Entitlement)"*. **We add a fourth
question: what do they owe, and are they clear to be served?**

> [!danger] Rejection criterion
> Any proposed table that duplicates `customer_account`, `customer_contact`,
> `csm_consumer`, `sn_customerservice_case` or `sn_install_base_sold_product` is
> rejected on sight. We are not building a CRM — ServiceNow already ships one
> (Sales CRM / CSM / FSM on a shared CRM Foundation, where *"A record created in
> one product is immediately available to the others"*). We are building the ERP
> join that is missing from it.

Likewise, case→incident/problem/change linkage is shipped — plugin `com.sn_cs_sm`,
extension point `sn_cs_sm.CSMIncidentIntegrations`, priority via `dl_u_priority`
(`ServiceNowOfficialDocs/customer-service-management/csm-integration-service-management.md`,
`.../itsm-extension-points.md`, `.../csm-integration-sm-incident.md`).
**Consume it. Do not rebuild it.**

---

## 4. The UI — React, officially

The corpus confirms React is a first-class, documented option —
`ServiceNowOfficialDocs/application-development/ui-development-react.md`:

> *"With the ServiceNow IDE or ServiceNow SDK, you can use React in an
> application to create a UI page in ServiceNow Fluent code. The ServiceNow
> Fluent UI Page API refers to an HTML entry point (`index.html`) that loads the
> page at the endpoint provided. After building and installing the application on
> an instance, the static assets are stored in the appropriate tables."*

The documented file layout:

```javascript
// src/fluent/erp-360.now.ts
import '@servicenow/sdk/global'
import { UiPage } from '@servicenow/sdk/core'
import erp360Page from '../../client/index.html'

UiPage({
    $id: Now.ID['erp-360-page'],
    endpoint: 'x_u4bsh_erpcrm_360.do',
    description: 'ERP/CRM 360',
    category: 'general',
    html: erp360Page,
    direct: true,
})
```

```xml
<!-- src/client/index.html -->
<html>
<head>
  <title>ERP/CRM 360</title>
  <sdk:now-ux-globals></sdk:now-ux-globals>
  <script src="./main.jsx" type="module"></script>
</head>
<body><div id="root"></div></body>
</html>
```

```javascript
// src/client/main.jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './app'

const rootElement = document.getElementById('root')
if (rootElement) {
    ReactDOM.createRoot(rootElement).render(
        <React.StrictMode><App /></React.StrictMode>
    )
}
```

Supports JS/JSX and TS/TSX. Start from a **React template** in the ServiceNow IDE
or SDK. Reference implementations: the `ServiceNow/sdk-examples` GitHub repo,
named in the doc.

**Use Next Experience components inside React** via the npm wrapper — the doc:
*"You can use some Next Experience Components in a React application with the
React Wrapper Component Library npm package"* — `@servicenow/react-components`
on the public npm registry. Install through Build Agent, the ServiceNow IDE, or
the SDK (see `.../servicenow-sdk/use-third-party-libraries.md`). **This is how
"easy to use" gets satisfied without hand-rolling a design system**: the app looks
native because it is using the native components.

### Where the UI lives

| Surface | Tech | Content |
|---|---|---|
| **ERP/CRM 360 workspace** | React UI Page (above) | Account 360, control tower, health |
| **Account panel** | UI Builder page/component | ERP balance, overdue invoices, credit status, open orders |
| **Case panel** | UI Builder component | The one-line answer: *is this account clear to be served?* |

UI Builder is the sanctioned route for workspace surfaces —
*"a visual, drag-and-drop page builder for workspaces and custom web experiences
using Next Experience components"*
(`ServiceNowOfficialDocs/application-development/dev-get-start-ui-tools.md`,
`.../ui-builder/ui-builder-overview.md`). CSM agents already work in a
Configurable Workspace
(`.../customer-relationship-management/crm-user-management.md`), so a panel drops
into their existing surface rather than sitting on a separate URL. If a bespoke
component is needed beyond what Component Builder can express, ServiceNow CLI
components are *"for developers who need to write custom HTML, CSS, and
JavaScript... stored in the `sys_uib_toolbox_component` table"*
(`.../ui-builder/component-builder.md`, `.../application-development/custom-components.md`).

**Rule of thumb:** the deep, exploratory, multi-panel experience is the React UI
Page. The in-context glance is a UI Builder panel. Do not build the same view
twice.

### Precedent, and the debt to avoid

`Applications/capacity-planner/capacity-planner.md` is the in-house precedent:
scoped app `x_u4bsh_capmgmt`, built with the **Now SDK (Fluent)**,
`@servicenow/sdk` 4.8.0, tables via the Fluent Table API, Scripted REST API for
data operations, *"a custom single-page frontend (vanilla JS SPA) served at
`x_u4bsh_capmgmt_planner.do`"*.

Copy the **process**. Do not copy the vanilla-JS SPA — the React UI Page above is
its supported successor at the same kind of endpoint. And read §12 of that note
before starting, because its debts are the ones this app will otherwise repeat:

- **N+1 queries.** *"always check before adding per-row logic... collect IDs
  first, then batch-fetch."* Both `derive-initiative-dates` and `getData` had to be
  rewritten this way. Against a remote table backed by a network call, an N+1 is
  not slow — it is an outage. **Batch by construction in every query script.**
- **Read and write paths must stay separate.** *"`saveToServiceNow()` and
  `doExport()` / `buildXLSX()` are two distinct actions... They must remain
  separate code paths."*
- **Deploy gap:** *"The SDK does not create `sys_properties` rows from `Record()`
  declarations when the sys_id is fake — the deploy finds no record with that
  sys_id and silently skips it."* Verify every system property exists post-deploy;
  do not assume.
- **URL convention:** use `_list.do` / `.do`, **not** `.list`, which *"fails in
  the Next Experience shell."*
- **Inactive business rules are invisible.** `propagate-initiative-changes` has
  `active: false` and silently stopped propagating for months. Any BR shipped
  inactive must be documented as such, loudly.

---

## 5. The Comp AI CRM idea, ServiceNow-converted

Source (fetched from GitHub — **not** in the vault, treat as unverified):
`trycompai/crm` is agentic-first — *"The agent is not a feature of the CRM; the
CRM is where the agent keeps its notes."* Stack: Eve (Vercel durable agents),
Next.js, NestJS/tRPC, PostgreSQL/Prisma, Bun, single-tenant. Three entities
(contacts, companies, deals), each with an Agent tab. Principle of evidential
integrity: *"nothing about a person is guessed"* — strong evidence updates
records, weaker signals become human-reviewed suggestions. 18 authored tools;
skills as versioned markdown; work queue with `FOR UPDATE SKIP LOCKED` leases;
sandboxed execution with network-denied egress.

**The good idea here is real and worth taking. The stack is not.** Conversion:

| Comp AI concept | ServiceNow conversion | Verdict |
|---|---|---|
| *"nothing is guessed"* — evidence over confidence scores | Every ERP figure renders with **source ERP system + as-of timestamp**. A failed or stale fetch renders **"unavailable"** — never blank, never `0` | ✅ **Adopt. This is the best idea in the repo** |
| Evidence ledger; strong evidence writes, weak becomes suggestion | `x_u4bsh_erpcrm_fact` (observation + source + observed_at + grade) and `x_u4bsh_erpcrm_suggestion` (human-approval queue) | ✅ Adopt (L5) |
| Agent tab — research trail, discarded leads, open questions | Transparency panel driven by `x_u4bsh_erpcrm_call_log`: which ERP systems answered, latency, cache hit/miss, what failed and when | ✅ Adopt — **and it doubles as the control tower's health view** |
| 18 authored tools | AI Agent Studio tools (`ServiceNowOfficialDocs/application-development/dev-get-start-platform-and-ae-ai-tools.md` — *"You define the agent's role, its step-by-step instructions, and the tools it has access to"*) | ⚠️ Licensed, L5 only |
| Skills as versioned markdown | Script Includes + Now Assist Skill Kit, under now-sdk source control | ✅ Adopt |
| Human-in-the-loop before any write | Already proven in-house — the PCCC NAP approval pattern (`ServiceNowOfficialDocs/custom-solutions/proactive-customer-case-communicator/`) | ✅ Adopt, reuse the pattern |
| React + shadcn/ui frontend | React UI Page + `@servicenow/react-components` (§4) | ✅ Adopt the language, not the libraries |
| Eve durable agents, Next.js, NestJS, tRPC, Prisma, Bun | — | ❌ **Nothing ports. Do not attempt.** |
| `FOR UPDATE SKIP LOCKED` lease queue | No equivalent primitive is exposed. Use a Scheduled Job + claim field + optimistic re-read | ❌ **Redesign, do not port** — say so explicitly rather than faking it |
| Sandbox with network-denied egress, zero DB access | Scoped app boundary + ACLs + `u_read_only` on ERP systems | ⚠️ Weaker guarantee. **State the difference; do not claim parity** |
| Single-tenant by design | ServiceNow is single-instance already | ➖ Moot |

**The synthesis worth stating out loud:** Comp AI's thesis is that a CRM is where
an agent keeps evidence about people. Ours is that an ERP-context layer is where
an agent keeps *evidence about money and entitlement*, and the same discipline
applies — provenance on every number, human approval before any write-back, and
the integration's own health visible to the person relying on it. That is a
coherent product, not a port.

---

## 6. Retrieval playbook — use the second brain, do not recall

**Invoke `/second-brain` for every platform question.** Do not answer ServiceNow
questions from memory; this corpus has been curated and your training data has
not. If retrieval and your prior belief conflict, cite the document and say so.

Agent selection:
- `servicenow` — vendor platform docs (remote tables, REST, UI Builder, CSM)
- `personal` — in-house apps and notes, including **this file** (it lives under
  `Applications/`) and `Applications/capacity-planner/`
- `general` — when unsure

Queries worth running verbatim before designing each layer:

| Layer | `sn_search` query | Agent |
|---|---|---|
| L1 | `ERP source legal entity multi-ERP abstraction layer` | `servicenow` |
| L2 | `RESTMessageV2 outbound REST OAuth profile setAuthenticationProfile` | `servicenow` |
| L2 | `outbound REST authentication limitations retry MID server` | `servicenow` |
| L3 | `create script definitions for a remote table query v_table v_query` | `servicenow` |
| L3 | `remote table cache TTL isolation enhanced capacity` | `servicenow` |
| L3 | `setting up a remote table integration high-level setup procedure` | `servicenow` |
| L4 | `UI page development with React Fluent UiPage index.html main.jsx` | `servicenow` |
| L4 | `UI Builder component builder custom components ServiceNow CLI` | `servicenow` |
| L4 | `capacity planner known issues architectural debt N+1` | `personal` |
| L5 | `AI Agent Studio build custom AI agents tools` | `servicenow` |
| CSM | `CSM data model account contact consumer sold product install base` | `servicenow` |
| Unit4 | `Unit4 ERPx integration endpoints transform maps limits` | `personal` |
| Unit4 | `Zero Copy Connector ERP remote tables extraction tables` | `general` |

Use `sn_lexical` for exact identifiers — `sys_script_vtable`, `v_table`,
`RESTMessageV2`, `oauth_entity_profile`, `sn_install_base_sold_product`,
`com.glide.script.vtable`, `sn_fcms_intg`. Dense search paraphrases; ripgrep does
not.

Expand promising hits with `sn_get_section` on the `parent_id`; use `sn_outline`
to see a document's shape first. **Prefer `sn_search` over `sn_research`** —
measured 2026-08-05, `sn_research` retrieves worse (recall 0.345 vs ~0.53) at
3–11s cost.

**The Unit4 compendium is in the corpus** at
`other-applications/unit4-erp/Unit4_ERP_Integration_Compendium_ServiceNow.md`
(source class `custom-app`, so reachable via `personal` and `general`). Read §1A
here first, then go to the compendium for endpoint-level detail.

Known gaps — the corpus does **not** answer these, so do not invent:
- credentials, and the production (non-sandbox) endpoint equivalents
- the Unit4 customer-master schema, and whether its key is already on
  `customer_account`
- Zero Copy Connector entitlement, and whether a Unit4 content pack exists
- Now Assist for App Engine entitlement status
- the 16 unnamed transform maps and the unexposed flow definitions

---

## 7. Which agents to use, per phase

| Phase | Agent | Why |
|---|---|---|
| Requirements → stories | `ba-agent` | Produces `rm_story` records with acceptance criteria and story points, grounded in the docs index |
| Technical design | `architect` | Tables, BRs, ACLs, integrations, UI specs, build-order instructions, test plan traced to ACs |
| Scope / update-set sign-off | `governance` | **Mandatory before any build.** Read-only gate; flags Global-scope use and cross-scope calls; requires an explicit human YES |
| Build | `developer` | Builds in dependency order; refuses to proceed without a governance-approved change manifest |
| Validation | `tester` | Executes the architect's test plan against what was actually built, never trusting the dev log |
| Defect scan | `bug-hunter` | N+1 GlideRecord, scope violations, insecure ACLs, deprecated APIs. **Run this specifically against every remote-table query script** |
| Small one-offs | `dispatcher` | Single scripts, quick fixes, general questions |
| Whole-feature run | `orchestrator` | Runs BA → Architect → Governance → Developer → Tester with a persistent workspace |

**Recommended:** drive phases 1–4 manually with `architect` → `governance` →
`developer` → `tester`, so the licensing constraint gets human eyes at the
governance gate. Reserve `orchestrator` for L3/L4 once the design is settled.

`bug-hunter` earns its keep here more than usual: a remote-table query script that
issues one HTTP call per row will pass every functional test and destroy the
instance under load.

---

## 8. Build phases and gates

A phase is complete only when its gate has **pasted evidence** — a command and its
real output, a screenshot, or a test result. Not "it should work".

**Phase 0 — Feasibility.** *(Expanded 2026-08-18 — this phase now carries the
decisions that determine whether L2/L3 get built at all.)*
1. **Zero Copy Connector for ERP: entitled? Unit4-compatible?** (§1A.7) If yes,
   re-scope L2/L3 to configuration before proceeding.
2. **Does `customer_account` already carry the Unit4 customer key?** (§1A.3)
3. Confirm `com.glide.script.vtable` is active (`sys_db_object` shows the Remote
   Table flag; `sys_script_vtable` exists).
4. Confirm `com.sn_customerservice` and Now Assist for App Engine entitlement.
5. Enumerate the real transform maps, flows and Scripted REST APIs on the
   instance — the compendium names only a subset (§1A.8).
6. Pick **one** object (recommend: invoices) as the vertical slice. The ERP is
   already decided: **Unit4 ERPx**.
→ **Gate:** written answers to 1–5, pasted evidence for 3–5, and a named object.
**Do not start Phase 1 until question 1 is answered** — a yes changes the plan.

**Phase 1 — Control tower (L1).**
Four stored tables, ACLs, list views, a React or UI Builder admin page.
→ **Gate:** two ERP system records configured (one real, one deliberately broken)
and an account cross-reference resolving correctly.

**Phase 2 — Connector runtime (L2).**
`RESTMessageV2` wrapper Script Include: auth profile resolution, timeout, our own
retry/backoff, circuit breaker, `call_log` write on every attempt.
→ **Gate:** a successful live call **and** a forced-failure call, both logged, with
the breaker demonstrably opening. **Test the failure path before the happy path.**

**Phase 3 — First remote table (L3).**
`x_u4bsh_erpcrm_rt_invoice` + query script driven by `object_map`. Set Cache TTL
deliberately and record why.
→ **Gate:** real ERP invoices rendering in a native list view, filterable.
Measured latency at TTL=0 and at your chosen TTL, both pasted. Confirm no row is
persisted anywhere.

**Phase 4 — Presentation (L4).**
React UI Page + Account panel + Case panel. Provenance and as-of on every figure.
→ **Gate:** an agent opens a real case and answers *"is this account clear to be
served?"* without leaving ServiceNow. Plus: with the ERP switched off, the panel
says **"unavailable"** — verified, not assumed.

**Phase 5 — Agentic layer (L5). OPTIONAL.**
Only if Now Assist for App Engine is licensed. Evidence ledger, suggestion queue,
AI Agent Studio agent, human approval before any write.
→ **Gate:** no write to any record without a human approval step, proven by
attempting one.

**Second ERP is the real test of the design.** Adding it must require zero new
code — only `erp_system` + `object_map` rows. Schedule that as an explicit
exercise, not an assumption.

---

## 9. Non-negotiables

1. **Never store ERP financial data in ServiceNow tables.** Remote tables only.
   The moment it is persisted, it is stale, it is a compliance surface, and it is
   a reconciliation problem.
2. **No silent failure.** A failed or timed-out ERP call renders as
   **"unavailable"** with the reason. Never blank, never `0`, never a stale figure
   presented as current. A wrong credit-limit shown confidently is worse than no
   figure at all.
3. **Provenance on every number** — which ERP system, as of when, cached or live.
4. **Read-only by default.** `u_read_only = true`. Write-back to an ERP is a
   separate, explicitly approved decision per system.
5. **Batch, never loop.** No per-row HTTP calls in a query script. Ever.
6. **No new table that duplicates a CRM Foundation object** (§3).
7. **No dependency on IntegrationHub, `sn_fcms_intg`, or any S2P component.**
   If a design needs one, it is the wrong design — escalate, do not smuggle it in.
8. **Financial data is not visible to every agent by default.** ACL-gate it, and
   assume the customer portal never sees it until someone explicitly decides
   otherwise.
9. **Every architectural decision that rejects an alternative gets written down**
   with the rejected option and why.

### Roles to start from

`ServiceNowOfficialDocs/customer-relationship-management/customer-relationship-management/crm-user-management.md`:
`sn_customerservice_agent` (B2B agent), `sn_customerservice.consumer_agent` (B2C),
`sn_customerservice_manager` (service manager). Add app-local roles:
`x_u4bsh_erpcrm.viewer`, `.finance_viewer`, `.admin`. Financial figures require
`.finance_viewer`, granted deliberately — **not** implied by
`sn_customerservice_agent`.

---

## 10. Open questions for the first working session

**Answered by §1A** — do not re-ask:
- ~~Which ERP first, and does it expose REST?~~ → **Unit4 ERPx, REST, live**
- ~~MID Server available?~~ → **Not used on this cloud-to-cloud path**
- ~~Is IntegrationHub available?~~ → **Yes, 23 ERP flows in production**

**Still open, in priority order:**

1. **Is Zero Copy Connector for ERP entitled, and does it work with Unit4?**
   (§1A.7) This is now the highest-value question in the brief — a yes potentially
   removes L2 and most of L3. The compendium flags that its documentation is
   *"generic and SAP-oriented"* with no confirmed Unit4 content pack.
2. **Does `customer_account` already carry the Unit4 customer key?** (§1A.3) The
   `Unit4 - Cutomer Account` transform map may have solved the correlation problem
   already. Inspect before building `account_xref`.
3. Cache TTL per object, modelled against the **500 req/min** ceiling and the
   **concurrency-10** recommendation (§1A.4) — not chosen by feel.
4. Expected row volumes — does anything exceed 1000 rows and need Enhanced
   Capacity?
5. Is write-back to the ERP ever in scope, or is this read-only forever? Note Zero
   Copy supports *"read, update and create"*, so the answer is no longer forced by
   the technology.
6. Who is the primary user — CSM agent, finance, or account manager? The Case
   panel and the 360 workspace serve different people. Design for one first.
7. What do the remaining **16 unnamed transform maps** and **~2 unnamed flows**
   do? (§1A.8) Consider `sn-instance-scan` rather than manual enumeration.
8. Is `com.sn_customerservice` active, and is Now Assist for App Engine licensed?
   (Carried from §1.)

---

## 11. Honest risk register

| Risk | Severity | Mitigation |
|---|---|---|
| **We now own ERP connectors that SAP/Oracle will change.** This is the real cost of avoiding the licence, and it is ongoing, not one-off | High | Keep all ERP-specific detail in `object_map` data, never in code. Version the field maps |
| **No IntegrationHub retry policy** — must be hand-written | Medium | Phase 2 gate tests the failure path first |
| **Scope creep into "a general ERP integration framework"** | High | One ERP, one object, end to end, before anything is generalised. The second ERP is the test, not the goal |
| **Remote table latency makes lists hang** | Medium | Cache TTL, Enhanced Capacity, and a hard client-side timeout with a graceful "unavailable" |
| **Financial data leaking to the customer portal** | High | ACL from day one; portal explicitly denied; `bug-hunter` pass on ACLs |
| **Rebuilding CSM by accident** | Medium | §3 rejection criterion, enforced at the `governance` gate |
| **L5 built before L1–L4 are solid** | Medium | Agentic layer is last and optional. An AI agent over an unreliable data layer produces confident wrong answers — the exact failure mode Comp AI's evidence principle exists to prevent |
| **Building L2/L3 by hand when Zero Copy Connector already does it** | **High** | Phase 0 must answer the entitlement/compatibility question first (§1A.7). This is now the largest single source of wasted effort in the plan |
| **Breaching Unit4's 500 req/min limit and getting suspended for a minute** | **High** | Non-zero Cache TTL, batching, concurrency ≤10, and honouring `Retry-After` (§1A.4). A rate-limit suspension looks exactly like an outage to an agent |
| **Duplicating a legal-entity table when `x_u4bsh_finance_le` exists** | Medium | Reference it (§1A.3). Same rejection criterion as the CRM Foundation objects |
| **Pointing a non-production ServiceNow instance at Unit4 PROD** | High | Explicit Unit4 rule; enforce via Connection Alias configuration (§1A.4) |
| **Treating the compendium's inventory as complete** | Medium | It names 9 of 25 maps and flags six other gaps itself (§1A.8). Verify on the instance |

---

## 12. Verdict on the shape of this

The original ask was a CRM + an ERP control tower + a port of an agentic CRM.
After retrieval and one licensing constraint:

- **CRM:** not built. ServiceNow ships Sales CRM / CSM / FSM on a shared
  foundation. We build the ERP join that is genuinely missing from it.
- **ERP control tower:** built, and now justified — the vendor's own framework
  sits behind a licence the org does not hold. We copy its *concepts* (ERP source,
  legal-entity mapping, abstraction layer) without its code, and we do it on
  base-instance plugins only.
- **Comp AI port:** two ideas adopted (evidence provenance, visible integration
  state), the stack discarded, and the parts that genuinely do not port named as
  such rather than faked.
- **React:** officially supported via Fluent `UiPage`. The user's instinct was
  right and the platform agrees.

**Revised 2026-08-18, after the Unit4 compendium (§1A):** the plan is more
tractable than it looked and the scope is smaller. IntegrationHub is available,
the ERP is known and REST-based, no MID Server is needed, and master data already
flows into `customer_account`, `service_entitlement` and the install base. The
remaining job is genuinely the financial half of the 360 view.

But two things must be settled before a line of code:

1. **Zero Copy Connector for ERP** may already be L2 + most of L3. Answer the
   entitlement and Unit4-compatibility question first (§1A.7).
2. **Check whether `customer_account` already holds the Unit4 key** before
   building a cross-reference table for it (§1A.3).

Get both wrong and this becomes weeks of rebuilding things that exist. The hard
part was never the technology — it is finding out what is already there, and the
compendium just moved that a long way forward.

---

## Appendix A — Project setup with now-sdk, from zero

Do this **before Phase 1**. Nothing below is optional, and two items are traps
that have already cost time in this org.

### A.0 Never assume `now-sdk` is on `$PATH`

`npx @servicenow/sdk init` installs the SDK **into the application directory, not
globally** — the doc says so explicitly (A.3). A bare `now-sdk build` therefore
works only on a machine where someone happened to install it globally, and fails
on a clean checkout.

**Always invoke it through `npx` from the application directory, or through an
npm script.** Both resolve the locally installed binary regardless of machine:

```bash
npx now-sdk <command>      # from inside the app directory
npm run build              # if wrapped as a script — see A.5
```

Every command in this appendix follows that rule. If you see a bare `now-sdk` in
any older note or doc, treat it as shorthand, not as a working command on a fresh
machine.

The same applies to the instance alias: `<alias>` below is whatever you registered
in A.2. Do not hardcode someone else's.

### A.1 Prerequisites — node version

The SDK's entry point resolves whichever `node` is first on `$PATH`. Verify
before anything else:

```bash
node --version      # must be a modern LTS
```

> [!warning] If you are on zsh with nvm
> From `wiki/concepts/scoped-apps.md`: *"If nvm is only loaded in `~/.bashrc` (not
> `~/.zshrc`), zsh sessions fall back to system Node (v12), causing
> `Unexpected token '?'` errors in subcommands that use modern JS (e.g.
> `now-sdk init` with inquirer). `--help` survives because it avoids modern
> syntax. Fix: add the nvm loader block to `~/.zshrc`."*
>
> Symptom to recognise: `--help` works, `init` throws `Unexpected token '?'`.
> That is Node, not the SDK. Do not debug the SDK.

### A.2 Authenticate

```bash
npx @servicenow/sdk auth --add <instance-url> --type basic|oauth --alias <alias>
npx now-sdk auth --list
npx now-sdk auth --use <alias>
```

Sources: `ServiceNowOfficialDocs/now-platform/ServiceNow_Local_Development_Guide.md`
(the in-house guide — it hardcodes `https://unit4dev1.service-now.com` and the
alias `unit4dev1`, which are that instance's, not universal) and
`Applications/capacity-planner/capacity-planner.md` §11.

Pick your own alias and keep it consistent. Everything downstream takes
`--auth <alias>`. Credentials are stored by the SDK per machine — a fresh machine
needs `auth --add` again before anything else works.

### A.3 Create the application

`ServiceNowOfficialDocs/application-development/servicenow-sdk/create-application-now-sdk.md`:

```bash
mkdir erp-crm-360 && cd erp-crm-360
npx @servicenow/sdk init
```

> *"Using the `npx` command installs the ServiceNow SDK in your application
> directory instead of globally."*

Answer the prompts:

| Prompt | Answer for this app |
|---|---|
| `Select a template` | **A React template.** The doc: *"Select a template that determines the default application structure, such as whether to create a full-stack application that supports UI development and whether to use JavaScript or TypeScript to create modules."* And from the React doc: *"To get started using React, select one of the React templates when creating an application with the ServiceNow IDE or ServiceNow SDK."* TypeScript preferred |
| `Name of ServiceNow Application` | `ERP CRM 360` |
| `NPM package name` | `erp-crm-360` |
| `Create a Global/Scoped App?` | **Scoped** — *"protected by identifying and restricting access to application files and data"* |
| `Scope name` | `x_u4bsh_erpcrm` |

> [!warning] Scope name rules
> *"The scope name must be unique on the instance, begin with `x_<prefix>`, and be
> **18 characters or fewer**."* `x_u4bsh_erpcrm` is 14 — fits. If you rename the
> app, re-check the length before running `init`; it is not fixable afterwards
> without recreating.

Then:

```bash
npm install                          # required before the first build — init says so
npx now-sdk build
npx now-sdk install --auth <alias>
```

**Alternative — pulling an existing app** rather than creating one:

```bash
npx @servicenow/sdk init --from <APPLICATION_SYS_ID> --auth <alias>
```

### A.4 The daily loop

Run from the application directory:

```bash
# sync first
npx now-sdk transform --auth <alias>

# develop locally

# build and deploy
npx now-sdk build
npx now-sdk install --auth <alias>
```

**Why `transform` matters** — *"The `transform` command synchronizes metadata
changes from the instance into your local project by converting them into source
code. It should be used frequently to avoid drift between local and instance
versions."*

Conflict rules, verbatim from the same guide:
- *"Always run `transform` before starting work."*
- *"Avoid editing the same records both locally and directly in the instance at
  the same time."*
- *"Use a consistent workflow (`pull → change → build → deploy`)."*
- *"If unsure, run `transform` again before deploying."*

Changes made in the browser that **must** be pulled with `transform` or local
code will overwrite them on the next deploy: *"Updating a Business Rule from the
UI, Editing a Script Include in Studio, Changing form layout or UI Policy,
Modifying ACLs or roles."*

This bites hardest on this app specifically, because **remote table script
definitions (`sys_script_vtable`) are frequently tweaked in the browser while
debugging a query.** Transform before every build, without exception.

Useful: `npx now-sdk --help`, and `<command> --help` for parameters (e.g.
`npx now-sdk auth --help`).

### A.5 npm script wrappers — the portable way to run this

Wrap the commands in `package.json` so nobody has to remember `npx` or worry
about `$PATH`. Inside an npm script the locally installed binary is already on
the path, so a bare `now-sdk` is correct **there and only there**:

```json
{
  "scripts": {
    "build":  "now-sdk build",
    "deploy": "npm run build && now-sdk install",
    "sync":   "now-sdk transform"
  }
}
```

```bash
npm install                       # one-time: SDK and dependencies
npm run sync   -- --auth <alias>
npm run deploy -- --auth <alias>
```

The capacity planner uses the same wrapper pattern
(`Applications/capacity-planner/capacity-planner.md` §11), and records why the
chaining matters:

> *"`npm run build` must always precede `npm run deploy`. A failed build leaves
> prior artifacts in `dist/` so deploying without rebuilding ships stale output."*

That failure mode is silent, which is why `deploy` above chains `build` rather
than trusting anyone to remember. Do not split them back apart.

### A.6 Two manual steps after every deploy

From `Applications/capacity-planner/capacity-planner.md` §11:

1. **Commit the Update Set.** In-browser: System Update Sets → find the
   `x_u4bsh_erpcrm` update set → Complete → Preview → Commit.
2. **Hard-refresh the browser** on the app's `.do` endpoint. *"The BYOUI JS asset
   is aggressively cached — a normal refresh can silently serve the previous
   build."* This applies directly to the React UI Page in §4: you will otherwise
   spend an afternoon debugging a bundle that was never loaded.

### A.7 The `sys_properties` placeholder trap

Already flagged in §4, repeated here because it belongs to the deploy step:

> *"The SDK does not create `sys_properties` rows from `Record()` declarations
> when the sys_id is fake — the deploy finds no record with that sys_id and
> silently skips it."*

Fix, per the capacity planner note: navigate to `sys_properties_list.do`, select
the app scope, create the property manually, copy the generated sys_id, and update
`src/fluent/generated/keys.ts` with the real value.

**After every deploy that adds a property, verify the row exists.** Do not assume
it landed. This app will have properties for default cache TTLs and circuit-breaker
thresholds, and a missing one fails to a default rather than an error — the exact
shape of bug that survives a green test run.

### A.8 Expected repository layout

Derived from the React UI page doc
(`ServiceNowOfficialDocs/application-development/ui-development-react.md`) and the
capacity planner's structure:

```
erp-crm-360/
├── package.json
├── src/
│   ├── fluent/
│   │   ├── tables/            # erp_system, object_map, account_xref, call_log
│   │   ├── records/           # system properties, ACLs
│   │   ├── erp-360.now.ts     # UiPage definition
│   │   └── generated/keys.ts  # ← watch the placeholder sys_ids (A.7)
│   └── client/
│       ├── index.html         # <sdk:now-ux-globals> + <script src="./main.jsx">
│       ├── main.jsx           # React entry point
│       └── app.jsx
└── dist/                      # build output — never edit, never commit by hand
```

Remote table **script definitions** live in `sys_script_vtable` on the instance.
Decide early whether they are authored locally as Fluent records or in the browser
and pulled with `transform` — and then hold that line. Mixing the two is how the
PCCC router ended up with two divergent copies of the same script.

### A.9 Reference

- `ServiceNowOfficialDocs/application-development/servicenow-sdk/servicenow-sdk-cli-commands.md` — full CLI reference (`install`, `build`, `transform`, …)
- `ServiceNowOfficialDocs/application-development/servicenow-sdk/create-application-now-sdk.md` — creating from scratch
- `ServiceNowOfficialDocs/application-development/servicenow-sdk/build-deploy-application-now-sdk.md` — build and install procedure
- `ServiceNowOfficialDocs/application-development/servicenow-sdk/convert-application-now-sdk.md` — converting an existing app
- `ServiceNowOfficialDocs/now-platform/ServiceNow_Local_Development_Guide.md` — the in-house guide, instance-specific
- `ServiceNowOfficialDocs/application-development/servicenow-sdk/use-third-party-libraries.md` — installing `@servicenow/react-components` and other npm deps
- `wiki/concepts/scoped-apps.md` — scoping, namespacing, and the nvm/zsh and `global.GlideAjax` gotchas
