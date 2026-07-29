---
aliases:
  - "Describe the types of challenges you anticipate So"
area: "CTA"
source: notion-export
tags:
  - cta-program
  - case-study
  - sovereign-bank
  - governance
  - cmdb
  - exam-prep
---

# Describe the types of challenges you anticipate Sovereign Bank may encounter

multiple countries might have different GDPR rules

Remedy is highly customized, so it will be hard to implement all customizations in servicenow

The process of moving people from one platform that, with all their flows, are used to into a newer one, which is ServiceNow.

Re train people might also be challenging

Making ServiceNow as simple to use as uber or amazon while having all the previous process's.

>ITSM - Incident<

Uniformization of incident process or to implement all that existed before might be a bit confusing

A way to understand what’s an INC and what’s a CASE to improve the quality of the service

Reducing the amount of SLAs might be hard to do it

>ITSM - Problem<

>ITSM - Change<

>CMDB<

After years of multiple third party tools updating the values of CI, data quality might be compromised.

____________________________________________________________________________________

## **1. Technical Challenges**

### **a. Legacy System Complexity & Migration Risks**

- Remedy is highly customized, making data extraction, transformation, and migration **complex**.
- **Risk of data loss or inconsistency** during migration (e.g., CMDB, incidents, SLAs).
- Need to ensure **ServiceNow aligns with compliance** (GDPR, FISMA, PDPA).

### **b. CMDB & ITOM Implementation Risks**

- **CMDB data quality issues** due to years of **fragmented** asset tracking.
- Difficulties in **Discovery & Service Mapping**, given inconsistent **credentials and outdated infrastructure**.
- Need to **enforce governance** (CSDM adoption, data certification, and automation).

### **c. Security, Compliance & Data Governance**

- **Cross-border regulations** (UK GDPR, EU GDPR, FISMA, PDPA) requiring **data encryption & access control**.
- **Data segregation & residency requirements**, especially for financial regulations.
- Need for **real-time field-level encryption** without disrupting reports.

### **d. Integrations & Platform Extensibility**

- **Hybrid cloud complexity** (AWS, Azure, vCenter, private network restrictions).
- Legacy **Enterprise Service Bus (ESB) harmonization** (Tibco target state).
- **SSO authentication** (SAML, ADFS, MFA) across multiple regions.

### **e. Release & Upgrade Management**

- **Avoiding technical debt** while ensuring a **lean ServiceNow implementation**.
- Risk of **"rogue customizations"**, complicating **future upgrades**.
- Keeping pace with **ServiceNow's release cycle** (+8 weeks SLA).

---

## **2. Organizational & Cultural Challenges**

### **a. Resistance to Change**

- **"This is how we’ve always done it"** mindset, especially from **senior ITSM staff**.
- Key stakeholders (process owners, managers) may resist **standardization** of workflows.
- Escalations and roadblocks citing **"imagined regulatory requirements"**.

### **b. Business Unit Alignment & Process Standardization**

- Different **BUs have customized incident & change management processes**.
- **Standardizing SLAs and KPIs** across a global organization.
- Pushback from **Li Na (Enterprise Architect)** who believes heavy customization is needed.

### **c. Training & Adoption**

- **No instructor-led training**; reliance on **Guided Tours for end-users**.
- Staff redeployment & possible **job losses** (impacting morale).
- Ensuring **HR teams adopt case management** instead of using **email-based ticketing**.

---

## **3. Strategic & Business Challenges**

### **a. Aligning with CIO Vision vs. Business Hesitation**

- **CIO mandates cloud migration**, but business leaders are hesitant due to risk aversion.
- Project Sponsor **Zhang Wei** is **pro-change**, but needs buy-in from Albert Wan (Program Director) and others.

### **b. Measuring & Demonstrating Business Value**

- **130+ KPIs need to be rationalized**, ensuring continued **value tracking**.
- Aligning **ServiceNow metrics with business goals** (reduced incident handling time, automation benefits).
- **Justifying ROI** by demonstrating efficiency gains & cost reduction.

---

## **4. Project Execution Challenges**

### **a. Implementation Methodology & Governance**

- **Ensuring adherence to Now Create methodology** (vs. ad-hoc execution).
- Establishing **proper governance** to prevent **uncontrolled customizations**.
- Ensuring **effective decision-making frameworks** (e.g., design authority, CAB).

### **b. Phased Deployment Strategy**

- **No "big bang" release** – needs a well-planned **incremental rollout**.
- **Legacy decommissioning** after data migration to ServiceNow.
- Ensuring that **ServiceNow adoption is sustained post-go-live**.

## Related
- [[How to access a Technical Challenge]]
- [[Introducing Sovereign Bank]]
- [[Text for slides]]

- [[01 Case study]]
- [[Architectural Principles]]
- [[How governance at Sovereign Bank would apply]]
- [[CMDB & CSDM]]