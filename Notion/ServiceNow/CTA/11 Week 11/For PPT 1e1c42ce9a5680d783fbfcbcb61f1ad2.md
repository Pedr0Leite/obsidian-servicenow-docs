---
aliases:
  - "11 Week 11 – For PPT"
area: "CTA"
source: notion-export
tags:
  - cta-program
  - week-11
  - testing-leading-practices
  - performance-optimization
  - go-live
  - case-study
---

# For PPT

**Slide 1: Title Slide**

**Title:** Week 11 – Testing Leading Practices, Performance Optimization & Go-Live Readiness

**Subtitle:** Sovereign Bank Case Study – Certified Technical Architect Program

**Presented to:** Albert Wan (Platform Owner) and Test Manager

---

**Slide 2: Recap & Objective**

**Last Week:** We outlined a PAD use case and defined a governance model for citizen developers with analytics designed from the start.

**This Week’s Objective:**

- Develop a contextual test strategy across the full SDLC.
- Recommend performance optimization tactics.
- Define go-live and hypercare planning.
- Build confidence across the business for a stable launch.

---

**Slide 3: When to Start Testing Planning**

**Answer:** Start **test planning during sprint 0**, not after development.

- Define **testing requirements with user stories**.
- Involve business testers early for **user acceptance clarity**.
- Identify test data, environments, roles, and testers before development finishes.

**Early planning reduces last-minute surprises and missed coverage.**

---

**Slide 4: Key Testing Types for Sovereign Bank**

- **Unit Testing** (by developers for logic accuracy)
- **Regression Testing** (automated with ATF across all releases)
- **User Acceptance Testing (UAT)** (manual testing with business users)
- **Performance Testing** (simulate concurrent usage)
- **Integration Testing** (ensure external system stability)

Use **Automated Test Framework (ATF)** and integrate testing into **Agile Development & Test** application to manage execution.

---

**Slide 5: Performance Optimization Best Practices**

- **Script Health Reviews:** Eliminate long-running or synchronous scripts.
- **Limit GlideRecord usage in client scripts**.
- **Index heavily queried fields** to reduce query time.
- **Remove unnecessary DOM manipulations** from portals and workspaces.
- **Asynchronous execution:** Use Scheduled Jobs and Event Queue.
- **Application Performance Profiler:** Use to identify slow transactions.

**Real-World Example:** HR instance performance dropped due to excessive client-side scripting and hardcoded ACLs – refactored to business rules + async processing.

---

**Slide 6: Prototype Test Plan – Key Components**

- **Pre-Sprint:** Define test strategy, test data, and coverage matrix.
- **Sprint-Based Testing:** Include ATF test creation and unit tests.
- **Post-Development:** UAT for each module with business leads.
- **Pre-Go-Live:** Regression and performance testing.
- **Post-Go-Live (Hypercare):** Daily defect tracking and patch validations.

**Include checkpoints for HR, ITSM, CSM modules.**

---

**Slide 7: Go-Live Communication & Implementation Plan**

- **Communication:**
    - Release notes to users with impact, benefits, contact points.
    - Pre-launch webinars for process walkthroughs.
    - Stakeholder updates for status tracking.
- **Implementation:**
    - Code freeze + smoke testing 48h pre-go-live.
    - Early access for pilot users.
    - On-call support during release window.

---

**Slide 8: Mitigation & Hypercare Plans**

**Mitigation Plan:**

- Define rollback strategy (update sets, clone snapshots).
- Plan for selective hotfix deployments post-release.

**Hypercare Support:**

- 2-week monitoring period.
- Daily standups with tech & business leads.
- Dedicated incident triage channel.
- Post-deployment review on week 3.

---

**Slide 9: Connecting to Core Business Needs**

- **Remedy Issues:** 18-month delays due to poor planning – avoided with agile, iterative testing.
- **Performance Concerns:** Resolved with profiling, scripting limits, async handling.
- **Customization Impact:** Rollbacks, performance testing, and scoped development mitigate upgrade risks.
- **Business Confidence:** Early testing, live communications, and rapid response build trust.

**This isn’t just technical prep – it’s business continuity planning.**

---

**Slide 10: Final Recommendation & Next Steps**

- Adopt agile-integrated testing with ATF and Agile Dev module.
- Execute targeted performance optimization on high-risk apps (e.g. HR).
- Establish clear go-live roles, fallback procedures, and hypercare checkpoints.
- Ensure continuous stakeholder communication and real-time support.

**With these steps, Sovereign Bank can confidently move to production with reduced risk and improved business engagement.**

## Related
- [[How to access a Technical Challenge]]
- [[Introducing Sovereign Bank]]
- [[Meet the team at Sovereign Bank]]
- [[11 Week 11]]
- [[11 Week 11 – Files]]
- [[Other relevant information]]