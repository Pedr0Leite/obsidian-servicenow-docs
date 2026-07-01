---
title: Agentic AI security and governance
description: Now Assist AI agents operate securely within the boundaries you define. Layered controls govern who can invoke each agent, what data it can access, how interactions are monitored, and how your organization retains oversight.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/now-assist-security.html
release: australia
topic_type: concept
last_updated: "2026-04-23"
reading_time_minutes: 4
tags:
  - platform-security
  - type-concept
---

# Agentic AI security and governance

Now Assist AI agents operate securely within the boundaries you define. Layered controls govern who can invoke each agent, what data it can access, how interactions are monitored, and how your organization retains oversight.

Deploying AI agents introduces security considerations that go beyond standard platform hardening. Agents act autonomously, invoke tools, access data, and make decisions on behalf of [[users|users]]. This requires controls at every layer: who can invoke an agent, what it can access once running, how its actions are logged, and what catches harmful or unintended behavior at runtime.

Now Assist is built on the ServiceNow AI [[platsec-sublanding|Platform security]] model. AI agents are subject to the same ACL enforcement, role-based access controls, and domain separation that govern all platform activity. The controls in these sections extend that foundation with capabilities specific to agentic AI. These include [[identity-landing|identity]] classification for AI users, role masking to enforce least-privilege during tool execution, and runtime guardrails through Now Assist Guardian. Readiness assessment tools help verify your instance is prepared before agents go to production.

## AI security concepts

<table id="table_udv_5wf_d3c" class="nav-card presentation"><tbody><tr><td>

[Permissions-based [[sc-access-control|access control]]\[Omitted image "bus-why-servicenow.svg"\] Alt text:Use Agent Role Inheritance, identity types, and granular roles to verify your AI agents have only the permissions they need, and can act only within their intended boundaries.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-permissions-based-access-control.md)

</td><td>

[Data protection\[Omitted image "bus-security.svg"\] Alt text:Learn how ServiceNow tools like [[encryption|Key Management Framework]], [[field-encryption|Field Encryption]], and [[data-classification|Data Classification]] protect your data, including where it is stored and processed, and how it stays isolated when third-party agents are involved.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-data-protection.md)

</td><td>

[Agent traceability and monitoring\[Omitted image "bus-scan.svg"\] Alt text:Use AI Control Tower and agent activity [[logs|logs]] to track what your agents do, what data they access, and when, and provide the auditable, explainable records your security and compliance teams require.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-[[c_AuditedTables|auditing]]-and-monitoring.md)

</td></tr><tr><td>

[Governance and admin safeguards\[Omitted image "bus-automated-testing-framework.svg"\] Alt text:Find guidance on managing roles, [[ca-policies|policies]], and configurations to reduce risk and meet compliance requirements, including HIPAA, GDPR, and NIST.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-governance-and-admin-safeguards.md)

</td><td>

[AI threat protection\[Omitted image "bus-problem-benefit.svg"\] Alt text:Learn how Now Assist helps defend against AI-specific threats including offensive content, prompt injection, and sensitive subject detection using Now Assist Guardian.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-threat-protection.md)

</td><td>

[External AI agent security\[Omitted image "bus-community.svg"\] Alt text:Learn how to monitor and govern AI agents from external providers, with visibility into third-party data flows and assurances that sensitive data stays properly isolated across your AI ecosystem.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/naai-3rd-party-security.md)

</td></tr></tbody>
</table>## AI security products

<table id="table_bm1_dbp_w3c" class="nav-card presentation"><tbody><tr><td>

[Now Assist Guardian\[Omitted image "bus-trust-in-us.svg"\] Alt text:Now Assist Guardian is built on the ServiceNow Small Language Model \(SLM\) and monitors generative AI interactions to detect offensive content, prompt injection attacks, and sensitive topics.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/now-assist-guardian.md)

</td><td>

 

</td><td>

[AI Control Tower\[Omitted image "ind-telecom-tower.svg"\] Alt text:The AI Control Tower is a platform that connects different parts of an organization to speed up the AI adoption.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-control-tower-landing.md)

</td></tr></tbody>
</table>-   **[[naai-permissions-based-access-control|Permissions-based access control]]**  
Use Agent Role Inheritance, identity types, and granular roles to verify your AI agents have only the permissions they need, and can act only within their intended boundaries.
-   **[[naai-data-protection|Data protection]]**  
Learn how ServiceNow security tools such as the Key Management Framework, Field Encryption, and Data Classification work to keep your data secure.
-   **[[naai-auditing-and-monitoring|Agent traceability and monitoring]]**  
Learn how to use tools like AI Control Tower to track, monitor, and report on your AI assets.
-   **[[naai-governance-and-admin-safeguards|Governance and admin safeguards]]**  
Find guidance on preparing your instance for AI deployment, maintaining domain separation, and reducing risk across your Now Assist implementation.
-   **[[naai-threat-protection|AI threat protection]]**  
Learn how Now Assist helps defend against AI-specific threats including offensive content, prompt injection, and sensitive subject detection using Now Assist Guardian.
-   **[[naai-3rd-party-security|External AI agent security]]**  
Learn how to monitor and govern AI agents from external providers, with visibility into third-party data flows and assurances that sensitive data stays properly isolated across your AI ecosystem.
-   **[[now-assist-guardian|Now Assist Guardian]]**  
Now Assist Guardian is built on the ServiceNow Small Language Model \(SLM\) and monitors generative AI interactions to detect offensive content, prompt injection attacks, and sensitive topics.
-   **[[naai-tutorial-overview|Create and secure an AI agent in Now Assist]]**  
Plan, build, secure, test, and deploy a Now Assist AI agent.

## Related

- [[naai-permissions-based-access-control|Permissions-based access control]]
- [[naai-data-protection|Data protection]]
- [[naai-auditing-and-monitoring|Agent traceability and monitoring]]
- [[naai-governance-and-admin-safeguards|Governance and admin safeguards]]
- [[naai-threat-protection|AI threat protection]]
- [[naai-3rd-party-security|External AI agent security]]
- [[now-assist-guardian|Now Assist Guardian]]
- [[naai-tutorial-overview|Create and secure an AI agent in Now Assist]]
- [[users|Users]]
- [[platsec-sublanding|Platform Security]]
- [[identity-landing|Identity]]
- [[sc-access-control|Access control]]
- [[encryption|Key Management Framework]]
- [[field-encryption|Field Encryption]]
- [[data-classification|Data Classification]]
- [[logs|Logs]]
- [[c_AuditedTables|Auditing]]
- [[ca-policies|Policies]]
