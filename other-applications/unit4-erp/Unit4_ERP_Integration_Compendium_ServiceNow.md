UNIT4 ERP INTEGRATION COMPENDIUM 

# **UNIT4** 

### **ERP Integration Compendium** 

ServiceNow, ERPx, ERP CR, APIs, flows, payloads, limits and governance 

###### **Scope** 

Consolidated from the Unit4 internal documents retrieved for this investigation, with emphasis on the implemented ServiceNow ↔ Unit4 ERP/ERPx integrations. Includes every endpoint, path, query parameter, JSON/XML example, integration object, limit and documented observation found in the retrieved source material. Unrelated personal data found in a OneNote page was intentionally excluded. 

###### **Prepared for Pedro Leite** 

17 August 2026 Technical working document 

Business (TLP Green)  |  Compiled 17 August 2026  |  1 

UNIT4 ERP INTEGRATION COMPENDIUM 

## **Contents** 

1. 1. Scope, evidence and caveats 

2. 2. Executive architecture view 

3. 3. Endpoint and interface catalogue 

4. 4. ServiceNow implementation inventory 

5. 5. Employee API REST integration 

6. 6. Employee update JSON Patch integration 

7. 7. Contract/rates SOAP integration 

8. 8. HR Letters and document integration 

9. 9. ServiceNow ERP Integration Framework 

10. 10. Zero Copy Connector for ERP 

11. 11. Unit4 cloud integration capabilities and constraints 

12. 12. API and platform limits 

13. 13. Security, authentication and operational concerns 

14. 14. Migration review and consultancy services 

15. 15. Gaps, contradictions and validation backlog 

16. Appendix A. Payloads and mappings 

17. Appendix B. Source register 

Business (TLP Green)  |  Compiled 17 August 2026  |  2 

UNIT4 ERP INTEGRATION COMPENDIUM 

#### **1. Scope, evidence and caveats** 

This compendium combines implementation-specific ServiceNow and Unit4 ERP/ERPx documentation with broader Unit4 cloud and ServiceNow ERP framework references. The implementation-specific source is the unit4dev1 integration summary, augmented by HR Letters technical documentation and an IntegrationHub action note. 

###### **Important evidence boundary** 

The document reproduces and organizes what is explicitly present in the retrieved sources. Where a source itself uses words such as “likely”, “appears”, or flags a concern, that wording is preserved as an observation rather than converted into a confirmed fact. 

- Primary implementation source: ERP Integration Summary - until 20 of April 2026.docx. 

- HR implementation source: ServiceNow HR Letters 1.docx. 

- Action mapping source: Developments.one, section “Action - Unit4 - GET ERP Employee info”. 

- Platform/governance sources: Unit4 ERP CR Cloud Service Description V.2026.Q2 and Unit4 Cloud Technical Guidelines and Limits v2.1. 

- ServiceNow framework sources: ERP Integration Framework and Zero Copy Connector markdown documentation. 

- Migration service sources: Integrations Review Service and Integrations Consultancy service descriptions. 

_Source: Retrieved internal Unit4 files listed in Appendix B._ 

#### **2. Executive architecture view** 

The documented unit4dev1 implementation connects ServiceNow to Unit4 ERPx using outbound REST messages, inbound Scripted REST APIs and Integration Hub flows. The implementation summary states that no MID Server is used for this cloud-to-cloud path. 

|**Direction**|**Mechanism**|**Documented use**|
|---|---|---|
|ServiceNow → ERPx|Outbound REST|Discovery, user tracking, employee<br>reads/updates and document operations.|
|ERPx → ServiceNow|Scripted REST APIs|Attachments, change requests, customer<br>contact management and customer emails.|
|ServiceNow orchestration|Integration Hub / Flow Designer|Provisioning, tracking, operations, support,<br>release and decommissioning.|
|Bulk/external → ServiceNow|Import Sets + Transform Maps|Entitlements, accounts, departments, legal<br>entities, install base, services and Salesforce<br>case data.|
|ServiceNow → Unit4 Business World<br>personnel service|SOAP|Add or update employee contract/rates fexi-<br>feld rows.|



###### **MID Server distinction** 

