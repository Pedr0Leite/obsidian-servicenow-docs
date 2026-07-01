---
aliases:
  - "06 Case Study – For PPT"
tags:
  - cta-program
  - encryption
  - scoped-apps
  - case-study
  - sovereign-bank
  - exam-prep
---

# For PPT

**Sovereign Bank: Security Architecture & Scoped Applications**

# **Slide 1: Title Slide**

- **Title:** Security Architecture & Scoped Applications for Sovereign Bank
- **Subtitle:** Balancing Security, Compliance, and Performance
- **Presented by:** [Your Name]
- **Audience:** Li Na (Enterprise Architect) & Security Architect

---

# **Slide 2: Agenda**

1. **Executive Summary** – Overview of objectives and key takeaways.
2. **Security Risks & Challenges** – Identifying key security issues at Sovereign Bank.
3. **Encryption Strategy for PII Data** – Best practices for securing sensitive data.
4. **Role-Based Decryption Model** – Ensuring controlled access and compliance.
5. **Scoped Applications – Development & Migration Strategy** – Best practices for application security.
6. **Security Best Practices for Sovereign Bank** – Recommended strategies for securing the platform.
7. **Roadmap for Implementation** – Phased approach for execution.
8. **Key Takeaways** – Summary of the most important points.
9. **Conclusion & Next Steps** – Key takeaways and action plan.

**Speaker Notes:**

“This agenda outlines our discussion today, covering Sovereign Bank’s security challenges, encryption strategies, scoped applications, and an implementation roadmap.”

---

# **Slide 3: Executive Summary**

- **Objective:** Provide guidance on **security architecture, scoped applications, and encryption strategies**.
- **Key Takeaways:**
    - Balance **security, compliance, and performance**.
    - Define **encryption policies** that meet regulatory requirements.
    - Ensure **scoped applications** are **secure, scalable, and upgrade-friendly**.

**Speaker Notes:**
“Today, we’ll discuss how Sovereign Bank can improve its security architecture while ensuring scoped applications meet business needs. We’ll also cover encryption best practices and compliance strategies.”

---

# **Slide 4: Security Risks & Challenges**

### **Key Security Challenges**

- **Encryption Issues** → Current database-level encryption disrupts integrations & reporting.
- **Regulatory Compliance** → Must align with **GDPR, FISMA, PDPA, and Privacy Act**.
- **Scoped App Security** → Need structured policies for development & migration.
- **Access Control & Role-Based Decryption** → Different countries require different encryption levels.

**Speaker Notes:**
“Sovereign Bank has strong security concerns due to past on-prem failures. We need an approach that secures data without impacting usability or reporting.”

---

# **Slide 5: Encryption Strategy for PII Data**

### **Recommended Approach**

✅ **Field-Level Encryption (FLE)** → Encrypt sensitive fields instead of entire database.

✅ **Role-Based Decryption** → Grant decryption access based on user roles & locations.

✅ **Encryption by Country** → Align encryption levels with regional compliance laws.

✅ **Automated Encryption Key Rotation** → Enhance security against breaches.

**Speaker Notes:**
“To reduce disruption, we recommend Field-Level Encryption. This ensures compliance with data privacy laws while allowing reporting and integrations to function smoothly.”

---

# **Slide 6: Role-Based Decryption Model**

### **How It Works:**

🔹 **Only authorized roles** can decrypt specific fields (e.g., HR can see salary data, but IT cannot).

🔹 **Encryption based on location** → UK data stored in UK; GDPR-compliant access rules.

🔹 **Audit logs** track decryption requests for compliance reporting.

**Speaker Notes:**
“This model ensures that only authorized personnel can view sensitive data while keeping us compliant with regional laws.”

---

# **Slide 7: Scoped Applications – Development & Migration Strategy**

### **Best Practices for Scoped Apps**

✔ **Use Scoped Applications for Custom Development** → Prevent unwanted platform-wide access.

✔ **Keep Business Logic Modular** → Allow easy upgrades without breaking dependencies.

✔ **Version-Controlled Releases** → Reduce risks in deployments.

✔ **Least Privilege Model** → Grant only necessary access rights.

**Speaker Notes:**
“Scoped applications improve security and upgradeability. By following these best practices, Sovereign Bank can standardize app development and minimize risks.”

---

# **Slide 8: Security Best Practices for Sovereign Bank**

### **Key Recommendations:**

🔒 **Enforce Multi-Factor Authentication (MFA)** → Prevent unauthorized access.

🔒 **Use Encrypted Data Stores** → Secure customer and employee data at rest.

🔒 **Monitor with Security Incident Response (SIR)** → Detect and respond to threats.

