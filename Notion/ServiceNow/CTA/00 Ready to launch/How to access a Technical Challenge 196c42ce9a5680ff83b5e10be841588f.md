---
aliases:
  - "How to access a Technical Challenge"
tags:
  - cta-program
  - case-study
  - sovereign-bank
  - exam-prep
  - cmdb
  - csdm
---

# How to access a Technical Challenge

# **1. Understanding the High-Level Business & IT Goals**

### **What to Look For in the Case Study?**

- **Why is Sovereign Bank moving to ServiceNow?** → Business drivers, pain points, and objectives.
- **What are the main outcomes expected?** → CMDB, automation, security, compliance, omnichannel support, etc.
- **What legacy systems exist today?** → **Remedy (ITSM), SAP SuccessFactors, Workday, SCCM, BMC Atrium, Tibco, etc.**
- **What platforms & integrations are involved?** → Cloud, on-premise, data security, identity management, etc.

### **How to Derive Technical Challenges?**

- Compare **current-state technologies** with **desired-state goals** to identify **gaps**.
- Check for **dependencies** that may introduce **risks, complexity, or integration issues**.
- Identify **bottlenecks or outdated systems** that **block modernization**.

---

# **2. Deep Dive into Key Technical Areas**

## **A. Data & CMDB Challenges**

### **What to Look For?**

- **Current CMDB state**: "Using a customized Remedy that holds CIs, updated through internal systems."
- **Issues with existing data**: "Fragmented asset tracking, reliance on spreadsheets, home-grown databases."
- **Desired future state**: "Centralized CMDB using Discovery and Change Management."

### **How to Identify Challenges?**

- **Data accuracy & consistency**: Multiple sources, **conflicting records**, or **missing dependencies**.
- **Data ingestion & reconciliation**: Can all tools integrate seamlessly into ServiceNow CMDB?
- **Governance model**: Who has control over **CI updates**? (e.g., "Only Config Team can edit CIs").
- **CSDM alignment**: Are there clear **data ownership and lifecycle processes**?

---

## **B. Security, Compliance & Data Governance Challenges**

### **What to Look For?**

- **Regulatory requirements**: "GDPR, FISMA, PDPA, UK Data Protection rules."
- **Data encryption requirements**: "PII fields must be encrypted per region."
- **Access controls**: "Segregation of data based on user roles and geographic location."

### **How to Identify Challenges?**

- **Can ServiceNow meet encryption needs?** Does the platform support **field-level encryption** while keeping data reportable?
- **Access control challenges**: Does Sovereign Bank need a **data residency** solution for different countries?
- **Compliance auditing requirements**: Does ServiceNow provide **audit logs & tracking** that meet external regulations?

---

## **C. ITOM (Discovery & Service Mapping) Challenges**

### **What to Look For?**

- **Existing Discovery tools**: "BMC Atrium for Asset Discovery, SCCM for desktops/laptops."
- **Challenges mentioned**: "Credentials are often a challenge for Unix discovery."
- **Desired outcome**: "Replace BMC Atrium with ServiceNow Discovery."

### **How to Identify Challenges?**

- **Credential management issues**: Some Unix-based systems require **privileged credentials**, which may be difficult to obtain.
- **Service Mapping gaps**: "Managing services via spreadsheets/home-grown tools leads to inaccuracies."
- **Integration complexity**: Are there **hybrid cloud challenges** (AWS, Azure, private data centers)?

---

## **D. Integrations & Platform Extensibility Challenges**

### **What to Look For?**

- **Current integration landscape**: "Multiple Enterprise Service Buses (ESBs), legacy systems, firewall restrictions."
- **Authentication setup**: "ServiceNow must integrate with SAML 2.0, ADFS 3.0, and MFA."
- **Security concerns**: "MID Servers must operate in a fail-safe mode in all environments."

### **How to Identify Challenges?**

- **Network segmentation issues**: Will ServiceNow have **direct access** to legacy on-premise applications?
- **Integration performance risks**: Is the **Tibco ESB harmonization project** a dependency for ServiceNow’s success?
- **Authentication & SSO issues**: Can the **SAML 2.0 & ADFS 3.0 setup** work across different geographies?

---

## **E. Upgrade & Release Management Challenges**

### **What to Look For?**

- **Current state**: "Last Remedy upgrade took **18 months**, with extensive customizations."
- **Desired future state**: "Ease of upgrade (ServiceNow release + 8 weeks)."

### **How to Identify Challenges?**

- **Customizations in Remedy**: Do they contain **hard-coded business logic** that will be difficult to replace?
- **Rogue customizations risk**: Will users attempt to **customize ServiceNow** beyond best practices?
- **Upgrade strategy**: Can Sovereign Bank align with **ServiceNow’s biannual release cycle** without disruptions?

---

# **3. Validating Challenges with Stakeholders & Architecture Best Practices**

### **Who to Focus On?**

- **Zhang Wei (Project Sponsor)** → Focused on high-level transformation goals.
- **Albert Wan (Program Director)** → Drives governance & business requirements.
- **Li Na (Enterprise Architect)** → May push for customizations, affecting governance.
- **Suzi Matsui (Lead Architect)** → Your main point of contact for best practices.

### **How to Validate a Challenge?**

1. **Confirm with architecture frameworks**:
    - **CSDM alignment** for CMDB challenges.
    - **NIST & ISO security principles** for compliance concerns.
    - **ServiceNow Upgrade Best Practices** for release planning.
2. **Cross-check with platform capabilities**:
    - Does ServiceNow **natively support the requirement**, or does it need **custom development**?
3. **Assess feasibility & risk**:
    - **Can the challenge be mitigated?** → What are the best approaches?
    - **Does it require major change management efforts?**

---

# **Conclusion: How to Develop Your Own Architectural Insights**

By **systematically assessing** technical areas like **CMDB, security, ITOM, integrations, and upgrades**, you can **identify challenges based on case study details**. Here’s a **quick method to remember** when analyzing future case studies:

1. **Extract** key details from the case study (current state, desired state).
2. **Compare** with ServiceNow capabilities & best practices.
3. **Identify gaps** in data quality, integrations, security, or governance.
4. **Validate with architecture principles** (CSDM, NIST, ITIL, ServiceNow best practices).
5. **Assess risks & dependencies**, ensuring feasibility.

## Related

- [[00 Ready to launch]]
- [[Introducing Sovereign Bank]]
- [[Architectural Principles]]
- [[CMDB & CSDM]]
- [[ServiceNow TOGAF vs ITIL 4]]