The unit4dev1 REST integration summary says no MID Server is used. The general ServiceNow Source-to-Pay ERP Integration Framework documentation says a MID Server is required for SOAP-based ERP integrations, but not for RESTbased integrations. The SOAP employee contract action resolves a dynamic HTTP(s) Connection endpoint; the source does not explicitly state its MID Server configuration. 

Business (TLP Green)  |  Compiled 17 August 2026  |  3 

UNIT4 ERP INTEGRATION COMPENDIUM 

#### **3. Endpoint and interface catalogue** 

|**Name**|**Direction / method**|**Endpoint or path**|**Authentication / notes**|
|---|---|---|---|
|ERPx Discovery|ServiceNow → ERPx, GET IDS|https://u4discovery-<br>sandbox.u4pp.com/api/v2|No authentication confgured.<br>Variables: services=authority;<br>sourcesystems=u4ids;<br>tenantId=b5cfb2be-56ba-48d3-<br>839b-bed90d4e57bb.|
|ERPx Tracking|ServiceNow → ERPx, POST|https://eu01.erpx-<br>api.unit4rd.com/v1/tracking/$ {userId}/enable/${trackingId}?<br>userId=${userId}&trackingId=$ {trackingId}|OAuth 2.0 selected, but no OAuth<br>profle assigned in the<br>documented confguration.|
|Unit4 Attachments|ERPx → ServiceNow|/api/u4bsh/unit4_attachments|Active Scripted REST API.|
|Unit4 Change Request|ERPx → ServiceNow|/api/u4bsh/<br>unit4_change_request|Active Scripted REST API.|
|Unit4 Customer Contact<br>Management|ERPx → ServiceNow|/api/u4bsh/ccm|Active Scripted REST API.|
|Unit4 Customers Emails|ERPx → ServiceNow|/api/u4bsh/<br>unit4_customers_emails|Versioned; active Scripted REST<br>API.|
|Employee read|ServiceNow → Unit4 ERP, GET|{Connection Alias base<br>URL}/objects/employees?<br>companyId={companyId}<br>&flter=personId eq {employeeId}<br>&select={optional select}|Password (2-Way) through<br>Connection Alias.|
|Employee update|ServiceNow → Unit4 ERP, PATCH|{Connection Alias base<br>URL}/employees/{Employee ID}?<br>companyId={companyId}|Content-Type: application/json-<br>patch+json.|
|Personnel contract row|ServiceNow → UBW, SOAP<br>AddFlexiFieldRows|Dynamic endpoint from HTTP(s)<br>Connection record|Credentials in SOAP body:<br>Username, Client/Company ID<br>and Password.|



_Source: ERP Integration Summary - until 20 of April 2026; inbound paths and detailed employee/contract interface sections._ 

#### **4. ServiceNow implementation inventory** 

##### **4.1 Integration Hub flows** 

|**Flow**|**Documented purpose**|
|---|---|
|ERPx User Tracking Integration v2 / ERPX User Tracking Integration|Core user tracking; source describes the trigger relationship as likely.|
|JIT ERPX Trigger|Just-in-time user provisioning trigger.|
|u4ia service request ERPx|Creates new Partner ERPx cloud service requests.|
|ERP Cloud Customer Web Trace Request|Web trace request handling.|
|Database Audit (ERP:CR & ERPx)|Audit queries.|
|Create new ERPX service|Creates environment-related objects.|
|Activation of ERPx Feature SR|Creates tasks in Change when activating ERPx features.|
|Decommission of ERPx application service|Generates four Change tasks for decommissioning.|
|UWID Assignment - ERPx|Assigns UWIDs to ERPx tenants.|



Business (TLP Green)  |  Compiled 17 August 2026  |  4 

UNIT4 ERP INTEGRATION COMPENDIUM 

|Unit4 - ERPx tenant SQL readonly access|Grants SQL read-only access to ERPx tenants.|
|---|---|
|Enable ERPx Database login|Operational/support fow.|
|Download ERPx tenant license fle|Operational/support fow.|
|Get Log File ERPX|Operational/support fow.|
|ERPx Partner Industry Model release|DevOps/release pipeline fow.|
|ERPx training environment backup publish|DevOps/release pipeline fow.|
|ERPx SQL Script to DevOps|DevOps/release pipeline fow.|
|U4ia ERPx Tenant End Date Extension|Extends tenant end dates.|
|Disable Sampling for ERPx for 2 hours|Temporarily disables sampling.|
|ERP Cloud database backup request|Cloud operations fow.|
|ERP Cloud Customer web endpoints reset|Cloud operations fow.|
|ERP Cloud Customer License Retrieval|Cloud operations fow.|



