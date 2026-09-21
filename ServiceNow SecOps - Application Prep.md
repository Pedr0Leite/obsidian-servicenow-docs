---
tags: [servicenow, secops, job-prep]
created: 2026-09-11
---

# ServiceNow Security Operations (SecOps) — Application Prep Notes

> Compiled from the local `obsidian-servicenow-docs` vault (ServiceNowOfficialDocs/security-management) plus current web sources. Use this as a talking-points sheet for a SecOps-related application/interview.

## 1. Big picture positioning

ServiceNow Security Operations unifies security and IT workflows on one platform (single data model, shared CMDB, shared workflow engine with ITSM/ITOM) rather than the traditional siloed SOC tool stack. Pitch: "orchestration layer that turns security alerts into structured, prioritized, auditable work — using the same platform IT already runs on."

**Important 2026 positioning point:** ServiceNow is consolidating Vulnerability Response, Application Vulnerability Response (AVR), Container Vulnerability Response (CVR), and Configuration Compliance under a new **Unified Security Exposure Management (USEM)** workspace (replacing the older "Vulnerability Manager Workspace"), giving cross-domain exposure visibility (infra + app + container + config) instead of siloed views. Mention this — it signals current knowledge, not stale docs.

Core modules: **Security Incident Response (SIR)**, **Vulnerability Response (VR)**, **Threat Intelligence (Security Center)**, **Configuration Compliance**. Adjacent modules: **Data Loss Prevention (DLP) Incident Response**, **SBOM (Software Bill of Materials)**.

## 2. Security Incident Response (SIR)

- SOAR-style case management: detect → triage → respond → close, with orchestration and playbooks.
- Core table `sn_si_incident`; fields include severity/risk score (calculated, color-coded), category/subcategory, response tasks, observables (IOCs), affected users/CIs.
- Playbooks are MITRE ATT&CK-aligned (phishing, malware, credential dumping, failed login, etc.).
- **Major Security Incident Management (MSIM):** escalates a standard incident to major-incident status; auto-creates SharePoint folders + Teams channels; produces Post-Incident Review (PIR) reports.
- **SIR Workspace:** multi-tab UI, AI Search across incidents/tasks/observables, shift handover, relationship graphs, CISO dashboard with geo-heatmap.
- **Roles:** `sn_si.admin`, `sn_si.analyst`, `sn_si.manager`, `sn_si.ciso`, `sn_si.basic`.
- **Integrations:** Splunk, QRadar, ArcSight, Azure Sentinel, AWS Security Hub, CrowdStrike Falcon, Microsoft Defender/Graph, Carbon Black, Palo Alto (firewall/Wildfire/AutoFocus), McAfee, FireEye, Zscaler, Slack/Teams.
- **Now Assist for SIR (GenAI):** summarize incidents, recommend next steps, draft closure notes, generate correlation insights/resolution plans/PIR reports/shift-handover reports, agentic close/resolve workflows. Sold as SOC efficiency/time-to-triage reduction.

## 3. Threat Intelligence Security Center (TISC)

- Central workspace to ingest and operationalize threat intel: curated OSINT feed catalog + premium feeds, STIX/MISP/JSON ingestion, automated observable extraction from files.
- Enrichment/validation with confidence scoring, correlation rules engine, MITRE ATT&CK kill-chain mapping.
- Dedicated Threat Analyst workspace with an investigation canvas; Threat Case management; domain separation (useful for MSSPs).
- Feeds internal sources back in from VR, SIR, CMDB; CrowdStrike Falcon EDR real-time monitoring.
- **Roles:** `sn_sec_tisc.admin`, `sn_sec_tisc.analyst`.

## 4. Vulnerability Response (VR) family (now under USEM)

- Ingests vulnerability data (NVD + scanners: Qualys, Tenable, Rapid7, etc.), prioritizes by risk/exploitability, and drives remediation to closure via Vulnerable Items (VITs) and Vulnerability Groups.
- **Personas** (assigned via Setup Assistant): Vulnerability Admin, Vulnerability Analyst, Remediation Owner, CI Manager, Exception Manager. Granular roles (`read_all`/`write_all`/`read_assigned`/`write_assigned`) allow finer control than personas.
- **Application Vulnerability Response (AVR):** separate subscription; imports Application Vulnerable Items (AVITs); own change-management remediation flow.
- **Container Vulnerability Response (CVR):** separate subscription; imports Container Vulnerable Items (CVITs) from internal/external sources incl. NVD.
- **IT Remediation Workspace:** lets IT teams create change requests, rescan VITs, submit exception requests directly — bridges security and IT ops.
- **Now Assist for VR (GenAI):** assess exposure to critical CVEs, SLA compliance insight for vulnerable items.

## 5. Configuration Compliance (Secure Configuration Assessment)

- Ingests scan results from scanners (Qualys, Tenable.io, Prisma Cloud, Microsoft Defender for Cloud, AWS Inspector/Security Hub) and aggregates against the CMDB to find non-compliant configurations.
- **Terminology renamed in v14.9** (good "I keep current" detail): Policy → Test Group; Test Result Group → Remediation Task; Group Rules → Remediation Task Rules.
- Core objects: Policies/Test Groups (benchmarks like CIS/SCAP), Tests, Test Results (pass/fail per CI), Remediation Tasks (grouped failing results), Exceptions (risk-acceptance with approval workflow).
- Remediation routed through **Change Request** integration; auto-close rules can close resolved test results automatically.
- **Roles:** `sn_vulc.read`, `sn_vulc.write`, `sn_vulc.admin`; `itil` role needed for change requests from remediation tasks.