🔒 **Regular Security Audits** → Ensure ongoing compliance.

**Speaker Notes:**
“These security measures will strengthen Sovereign Bank’s defenses while maintaining system performance.”

---

# **Slide 9: Roadmap for Implementation**

### **Phased Approach:**

1️⃣ **Phase 1:** Implement **Field-Level Encryption** for high-risk data.

2️⃣ **Phase 2:** Deploy **Scoped Applications** for custom development.

3️⃣ **Phase 3:** Enable **Role-Based Decryption & Audit Logging**.

4️⃣ **Phase 4:** Standardize security policies & automation.

**Speaker Notes:**
“This phased approach ensures a smooth transition while keeping security at the core of the implementation.”

---

# **Slide 10: Key Takeaways**

### **Main Points to Remember:**

✅ **Field-Level Encryption** ensures security while maintaining integration capabilities.

✅ **Role-Based Decryption** provides controlled access while complying with regulations.

✅ **Scoped Applications** improve security, standardization, and ease of upgrades.

✅ **Security Best Practices** like MFA, monitoring, and audits protect the platform.

✅ **Phased Roadmap** ensures a structured, manageable implementation.

**Speaker Notes:**
“These key takeaways summarize our approach to security and scoped applications. By following these principles, Sovereign Bank can achieve a secure and scalable ServiceNow implementation.”

---

# **Slide 11: Conclusion & Next Steps**

✅ **Secure Data Without Disrupting Operations** → Field-Level Encryption minimizes impact.

✅ **Develop & Migrate Scoped Applications Securely** → Protect data integrity & compliance.

✅ **Standardize Security Across the Enterprise** → Implement access control, MFA, and audits.

**Speaker Notes:**
“Sovereign Bank can achieve a secure, compliant, and scalable platform by implementing these strategies. Next steps include finalizing encryption policies and beginning scoped app development.”

---

---

### **Key Factors to Consider (Covered in These Slides)**

✅ **Low-Disruption Custom Applications (Slide 7 - Scoped Applications Strategy)**

- **Solution:** Scoped applications ensure controlled, modular development, reducing the risk of uncontrolled modifications.
- **Why It Works:** This avoids repeating past failures from the on-prem IT solution while keeping applications upgrade-friendly.

✅ **CTAs Advising Internal Teams (Slide 7 - Scoped Applications Best Practices)**

- **Solution:** CTAs focus on **best practices for app development**, version control, and enforcing **least privilege access**.
- **Why It Works:** CTAs provide architectural guidance while letting Sovereign Bank’s development teams execute.

✅ **Encryption Challenges (Slide 5 & 6 - Encryption & Role-Based Decryption)**

- **Solution:** Move away from **database-level encryption** to **Field-Level Encryption (FLE)** with **role-based decryption**.
- **Why It Works:** This improves integration compatibility, ensures compliance, and **doesn't impact reporting**.

---

### **Discussion Questions (Answered in These Slides)**

1️⃣ **How do you balance choosing security tools while maintaining performance and convenience?**

✔ **Slide 5 & 6 (Encryption Strategy & Role-Based Decryption)** – Implement **FLE**, control decryption access, and avoid performance-heavy database encryption.

2️⃣ **Sovereign Bank’s business technology needs, security risks, and mitigations?**

✔ **Slide 3 (Security Risks & Challenges)** – Identifies key risks (encryption issues, compliance, scoped app security).

✔ **Slide 8 (Security Best Practices)** – Defines **MFA, Security Incident Response, and Encryption Policies** as key mitigations.

3️⃣ **The best strategy for creating & migrating scoped applications while maintaining security?**

✔ **Slide 7 (Scoped Applications Strategy)** – Scoped apps provide **controlled access, ease of upgrades, and modular development** to prevent uncontrolled modifications.

4️⃣ **How do you ensure reporting has minimal impact while encryption requirements are upheld?**

✔ **Slide 5 & 6 (Field-Level Encryption & Role-Based Decryption)** – **Encrypt only critical fields**, use **real-time decryption**, and enable **controlled reporting access**.

---

### **Final Confirmation**

✔ **All key factors & discussion points are answered.**

✔ **The slides align with Sovereign Bank’s needs.**

✔ **The approach minimizes disruption while ensuring compliance & security.**

Would you like any **refinements or deeper explanations** on any of these points? 🚀

## Related

- [[06 Case Study]]
- [[06 Week 6]]
- [[Comparing ServiceNow encryption solutions]]
- [[Scoped Application leading practices]]
- [[Alternative Encryption Products to GlideEncrypter]]