The source states there are 23 ERP-specific flows, while the combined/grouped rows explicitly named in the source expose the items above. Where several flow names were grouped in one row, they are expanded individually here. 

##### **4.2 Transform maps and targets** 

|**Transform map**|**Source → target**|
|---|---|
|Unit4 Entitlement V3|u_unit4_entitlements_v3 → service_entitlement|
|Unit4 - Cutomer Account|CSM import → customer_account|
|Unit4 Populate departments|Cost Centers → cmn_department|
|Unit4 - imp Legal Entity|u_imp_legal_entities → x_u4bsh_fnance_le|
|Unit4-Installbase-Sold Products|CSM import → sn_install_base_m2m_installed_product|
|Unit4 Application Services V2|Import → cmdb_ci_service_discovered|
|Unit4 - Transform Sales Force Cases|Salesforce import → sn_customerservice_case|
|Unit4 - Import SF case Comments & Worknotes|Salesforce import → sn_customerservice_case|
|Unit4 - product/version|u_product_version_update → CSM Data Lookup|



The source states that 25 maps exist, but only the maps above were explicitly listed in the retrieved summary. The remaining map names and field-level scripts were not present in the retrieved content. 

##### **4.3 Script include and scheduled jobs** 

|**Object**|**State/frequency**|**Purpose / observation**|
|---|---|---|
|ERPxAppFilter|Inactive; source says last updated 25 August<br>2025|Source describes it as likely a flter utility and<br>fags possible routing/fltering side efects.|
|ERPx Cases unassigned_P1|Every 1 hour|Report on unassigned P1 ERPx cases.|
|ERPx ERP7 Unassigned P1 Problems|Every hour|Report on unassigned P1 problems.|
|ERPx_SQL Repetitive Tasks|Every 30 minutes|Report on repetitive SQL tasks.|



Business (TLP Green)  |  Compiled 17 August 2026  |  5 

UNIT4 ERP INTEGRATION COMPENDIUM 

|PM - EMEA - ERP/ERPx - UWID Done|Weekly|PM automation.|
|---|---|---|
|Scheduled execution of PM - ERPx - Unass...|Repeating|PM execution; name was truncated in the<br>source.|



#### **5. Employee API REST integration** 

|**Property**|**Value**|
|---|---|
|Action|Unit4 - GET ERP employee / Unit4 - GET ERP Employee info|
|Protocol|REST|
|HTTP method|GET|
|Resource|objects/employees|
|Base URL|Dynamic from Connection Alias|
|Authentication|Password (2-Way) through Connection Alias|
|companyId|Mandatory Company ID query parameter|
|flter|Mandatory OData flter: personId eq {Employee ID}|
|select|Optional feld selection string|
|Response|JSON array; index [0] is treated as the employee record|



```
GET {baseUrl}/objects/employees
```

- `?companyId={Company ID}` 

```
    &filter=personId eq {Employee ID}
```

```
    &select={optional comma-separated/select expression}
```

A sibling action, Unit4 - GET ERP employee contract info, uses the same endpoint and filter but selects contract-focused fields and extracts Contract Rows, Contract Type, Contract End Date, Employment End Date and Employment Start Date. 

##### **5.1 IntegrationHub action metadata** 

|**Action**|**Sys ID**|**Inputs**|**Outputs**|
|---|---|---|---|
|Unit4 - GET ERP Employee info|6db6831387184714d939a7573cb<br>b35e3|Connection Alias; Company ID;<br>Employee ID|full_name; position; department;<br>response_code; Action Status|
|Unit4 - GET ERP Employee Rates|3f6658bf87980f14d939a7573cbb<br>353c|Connection Alias; Company ID;<br>Employee ID; optional Efective<br>Date|salary; currency; pay_frequency;<br>response_code; Action Status|
|Unit4 Send Document to ERP|Not stated in retrieved section|Connection Alias; Attachment ID;<br>Company ID; Employee ID;<br>Document Type|Output details were not present<br>in the retrieved matching passage|



