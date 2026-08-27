---
aliases:
  - "Architectural Principles"
area: "CTA"
source: notion-export
tags:
  - cta-program
  - architecture-principles
  - csdm
  - cmdb
  - governance
  - exam-prep
---

# Architectural Principles

## **1. Common Service Data Model (CSDM) Principles**

CSDM is a **framework for structuring CMDB data** in ServiceNow to ensure proper governance, data quality, and IT visibility.

### **Key CSDM Principles**

- **Data Ownership & Governance** → Ensure **CMDB data** is owned by dedicated teams and updated via **Change Management or Discovery**.
- **Separation of Concerns** → Keep **business services, technical services, and CIs distinct** to avoid data confusion.
- **Lifecycle Management** → Establish **clear processes** for creating, updating, and retiring **CIs and services**.
- **Alignment with ITOM & ITSM** → Ensure **Incident, Problem, and Change processes leverage the CMDB** effectively.
- **Data Quality & Certification** → Use **CMDB Health Dashboards** to enforce **completeness, correctness, and compliance**.

### **How to Apply This to the Case Study?**

- Sovereign Bank’s **CMDB is fragmented**, with multiple discovery tools (BMC Atrium, SCCM, etc.).
- They need a **governed CMDB aligned with CSDM**, ensuring data updates via **Discovery & Change Management**.

---

## **2. ITIL & ServiceNow Best Practices**

ITIL (IT Infrastructure Library) is a **standard framework for ITSM**, and ServiceNow incorporates **ITIL best practices** into its platform.

### **Key ITIL Principles (Relevant to ServiceNow Implementation)**

- **Standardized Incident, Problem & Change Processes** → Avoid **BU-specific customizations** that create inefficiencies.
- **Automated Ticket Handling** → Use **Agent Intelligence, Virtual Agent, and Workflow Automation**.
- **Clear Approval & Risk Models for Change Management** → Implement **CAB process enhancements & automated risk scoring**.
- **Knowledge-Centric Support** → Integrate **Knowledge Articles** into Incident and Problem workflows.
- **Service Catalog & Request Fulfillment** → Ensure **standardized service offerings** across all business units.

### **How to Apply This to the Case Study?**

- Sovereign Bank has **inconsistent incident & change processes** across divisions.
- A **single ITIL-aligned process** must be enforced using **ServiceNow’s out-of-the-box capabilities**.

---

## **3. NIST & ISO Security Frameworks**

Security frameworks help ensure **data protection, compliance, and risk management** in ServiceNow.

### **Key NIST & ISO 27001 Security Principles**

- **Zero Trust Architecture** → Enforce **least privilege access** and **role-based controls** in ServiceNow.
- **Data Encryption & Protection** → Apply **field-level encryption** for sensitive fields (e.g., SSN, PII).
- **Auditability & Compliance Tracking** → Use **Activity Logs, Change Audits, and Automated Compliance Reports**.
- **Regulatory Adherence** → Ensure alignment with **GDPR, FISMA, PDPA, and other financial industry regulations**.
- **Secure Integrations** → Use **encrypted connections, MID Servers, and multi-factor authentication**.

### **How to Apply This to the Case Study?**

- Sovereign Bank **needs to comply with GDPR, FISMA, PDPA** → ServiceNow must enforce **data segregation, encryption, and access controls**.
- **SSO & Authentication (SAML, ADFS, MFA)** must follow **ISO security best practices**.

---

## **4. ServiceNow Upgrade & Customization Best Practices**

To ensure **long-term platform health**, ServiceNow enforces **guidelines for upgrades and customizations**.

### **Key Principles for Upgrade & Customization Management**

- **Limit Customizations** → Use **ServiceNow Out-of-the-Box (OOB) features** whenever possible.
- **Adopt a Configuration-Over-Customization Approach** → Configure **Flow Designer, Business Rules, and UI Policies** instead of writing scripts.
- **Ensure Upgrade Compatibility** → Follow ServiceNow’s **biannual release cycle (+8 weeks SLA)**.
- **Governance for Custom Development** → Establish **design review boards** to approve modifications.
- **Use Scoped Applications for Extensions** → Keep custom logic isolated to **prevent future upgrade conflicts**.

### **How to Apply This to the Case Study?**

- Sovereign Bank’s **Remedy instance was highly customized, making upgrades painful (18+ months for last upgrade)**.
- **They must avoid "rogue customizations"** in ServiceNow to ensure **seamless future upgrades**.

---

## **5. ServiceNow Integration Best Practices**

Integrations must be **secure, scalable, and compliant** with **Sovereign Bank’s hybrid cloud & security requirements**.

### **Key Integration Principles**

- **Use MID Servers for Secure On-Premise Integrations** → Helps Sovereign Bank handle **private network restrictions**.
- **Follow REST/SOAP Standards** → Avoid **direct database access**; use **web services & APIs**.
- **Ensure High Availability** → Configure **fail-safe mode for MID Servers**.
- **Centralize Identity Management** → Use **SAML 2.0 & ADFS 3.0** for authentication.
- **Ensure Compliance with Data Residency Laws** → Encrypt and **store data based on regional regulatory needs**.

### **How to Apply This to the Case Study?**

- Sovereign Bank’s **hybrid network & regulatory segmentation (UK, EU, US, Asia) require strict access control**.
- They must **ensure compliance-aware integrations** with their **HR (SuccessFactors, Workday), Finance, and IT systems**.

---

# **Final Takeaway: How to Apply These Principles to Any Case Study?**

1. **Identify** the **current-state challenges** (e.g., fragmented CMDB, compliance risks, lack of automation).
2. **Compare** the **desired future state** (e.g., centralized CMDB, automated workflows, secure integrations).
3. **Validate** the best approach using **CSDM, ITIL, NIST, ISO, and ServiceNow best practices**.
4. **Check dependencies & risks** (e.g., integration conflicts, regulatory issues, business resistance).
5. **Ensure governance & sustainability** (avoid rogue customizations, align with ServiceNow’s upgrade strategy).

## Related
- [[How to access a Technical Challenge]]
- [[Describe the types of challenges you anticipate So]]
- [[02 Case study – Files]]

- [[01 Week 1]]
- [[Architect Responsibilities]]
- [[CMDB & CSDM]]
- [[ServiceNow TOGAF vs ITIL 4]]
- [[Comparing ServiceNow encryption solutions]]