## 6. Data Loss Prevention (DLP) Incident Response

- Manages sensitive-data exposure incidents (financial, health, PII/SSN) surfaced by third-party DLP tools.
- Key objects: DLP Incidents, Smart Response Rules (auto-remediation), Assignment/Auto-escalation Rules, Delegation, Repeat Offender Identification, Evidence Files (quarantine/preview/download), Archiving Rules.
- **Three workspaces** (good talking point — shows multi-persona design): End User/Manager Workspace (employees acknowledge/justify/request release), Analyst/Ops Workspace (triage, assign, close, trend analysis), Dashboard (incident volume trends).
- **Integrations:** Microsoft Purview DLP, Netskope, Proofpoint, Symantec DLP, ICAP.

## 7. SBOM (Software Bill of Materials)

- Tracks open-source/third-party software components across the app portfolio; surfaces license risk and component vulnerabilities from uploaded SBOM files (CycloneDX 1.0–1.6, SPDX 2.2–2.3).
- **Three-app architecture:** (1) Data Model for SBOM — base tables/ACLs/roles; (2) SBOM Core — required, upload API + parsing + inventory workspace; (3) SBOM Response — dashboards, license administration, auto-creates Application Vulnerable Items (AVITs), integrates OSV.dev (vuln intel) + Deps.dev (stale/abandoned package detection); requires Vulnerability Response.
- Key objects: BOM Entity (root of an uploaded SBOM), Component Inventory (with transitive deps), license classification (banned/restricted/missing), Policy as Code Engine (PaCE) flags stale/abandoned components.
- **Personas:** vulnerability managers/analysts (risk exposure), lawyers/IT managers/auditors/software asset managers (license review).

## 8. Certification exam domains (useful as an interview knowledge checklist)

### CIS-VR (Certified Implementation Specialist – Vulnerability Response)
90 min, 45 questions, $450.
| Domain | Weight |
|---|---|
| VR Applications & Modules | 25% |
| Getting Data into VR (scanner integrations, enrichment) | 25% |
| Tools to Manage VR (workspaces, classification/assignment/remediation task rules, calculators) | 23% |
| Automating VR (exceptions, workflows, close-out) | 20% |
| VR Dashboards & Reports | 7% |

### CIS-SIR (Certified Implementation Specialist – Security Incident Response)
Six domains; Automation & Standard Processes is the largest at 30% (double the next domain), remaining five domains 12–15% each:
1. Security Incident Response Overview
2. Security Incident Creation and Threat Intelligence
3. Security Incident and Threat Intelligence Integrations
4. Security Incident Response Management
5. Risk Calculations and Post Incident Response
6. Security Incident Automation (30%)

Both exams assume general ServiceNow platform competence — they're specialization exams layered on top of admin/dev fundamentals, not entry points.

## 9. Talking points / differentiators to have ready

- **Single platform, single data model:** incidents, vulnerabilities, CIs, and change requests live in one system — no swivel-chair between SOC tools and ITSM.
- **CMDB-driven prioritization:** vulnerabilities/misconfigurations are scored against business-critical CI context (asset criticality), not just raw CVSS.
- **Change-managed remediation:** vulnerability/compliance remediation flows through standard Change Management, so security work is auditable and doesn't bypass IT process.
- **GenAI (Now Assist) layered across SIR/VR:** summarization, next-step recommendation, auto-drafted closure/PIR reports — pitched as SOC analyst time savings.
- **USEM consolidation (2026):** cross-domain exposure view spanning infra, app, container, and config — competitive answer to "why not just use point tools like Qualys/Tenable directly."
- **Broad integration ecosystem:** dozens of SIEM/EDR/scanner/threat-feed connectors out of the box (Splunk, QRadar, CrowdStrike, Qualys, Tenable, Microsoft Sentinel/Defender, Proofpoint, etc.).

## Sources
- [ServiceNow Security Operations Reviews — G2](https://www.g2.com/products/servicenow-security-operations/reviews)
- [ServiceNow Security Operations (SecOps): Comprehensive Guide — Reco](https://www.reco.ai/hub/servicenow-security-operations-secops)
- [Vulnerability Response Data Sheet — ServiceNow](https://www.servicenow.com/standard/resource-center/data-sheet/ds-vulnerability-response.html)
- [Security Operations Data Sheet (PDF) — ServiceNow](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/data-sheet/ds-security-operations.pdf)
- [Vulnerability Response product page — ServiceNow](https://www.servicenow.com/products/vulnerability-response.html)
- [CIS-VR certification — ServiceNow University](https://learning.servicenow.com/lxp/en/pages/now-learning-get-certified?id=amap_detail&achievement_id=588e1d77dbc27f40de3cdb85ca96192b)
- [CIS-VR Exam Syllabus — ProcessExam](https://www.processexam.com/servicenow/servicenow-cis-vr-certification-exam-syllabus)
- [CIS-SIR Exam Syllabus — ProcessExam](https://www.processexam.com/servicenow/servicenow-cis-sir-certification-exam-syllabus)
- [CIS-SIR Study Guide — iSecPrep](https://www.isecprep.com/2026/07/21/servicenow-cis-sir-security-incident-response-study-guide/)