###### **Documentation inconsistency** 

The HR Letters document describes “Unit4 - GET ERP Employee Rates” as a REST action returning salary/rate data. The implementation summary separately says the “Rates API” for contract lines is SOAP AddFlexiFieldRows and is a write operation. Treat these as separate actions unless the instance confirms otherwise. 

Business (TLP Green)  |  Compiled 17 August 2026  |  6 

UNIT4 ERP INTEGRATION COMPENDIUM 

##### **5.2 Employee field mapping example** 

```
{
```

```
  "full_name_fx": "customFieldGroups/hrna0102/full_name_fx",
  "id_type_fx": "customFieldGroups/cia00hr07/id_type_fx",
  "id_number_fx": "customFieldGroups/cia00hr07/id_number_fx",
  "contract_type_fx": "customFieldGroups/hrc0100/contract_type_fx",
  "bonus_type": "relatedValues[relationId=X750]/description",
  "bonus_type_code": "relatedValues[relationId=X750]/relatedValue",
  "currency": "relatedValues[relationId=A2]/description",
  "currency_iso3_code": "relatedValues[relationId=A2]/relatedValue"
}
```

_Source: Developments.one, “Action - Unit4 - GET ERP Employee info”. Unrelated personal information on the same page was excluded._ 

#### **6. Employee update JSON Patch integration** 

|**Property**|**Value**|
|---|---|
|Action|Unit4 - PATCH ERP employee|
|Method|PATCH|
|Resource|employees/{Employee ID}|
|Query|companyId={Company ID}|
|Content-Type|application/json-patch+json|
|Body|JSON Patch array / implementation wrapper shown below|
|Base URL|Dynamic from Connection Alias|



```
{
  "employeeInfo": [
    {
      "op": "Replace",
      "path": "customFieldGroups/hrc0116",
      "value": {
        "date_marital_status_fx": "...",
        "place_of_birth": "...",
        "education": "...",
        "document_number": "...",
        "document_to_identify": "...",
        "document_issue_date_xf": "...",
        "document_expiration_date_xf": "...",
        "document_issue_country": "..."
      }
    },
    {
      "op": "Replace",
      "path": "personalInformation",
      "value": { "...": "source abbreviates this object" }
    }
  ]
}
```

Country-specific payload builders are documented for BE, SG, ID, DE, MY, PT, UK, ES and PL. The source notes different customFieldGroups paths, including hrc0116 for Belgium and hrc0100 for others. 

- Civil status and date 

- Place of birth and education 

Business (TLP Green)  |  Compiled 17 August 2026  |  7 

UNIT4 ERP INTEGRATION COMPENDIUM 

- Identity/document fields 

- Home address and personal contacts 

- Bank details 

- Billability code 

- Income category and cost category 

- Employment start/end dates 

- Probation end date 

#### **7. Contract/rates SOAP integration** 

|**Property**|**Value**|
|---|---|
|Action|Unit4 - Add employee contract line to ERP|
|Protocol|SOAP|
|SOAP action|AddFlexiFieldRows|
|Namespace|http://services.agresso.com/PersonnelService/<br>PersonnelServiceV201010|
|Endpoint|Dynamic from HTTP(s) Connection record looked up in step 1|
|Credentials|Username + Client/Company ID + Password inside <per:credentials>|
|FlexiGroup|HRC0100|
|Row identifer|RowNo|



Business (TLP Green)  |  Compiled 17 August 2026  |  8 

UNIT4 ERP INTEGRATION COMPENDIUM 

