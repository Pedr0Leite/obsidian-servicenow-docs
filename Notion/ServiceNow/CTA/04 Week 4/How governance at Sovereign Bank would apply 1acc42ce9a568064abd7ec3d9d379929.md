---
aliases:
  - "How governance at Sovereign Bank would apply"
area: "CTA"
source: notion-export
tags:
  - cta-program
  - governance
  - case-study
  - sovereign-bank
  - exam-prep
---

# How governance at Sovereign Bank would apply

Absolutely! Here’s how governance at Sovereign Bank would apply to each principle with concrete examples of **decisions, stakeholders, and decision-making processes**:

---

### **1️⃣ Drive Your Transformation Vision**

**Example:** **Aligning ServiceNow investment with strategy by defining platform governance early**

- **Decision to be made & timing:**
    - Decision: Standardize **configuration vs. customization** to align with long-term scalability.
    - Timing: Before major implementations begin (pre-ITSM rollout).
- **Who is involved in decision-making?**
    - **Technical Governance Board** (Enterprise Architect, Platform Owner, IT Operations).
    - **Business Leaders** (Risk & Compliance, Service Owners).
- **How decisions are made?**
    - Governance Board **establishes guardrails** (e.g., “no new scripting unless business case justifies it”).
    - **Approval process:**
        - If a customization request arises, a **review panel assesses** whether it aligns with the transformation roadmap.
        - If approved, it follows a **controlled release process** with documentation and rollback plans.

---

### **2️⃣ Deliver the Right Work at the Right Time**

**Example:** **Prioritizing ITSM rollout before ITOM to ensure process maturity**

- **Decision to be made & timing:**
    - Decision: Implement **ITSM (incident, problem, change) first**, then move to ITOM (discovery, automation).
    - Timing: During the roadmap planning phase (before implementation sprints begin).
- **Who is involved in decision-making?**
    - **Enterprise Architect (Li Na)** – ensures the phased approach aligns with architecture principles.
    - **ServiceNow Product Owner (Albert Wan)** – prioritizes based on business urgency.
    - **ITSM & ITOM Process Owners** – validate dependencies and readiness.
- **How decisions are made?**
    - **Governance Board reviews dependencies** (e.g., ITOM requires a solid CMDB, which ITSM helps establish).
    - **Risk assessment & backlog prioritization:**
        - If **ITOM launches too early**, it may result in poor discovery data due to an immature CMDB.
        - Decision is **documented in the release plan**, and only when ITSM adoption is stable does ITOM proceed.

---

### **3️⃣ Maintain the Integrity of Your ServiceNow Implementation**

**Example:** **Enforcing strict instance governance to prevent unauthorized changes**

- **Decision to be made & timing:**
    - Decision: Define **instance strategy** (Dev, Test, UAT, Production) and control **who can modify production**.
    - Timing: Before development begins and continuously enforced.
- **Who is involved in decision-making?**
    - **Platform Owner (Albert Wan)** – owns the instance management process.
    - **Change Advisory Board (CAB)** – approves production changes.
    - **Security & Compliance Teams** – ensure changes comply with financial regulations.
- **How decisions are made?**
    - **Strict governance policy:**
        - No **direct changes in production** – all changes go through **Dev → Test → UAT → Production**.
        - **CAB reviews major changes** (custom workflows, integrations) to ensure they follow best practices.
    - If a change **violates** governance (e.g., direct modification of a core table in production), it is **rejected** and must go through the proper deployment pipeline.

---

### **Summary of Governance in Action at Sovereign Bank**

| Governance Principle | Decision & Timing | Stakeholders | Decision-Making Process |
| --- | --- | --- | --- |
| **Drive Your Transformation Vision** | Standardize **configuration vs. customization** (before implementation) | Governance Board, Business Leaders | Establish platform guardrails, review customization requests |
| **Deliver the Right Work at the Right Time** | Implement **ITSM first**, ITOM later (during roadmap planning) | Enterprise Architect, Product Owner, Process Owners | Review dependencies, assess risks, adjust backlog prioritization |
| **Maintain the Integrity of Your Implementation** | Define **instance governance & change controls** (before development starts) | Platform Owner, CAB, Security Team | Enforce **no direct production changes**, CAB approval for major changes |

---

This approach ensures Sovereign Bank’s **ServiceNow governance remains structured, scalable, and aligned with business goals.** Would you like to integrate this into your slides? 🚀

## Related
- [[Describe the types of challenges you anticipate So]]
- [[Text for slides]]
- [[01 Case study – For PPT]]

- [[04 Week 4]]
- [[04 Case Study]]
- [[Points to prevent burnout]]
- [[Architectural Principles]]