```
<soapenv:Envelope
  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:per="http://services.agresso.com/PersonnelService/PersonnelServiceV201010">
  <soapenv:Header/>
  <soapenv:Body>
    <per:AddFlexiFieldRows>
      <per:company>{Company ID}</per:company>
      <per:resourceId>{Employee ID}</per:resourceId>
      <per:flexiGroupList>
        <per:FlexiGroupUnitType>
          <per:FlexiGroup>HRC0100</per:FlexiGroup>
          <per:FlexiFieldRowList>
            <per:FlexiRowUnitType>
              <per:RowNo>{Contract Row}</per:RowNo>
              <per:FlexiFieldList>
                <per:FlexiFieldUnitType>
                  <per:ColumnName>date_from_val_xf</per:ColumnName>
                  <per:Value>{Date From}</per:Value>
                </per:FlexiFieldUnitType>
                <per:FlexiFieldUnitType>
                  <per:ColumnName>date_to_val_xf</per:ColumnName>
                  <per:Value>{Date To}</per:Value>
                </per:FlexiFieldUnitType>
                <per:FlexiFieldUnitType>
                  <per:ColumnName>contract_type_fx</per:ColumnName>
                  <per:Value>{Contract Type}</per:Value>
                </per:FlexiFieldUnitType>
              </per:FlexiFieldList>
            </per:FlexiRowUnitType>
          </per:FlexiFieldRowList>
        </per:FlexiGroupUnitType>
      </per:flexiGroupList>
      <per:credentials>
        <per:Username>{Username}</per:Username>
        <per:Client>{Company ID}</per:Client>
        <per:Password>{Password}</per:Password>
      </per:credentials>
    </per:AddFlexiFieldRows>
  </soapenv:Body>
</soapenv:Envelope>
```

|**UBW column**|**Meaning**|
|---|---|
|date_from_val_xf|Contract start date|
|date_to_val_xf|Contract end date|
|contract_type_fx|Contract type code|



#### **8. HR Letters and document integration** 

The HR Letters implementation uses ServiceNow flows and subflows to retrieve ERP data, generate PDF documents and send those attachments to Unit4 ERP. 

|**Subfow / action**|**Role in the integration**|
|---|---|
|Unit4 ERP Employee integration|Calls the employee-info action and exposes employee data to HR<br>fows.|
|Unit4 ERP Rates integration|Exposes salary, currency and payment-frequency outputs.|



Business (TLP Green)  |  Compiled 17 August 2026  |  9 

||UNIT4 ERP INTEGRATION COMPENDIUM|
|---|---|
|Unit4 ERP Document Integration|Sends a generated attachment/document to Unit4 ERP using<br>Connection Alias and attachment data.|
|Unit4 Send Document to ERP|Low-level REST action for sending a PDF attachment.|
|Generate document template - HTML|Converts generated HTML into a PDF attachment.|
|Move Attachment from HR Case to HR Task|Copies/moves the generated attachment for task-level review/access.|



##### **8.1 Promotion Letter flow integration path** 

- Trigger: HR Task record created for the Salary Changes and Promotions service/template with the documented shortdescription condition. 

- Select the correct ERP Connection Alias based on company data. 

- Look up parent HR case and employee HR profile. 

- Set ERP Company ID from Company → Company ID and ERP Employee ID from HR Profile → Employee number. 

- Generate promotion-letter HTML and convert it to a PDF attachment. 

- Invoke Unit4 ERP Document Integration with the selected Connection Alias and generated attachment. 

- Log and terminate on document-generation or ERP-send errors. 

- Move/copy the attachment from HR Case to HR Task. 

_Source: ServiceNow HR Letters 1.docx, HR Promotion Letter flow and shared component sections._ 

#### **9. ServiceNow ERP Integration Framework** 

The Source-to-Pay ERP Integration Framework supports primary data and transactional data exchange, including purchase orders, receipts, invoices, fixed assets and tax information across multiple ERP instances. 

- ERP Sources represent ERP instances used for import and export and are mapped to legal entities. 

- At least one ERP Source must be configured for each legal entity in every target instance. 

- Third-party ERP is the documented system of record for primary-data entities. 

- Source-to-Pay is the documented system of record for purchase orders and receipts. 

- Invoices may be created in Source-to-Pay or through external supplier portals. 

- The framework and Source-to-Pay Integration Framework provide an abstraction layer from backend-specific structures. 

- The Finance - ERP Integration store application is required. 

|**Role**|**Capabilities**|
|---|---|
|sn_fcms_intg.admin|Install integration applications; system settings; manage integration<br>infrastructure.|
|sn_shop.procurement_specialist|Defne/manage ERP Sources, parameters and workfows.|
|sn_fcms_intg.integration_user|ERP source settings, web-service authorization, Park/Post/Reverse<br>services, mappings, staging tables and integration processes.|
|import_transformer|Data transformation operations.|
|soap|SOAP-based web-service integrations.|



##### **9.1 MID Server rule** 

The framework documentation states that SOAP integrations require a configured MID Server, while REST integrations do not. This is general framework guidance and does not, by itself, prove how the documented HR SOAP action is deployed in unit4dev1. 

Business (TLP Green)  |  Compiled 17 August 2026  |  10 

UNIT4 ERP INTEGRATION COMPENDIUM 

#### **10. Zero Copy Connector for ERP** 

Zero Copy Connector for ERP is a ServiceNow scoped application for retrieving and updating ERP data from a system of record. It was previously named ERP Data Hub and ERP Canvas. 

- Creates models containing ERP data in remote tables and extraction tables. 

- Supports read, update and create operations through ERP models. 

- Remote tables run an associated script against an external data source. 

- Extraction tables use scheduled queries and transform tables for larger datasets and refresh needs. 

- The source says the connector mirrors ERP data and does not replicate it into the ServiceNow AI Platform. 

- ERP data can be used in ServiceNow Studio, Creator Studio, Workflow Studio, Table Builder, UI Builder and Workspace Builder. 

- Content packs provide predefined models and process extensions. 

- Domain separation is documented as unsupported. 

##### **10.1 Installation and configuration** 

- Install from the ServiceNow Store; admin role required. 

- Confirm product and dependent-application entitlements before requesting installation. 

- Enable sn_erp_integration.enableModelModification in the correct scope to edit, customize and clone ERP models and tables. 

- Role sn_erp_integration.erp_admin is required to configure the system-of-record connection. 

- The connection and login credential are used together, and credentials must match the system-of-record service user. 

- Connections may be direct or through a load balancer; available RFC or HTTP connections can be selected on the ERP system record. 

#### **11. Unit4 cloud integration capabilities and constraints** 

Unit4 ERP CR documentation lists APIs, web services, batch file interfaces and optional read-only access to a replicated production database as integration options. User access is over HTTPS. 

|**Area**|**Documented rule / capability**|
|---|---|
|SFTP|AES256-SHA2; TCP 41667; import/export only; executable fles<br>prohibited; 50 concurrent connections per account.|
|SFTP credentials|Two sets per environment by default: Data Import and Data Export;<br>user/password authentication.|
|Web/Desktop authentication|WS-Federation, SAML-P, OpenID Connect and application-specifc<br>credentials.|
|Internet communication|Web Client over HTTPS; Desktop Client over encrypted TLS.|
|Custom integrations|Permitted, but customer owns maintenance and compatibility for non-<br>standard components.|
|Custom code|Must be documented, transparent/readable and packaged with non-<br>interactive installation routines.|
|Direct local resource access|Not permitted; access must use approved abstraction methods.|
|API lifecycle|Use the most recent API version; supported previous versions retain<br>backward compatibility until end of life; EOL announcement at least<br>18 months in advance.|
|Database replica|Read-only replication may be provided for ERP CR/ERP7 and selected<br>products; exclusions apply.|
|Environment matching|PROD ↔ PROD; matching non-production types; non-production ↔<br>production is not supported or allowed.|



Business (TLP Green)  |  Compiled 17 August 2026  |  11 

UNIT4 ERP INTEGRATION COMPENDIUM 

#### **12. API and platform limits** 

##### **12.1 General Unit4 SaaS web API limits, excluding ERPx** 

|**Limit**|**Environment**|**Value**|
|---|---|---|
|HTTP requests per minute|PROD, PREV, ACPT01, ACPT02|500 per minute per environment|
|HTTP requests per minute|ACPT03-11|1,500 per minute shared|
|Inbound/outbound API size|All environments|350 MB per minute|



- When exceeded, subsequent requests are suspended for one minute. 

- Documented responses include HTTP 429, Retry-After, connection closure request and TCP termination. 

- Recommended handling: usage monitoring, batching, caching, throttling, exponential backoff and honoring Retry-After. 

##### **12.2 ERP CR / ERP7 technical limits** 

|**Limit**|**Value**|
|---|---|
|httpRuntime executionTimeout|360 seconds|
|maxRequestLength fle upload|58,368 KB|
|Web REST API timeout|120 seconds|
|SOAP API timeout|120 seconds|
|Private API memory limit|4 GB|
|Recommended REST API concurrency|10|
|Recommended SOAP call frequency|60/minute|
|Recommended SOAP concurrency|10|
|Files per Data Files folder|150,000|
|FIC extraction|2 years of data|
|Recommended number of clients for ERP/ERPx|50; source adds escalation guidance above 50/100|



##### **12.3 ERPx limits** 

|**ERPx limit**|**Value**|
|---|---|
|Web application request timeout|110 seconds|
|Public API Gateway request timeout|240 seconds|
|Long-running SQL from web application/Public API|240 seconds|
|Information Browser SQL from business reports|60 minutes|
|Business-report SQL|24 hours|
|Web application client idle session|20 minutes|
|Recommended number of clients|50|



Business (TLP Green)  |  Compiled 17 August 2026  |  12 

UNIT4 ERP INTEGRATION COMPENDIUM 

##### **12.4 ERPx connectivity** 

|**Setting**|**Requirement**|
|---|---|
|TLS|Minimum 1.2|
|WebSockets|Required for SignalR real-time communication|
|HTTPS|Port 443 for primary communication|
|HTTP|Port 80 redirects to HTTPS|
|Non-standard browser ports|Not required|
|Firewall/proxy|Allow unit4cloud.com and subdomains|



#### **13. Security, authentication and operational concerns** 

|**Finding**|**Evidence status**|**Action**|
|---|---|---|
|ERPx Tracking OAuth profle missing|Explicitly stated in integration summary|Assign/validate OAuth profle or confrm<br>dynamic token handling in the fow.|
|Discovery endpoint has no authentication|Explicitly stated|Confrm whether sandbox/public behavior is<br>intended and defne production equivalent.|
|Credentials in SOAP body|Explicitly shown in envelope|Confrm storage, masking, transport<br>encryption and logging controls.|
|Employee REST uses Password (2-Way)|Explicitly stated|Validate credential rotation, ACLs and<br>alias/environment separation.|
|Inactive ERPxAppFilter|Explicitly stated; functional purpose<br>presented as likely|Check references and execution history<br>before deciding whether inactive state is safe.|
|Environment mixing prohibited|Explicit Unit4 cloud rule|Enforce same-type environment mapping in<br>ServiceNow Connection Aliases.|
|Rate limiting/backof|Explicit Unit4 limits and guidance|Implement retry/backof and telemetry<br>around REST/SOAP actions.|
|Personal data exposure|Employee endpoints carry HR/identity/bank<br>felds|Apply least privilege, feld minimization and<br>safe log practices; this is an implementation<br>recommendation based on the listed felds.|



###### **Secret handling** 

This compendium contains endpoints, tenant identifiers, table names and payload structures from internal documentation. It intentionally does not reproduce unrelated personal identifiers found in the OneNote source. Treat the document as internal technical material and review access before wider distribution. 

#### **14. Migration review and consultancy services** 

|**Service**|**Scope**|**Deliverable**|
|---|---|---|
|Cloud Migration for ERP - Integrations Review<br>Service|Workshop; review up to 25 customer-<br>identifed integrations; standard-method<br>guidance; identify cloud-compliance<br>changes.|Integrations Analysis Document|



Business (TLP Green)  |  Compiled 17 August 2026  |  13 

|||UNIT4 ERP INTEGRATION COMPENDIUM|
|---|---|---|
|Cloud Migration for ERP - Integrations<br>Consultancy Service|Support adoption of review changes,<br>customer testing and migration/confguration<br>assistance.|Integration Confguration Document|



- Review Service prerequisite: recent Cloud Migration Assessment and Standard Migration Service. 

- Customer project team should include experienced project, architecture/technical and subject-matter roles. 

- Consultancy requires an Integration Review Document and access to people or documents with detailed knowledge of the integrations. 

#### **15. Gaps, contradictions and validation backlog** 

|**Gap**|**Why it matters**|
|---|---|
|Only 9 of the stated 25 transform maps are named|Field-level and transformation-script completeness cannot be<br>confrmed.|
|Flow count says 23, but the source groups several names and does<br>not expose full defnitions|Trigger tables, conditions, inputs, outputs and error handling remain<br>incomplete for many fows.|
|Inbound Scripted REST APIs lack resource/method/schema detail|Request/response JSON, version paths, ACLs and error models are not<br>available in the retrieved source.|
|Document-send action lacks endpoint and payload|The HR document integration cannot be reproduced from the retrieved<br>content alone.|
|Employee rates documentation difers between REST read and SOAP<br>contract write|Instance-level action inspection is required to distinguish scope and<br>naming.|
|PATCH sample abbreviates personalInformation|The complete country-specifc JSON payloads are not present.|
|SOAP endpoint is dynamic|Actual host/path and MID Server routing are not shown.|
|Zero Copy documentation is generic and SAP-oriented|No retrieved source explicitly confrms a Unit4 ERP content pack or<br>connection implementation.|
|Search result corpus was very large|This compendium covers all relevant content from the retrieved high-<br>confdence documents, not every loosely matching item in the search<br>index.|



#### **Appendix A. Payloads and mappings** 

##### **A.1 Employee selection mapping** 

```
{
  "full_name_fx": "customFieldGroups/hrna0102/full_name_fx",
```

```
  "id_type_fx": "customFieldGroups/cia00hr07/id_type_fx",
```

```
  "id_number_fx": "customFieldGroups/cia00hr07/id_number_fx",
```

```
  "contract_type_fx": "customFieldGroups/hrc0100/contract_type_fx",
```

```
  "bonus_type": "relatedValues[relationId=X750]/description",
```

```
  "bonus_type_code": "relatedValues[relationId=X750]/relatedValue",
  "currency": "relatedValues[relationId=A2]/description",
  "currency_iso3_code": "relatedValues[relationId=A2]/relatedValue"
}
```

Business (TLP Green)  |  Compiled 17 August 2026  |  14 

UNIT4 ERP INTEGRATION COMPENDIUM 

##### **A.2 Employee PATCH wrapper** 

```
{
```

```
  "employeeInfo": [
    {"op":"Replace","path":"customFieldGroups/hrc0116","value":{"...":"see section 6"}},
    {"op":"Replace","path":"personalInformation","value":{"...":"source abbreviated"}}
  ]
}
```

##### **A.3 Core employee API patterns** 

```
GET   {baseUrl}/objects/employees?companyId={companyId}&filter=personId eq {employeeId}
&select={select}
```

```
PATCH {baseUrl}/employees/{employeeId}?companyId={companyId}
Content-Type: application/json-patch+json
```

##### **A.4 Inbound ServiceNow API base paths** 

```
/api/u4bsh/unit4_attachments
/api/u4bsh/unit4_change_request
/api/u4bsh/ccm
/api/u4bsh/unit4_customers_emails
```

#### **Appendix B. Source register** 

|**Source fle**|**Relevant coverage**|
|---|---|
|ERP Integration Summary - until 20 of April 2026.docx|unit4dev1 architecture, endpoints, inbound APIs, fows, maps, jobs,<br>employee REST, PATCH and contract SOAP.|
|ServiceNow HR Letters 1.docx|HR fows, actions, subfows, sys_ids, inputs/outputs and document<br>integration.|
|Developments.one|Employee action input example and JSON property-path mapping.|
|Unit4 ERP CR Cloud Service Description V.2026.Q2.docx|Integration options, customisation responsibilities, API lifecycle and<br>optional services.|
|Unit4 Cloud Technical Guidelines and Limits.pdf, v2.1, July 2026|Protocols, API limits, ERP/ERPx limits, ports, replication restrictions<br>and environment rules.|
|erp-integration-framework.md|Source-to-Pay framework, records of authority, roles and MID Server<br>rule.|
|erp-integration-overview.md|Zero Copy Connector overview and learning/confguration references.|
|exploring-erp-integration.md|Remote/extraction table concepts and tool usage.|
|install-erp-integration.md|Installation, entitlement and model-modifcation property.|
|erp-integration-reference.md|Domain separation, fow action, tables/models and reference topics.|
|set-up-erp-integration-connection.md|Connection/credential prerequisites and setup fow.|
|Success Catalog - Integrations Review Service.docx|Migration review service scope and deliverable.|
|Success Catalog - Integrations Consultancy.docx|Migration consultancy scope and deliverable.|



###### **Compilation note** 

All endpoint strings, paths, JSON/XML snippets, table names, sys_ids and limits included above were taken from the retrieved internal documentation. Missing details are explicitly called out rather than invented. 

Business (TLP Green)  |  Compiled 17 August 2026  |  15 

