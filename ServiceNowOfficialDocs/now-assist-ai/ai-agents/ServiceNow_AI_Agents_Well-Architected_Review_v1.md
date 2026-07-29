# ServiceNow AI Agent Well-Architected Review

> Literal Markdown transformation of `ServiceNow_AI_Agents_Well-Architected_Review_v1.pdf`. Source links and page context are preserved where available from the PDF.

---

<!-- page_1 -->
## Page 1

![Extracted image from page 1](ServiceNow_AI_Agents_Well-Architected_Review_v1_assets/ServiceNow_AI_Agents_Well-Architected_Review_v1_page_1_image_1.png)

ServiceNow AI Agent
Well-Architected
Review

A Framework for Production-Ready Agentic Use
Cases

---

<!-- page_2 -->
## Page 2

Author: TJ Lincoln
www.servicenow.com

© 2026 ServiceNow, Inc. All rights reserved. ServiceNow, the ServiceNow logo, and other ServiceNow marks are
trademarks and/or registered trademarks of ServiceNow, Inc. in the United States and/or other countries. Other
company names, product names, and logos may be trademarks of the respective companies with which they are
associated.

                                                                                              2

**Links on this page:**

- [Author: TJ Lincoln www.servicenow.com](http://www.servicenow.com/)

---

<!-- page_3 -->
## Page 3

Table of Contents
Table of Contents ..................................................................................................................................................................................................... 3

Version History ........................................................................................................................................................................................................... 5

Acknowledgements ................................................................................................................................................................................................. 5

Executive Summary ................................................................................................................................................................................................. 6

  Who Should Use This Framework ............................................................................................................................................................... 6

  How to Use This Framework .......................................................................................................................................................................... 6

Pillar 1: Agent Design & Architecture ................................................................................................................................................................. 7

  Overview ................................................................................................................................................................................................................. 7

   Design Principles ................................................................................................................................................................................................. 7

  Assessment Questions .................................................................................................................................................................................... 8

   Leading Practices ............................................................................................................................................................................................. 10

  Common Pitfalls ................................................................................................................................................................................................ 14

Pillar 2: Security & Compliance ......................................................................................................................................................................... 15

  Overview ............................................................................................................................................................................................................... 15

   Design Principles ............................................................................................................................................................................................... 15

  Assessment Questions ................................................................................................................................................................................... 17

   Leading Practices ............................................................................................................................................................................................ 20

  Common Pitfalls ............................................................................................................................................................................................... 24

Pillar 3: Reliability .................................................................................................................................................................................................... 24

  Overview .............................................................................................................................................................................................................. 24

   Design Principles .............................................................................................................................................................................................. 24

  Assessment Questions ................................................................................................................................................................................. 25

   Leading Practices ............................................................................................................................................................................................. 27

  Common Pitfalls ................................................................................................................................................................................................ 31

   Technical Reference ....................................................................................................................................................................................... 31

Pillar 4: Operational Excellence ........................................................................................................................................................................ 31

  Overview ............................................................................................................................................................................................................... 31

   Design Principles ............................................................................................................................................................................................... 31

  Assessment Questions ................................................................................................................................................................................. 33

   Leading Practices ............................................................................................................................................................................................ 35

  Common Pitfalls ............................................................................................................................................................................................... 36

Pillar 5: Cost Optimization & Value Measurement ................................................................................................................................... 37

  Overview ............................................................................................................................................................................................................... 37

   Design Principles ............................................................................................................................................................................................... 37

                                                                                        3

---

<!-- page_4 -->
## Page 4

Assessment Questions ................................................................................................................................................................................. 38

   Leading Practices ............................................................................................................................................................................................ 40

  Common Pitfalls ............................................................................................................................................................................................... 43

Pillar 6: User Experience ..................................................................................................................................................................................... 44

  Overview .............................................................................................................................................................................................................. 44

   Design Principles .............................................................................................................................................................................................. 44

  Assessment Questions ................................................................................................................................................................................. 44

   Leading Practices ............................................................................................................................................................................................ 46

  Common Pitfalls ............................................................................................................................................................................................... 48

Running and Scoring the Framework Assessment ................................................................................................................................ 48

Appendix A: Assessment & Scoring Guide ................................................................................................................................................. 51

   Design Principles and Leading Practices ............................................................................................................................................... 51

  Recommended Frequency .......................................................................................................................................................................... 51

  How to Score Questions ................................................................................................................................................................................ 51

   Calculating Your Score .................................................................................................................................................................................. 52

   Maturity Levels .................................................................................................................................................................................................. 53

   Critical Pillar Requirements ......................................................................................................................................................................... 53

Appendix B: Further Reading & Resources ................................................................................................................................................ 55

  ServiceNow Resources ................................................................................................................................................................................. 55

  ServiceNow Community Articles .............................................................................................................................................................. 55

   Contact & Support ........................................................................................................................................................................................... 56

                                                                                 4

---

<!-- page_5 -->
## Page 5

Version History

 Version                          Date                            Notes

 1.0                                       April 2026                                     Initial Release

Acknowledgements

This whitepaper would not be possible without the valuable contributions of the following people at ServiceNow:
Christian Pecora, Natalia Heel, and Vyoma Gajjar

                                                                                      5

---

<!-- page_6 -->
## Page 6

Executive Summary

ServiceNow AI Agents represent autonomous digital workers that intelligently orchestrate workflows, skills, and
actions across the enterprise. As organizations deploy agents to handle increasingly complex business
processes, architectural excellence becomes critical for realizing value while managing risk.

This Well-Architected Review provides a structured methodology for designing, deploying, and operating
ServiceNow AI Agents that deliver measurable business value while maintaining security, reliability, and
governance standards. The framework consists of six interconnected pillars covering:

       1.   Agent Design & Architecture
     2.   Security & Compliance
     3.   Reliability
     4.  Operational Excellence
     5.  Cost Optimization
     6.  User Experience

Each pillar includes leading practices, assessment questions, and implementation guidance.

Unlike generic AI best practices, this framework is grounded in ServiceNow-specific capabilities including:

     •     AI Agent Studio: Natural language development environment for AI Agents
     •     AI Control Tower: Centralized governance and monitoring
     •     AI Agent Fabric: External integration backbone using MCP and A2A protocols
     •     Agentic Evaluations: Pre-production quality validation
     •     AI Value Framework: Proven methodology for measuring business impact

Who Should Use This Framework
     •    ServiceNow architects and platform owners
     •    AI/ML engineers building agents
     •     AI Stewards facilitating governance between Innovation, Legal, Security, Risk, and Compliance teams
     •     Security teams implementing AI governance
     •     Business leaders responsible for AI strategy
     •     Operations teams managing agent deployments

How to Use This Framework

Pre-Development: Familiarize yourself with the pillars within the framework to ensure that post-development
remediation activities are kept to a minimum.

Initial Assessment: The assessment should be completed for each workflow ahead of launching it. Review each
pillar for a specific workflow or use case. Answer assessment questions honestly by checking all boxes that apply
or marking YES/NO/N/A. Calculate your score and identify gaps.

Prioritization: Focus on lowest-scoring pillars first and then balance quick wins against systemic improvements
required for launching the AI Agent or Agentic Workflow.

                                                                                       6

---

<!-- page_7 -->
## Page 7

Reevaluate: Reassess until your workflow or use case is production ready.

Periodic Reviews: Reassess when changes are made for continuous optimization and governance monitoring.

  Automated Scoring Available
   This framework is available as an interactive scoring tool that automates the assessment process –
   eliminating manual calculation, surfacing gaps in real time, and generating a scored results report aligned to
    this framework. To access the tool or request a guided AI Agent Well-Architected Review for your
   organization, contact your ServiceNow Account Team or Impact Team.

Note: Complete scoring instructions, including calculation methodology and maturity levels, can be found in
Appendix A: Assessment & Scoring Guide.

Pillar 1: Agent Design & Architecture

Overview

Well-designed agents follow clear architectural patterns including building AI Agents that have a single
responsibility, are modular, appropriately complex, and contain structured integration with other agents and
systems.

Design Principles

Single Responsibility & Specialization

Each agent should have one clearly defined purpose and scope. Build specialized agents rather than generalist
agents, similar to how a human team has distinct roles with specific expertise.

Modularity and Reusability

Design agents to be composable and assignable to different agentic workflows when practical. Smaller, focused
agents enable greater flexibility, easier troubleshooting, and reusability across multiple workflows.

Appropriate Complexity & Tool Limits

Keep agents at or below 15 tools when possible. This performance threshold represents the point where
orchestration complexity and tool selection reliability begin to degrade. Create separate specialized agents when
complexity exceeds this guideline.

Structured Prompting & Clear Instructions

Role definitions should specify the agent’s persona, expertise domain, and guardrails. Instructions should provide
step-by-step actions using Markdown formatting, with numbered steps (1., 1.1., 2.) for sequential actions and
headers (#, ## or ### etc.) for organizational structure.

                                                                                                   7

---

<!-- page_8 -->
## Page 8

Platform-Powered Tool Processing

Design tools that leverage ServiceNow platform capabilities (Flow Designer, scripts) to pre-process, filter, and
analyze data before returning results to agents. Rather than passing raw data that forces agents to perform
complex analysis, use the platform's deterministic processing to return decision-ready outputs. This reduces LLM
token consumption, improves reliability, and offloads heavy computational work to the platform layer.

Knowledge Management for RAG Retrieval

When agents use grounded prompts leveraging Retrieval Augmented Generation (RAG) to fetch Knowledge Base
articles or other external unstructured documents, article quality directly impacts agent accuracy. Well-structured
KB articles improve retrieval precision, reduce hallucinations, and enhance AI Agent answer quality.

AI Agent Fabric Integration Architecture

Leverage Model Context Protocol (MCP) for external tool and data access and use Agent2Agent (A2A) protocol for
communication between ServiceNow and third-party agents. Agents can function as either primary orchestrators
or secondary participants when invoked in multi-agent workflows.

Orchestrator-Based Coordination

The AI Agent Orchestrator uses Chain-of-Thought reasoning with the ReAct framework. The orchestrator provides
shared memory across agent teams and coordinates multi-agent collaboration for complex workflows. Avoid
including system-level prompts (e.g., “think step-by-step”) during prompt engineering, as they are already built
into the orchestrator.

Assessment Questions

Design & Structure

Q1: How do you ensure agent architecture follows design best practices? (Select all that apply)

     •   ☐ Each agent has clearly documented purpose distinguishing it from other agents
     •   ☐ Agents kept at 15 tools or fewer unless performance testing justifies higher count
     •   ☐ Multiple prompt versions maintained in AI Agent Studio for experimentation/rollback
     •   ☐ Tools organized strategically in multi-agent workflows (by data domain, workflow phase, or shared
       dependencies)

Q2: How do you structure agent instructions for optimal orchestrator performance? (Select all that apply)

     •   ☐ Instructions use numbered sequential steps with clear validation gates (If/Then logic)
     •   ☐ Specific fallback actions defined for failure scenarios (not “handle appropriately”)
     •   ☐ Prompts written in second-person imperative with specific context
     •   ☐ Agents reference ServiceNow tables/fields correctly using tools for data operations
     •   ☐ Subject matter experts validated agent logic follows business rules

Q3: How do you design tools for clarity and orchestrator alignment? (Select all that apply)

                                                                                    8

---

<!-- page_9 -->
## Page 9

•   ☐ Tool names are descriptive and unique (not “Tool 1” or conflicting with orchestrator tools)
     •   ☐ Tool descriptions clearly explain inputs, outputs, and when each tool should be used
     •   ☐ Common tools available to each agent without requiring handoffs to other agents
     •   ☐ Tools use platform processing (Flow/Script) to return decision-ready outputs rather than raw data
         requiring agent analysis

Q4: AI Agents are non-deterministic. Are you minimizing probabilistic behavior by adding deterministic tools to
your AI Agent and consolidating tools that are dependent upon each other (e.g., subflow A, B, and C always run in
order and the output is sent from the first to the second etc.)?

     •   ☐ YES - ☐ NO - ☐ N/A

Knowledge Management for RAG

Note: If your workflow does not use a Search Retrieval Tool (e.g., Search the Knowledge Base or Search Similar
Records), mark all questions 5-8 as N/A.

Q5: Have you identified the critical Knowledge Base articles for your use case?

     •   ☐ YES - ☐ NO - ☐ N/A

Q6: Have you tested agent retrieval effectiveness using a golden dataset of common user queries to quantify
retrievability?

     •   ☐ YES - ☐ NO - ☐ N/A

Q7: Are you monitoring knowledge gaps through Knowledge Center (in Zurich Patch 4 and newer)?

     •   ☐ YES - ☐ NO - ☐ N/A

Q8: For agents using a search retriever, have you limited retrieval to high-quality, optimized KB articles only (as
applicable when article curation is a work-in-progress)?

     •   ☐ YES - ☐ NO - ☐ N/A

Foundational KB Practices

Note: If you answered YES to questions 5-8 above, you may mark Question 9 as N/A. This question provides
foundational practices for teams still building KB maturity.

Q9: How do you structure Knowledge Base articles for agent retrieval? (Select all that apply)

     •   ☐ KB articles follow structured format with clear H1 titles, H2/H3 headings, opening summaries
     •   ☐ KB articles optimized with front-loaded key terms, error codes, product names

                                                                                       9

---

<!-- page_10 -->
## Page 10

•   ☐ KB articles are atomic and focused (one article = one problem/solution)
     •   ☐ Stale or duplicate KB content regularly reviewed and retired
     •   ☐ N/A - Not using Search Retrieval Tool or answered YES to Q5-8

Integration Architecture

Note: If your workflow does not use external agents via A2A protocol OR MCP servers for external tools/data, mark
questions 10-11 as N/A. Question 12 applies to all workflows.

Q10: How do you integrate with external agents and systems? (Select all that apply)

     •   ☐ External integrations use AI Agent Fabric with MCP or A2A protocols (not custom point-to-point)
     •   ☐ Agent-to-agent and/or MCP communication clearly documented in agentic workflow / AI Agent
         respectively
     •   ☐ N/A – A2A and MCP not in use for this use case

Q11: Do Agents leverage Workflow Data Fabric for unified data access?

     •   ☐ YES - ☐ NO - ☐ N/A – Workflow Data Fabric not applicable

Q12: Are platform-native capabilities used where available (Integration Hub, Workflow Studio, Record Operations)?

     •   ☐ YES - ☐ NO - ☐ N/A

Leading Practices

Agent Design & Structure (Questions 1-3)

Agent Composition Patterns

Build specialized agents with specific expertise – think of a software team with separate workers for frontend,
backend, and QA rather than one generalist developer. Design agents for reusability so a single agent can be
used across multiple agentic workflows. Document agent personas clearly (e.g., IT security expert, ServiceNow
resolution specialist) and keep within the 15-tool limit per agent for optimal performance.

Multi-Agent Tool Organization

When designing workflows with multiple coordinated agents, organize AI Agents and their tools strategically to
optimize orchestration efficiency:

       1.  Group by data domain: Keep tools operating on the same record type together (incident tools in one
         agent, KB tools in another) for clearer agent specialization and easier troubleshooting.
     2.  Group by workflow phase: Organize tools by process stage (diagnostic tools vs resolution tools) to match
        agent handoff patterns and sequential execution flow.
     3.  Minimize context passing: Keep tools sharing inputs/outputs together within the same agent to reduce
       overhead of passing data between agents in multi-agent orchestrations.

                                                                                                   10

---

<!-- page_11 -->
## Page 11

Memory & Data Flow

Use memory to reference earlier tool outputs (e.g., “Step 1: Get Incident Description… Step 5: Rewrite the Incident
description…”) and pass context between agents in agentic workflows without repeating data fetches. Enable
long-term memory via AI Agent data access settings for cross-session retention, which reduces redundant tool
calls and improves efficiency.

Version Control & Experimentation

Maintain multiple versions of agent prompts in AI Agent Studio and test variations to optimize performance and
accuracy. Roll back to previous versions if changes degrade results, and document what changed between
versions and why.

Testing & Iteration

Use AI Agent Studio testing playground with Decision Log analysis to review the Activity tab and replay past
executions for understanding agent reasoning. Test with realistic data and scenarios beyond just happy paths,
starting with 5-10 test records in sub-production before promoting to production. Use Now Assist to generate initial
prompts, then refine them iteratively.

For comprehensive pre-production validation, use Agentic Evaluations to assess Tool Choice Accuracy and Tool
Calling Correctness at scale across test scenarios – discussed in greater detail in Pillar 4 (Operational Excellence).

Prompt Structure & Formatting

Use Markdown formatting with # for sections, ## for subsections, and bold for key terms. Number sequential
steps (1., 1.1., 2., 2.1.) for ordered actions and use bullet points (-) for non-sequential lists. Write from a second-
person point of view using imperative verbs such as “Analyze,” “Retrieve,” and “Validate.”

Clear Instructions & Context

Provide specific instructions rather than vague directives (e.g., “If error found, send notification to service desk
manager” instead of “Handle issue appropriately”). Include validation gates such as “Do NOT proceed until task
details are collected,” and use If/Then conditional logic for branching (e.g., “If similar tasks OR knowledge articles
present: [actions]. If NOT present: [fallback]”). Explicitly state when steps should end execution by specifying
“Finish execution with Observation as: [message].”

Tool Design & Usage

Name tools descriptively (e.g., “Get Similar Tasks” rather than “Tool 1”) and avoid names that conflict with internal
orchestrator tools such as Organize_general_knowledge, Math, Fallback, Finish, Join, Generate_content,
Check_with_other_agents, and Communicator_agent. Include tool descriptions that explain when and why to use
each tool (e.g., “This tool fetches tasks similar to a given type. You will be passed table and record number as
inputs”). Describe the purpose of inputs in tool descriptions to strengthen the orchestrator’s understanding, state
mandatory inputs and outputs explicitly, and use tools for data filtering and manipulation instead of relying on
prompts.

Smart Tool Design: Platform Pre-Processing

Design tools that perform data processing, filtering, and analysis within the platform layer before returning results
to agents. Instead of passing raw datasets requiring agent analysis, use Flow Designer or Script logic to pre-
process data and return structured, decision-ready outputs.

                                                                                                                                        11

---

<!-- page_12 -->
## Page 12

As an example, rather than returning 1,000 incident records for agent analysis, use Flow logic to filter by
priority/SLA status, score criticality, and return top 10 actionable incidents with recommended next steps.

Structure tool outputs with clear fields like recommended_action, confidence_score, critical_items, and
next_steps so agents receive intelligence rather than raw data.

This approach reduces token consumption, leverages the platform's deterministic capabilities for complex
calculations, and improves agent reliability by offloading analytical work to the platform.

Tool Distribution: Duplication vs Centralization

When designing multi-agent workflows, decide whether to duplicate common tools across agents or centralize
them. Consider this example with 'Record Management' and 'Resolution Plan' agents:
       1.   ‘Record Management’ AI Agent gets record details
     2.  The ‘Resolution Plan’ AI Agent invokes tools to search for similar resolved incidents or find knowledge
          articles
     3.  When a resolution plan is available, the orchestrator must leverage the ‘Record Management’ AI Agent to
         write its results back to work notes

If you persist findings often to maintain auditability and create checkpoints, this ping-pong activity between agents
becomes laborious, increases handoffs where errors can occur, and adds latency.

Duplicating simple tools (e.g., Update Work Notes or Add Comment) enables agents to execute common
operations directly without handoffs to other agents, improving self-sufficiency. However, this consumes tool slots
and increases maintenance when tool logic changes, particularly when staying within the 15-tool performance
threshold. Centralizing saves tool budget and simplifies maintenance but creates dependencies where agents
must coordinate with each other for common operations.

Recommendation: Duplicate simple, stable utilities when agents are well below the 15-tool performance threshold
and workflow latency is critical. Centralize complex tools with business logic, tools requiring frequent updates, or
when approaching the 15-tool soft maximum.

Knowledge Base Optimization for RAG Retrieval (Questions 4-8)

Organizations that are adopting AI Agents typically prefer jumping straight into building, but oftentimes it’s the data
foundations that make a use case successful. You should always start with data and knowledge article curation.
It’s unglamorous and sometimes tedious work, but it offers the largest return on the effort you invest.

When agents use grounded prompts to retrieve Knowledge Base articles, KB quality directly impacts retrieval
accuracy and answer quality. Optimize your KB using these leading practices:

Use Clear, Specific Titles (H1)

Make titles concise but descriptive – for example, use “Reset Your Password Using Self-Service Portal” rather than
“Password Help.” Titles carry significant weight in both BM25 keyword scoring and semantic similarity ranking.
Front-load key terms by placing product names, error codes, and issue types at the start of each title.

Start with a Summary

Begin each article with a one-sentence summary of what the article solves. This surfaces key context early,
improving retrieval quality and chunking accuracy for LLM-generated summaries. For example: “This article
explains how to reset MFA when locked out of your account.”

                                                                                                               12

---

<!-- page_13 -->
## Page 13

Use Structured Headings (H2/H3) to Break Up Content

Divide articles into clear sections such as Issue, Symptoms, Resolution Steps, and Additional Notes to enhance
readability and aid the embedding model’s understanding of intent and answerability. Use a consistent heading
structure across the knowledge base to improve retrieval patterns.

Front-Load Key Terms and Concepts

Important phrases, terminology, error codes, product names should appear early in article (first 2-3 sentences).
This improves both keyword hit rates and embedding match confidence. Example: “Error Code 403 appears
when…” not “When this happens, you might see 403…”

Define Company-Specific Terminology Early

Spell out acronyms on first use (e.g., 'Employee Service Center (ESC)'), explain niche products and company-
specific tools, and define any custom branding where internal names differ from standard terms (e.g.,
'myAlectriPortal (ServiceNow Employee Center)'). This ensures the LLM can understand company-specific
language not in its training data.

Use Simple, Declarative Sentences

Avoid overly technical or run-on sentences, prioritizing clarity over verbosity. E5 embedding models better
understand sentence-level semantics with clean, declarative text, so break complex concepts into multiple short
sentences.

Use Numbered or Bulleted Lists for Step-by-Step Instructions

Use numbered or bulleted lists to make instructions scannable and easier to follow, which improves semantic
relevance when matching intent-driven queries like “How do I reset MFA?” For example: “1. Navigate to User
Profile. 2. Click Reset MFA. 3. Scan QR code.”

Add Rich Metadata (Product, Category, Audience)

Leverage KB metadata fields and tags to improve filtering, AI Search profile tuning, and LLM-based reranking. Tag
articles with product names, categories (e.g., troubleshooting, how-to), and intended audience (e.g., end user,
admin).

Provide Text Alternatives for Media

For images, include alt-text or an explanation of the image in the article body. For videos and audio, provide
transcripts or summaries in text format. Transcripts also improve accessibility for users with disabilities and
ensure content remains searchable even if media files are not indexed.

Attachment Optimization

Supported formats for AI Search indexing include .aspx, .html/.htm, .xls/.xlsx, .ppt/.pptx, .doc/.docx, .txt, and .pdf
(searchable text only). Keep AI Search indexing limits in mind:

     •     AI Search indexes only the first 1 MB of attachment data.
     •    Attachments larger than 25 MB are ignored entirely.
Recommendation: Keep critical content in the article body and use attachments as supplementary material.

Avoid Ambiguous or Generic Language

                                                                                                          13

---

<!-- page_14 -->
## Page 14

Replace vague terms such as “this issue,” “that error,” or “various problems” with specific identifiers. For example,
use “404 Not Found error” instead of “that error.” This reduces noise and boosts semantic accuracy for question-
answer matching.

Keep Articles Atomic and Focused

Each article should address one problem and one solution – don’t bundle multiple issues into a single article. This
improves retrievability and prevents dilution of semantic signals during chunking.

Maintain and Retire Stale Content

Regularly review and deprecate outdated or duplicate articles to reduce noise in the knowledge base and
improve precision. This enhances reranking outcomes in dense retrieval. Schedule quarterly KB audits to maintain
quality.

Integration Architecture (Questions 10-12)

Integration via AI Agent Fabric

For external agents, create an AI Agent with type = ‘External’ and add a Provider record with the Connection &
Credential alias containing the Agent Card URL. ServiceNow agents can serve as either primary orchestrators or
secondary participants when invoked. Use MCP to connect agents to external tools, data, and systems, and use
A2A for agent-to-agent collaboration with third-party platforms.

Platform-Native Capabilities First

When practical, prioritize platform-native capabilities. Use Integration Hub for external system connections,
Workflow Studio for workflow orchestration, Record Operations for CRUD actions, and Workflow Data Fabric for
unified data access when available. Build custom integrations only when platform-native options are insufficient.
The goal is maintainability and reuse, not a strict tooling hierarchy.

Common Pitfalls
     •     Creating overly broad agents trying to do everything
     •     Building agents with greater than 15 tools that may create tool selection confusion and performance
        degradation
     •    Vague instructions like “handle appropriately” or “do something else”
     •    Combining multiple actions in run-on sentences confusing the orchestrator
     •     Generic tool names (e.g., Tool 1 or Get Data) instead of descriptive names
     •    Not accounting for non-deterministic LLM behavior in testing
     •     Leaving placeholder text or notes in instructions
     •     Repeating instructions in both agent and tool descriptions unnecessarily
     •    Not collaborating with SMEs to validate business logic
     •    Poor KB quality for RAG: Using vague titles, omitting opening summaries, writing run-on paragraphs, or
        maintaining stale content—all of which cause retrieval failures and hallucinations

                                                                                                     14

---

<!-- page_15 -->
## Page 15

Pillar 2: Security & Compliance

Overview

Secure AI agents protect sensitive data, maintain access controls, prevent unauthorized actions, and comply with
regulatory requirements. Security spans authentication, authorization, data encryption, integration security, and
responsible AI governance.

Design Principles

Security Controls: User Access and Data Access

Define User Access: Creates ACL determining who can discover or invoke the agentic workflow (users with
specified roles, authenticated users, or public).

Define Data Access: Determines user identity the workflow runs as and what data it can access. The two
configuration options for data access are Dynamic user (with role-masking or prior to ZP4+ / YP11+ without) or AI
user (dedicated sys_user).

Role-Masking is now required: For the dynamic user option, developer and security personas must select
approved roles limiting data access to subset of invoking user’s roles. Role-masking enforces the principle of least
privilege, enabling AI Agents to run with minimum necessary permissions.

Critical: When using AI User execution identity, never assign admin or itil_admin roles. This common anti-pattern
bypasses Role-Based Access Control and creates severe security risks.

Prompt Injection & Content Protection via Now Assist Guardian

Now Assist Guardian can be enabled from the AI Agent Studio Settings. Two guardrails are available:

Offensiveness Detection: Scans for 16 categories of harmful language (hate speech, bias, toxic tone) and is
configurable to Log or Block and Log.

Prompt Injection Protection: Detects malicious attempts to manipulate agent behavior and blocks harmful
prompts. Now Assist Guardian can terminate execution plans or tests when harmful content is detected during
any step.

Grounded Prompts to Prevent Hallucinations

Use grounded prompt templates (RAG) that tie agent responses to verified platform data, which reduces
hallucination risk compared to relying on general LLM knowledge. Set appropriate temperature parameters in Skill
Kit for more deterministic outputs, as lower temperature increases grounding.

Responsible AI Governance & Bias Testing

The AI framework at ServiceNow is guided by four principles: Human-centered, Inclusive, Transparent, and
Accountable. High-risk agents that could make bias-prone decisions affecting people should be reviewed by your
Enterprise AI Governance Steering Committee. Before deployment, the Responsible AI team should also conduct
bias testing for any agents involved in hiring, credit allocation, or resource-allocation decisions. The Responsible
AI team should also evaluate compliance against relevant regulations and standards including ISO 42001 (AI

                                                                                                         15

---

<!-- page_16 -->
## Page 16

Management System), EU AI Act, HIPAA (healthcare data), PCI DSS (payment data), and other industry-specific
requirements.

Auditability & Execution Monitoring

All agent actions are logged to execution plans in the sn_aia_execution_plan table, while system logs and event
logs track agent activity for forensics and security investigations. Execution plan monitoring enables detection of
suspicious patterns, authorization failures, and unusual tool usage.

Integration Security for Third-Party Systems

Critical: When agents access third-party data via MCP servers or A2A protocols, design permission validation into
your architecture.

A2A Limitation: A2A protocol does not natively enforce RBAC or delegated authorization and must be
implemented manually. Users invoking AI Agents in ServiceNow must have authorization to view data retrieved
from an external source. Implement permission mapping by documenting which ServiceNow roles can access
which external systems and data. Encrypt data in transit between agents and external systems using TLS 1.2+ with
certificate-based mutual authentication where possible.

Platform Security Foundation

Your AI agents will only be as secure as the underlying ServiceNow platform. Before deploying AI agents to
production, this is an excellent opportunity to evaluate your platform security posture using the ServiceNow
Security Center and Security Leading Practices Guide.

Key Platform Security Areas to Review:

Authentication & Access Control: Enforce Multi-Factor Authentication (MFA) for all admin and privileged accounts
and configure SAML 2.0 or SSO (recommended over local accounts). Enable the High Security Plugin (HSP) with
“default deny” property, change default admin passwords, and enforce password policies.

Data Protection: Configure Field Encryption Enterprise for sensitive data including PII, financial records, and health
information. Enforce TLS 1.2+ for all integrations and data in transit. Maintain a ServiceNow Security Center (SSC)
Hardening compliance score reviewed with critical gaps addressed.

Monitoring & Logging: Enable table auditing for critical tables and monitor Security Center metrics for privilege
escalation attempts, failed login attempts, and unauthorized admin account creation. Review event logs and
system logs regularly to maintain security awareness.

Governance: Keep security contact details current in ServiceNow Support with a minimum of 2 contacts plus a
distribution list. Schedule quarterly Security Center reviews and follow a patch management process that aligns
with ServiceNow’s end-of-life policy, ensuring support for N and N-1 versions.

Assessment Recommendation: Review your SSC Hardening score and address critical platform security gaps
before broad AI agent deployment. Agents inherit platform security strengths and weaknesses.

                                                                                                          16

---

<!-- page_17 -->
## Page 17

Assessment Questions

Access Control & Authentication

Q1: How do you implement User Access Controls for this workflow? (Select all that apply)

Note: These apply to both Dynamic User and AI User.

     •   ☐ User Access ACL configured to restrict who can discover or invoke the workflow
     •   ☐ User Access ACL scoped to specific roles (not “Public” or “All Authenticated Users”)
     •   ☐ Workflow not discoverable by unintended roles in AI Agent Studio / Skill Kit

Q2: When using Dynamic User as the execution identity, is the Dynamic User restricted to approved /
least-privilege roles?

     •   ☐ YES - ☐ NO - ☐ N/A – using AI User

Q3: When using Dynamic User, is role masking (ZP4+ / YP11+) applied to reduce unnecessary privileges?

     •   ☐ YES - ☐ NO - ☐ N/A – Using AI User or version does not support role masking

Q4: When using an AI User as the execution identity, how do you ensure adherence to least-privilege access?
(Select all that apply)

     •   ☐ AI User assigned minimum necessary roles only (no admin/itil_admin/etc.)
     •   ☐ AI User permissions reviewed to confirm they do not exceed dynamic user permissions unless
          justified by the workflow requirements
     •   ☐ N/A – using Dynamic User

Data Access & Permissions

Q5: Do Data Access controls restrict the workflow to minimum necessary tables/fields using any combination of
Table ACLs, Field ACLs, GlideRecordSecure in scripts and/or scoped application boundaries?

     •   ☐ YES - ☐ NO

Q6: Can the Agent access the needed data when field-level ACLs are applied to sensitive fields?

     •   ☐ YES - ☐ NO - ☐ N/A – Field-level ACLs not in use

Q7: Do Domain Separation boundaries correctly enforce which domains the agent can access, and is
sys_restricted_caller_access configured when cross-scope calls are required?

     •   ☐ YES - ☐ NO - ☐ N/A – Domain separation not in use

                                                                                                                   17

---

<!-- page_18 -->
## Page 18

Q8: How is Knowledge Article access being enforced?

     •   ☐ Knowledge Base–level user criteria applied correctly
     •   ☐ Knowledge Article–level user criteria or Knowledge Blocks used for persona-specific access
     •   ☐ Confirmed Agent retrieval via AI Search / RAG respects KB user criteria and field-level visibility
     •   ☐ N/A – Search retrieval tool not in use for this use case

Content Security and Prompt Protection

Q9: How do you protect this workflow from prompt injection and harmful content? (Select all that apply)

     •   ☐ Grounded prompt templates (RAG) used, tying responses to verified platform data
     •   ☐ All user inputs sanitized and validated before tool invocation
     •   ☐ A process has been established to monitor AI Agent execution logs for suspicious or anomalous
        patterns in production.
     •   ☐ Tools invoked only with validated parameters (prevents tool-misuse attacks)

Q10: Has enabling Now Assist Guardian (offensiveness + prompt injection protection) been evaluated for this use
case?

Note: Now Assist Guardian evaluates all GenAI Controller-bound prompts when enabled.

     •   ☐ YES - ☐ NO - ☐ N/A – Not relevant to our AI Agent use cases

Q11: Has enabling Data Privacy for Now Assist (sensitive data masking) been evaluated according to your security
posture?

Note: Data Privacy for Now Assist is a platform-wide masking control applied to all prompts routed through the
GenAI Controller when enabled.

     •   ☐ YES - ☐ NO - ☐ N/A – Sensitive data is not handled by our AI Agents

Responsible AI & Governance

Q12: For high-risk agents making people-affecting decisions, has bias testing been conducted by your
Responsible AI team and are bias/fairness evaluation artifacts being stored as an audit trail?

     •   ☐ YES - ☐ NO - ☐ N/A – Agent has been formally assessed and classified as low-risk

Q13: Agents formally assessed as high-risk should undergo further review. Has this workflow been reviewed by an
Enterprise AI Governance Steering Committee (or similar)?

     •   ☐ YES - ☐ NO - ☐ N/A – Not required or aligned to our AI Governance policies

                                                                                                        18

---

<!-- page_19 -->
## Page 19

Q14: Has your Responsible AI team evaluated this use case against any required or voluntarily adopted
regulations or standards (e.g., ISO 42001, EU AI Act, HIPAA, PCI DSS, or other industry-specific requirements)?

     •   ☐ YES - ☐ NO - ☐ N/A – The use case does not need to align to regulations/standards

Q15: Is this workflow registered in centralized inventory (AI Control Tower or similar) with documented ownership
and risk classification?

     •   ☐ YES - ☐ NO - ☐ N/A

Security Monitoring & Audit

Q16: How do you secure agent execution and maintain audit trails? (Select all that apply)

     •   ☐ Agent execution identity (Dynamic vs AI User) logged for every run
     •   ☐ Table auditing enabled for sensitive data the workflow interacts with
     •   ☐ Execution logs accessible to compliance / SecOps reviewers

Q17: Is Long-term memory reviewed for privacy compliance?

     •   ☐ YES - ☐ NO - ☐ N/A – Long-term memory not enabled

Integration Security

Q18: When using third-party or external integrations, are the following authorization patterns documented,
configured, and implemented? (Select all that apply)

     •   ☐ Authorization pattern documented (“which roles may call which external systems”)
     •   ☐ Architecture-level authorization implemented using ACLs + tool-scope boundaries
     •   ☐ N/A – Not using third-party or external integrations for this use case

Q19: When using third-party or external integrations, are secure credential and transport controls in place? (Select
all that apply)

     •   ☐ MCP / integration credentials stored in Connection & Credential Aliases (no hardcoded secrets)
     •   ☐ TLS 1.2+ confirmed for all external endpoints (ServiceNow enforces TLS for all platform traffic; ensure
         external systems also comply).
     •   ☐ Mutual authentication (cert-based) enabled where supported
     •   ☐ N/A – Not using third-party or external integrations for this use case

                                                                                                          19

---

<!-- page_20 -->
## Page 20

Data Protection & Encryption

Q20: If agents access encrypted sensitive data (PII, financial, health), are cryptographic modules configured for
encrypted data access? (Select all that apply)

     •   ☐ Module Access Policies (MAPs) configured to restrict decryption to the required execution identities
     •   ☐ Execution identity (Dynamic/A.I. User) explicitly authorized in MAPs
     •   ☐ Verified that agents cannot access encrypted fields beyond what their execution identity is authorized
         to decrypt
     •   ☐ N/A – workflow does not gather encrypted PII, PHI, financial or health data

Leading Practices

Security Controls: Required Configuration (Question 1-4)

ServiceNow AI Agent Studio now requires Security Controls configuration for all agentic workflows. This two-part
security model controls both WHO can use agents and WHAT data agents can access.

Part 1: Define User Access (Discovery and Invocation Control)

Creates an Access Control List (ACL) determining which users can discover or invoke the agentic workflow. Three
options are available:

       1.   Users with specified roles (RECOMMENDED) – the most secure option with explicit role requirements
     2.  Authenticated users – any logged-in user can access (less restrictive) or
     3.   Public – anyone can access (least secure and rarely appropriate).

The ACL is created automatically when you save and continue during the guided setup and can be edited later in
the guided setup or directly in the ACL table with an elevated role.

Best practice: Use “Users with specified roles” and select minimum necessary roles for business requirement.
Example: service desk agents for ITSM workflows might require itil role.

Part 2: Define Data Access (Execution Identity and Role-Masking)

Determines the user identity that the agentic workflow runs as and what data it can access. Two options:

Option A: Dynamic User (Default, with Role-Masking in ZP4+ or YP11+)

The workflow runs with permissions of the user invoking it. Role-Masking uses the “Approved roles” to limit
execution to a subset of the invoking user’s roles, implementing the principle of least privilege. For instance, even
if a user has 10 roles, the agent only runs with the 3 approved roles. In ZP4 & YP11 and newer, you cannot save and
continue without configuring role-masking. It’s important to note that role masking cascades from Agentic
Workflow approved roles to AI Agent approved roles to Skills (as tools) approved roles.

Example: If a user has admin, itil, and sn_aia.admin roles but the workflow is configured with only the itil role, when
the user invokes the workflow, the agents run with ONLY itil permissions – not admin privileges.

Overriding role-masking is possible but this is NOT recommended and should be used with caution or during
authorization troubleshooting in lower environments. You can access the Agent Access Role Configurations table

                                                                                     20

---

<!-- page_21 -->
## Page 21

[sys_agent_access_role_configuration] and check “allow all roles” to disable role-masking, but this violates the
principle of least privilege so is not recommended.

Option B: AI User

Uses a dedicated sys_user record with preconfigured roles that are independent of the invoking user. This option
is useful when the agent needs different permissions than the typical user invoking the AI Agent. The AI user’s
roles are displayed and fixed when you select this option.

Leading practice: If using AI user, create with minimum necessary roles (avoid admin/ITIL_admin). ACLs on agent
tools (Flow Actions, Subflows, Skills) are checked against the AI user’s permissions.

When to Use Which Option:

     •    Dynamic user: Use for most scenarios where the agent should only see and perform actions that the
        invoking user can perform, following the principle of least privilege.
     •     AI user: Use when all users need the same elevated permissions or when the workflow requires
        consistent permissions regardless of who invokes it.

Security Impact:

The User Access ACL prevents unauthorized discovery and execution of agents. Data Access controls (role-
masking or AI user) prevent privilege escalation through agents. Together, these mechanisms implement
defense-in-depth for agent security.

Knowledge Article Security (Question 8)

AI Agents honor existing Knowledge Base security controls including ACLs, User Criteria, and can_read access.
When agents use Search Retrieval tools to fetch KB articles, they retrieve only articles the invoking user has
permission to view. No AI-specific KB security configuration is required – agents inherit the security posture you've
already established for your Knowledge Base.

Verify that your KB security is properly configured using standard ServiceNow ACL and User Criteria functionality
before enabling agent retrieval.

Grounded Prompts (RAG) to Reduce Hallucinations (Question 9)

Use grounded prompt templates that tie agent responses to verified platform data (e.g., Knowledge Base, or
similar records). Configure agents to search trusted data sources before responding and base responses only on
retrieved articles. Validate agent responses against source data during testing using Agentic Evaluations. You
should avoid relying on general LLM knowledge as the model may hallucinate incorrect information or leak
training data.

Now Assist Guardian: Dual Protection for AI Agents (Question 10)

Enable this feature in AI Agent Studio by navigating to Settings.

Offensiveness Detection: This feature scans for 16 categories of harmful language including hate speech, bias,
and toxic tone. Configure it to either log detections or block and log.

Prompt Injection Protection: This feature detects malicious attempts to manipulate agent behavior and can
terminate execution plans when harmful content is detected. Configure it to either log detections or block and log.

                                                                                                               21

---

<!-- page_22 -->
## Page 22

You can find detection events in the sys_generative_ai_metric table, or you can export logs as a CSV for analysis
from the Now Assist Guardian Settings page in AI Agent Studio.

Bias Testing for High-Risk Agents (Question 12)

Identify agents making people-affecting decisions such as hiring, loan approval, resource allocation, and
performance evaluation. Conduct bias testing with representative datasets that reflect protected classes, testing
across race, gender, age, disability status, and national origin. Document testing results, any identified biases, and
mitigation strategies employed. Retest after significant prompt changes, data source changes, or model updates.

Responsible AI Governance Implementation (Questions 12-14)

Apply security and governance gates at each phase of the Agent Development Lifecycle (ADLC). For high-risk use
cases, a sample review process may look like:

       1.   Identify people-affecting agents
     2.  Submit to your Enterprise AI Governance Steering Committee for review
     3.  Bias testing complete, if applicable
     4.  Document approval decision
     5.  Deploy with monitoring

Document agents in a centralized inventory system (AI Control Tower or similar) with its business purpose,
capabilities, limitations, known risks, ownership, and compliance mappings. You may also want to record risk
classifications and lifecycle statuses for all agents in the inventory system. Understand the Shared Responsibility
Model to align your security, governance, and operational posture with your responsibilities. Generally, customers
own agent configuration/access control/data classification and ServiceNow owns platform infrastructure security.

AI Governance Program Structure (Questions 13-14)

Consider structuring your AI governance program across multiple levels:

     •    Board Oversight: Your Board and Audit Committee provide executive oversight of the AI governance
       program
     •     Executive Steering: An Enterprise AI Governance Steering Committee at the C-suite level approves the AI
       governance plan and escalation decisions
     •    Working Committee: A multidisciplinary team including platform experts, AI practitioners, and legal and
       compliance professionals conducts architecture reviews, technical design reviews, and risk assessments

Document all AI initiative decisions with checkpoints for compliance verification.

Agent Execution Plan Monitoring (Question 16)

Monitor the sn_aia_execution_plan table for execution state (Completed, Failed, In Progress), duration anomalies,
and error patterns. Configure alerts for repeated failures, authorization errors, unusual execution frequency, and
unexpected tool usage. Review Decision Logs when investigating security incidents to trace agent chain-of-
thought reasoning and use the replay capability in the Activity tab to reconstruct exactly what the agent did during
suspicious activity. Export execution logs for compliance audits, security forensics, and root cause analysis.

                                                                                             22

---

<!-- page_23 -->
## Page 23

Third-Party Integration Security (Question 18-19)

Critical Limitation: A2A protocol does not natively support delegated authorization or RBAC. Permission validation
must be designed into your architecture and mapped manually.

Architecture-Level Authorization Design: Design access controls at the agentic workflow level using Security
Controls (User Access ACLs). Only grant users access to the agentic workflow or agent  if they have authorization
to view external system data. When practical, create an access matrix specifying which ServiceNow roles can
access which external systems and data sources, then test with users having different role combinations to
validate Security Controls enforcement.

Audit Trail: Log all external data retrievals with user, timestamp, and source system for compliance tracking.

MCP Credential Security: Store MCP server credentials in Connection & Credential alias records (not hardcoded
in tools/scripts).

Transport Security: Ensure that TLS 1.2+ is supported for all external endpoints. ServiceNow enforces TLS 1.2+ for
all platform traffic so confirm that all external endpoints also support data in-transit encryption.

Certificate-Based Authentication: For external integrations, implement certificate-based mutual authentication
where possible.

Field Encryption: Configure cryptographic modules with Module Access Policies (role/scope/script-based) if
agents access sensitive encrypted fields.

Secure Scripting in Agent Tools

When using Script tools or Flow Script steps:

     •    Use GlideRecordSecure() instead of GlideRecord() to enforce ACLs
     •    Use addUserEncodedQuery() instead of addEncodedQuery() for additional security

GlideRecordSecure evaluates all ACLs (read/write/create/delete) preventing unauthorized data access.

// Do this

var queryString = "priority=1^ORpriority=2";
var now_GR = new GlideRecordSecure('incident');
now_GR.addUserEncodedQuery(queryString);
now_GR.query();
while (now_GR.next()) {
       gs.addInfoMessage(now_GR.getValue('number'));

}

// Not this

var queryString = "priority=1^ORpriority=2";
var now_GR = new GlideRecord('incident');
now_GR.addEncodedQuery(queryString);
now_GR.query();
while (now_GR.next()) {
       gs.addInfoMessage(now_GR.getValue('number'));
}

This is especially important when agents run as AI user (elevated permissions) as GlideRecordSecure ensures
that the AI User’s ACLs are still enforced.

                                                                                          23

---

<!-- page_24 -->
## Page 24

Common Pitfalls
     •    Not configuring Security Controls (User Access and Data Access) properly. Role-Masking is required in
       ZP4+ and YP11+
     •     Disabling role-masking by checking “allow all roles” in Agent Access Role Configurations table (violates
         least privilege)
     •     Using overly permissive User Access ACLs (Public or All Authenticated Users) instead of specific roles
     •     Configuring “Run as” with overprivileged AI user accounts (admin/ITIL_admin roles) instead of minimum
        required permissions
     •    Not designing authorization validation for A2A integrations – A2A protocol doesn’t natively enforce RBAC,
       which allows agents to become privilege escalation vectors if authorization validation is not designed into
        the workflow architecture
     •    Not enabling both Now Assist Guardian guardrails for AI Agents (Offensiveness Detection and Prompt
         Injection Protection)
     •     Using general LLM knowledge instead of grounded prompts (RAG) allowing hallucinations that could leak
         sensitive information
     •     Skipping bias testing for agents making people-affecting decisions (hiring, credit, resource allocation)
     •    Not monitoring agent execution plans for security anomalies (unusual patterns, authorization failures)
     •    Hardcoding MCP server credentials in tools/scripts instead of Connection & Credential alias records
     •     Deploying high-risk agents without Enterprise AI Governance Committee review
     •     Using GlideRecord() instead of GlideRecordSecure() in Script tools, allowing ACL bypasses
     •    Assuming platform security automatically extends to AI agents without specific validation
     •    Not maintaining agent documentation

Pillar 3: Reliability

Overview

Reliable agents operate predictably within technical constraints, handle errors gracefully, prevent cascading
failures, and recover from issues without manual intervention. This pillar merges performance and reliability
concerns specific to AI agents.

Design Principles

Respect Technical Boundaries

Agents must operate within technical constraints, as exceeding performance thresholds causes unpredictable
behavior, degradation, and potential failures. Monitor for timeout errors and tool selection confusion, noting that
continuous tool execution (maximum consecutive number of invocations for the same tool) is limited by the
sn_aia.continuous_tool_execution_limit property.

                                                                                      24

---

<!-- page_25 -->
## Page 25

Prevent Recursive Execution Loops

Recursive loops waste assists, degrade performance, and can cause production performance issues. Implement
three layers of protection to mitigate looping behavior: trigger design, filter conditions, and built-in recursive
checks.

Graceful Degradation & Error Handling

Not all errors are created equal. A robust agentic solution prioritizes error handling by balancing:

       1.   Frequency: How often does the error occur?
           e.g., over 20% of scenarios, between 10 to 20% of the time or under 10% of all use cases
     2.   Impact: Does it block critical workflows or create minor friction?

Your approach to error handling and time investment should match the risk level. High frequency errors (> 20%)
warrant comprehensive recovery paths with fallback actions and should be considered critical to remediate. Low-
frequency errors (< 10%) can have simpler error handling with manual escalation paths.

For all errors, agents should handle partial success scenarios gracefully. They should provide clear feedback
messages when tools fail or don’t return results and inform users of outcomes rather than allowing silent failures.

AI Agent Execution Patterns

AI Agents execute synchronously and are optimized for single-execution reasoning and not iterative loops or long-
running operations. Loop logic, retry operations, and batch operations should be implemented in flows or scripts
that call the agent externally, not within the agent instructions. For operations taking longer than 0.5 seconds, use
asynchronous patterns with callbacks or polling rather than blocking agent executions. Understanding these
execution characteristics ensures reliable, scalable implementations.

Assessment Questions

Technical Limits & Performance

Q1: Are agents tested under realistic data loads to ensure completion within acceptable timeframes without
timeouts?

     •   ☐ YES - ☐ NO - ☐ N/A

Q2: Do agents stay within the 15-tool maximum, with performance monitoring showing consistent tool selection
times?

     •   ☐ YES - ☐ NO - ☐ N/A

Q3: For tools processing large datasets, are limits and filters implemented to prevent excessive data processing?

     •   ☐ YES - ☐ NO - ☐ N/A

                                                                                         25

---

<!-- page_26 -->
## Page 26

Recursive Loop Prevention

Q4: How do you prevent recursive execution loops? (Select all that apply)

     •   ☐ Status and Assist Consumption dashboards in AI Agent Analytics monitored during development
     •   ☐ Recursive protection properties verified and modified as necessary (50 creates/15min, 5
        updates/15min)
     •   ☐ Trigger conditions include loop-breaking fields (Assignment Group change, custom flag)

Q5: For use cases using On Record Updated triggers, does the agent update a field that causes the trigger
condition to evaluate to FALSE (preventing loops)?

     •   ☐ YES - ☐ NO - ☐ N/A

Q6: For Scheduled triggers, does the record scope in your data retrieval tool align with your trigger frequency to
prevent the same records being analyzed in multiple executions?

     •   ☐ YES - ☐ NO - ☐ N/A

Q7: Are Inbound Email triggers used alone (not combined with On Record Created or Updated triggers) to prevent
duplicate executions?

     •   ☐ YES - ☐ NO - ☐ N/A

Error Handling & Recovery

Q8: How do you handle errors and validate tool prerequisites? – required for all agents (Select all that apply)

     •   ☐ Users informed when agent actions fail with clear error messages (not silent failures)
     •   ☐ Agents validate prerequisite data before proceeding with clear stop conditions

Q9: For high frequency or critical risk scenarios (> 20%), how is recovery and fallback handled gracefully? (Select
all that apply)

     •   ☐ Agent instructions and tools include fallback actions for scenarios where tools fail or return no results
     •   ☐ Recovery paths are documented and tested
     •   ☐ N/A – all errors are low-frequency (<20%), non-critical, and do not require comprehensive recovery
       mechanisms

Execution Patterns

Q10: For batch processing scenarios, do you use external flows/scripts that call agents once per record rather
than implementing loops within agent instructions?

     •   ☐ YES - ☐ NO - ☐ N/A – Agent does not process batches of records

                                                                                          26

---

<!-- page_27 -->
## Page 27

Q11: For long-running operations (>0.5 seconds), do you use async patterns with callbacks or polling rather than
blocking agent execution?

     •   ☐ YES - ☐ NO - ☐ N/A – All agent operations complete in <0.5 seconds

Q12: Is loop logic and retry logic implemented in flows/scripts rather than in agent instructions?

     •   ☐ YES - ☐ NO - ☐ N/A – Agent does not require loop or retry logic

Testing Failure Scenarios

Q13: Before production deployment, do you test agents with edge cases (missing data, malformed inputs, tool
failures) and start with small record batches (5-10 records) in sub-production before scaling to production-scale
testing?

     •   ☐ YES - ☐ NO

Leading Practices

Respect Technical Limits & Performance Optimization (Questions 1-3)

Test agents under realistic data loads to ensure completion within acceptable timeframes and limit tools per
agent to a maximum of 15 for optimal orchestrator performance and predictable tool selection. Use tools for heavy
data operations such as filtering, sorting, and aggregation instead of relying on prompts, and offload complex
prompt requirements to Skill Kit custom skills that are reusable and don’t weigh down the agent. Optimize RAG
queries by limiting scope, using indexed fields, and caching frequent results. Similarly, limit external API calls by
batching them when possible and caching responses.

Recursive Loop Prevention: Three-Layer Strategy (Questions 4-7)

Layer 1: Trigger Selection

Understand the different trigger types: Record-Based (On Created, On Updated, On Created & Updated), Time-
Based (Scheduled), and Application-Based (Inbound Email). Avoid cascading executions by ensuring that if an
agent modifies a record, the update doesn’t satisfy other trigger conditions. Never combine Inbound Email triggers
with On Record Created/Updated triggers, as email actions create or update records so that configuration will fire
both triggers simultaneously. Use Scheduled triggers when analyzing data across multiple records for tasks such
as pattern detection or major incident identification.

Layer 2: Filter Conditions (Loop-Breaking Patterns)

Assignment Group Pattern (Recommended):

Assign the record to an assignment group designated for virtual workers using a filter of Active = True AND
Assignment Group = ‘AI Virtual Workers.’ The agent processes the record and then reassigns it to the human
fulfiller group, which causes the trigger condition to become false (since the assignment group has changed),

                                                                                                27

---

<!-- page_28 -->
## Page 28

thereby preventing retriggering. This pattern provides a clear audit trail and integrates seamlessly with AWA and
Predictive Intelligence.

Custom Flag Pattern:

Add a true/false field called “AI_Processed” with a filter of AI_Processed = False. The agent sets AI_Processed =
True early in its execution to prevent retriggering. Avoid modifying the State field, as it is used by other Now Assist
skills.

Layer 3: Recursive Check Properties (Safety Net)

Create Record Check: recursive_check.query_for_create_record property limits executions to 50
per 15-minute window by default. This applies to batch and API pathway scenarios processing multiple records.
For example, if a scheduled agent processes 60 records from yesterday, 50 will process successfully while 10 will
be rate limited.

Update Record Check: recursive_check.query_for_update_record By default, the system allows 5
executions per 15-minute window for On Record Update triggers where the filter condition remains true. For
example, if an agent adds work notes which updates the record and triggers the workflow again, after 5 iterations
the system applies rate limiting. This feature requires Now Assist AI Agents plugin v4.0.38 or later (Xanadu Patch
9+, Yokohama Patch 3+, or Zurich).

Loop Detection & Emergency Response

If you suspect a loop, monitor for them in AI Agent Studio by navigating to AI Agent Analytics → Status tab →
Execution plans and investigate the In Progress execution plans for duplicates. Also, monitor the Assist
Consumption tab for spikes and the top 10 agentic workflows consuming Assists. If a loop is detected, follow
these emergency steps:

       1.   Deactivate trigger immediately
     2.  Cancel executions in sn_aia_execution_plan with State = In Progress
     3.  Analyze root cause
     4.  Redesign with loop-breaking logic
     5.  Test with at least 5-10 records in sub-production

Error Handling & Graceful Degradation (Question 8-9)

Error Handling Patterns

Production AI Agents require different levels of error handling based upon how frequently errors occur and their
business impact. Implement error handling at the appropriate level for your use case:

     •     Universal Baseline: All AI Agents should produce clear, actionable error messages and avoid failing
           silently. Furthermore, tools must validate the payload for completeness before processing and include
         clear stop conditions when required data is missing.
     •    Comprehensive Handling: More comprehensive error handling should be designed for errors occurring
       more than 20% of the time or for critical use cases. You should implement fallback actions with
         alternative approaches so that the AI Agent can continue the workflow or default back to a human-driven
        process. Recovery paths should include logic to retry (as applicable) or gather supporting information by
          calling other tools. These fallback and recovery paths should be well-documented in the AI Agent
         instructions and tested thoroughly.

                                                                                        28

---

<!-- page_29 -->
## Page 29

It's important to distinguish between fallback actions and recovery paths with a few examples:
     •     Fallback Action: Agent asks the user for help or logs a detailed error when stuck
           §   Example: “I couldn’t find that record. Could you verify it for me?”
     •    Recovery Path: Complete sequence of steps that the AI Agent should take from error to resolution
           §   Example: Try another tool → Retry Query → Fallback to user → Escalate to a human-driven
              workflow

Building Structured Error Responses

Tools should return structured errors, rather than generic messages:

javascript

// Avoid
return { error: "Something went wrong" };

// Recommended
return {
    success: false,
    error_type: "validation_failed",
    user_friendly_message: "I couldn't complete this request because..."
};

Note: GlideRecordSecure is recommended for robust security and ACL enforcement. However, when tools
accept dynamic table names (e.g., from user input), validate the table exists using GlideRecord before
instantiating GlideRecordSecure to prevent uncatchable exceptions.

Documenting Recovery Paths in Agent Instructions

For comprehensive error handling (>20% frequency or critical scenarios), document the complete recovery
sequence in your agent instructions:

Example Pattern:
WHEN [Tool Name] Returns Error:
       1.  Check error_type field
     2.   IF error_type = "X":
        Try [alternative approach]
        Retry operation
     3.   IF still fails:
       Use FALLBACK to ask user for [information]
        Retry with user input (max 2 attempts)
     4.   IF all attempts fail:
         Escalate: "Unable to complete. Please contact [support]"
       Log error details for troubleshooting

Testing Recovery Paths

Systematically test error scenarios to verify recovery works as documented:

                                                                                          29

---

<!-- page_30 -->
## Page 30

•      Invalid inputs require clear error & correction request
     •     Missing prerequisites should mean validation stops with helpful guidance
     •     Tool failures trigger retry logic & fallback triggers appropriately
     •    Max retries exceeded events should escalate to a human process with proper context
Document test results for high-frequency errors to ensure reliability.

AI Agent Execution Patterns (Question 10-12)

AI Agents execute synchronously and are not optimized for loop logic in prompts. For operations requiring delays
or processing multiple records, implement loop and wait logic externally:

     •    Batch Processing: Use scheduled flows that loop through records and call the agent once per record
        (keep the recursive_check.query_for_create_record limit in mind)
     •    Long Running Operations: Use async patterns with external callbacks or polling
     •     Tool design: Tools must return quickly (ideally under 0.5 seconds); never use the “Wait for a duration of
        time” action in tools.

Avoid Looping Logic in Agent Prompts

Implementing loops in agent instructions causes repeated tool calls that can hit platform limits
(continuous_tool_execution_limit default: 7 consecutive calls). Avoid scenarios where you get a list
and then ask your agent to perform a for-each loop, continually invoking the same tool for each record. Instead,
get a list of all records in an external flow and call the AI Agent once for each record. This pattern is monitored by
recursive_check.query_for_create_record  (default: 50 executions per 15 minutes). If you
experience rate limiting, consider increasing the limit.

Handling Long-Running External Operations

When calling external systems that take more than 0.5 seconds, tools should return immediately and handle
responses asynchronously. There are two options for accommodating this pattern:

     •    Async with Callback (Preferred):
           §   Tool starts work, stores a correlation ID, submits the correlation ID externally, and the tool returns
              immediately
           §   External system POSTs results to the callback endpoint when complete
           §   The callback handler posts a message to a conversation (user-facing agents) or response table
             (autonomous agents)
           §  No polling required
           §   Important Note: Now Assist Skills added as AI Agent tools use the async method natively so
               leverage skills as an intermediary when possible.
     •     External Polling:
           §   Tool starts work and the response is recorded immediately
           §  A scheduled flow polls the status
           §   The flow posts results when complete (to Virtual Agent or response table)
           §   Key: Polling happens outside of the AI Agent, not in the agent instructions

                                                                                  30

---

<!-- page_31 -->
## Page 31

Testing for Reliability (Question 13)

Test with a minimum of 5-10 records in sub-production before deploying to production, starting small to catch
loops early when they’re less expensive and easier to fix. Test edge cases including missing data, malformed
inputs, tool failures, and network timeouts to verify that agents handle non-happy-path scenarios gracefully with
appropriate error messages. Use the Decision Log to trace the orchestrator’s reasoning when debugging failures.

Common Pitfalls
     •    Not testing for recursive loops before production deployment
     •     Using synchronous blocking waits (gs.sleep) in scripts or using "Wait for a duration of time" actions in AI
       Agent tools which ties up Virtual Agent threads
     •    Not monitoring assist consumption during development/testing
     •    Combining Inbound Email with On Record triggers causing duplicate executions
     •    Vague error handling - “figure out what went wrong and fix it” instead of specific fallback actions
     •    Not implementing loop-breaking fields in filter conditions
     •     Ignoring “Assist consumption spike” warnings in analytics dashboard
     •     Implementing polling loops in Agent Instructions
     •    Not using async patterns for operations more than 0.5 seconds – tools must return immediately and use
         either callbacks or external polling to receive responses

Technical Reference

Recursive Protection Limits:

                                 Time
 Protection Type        Default Limit   Window      Use Cases
 Create Record       50             15 minutes    Scheduled triggers, batch processing, API pathways
 Check                executions
 Update Record       5 executions    15 minutes   On Record Update triggers, On Record Created &
 Check                                        Updated

Pillar 4: Operational Excellence

Overview

Operational excellence for AI agents means running them sustainably at scale – with clear ownership, effective
monitoring, continuous improvement, and demonstrable ROI. This pillar ensures agents deliver measurable
business value that exceeds their operational cost while maintaining governance and lifecycle discipline.

Design Principles

Agent Development Lifecycle (ADLC)

Follow the seven-phase Agent Development Lifecycle:

                                                                                                           31

---

<!-- page_32 -->
## Page 32

1.   Discover & Plan:
        Includes activities such as stakeholder alignment, Responsible AI assessment, platform and data
        readiness checks, cost/value and feasibility analysis, use-case qualification/prioritization, and
         organizational change management (OCM) preparation.
     2.  Design & Build:
        Define agent goals and instructions, reasoning and prompt engineering patterns, human-AI teaming
        models, UX design, and overall tool architecture including how flows, scripts, retrievers, and skills will be
       used within the agentic pattern. Create and configure tools (flows, scripts, skills, retrievers), establish
         multi-agent orchestration where appropriate, and implement the agent logic for each workflow step.
       Ensure tool modularity and maintainability.
     3.   Evaluate:
       Use Data Kit and Agentic Evaluations to ensure outputs are grounded, complete, relevant, and aligned
        with expected reasoning. Conduct human-reviewed UAT for AI Agents and use ATF to test deterministic
        workflows, tools, flows, and scripts.
     4.  Deploy:
       Develop and execute a phased rollout strategy. Apply RBAC and ACLs using least privilege principles,
          finalize trigger configuration and communicate changes in line with your formal Organizational Change
       Management (OCM) program.
     5.   Monitor:
        Configure dashboards and observability mechanisms to track KPIs. Establish ongoing operational
        support for log review and issue analysis using the Decision Log and Activity tab to identify failure
        patterns such as wrong agent selection, wrong tool invocation, looping behavior, or poor output quality.
     6.  Optimize:
        Perform iterative continuous improvement based on usage analytics, user feedback, and error patterns.
       Update prompts, tools, and retrieval logic as needed. Address backlog items, retest after platform
       upgrades or patching, and improve latency/cost efficiency.
     7.   Retire:
       Decommission agents that no longer deliver value, no longer meet operational or compliance needs, or
       have been replaced by improved solutions. Reassess ROI, document retirement decisions, and
        introduce replacement strategies.

Ownership & Accountability

Every agent should have a clearly identified owner accountable for its performance, maintenance, and lifecycle
from go-live through retirement. Establish ownership during the Discover & Plan phase, document it in a
centralized inventory, and define escalation paths before production deployment.

Non-Deterministic Awareness
Not every task requires agentic AI. LLMs are non-deterministic, meaning the same input may produce different
outputs. It’s important to test extensively to understand the acceptable variance for your use case and determine
whether a static workflow, a Now Assist Skill, or a dynamic agentic workflow is the best fit. Consider whether you
truly need the reasoning engine built into Agentic AI, or whether chaining Skills together can lower Assist
consumption and maximize ROI.

                                                                                          32

---

<!-- page_33 -->
## Page 33

The most effective way to reduce probabilistic variation is to incorporate deterministic workflows into your AI
Agent as tools. When the output of one tool is always used as the input to the next, you can string workflows
together deterministically to minimize variability and avoid unnecessary Assist usage.

Pre-Production Quality Validation

Agentic Evaluations uses LLM-based judges to assess agents before deployment across three core metrics:
Overall Task Completeness, Tool Calling Correctness, and Tool Choice Accuracy. This serves as a
comprehensive validation checkpoint before production deployment.

Production Monitoring & Analytics

The AI Agent Analytics dashboard tracks key metrics including execution frequency, success rates, average
execution time, and failed calls. Use a continuous feedback loop to monitor agent performance, identify issues,
refine configurations, and re-evaluate outcomes.

Centralized Governance via AI Control Tower

AI Control Tower provides enterprise-wide visibility for all agents (both ServiceNow and third-party), embedded
compliance monitoring (EU AI Act, NIST AI RMF), end-to-end lifecycle management from ideation to retirement,
and real-time reporting on performance against business outcomes.

Continuous Improvement Culture

AI transformation is a journey, not a destination. Regularly iterate on agent prompts, tools, and workflows while
measuring key indicators such as accuracy, user adoption, and feedback quality.

Assessment Questions

Ownership Accountability

Q1: Is an accountable owner and backup identified for each agent?

     •   ☐ YES - ☐ NO - ☐ N/A

Q2: Are escalation paths documented for when agents fail, require updates, or exhibit unexpected behavior?

     •   ☐ YES - ☐ NO - ☐ N/A

Q3: Is the owner/support model documented in a centralized AI inventory or registry?

     •   ☐ YES - ☐ NO - ☐ N/A

Governance & Lifecycle

Q4: Do agent changes follow a defined Agent Development Lifecycle, including managing changes through AI
Agent studio with version control and sub-production testing?

     •   ☐ YES - ☐ NO - ☐ N/A

                                                                                       33

---

<!-- page_34 -->
## Page 34

Q5: Do you have a process in place to identify dormant, unused, or over-privileged agents to ensure they are
reviewed and decommissioned?

     •   ☐ YES - ☐ NO - ☐ N/A

Q6: Is there a formal agent retirement process documenting decommissioning decisions and communicating to
stakeholders?

     •   ☐ YES - ☐ NO - ☐ N/A

Pre-Production Validation

Q7: How do you validate agents before production deployment using Agentic Evaluations? (Select all that apply)

     •   ☐ Agents evaluated using Agentic Evaluations with LLM-based judges before production
     •   ☐ All three core metrics assessed: Overall Task Completeness, Tool Calling Correctness, and Tool
       Choice Accuracy
     •   ☐ Evaluation scores meet appropriate quality thresholds based upon risk and impact (Note: These
        thresholds will likely vary by use case)
     •   ☐ Baseline evaluations cloned for regression testing after each change
     •   ☐ Evaluation reports exported and shareable with compliance teams and leadership

Q8: How do you ensure evaluation dataset quality and representativeness? (Select all that apply)

     •   ☐ Evaluation dataset includes 10-50 samples for initial testing, scaling to 100-300 for production
        readiness
     •   ☐ Evaluation datasets include diverse scenario types (common requests, edge cases, high-risk failures)
     •   ☐ Test data sourced from production records cloned to sub-production environments
     •   ☐ Tested for output consistency by running the same inputs multiple times to confirm variance is
        acceptable for business requirements

Production Monitoring

Q9: How do you monitor agents in production? (Select all that apply)

     •   ☐ AI Agent Analytics dashboard reviewed regularly for execution frequency, success rates, failures
     •   ☐ Execution failures analyzed using Decision Logs and Activity tab replays
     •   ☐ Assist consumption monitored to detect spikes indicating potential loops or inefficiency
     •   ☐ Alerts configured for critical failures (agent errors, SLA breaches, unusual consumption)

                                                                                    34

---

<!-- page_35 -->
## Page 35

Leading Practices

Ownership & Accountability: Define Before Go-Live (Questions 1-3)

Assign a single owner per agent responsible for ongoing maintenance, prompt updates, troubleshooting failures,
and performance monitoring. Document owner name, email, backup owner, and escalation contact in a
centralized inventory system.

Establish support model:

Define clear accountability by answering:

    •  Who responds when an agent fails or produces incorrect results?
    •  Who approves prompt changes before production deployment?
    •  Who monitors analytics dashboards and acts on anomalies?
    •   What are the SLAs for responding to agent issues?

Traditional ITIL-based SLA response models may need to be modified when launching GenAI or Agentic
workflows. In use cases where their output is used in downstream decision-making or content is published to a
large population of employees or customers, damage control for hallucinated or inaccurate responses should be
performed immediately. Define response SLAs using a contain-first model. When an agent produces incorrect
results, hallucinations, or unexpected behavior, the first action should be to deactivate the agent's trigger or
disable the agent in AI Agent Studio. Do not troubleshoot it while it remains in production generating potentially
harmful outputs. Once contained, apply priority-based resolution timelines (e.g., 4 hours for critical, 24 hours for
normal) to diagnose root cause, remediate, validate with Agentic Evaluations, and restore to production.

When agents change (whether due to feature improvements or retirement), experience outages, or suffer
performance degradation, consider how those changes will be communicated and to whom.

Ensure Agent owners and users understand agent logic, tools used, business process supported, integration
points, and expected behavior. Create a knowledge transfer and organizational change management (OCM)
program to initially train users at deployment and update them when changes occur. Consider creating job aids,
demo vignettes, and holding office hours so that users are well-equipped and empowered to interact with the AI
Agent directly or interpret its output when an agent acts autonomously.

Ownership should be assigned to an individual or small team (2-3 people), not a large distribution list – a large
group creates a diffusion of responsibility. Avoid assigning use cases to a generic owner like “AI Team” without
specific names or contacts assigned, but balance individual accountability with continuity planning in case of role
changes or attrition.

Agentic Evaluations: Pre-Production Validation (Questions 7-8)

Setup & Configuration:

Navigate to Now Assist Skill Kit → Agentic Evaluations – this can also be reached from AI Agent Studio → Testing
→ "Start automated evaluation". Select “New auto evaluation” and follow the wizard. Ensure you select the agentic
workflow or standalone AI agent to evaluate, choose your evaluation metrics, and select a data source. All three
metrics are recommended: Overall Task Completeness, Tool Calling Correctness, and Tool Choice Accuracy.

                                                                                      35

---

<!-- page_36 -->
## Page 36

Note: UI elements and capabilities for Agentic Evaluations have improved in the Zurich family release and later.
Many of the foundational features remain the same, but navigation and features may vary slightly in your instance
on earlier family releases. Consult the ServiceNow product documentation for more details.

Evaluation Data Source Options:

       1.   Existing execution logs: Real-world performance from production/test
     2.  Manual testing: Run agent in AI Agent Studio to generate controlled scenarios
     3.  Automated generation: LLM acts as conversational partner, autonomously drives 50-100+ executions

Agentic evaluations execute real workflows and cause AI Agents to modify real records, so only run them in sub-
production.

Reading Results:

Results are displayed with rating badges including Excellent, Good, Moderate, and Poor. Drill into individual
execution logs to:

       1.   View the complete workflow
     2.  Review result explanations showing which steps succeeded or failed to identify common patterns
     3.  Follow recommended actions providing guidance on what to investigate next
     4.  Export reports for stakeholder approval

Leading Practices:

Start with 10-50 samples for initial debugging, then scale to 100-300 samples for production readiness validation.
Clone production records to sub-production to access evaluation datasets and ensure agents handle real-world
data complexity (e.g., missing fields, malformed entries, ambiguous input) that synthetic test data doesn't capture.
Structure datasets to reflect production scenario distribution. Your dataset will predominantly consist of common
requests that represent typical usage, with an appropriate representation of edge cases (missing/unexpected
data) and high-risk scenarios where failures have business impact. Measure value by task completion (did the
workflow deliver the business outcome?) rather than just whether the chat ended. Combine automated
evaluations for scale and consistency with human review for sensitive or ambiguous outputs. Focus on fixing
patterns across executions rather than individual failures and clone evaluations for regression testing after making
changes.

Continuous Improvement Process (Question 9)

Conduct weekly reviews of agent health dashboards, monthly analysis of value metrics and trends, and quarterly
portfolio reviews examining performance, value delivery, and optimization opportunities. Perform regular prompt
refinement based on Decision Log analysis and re-evaluate agents after changes using cloned baseline
evaluations.

Common Pitfalls
     •     Deploying agents without Agentic Evaluations pre-production validation
     •      Insufficient evaluation sample size (<10 executions)
     •     Reactive rather than proactive monitoring (discovering issues after user complaints)
     •    Not integrating with AI Control Tower for enterprise governance
     •    No clear ownership or accountability for agent performance

                                                                                       36

---

<!-- page_37 -->
## Page 37

•     Building overly complex agents when simpler solutions achieve same outcomes

Pillar 5: Cost Optimization & Value Measurement

Overview

Cost optimization ensures AI agents deliver measurable business value exceeding their operational cost through
strategic deployment, efficient design, and consumption discipline. Value measurement tracks both bottom-line
improvements (productivity, efficiency, deflection) and top-line impact (revenue growth, customer acquisition,
retention) depending on workflow objectives.

Design Principles

Business-Driven Use Case Prioritization

Before envisioning use cases, start with the business KPIs the organization needs to influence, and use
anticipated business value to guide how use cases are selected and prioritized. Operational cost savings and
productivity gains matter, but they shouldn’t be the sole focus. Don’t limit use-case selection to bottom-line
efficiency – some of the highest-ROI opportunities come from initiatives that drive top-line revenue. These
revenue-growth opportunities often involve use cases that impact customer acquisition, retention, and
competitive differentiation.

High-Volume, High-Impact Focus

Deploy agents on high-volume, low-complexity use cases first to maximize value. ServiceNow data shows that
across 500+ AI use cases, 43% involve workflow automation for low-complexity scenarios and 37% address
complex workflows. Target scenarios with the clearest ROI path.

Consumption-Based Efficiency

Agents consume assists based on the number of workflow actions they execute (excluding orchestrator and
communicator actions). Agentic Workflow runs are grouped into small, medium, or large tiers, with assist
consumption determined by the number of actions performed. Other Now Assist capabilities invoked as tools
inside an AI Agent – such as Skills, LLM-based Virtual Agent Topics, and Conversational Catalog Items – do not
consume Assists but do count as tool invocations, so they contribute to workflow sizing (Small, Medium or Large).

Right-Size Solution Complexity

Not every task requires agentic AI. Reserve agents for problems that need reasoning and planning capabilities
and use simpler tools for single-step tasks such as Now Assist Skills, Flow Designer, or Virtual Agent topics. The
most effective cost optimization is deliberately employing agentic workflows where workflows are dynamic and
using deterministic automation when the process is rule-based. Stringing deterministic workflows together into a
super tool for your AI Agent can minimize tool invocations, decreasing cost. "Know When Agentic AI Isn't the
Answer" by validating whether dynamic reasoning is essential to your use case.

                                                                                             37

---

<!-- page_38 -->
## Page 38

Framing Value Measurement and Realization

ServiceNow’s AI Value Framework measures value through three reinforcing dimensions: usage, user acceptance,
and productivity time value – expressed as total hours returned to the business. Rather than relying solely on
traditional “time saved” metrics, the framework emphasizes transformational productivity outcomes and ties AI
value directly to business KPIs.

While time-based benchmarks still provide a baseline (e.g., 15 minutes saved per agentic workflow execution), the
internal value realization teams at ServiceNow stress that time saved alone is an incomplete view of value.
Instead, value should also incorporate:

     •     Requestor Productivity Gains: Value created when end users successfully complete automated requests
        or find answers through conversational interactions
     •    Human Agent Efficiency Improvements: Reductions in effort through deflection, case/incident
         acceleration, and agentic workflow automation that increases throughput and reduces manual workload
     •     Operational Efficiency: Quantifiable improvements such as SLA adherence, reduced cycle times
       (AHT/MTTR), and elimination of manual process steps are common metrics used by process owners
     •     Experience Impacted: Improvements in satisfaction and friction reduction for employees or customers,
       which correlate strongly with adoption, sustained usage, and overall productivity
     •     Strategic Outcomes: Higher-order business results tied to top-line impact – customer acquisition,
         retention, revenue enablement – as well as improved decision velocity and organizational resilience

This more holistic model reflects how ServiceNow measures AI impact internally. Hours saved can be interpreted
as capacity created, cost takeout, or value repurposed to high-value work depending on your audience and the
business context for the conversation.

In practice, view time saved as the starting point. Modern AI Value measurement centers on productivity
throughput, qualitative experience improvements, adoption momentum, strategic alignment and measurable
business outcomes. The goal is not to just automate tasks but also unlock new capabilities that compound the
value that humans and organizations can achieve with AI assistance.

Assessment Questions

Value Definition

Q1: Ahead of development, were measurable business KPIs, cost metrics, and success indicators defined for this
agent to evaluate value vs. spend?

     •   ☐ YES - ☐ NO - ☐ N/A

Strategic Deployment

Q2: During use case prioritization, was this agent classified as highly valuable and feasible to maximize ROI?

     •   ☐ YES - ☐ NO - ☐ N/A

Q3: Have you validated that agentic AI is appropriate for this use case (requires reasoning/planning) vs. simpler
automation (skills, flows)?

                                                                                      38

---

<!-- page_39 -->
## Page 39

•   ☐ YES - ☐ NO - ☐ N/A

Cost Optimization – Development Cost

Q4: Have you reused existing platform resources (subflows, flow actions, catalog items, VA topics, skills) to
reduce development cost and maximize historical platform investment?

     •   ☐ YES - ☐ NO - ☐ N/A

Cost Optimization – Invocation Efficiency

Q5: Are trigger conditions designed to invoke agents only when they can add value, avoiding unnecessary
executions on non-applicable records?

     •   ☐ YES - ☐ NO - ☐ N/A

Cost Optimization – Runtime Optimization

Q6: Which consumption optimization strategies are addressed for this workflow? (Check if implemented OR if you
evaluated and determined it's not applicable)

     •   ☐ Recursive loop protections prevent wasteful assist consumption
     •   ☐ Prompts optimized to minimize unnecessary tool invocations
     •   ☐ Skills are used for data-intensive operations to speed execution
     •   ☐ Reusable workflows chained together when they have a dependent relationship to reduce Assist
       consumption

Cost Optimization – Assists Monitoring

Q7: Is assist consumption tracked using AI Agent Analytics to identify optimization opportunities?

     •   ☐ YES - ☐ NO

Value Measurement

Q8: Do you measure the business value delivered by this workflow? Value can be measured using time savings,
fulfiller productivity, workflow automation, or self-service outcomes.

     •   ☐ YES - ☐ NO - ☐ N/A

Q9: Do you measure revenue or growth impact delivered by this workflow? Revenue impact can include lead
conversion, upsell/cross-sell acceleration, reduced churn, higher sales capacity, or improved customer lifetime
value.

     •   ☐ YES - ☐ NO - ☐ N/A

                                                                                       39

---

<!-- page_40 -->
## Page 40

Leading Practices

Strategic Deployment for ROI (Questions 1-3)

Strategic Use Case Prioritization

Not all use cases are created equal – a small number will drive much of your AI value. Prioritize use cases along
two dimensions: feasibility (technical readiness, data availability, process maturity) and anticipated business
value. Start with use cases that score high on both. These use cases are your quick wins that build momentum,
prove ROI early, and fund what comes next. Over time, high-value use cases that initially lacked feasibility will
become achievable as your platform matures, your team gains experience, and enabling capabilities come online.
Ensure that you’re revisiting your pipeline quarterly to catch these shifts.

Meanwhile, don't discard low-value but highly feasible use cases entirely. Use cases falling into this category are
valuable for team training, hackathons, and building hands-on confidence with agentic patterns and could be
deployed if they still possess a positive ROI. What you want to avoid is spending cycles on use cases that are
neither valuable nor feasible. ServiceNow data shows that across 500+ AI use cases, 43% involve workflow
automation for low-complexity scenarios and 37% address complex workflows. Avoid stretch use cases or “art of
the possible” projects – they typically score high on the value axis but are complex and delay showing meaningful
progress to leadership. Instead, balance learning and quick wins first. Expand deliberately, and over time those
stretch initiatives will be within reach.

Right-Size Solution Complexity

For multi-step workflows that can be improved with the assistance of GenAI and have finite or well-defined output,
consider prompt chaining with custom skills. Prompt chaining breaks complex tasks into a sequence of discrete
steps where the output of one skill becomes the input to the next in the chain. Each skill is scoped to a single, well-
defined job, producing more reliable results versus asking a single skill to handle everything at once. Since each
step runs as a single skill rather than an agentic workflow, the premium for AI Agents can be avoided. To put this in
perspective, a small agentic workflow (the smallest tier) consumes 25 Assists per execution. If a similar outcome
can be achieved by chaining a couple micro skills together (consuming 1 or 2 Assists each) and the workflow
maintains similar value, assist consumption improves by 85-90%.

When in doubt, validate that the agentic approach is appropriate for your use case. Examples where simpler
solutions are better include single KB article lookups, basic field updates, and standard routing tasks.

Agent Portfolio Management

Conduct regular reviews at least quarterly to assess performance metrics, business value delivered and assist
consumption efficiency. Identify underutilized agents through analytics and decommission those no longer
providing value, while reallocating assists from low-value to high-value agents. Calculate the payback period as
agent development cost ÷ annual value delivered, and phase rollouts by starting with 2-3 workflows, measuring
ROI, then expanding based on results.

Development Cost Optimization (Question 4)

AI Agents can use tools including Flow actions, subflows, Virtual Agent topics, catalog items, and skills. Leverage
your existing investment in the platform to iterate on AI Agents quickly without duplication of effort. Before building
new tools, inventory existing platform assets by searching Flow Designer, Skill Kit, and Catalog Item registry to
identify reusable components.

                                                                               40

---

<!-- page_41 -->
## Page 41

Trigger Invocation Efficiency (Question 5)

Design trigger conditions to invoke agents only when they add value, avoiding unnecessary executions on non-
applicable records. Every agent invocation consumes assists, so precision filtering prevents waste.

Runtime Optimization (Question 6)

Prompt Optimization

Well-structured prompts reduce unnecessary tool invocations through conditional logic and validation gates. For
example, prompts that check prerequisites before making further tool invocations ("If incident not found, finish
execution") prevent wasteful action consumption.

Workflow Consolidation

When the output of one workflow becomes the input to the next workflow, consolidate them into a single
execution to reduce assist consumption.

Example:

Single Tool Invocation:

     •     “Categorize Incident" workflow completes → Output triggers "Route Incident" workflow
     •     Tool Invocations: 2 Actions Consumed

Super Tool Invocation:

     •     "Categorize and Route Incident" combined workflow
     •     Tool Invocations: 1 Action Consumed (50% reduction)

When to consolidate:

Workflows with dependent relationships where the output of one always becomes the input to the next.

When to keep separate:

Workflows that run independently or are reused by multiple upstream processes.

Leverage Skills & Components to Reduce Consumption

Skills used as tools do not consume Assists but do count toward workflow sizing (Small, Medium, Large), so
architect workflows to use skills for repetitive operations. Build reusable components that can be called by
multiple agents, offloading static logic to skills while reserving agent consumption for dynamic reasoning.

For agents processing large datasets, use Skill Kit to speed up execution and limit LLM calls by offloading heavy
data operations such as filtering, transformation, and aggregation to custom skills. Skill Kit custom skills are
reusable and don’t weigh down agent instructions, making them particularly effective for agents with complex
data processing requirements.

Loop Prevention for Cost Control

Implement a three-layer strategy to prevent wasteful assist consumption:

       1.   Trigger selection - avoid combining incompatible triggers

                                                                                                      41

---

<!-- page_42 -->
## Page 42

2.   Filter conditions – use Assignment Group, custom flag or other pattern to ensure a loop-breaking field is
        modified before updating the record
     3.  Recursive checks – ensure the safety nets such as 50 record creates per 15 minutes or 5 updates per 15
        minutes are active in your AI Agent properties based upon instance and store plugin versions

Monitor Status and Assist Consumption dashboards during development, and test with 5-10 records in sub-
production to catch loops when they are still inexpensive to fix.

Important: If a loop is detected, deactivate the trigger immediately, analyze the root cause, and redesign the
workflow before reactivating.

Consumption Monitoring (Question 7)

Track Assist Consumption

Use the AI Agent Analytics Assist Consumption dashboard to monitor usage per workflow and review the top 10
workflows consuming the most assists. Validate that consumption is justified by the value delivered, set up alerts
for consumption spikes that may indicate potential loops or inefficient design, and compare consumption against
budget forecasts regularly.

AI Agent Analytics: Production Monitoring

Status Dashboard:

The Status Dashboard displays execution plans with their state (Completed, In Progress, Failed), duration, and
timestamp. It also shows execution counts by workflow and agent, providing real-time execution monitoring.

Assist Consumption Dashboard:

The Assist Consumption Dashboard provides a graphical representation of assists consumed over time, identifies
the top 10 agentic workflows consuming the most assists, and tracks assists consumed per workflow and agent.
Watch for warning signs including a single agent with multiple invocations, sudden consumption spikes, or a single
workflow consuming unusually high assists.

Value Measurement Using AI Value Framework (Questions 8-9)

AI Agent-Specific Time Benchmarks (Illustrative Examples):

These benchmarks serve as reference examples for calculating value. Your actual time savings may vary based
on process complexity and organizational context:

     •    Automated agentic workflow: 15 minutes saved per successful execution
     •    Agent work action: 8.3 minutes saved per comment, work note, or record update
     •      Virtual Agent conversation (when using AI Agents): 11.32 minutes saved per successful conversation

Core Value Metrics:

Agent Productivity Score – Measures combined human + AI output against theoretical human maximum

     •     Formula: (Human agent actions + AI agent actions) ÷ Maximum possible human actions per hour
     •    ServiceNow benchmark: AI typically completes 40-45% of work actions when implemented effectively

                                                                                       42

---

<!-- page_43 -->
## Page 43

Workflow Automation Score – Measures percentage of work automated by AI

     •     Formula: AI agent work actions ÷ Total work actions on workflow
     •    ServiceNow benchmarks: 43% for low-complexity cases, 37% for complex cases

Self-Service Efficiency Score – Measures deflection effectiveness

     •     Formula: AI self-service interactions ÷ (AI self-service + live support requests)
     •     Target: 60%+ indicates strong deflection

Hours Saved – Translates time to capacity

     •     Formula: (Number of workflows per month × Minutes saved per workflow) ÷ 60
     •      Interpretation: Hours saved = capacity freed for strategic work, not just cost reduction

Financial Conversion

     •     Formula: Time saved (minutes) × Frequency × Cost per employee hour = Dollar value
     •     Example: 1,000 workflows × 15 min × $50/hr ÷ 60 = $12,500 monthly value

For detailed calculation methodology and additional worked examples, see AI Value Framework whitepaper pp. 5-
22.

Measure Acceptance Rates

Track the percentage of AI-generated content accepted by human agents without modification, as ServiceNow
benchmarks indicate that 60-100% acceptance rates are typical. Low acceptance rates (below 50%) suggest a
need for prompt refinement or additional grounding, so use acceptance data to continuously improve agent
quality.

Common Pitfalls
     •    Not establishing baseline metrics before deployment
     •      Failing to track business value metrics (time saved, deflection rates)
     •     Rebuilding functionality that already exists in Flow Designer, Skill Kit, or Catalog Items instead of reusing
        platform assets
     •    Broad trigger conditions causing agents to execute on non-applicable records, wasting assists
     •    Not consolidating dependent workflows, leading to multiple assist charges for sequential operations
     •    Not monitoring assist consumption for cost control, leading to budget overruns
     •     Using agentic AI for simple single-step tasks better suited for skills or flows
     •      Failing to measure actual business value and time saved (no ROI justification)
     •    Not identifying and stopping recursive loops quickly (expensive waste)
     •    Not tracking acceptance rates to validate AI-generated content quality
     •     Deploying on low-volume use cases with minimal ROI potential
     •    Not calculating financial value (time saved but no dollar conversion)
     •    Keeping underutilized agents running without regular portfolio review

                                                                                    43

---

<!-- page_44 -->
## Page 44

Pillar 6: User Experience

Overview

Exceptional user experience ensures agents are accessible, transparent, conversational, and deliver value
efficiently through intuitive interactions across multiple channels.

Design Principles

Channel Accessibility

Agents can be made accessible through multiple channels including the Now Assist Panel, Now Assist in Virtual
Agent, voice interfaces, UI actions, autonomous triggers, APIs, and Flows. Typically, developers should align the
channel with the persona who needs to leverage the Agent. For instance, triggers or the Now Assist Panel are
generally appropriate for fulfillers, Now Assist in Virtual Agent for most employees, and voice agents for deskless
workers (e.g., factory or hospital floor users).

Human Supervised Tools

Risk assessment during planning determines the appropriate level of AI Agent autonomy. A common risk-based
pattern is to configure AI Agents for autonomous read operations while requiring supervised tools (human
approval) for write or update operations. Developers and teams analyzing risk may put limits on what users can
accomplish autonomously to prevent unauthorized or high-impact changes.

Trade-off Consideration: Requiring human approval for actions limits value realization, as automation velocity
slows to the speed of the human-in-the-loop approver. However, this trade-off is often appropriate for managing
risk while building confidence in agent behavior.

Maturity Progression Pattern: Many customers start with supervised tools, battle-test the agent in production while
monitoring approval patterns, then toggle tools to autonomous once results are consistently approved without
modification. This graduated autonomy approach balances safety with scaling automation value over time.

Transparency & Clear Communication

Agent capabilities should be clearly communicated in the agent description and role definition so that users can
discover agents. Ensure outcomes are reported clearly through success and failure notifications.

Conversational Design Patterns

Design for natural language interaction where agents understand user intent from conversational descriptions.
The orchestrator handles sentiment analysis and understands affirmative and negative responses (e.g., “yes,”
“no,” “looks good,” “cancel that”). Use progressive disclosure by gathering information as needed throughout the
conversation rather than requesting everything upfront.

Assessment Questions

Accessibility & Discovery

Q1: Is this workflow accessible through its intended channel with proper configuration?

                                                                                 44

---

<!-- page_45 -->
## Page 45

•   ☐ YES - ☐ NO - ☐ N/A

Q2: Are agent names unique with no overlap causing orchestrator confusion (e.g., two agents both containing
“task analyzer”)?

     •   ☐ YES - ☐ NO - ☐ N/A

Q3: Can users easily find and invoke agents for their use cases without specialized knowledge?

     •   ☐ YES - ☐ NO - ☐ N/A

Interaction Design

Q4: How do you provide clear feedback and enable iterative refinement? (Select all that apply)

     •   ☐ Users can provide feedback to iteratively refine agent responses
     •   ☐ Critical actions require confirmation with outcome communicated to user
     •   ☐ N/A – Agent runs autonomously

Q5: Is the output format specified clearly (HTML, Markdown, numbered lists)?

     •   ☐ YES - ☐ NO - ☐ N/A

Q6: Do agents avoid referring to users by title/role in prompts (use “user” not “Service Desk Agent”)?

     •   ☐ YES - ☐ NO - ☐ N/A

Q7: For high-risk actions, are supervised tools configured requiring explicit user approval before execution?

     •   ☐ YES - ☐ NO - ☐ N/A

Communication & Transparency

Q8: How do you ensure transparent communication and appropriate escalation? (Select all that apply)

     •   ☐ Agent conversational outputs clearly communicate capabilities and constraints
     •   ☐ Escalation paths documented for when agents cannot complete tasks
     •   ☐ Clear next steps or action menus provided when multiple options exist
     •   ☐ N/A – Agent runs autonomously

Q9: Is agent output professional, conversational, and formatted appropriately for audience (technical vs. business
users)?

     •   ☐ YES - ☐ NO - ☐ N/A

                                                                                   45

---

<!-- page_46 -->
## Page 46

Leading Practices

Accessibility & Discovery (Questions 1-3)

Agent Discovery & Description

Write detailed agent descriptions using natural language explaining the AI Agent’s purpose, inputs, expected
outcomes. Highlight the uniqueness of each agent to differentiate from similar agents. The AI Agent description is
used by the orchestrator to discover and run agents in the Now Assist Panel or Virtual Agent. Ensure agent names
don’t overlap by avoiding naming multiple agents similarly. Two agents both containing "task analyzer" in their
names causes orchestrator confusion. Make names clearly distinct: "Incident Categorizer" vs "Case Categorizer"
or use a single generalized "Task Analyzer" if one agent handles all task types. Users shouldn’t need specialized
knowledge to locate an appropriate agent, so make agents easily discoverable and validate through user
acceptance testing.

Multi-Channel Accessibility

Make agents accessible through channels appropriate to the use case: Now Assist Panel for fulfillers, Now Assist
for Virtual Agent for employees, customers, or other requesters, voice for phone-based interactions, or UI Action
for on-demand invocation.

Interaction Design (Questions 4-7)

User Feedback & Iterative Refinement

Design clear interaction patterns for user input such as “Ask user to provide Incident number…” for data requests
and “Ask user for approval before continuing to next step” for authorization checkpoints. Enable iterative
refinement with instructions like “Refine output with user guidance and repeat until user is satisfied,” as the
orchestrator automatically understands sentiment signals including “yes,” “no,” “looks good,” and “change X.”
Create action menus that list multiple options for the user to select, with each option having its own instruction
section.

Supervised Tools for High-Risk Actions

Configure specific tools to run in Supervised mode, requiring explicit user approval for high-risk actions such as
sending emails, creating change requests, deleting records, or modifying critical fields. Use Autonomous mode for
low-risk actions like reading data, searching the knowledge base, or analyzing patterns. Always inform users of
outcomes by including instructions such as “After executing the tool, inform the user of the outcome (completed
or failed) based on tool output.”

Output Formatting & Consistency

Specify exact output formats within agent instructions. For error messages, provide the literal text the agent should
use (e.g., 'If Incident not found, inform user: "The Incident record could not be found."'). For structured outputs,
specify the format explicitly (e.g., 'Present as numbered list: 1. First step 2. Second step'). If using HTML or
Markdown formatting, include a representative example directly in the instructions so the agent understands the
expected structure.

Avoid User Role References in Prompts

                                                                                    46

---

<!-- page_47 -->
## Page 47

Use “user” instead of specific role titles in agent instructions. As an example, “Ask user for details” rather than “Ask
Service Desk Agent Tier II for details”. This prevents orchestrator confusion when users have different titles.

Communication & Transparency (Questions 8-9)

Clear Agent Descriptions & User-Facing Communication

Agent descriptions should clearly communicate purpose, capabilities, and constraints, while agent outputs should
set appropriate expectations through conversation (e.g., “I specialize in IT security incidents. I can analyze security
incidents and recommend remediation. For other requests, I’ll need to escalate to a different specialist”). Note that
the agent “role” field is primarily for internal and architectural use – users typically interact with agents through
descriptions, names, and conversational outputs, so document capabilities and limitations in agent descriptions to
support orchestrator matching.

Escalation Paths & Handoffs

Document when agents should escalate to humans – for example, when the task is too complex, the agent has
insufficient permissions, or the user explicitly requests human assistance. Include clear escalation instructions
such as 'If unable to resolve, escalate to: [human group/contact].' Also document alternative workflows so agents
have a defined backup plan when the primary path is blocked.

Action Menus & Next Steps

Provide clear next steps when multiple options exist (e.g., “Ask user which action to perform—always include ‘Add
Comment’ as an option and allow the user to skip if no action is desired”). Present options in numbered format for
clarity and allow users to skip or exit gracefully.

Confirmation Patterns for Critical Actions

Use mandatory confirmations for transparency – for example, “After executing Add Comment, inform the user of
the outcome (completed/failed) based on the tool output”. For high-impact actions, use supervised tools which
require user approval before acting. If the default approval prompt lacks sufficient context, instruct the agent to
proactively provide a more detailed explanation of what it intends to do when requesting approval. Once the
action is complete, have the Agent confirm what was done and provide receipt or reference.

Professional & Audience-Appropriate Tone

Include tone instructions in the AI Agent prompts such as 'professional yet conversational' or 'empathetic
technical translator,' adapting language for the intended audience — technical details for IT staff, business
language for executives. Avoid jargon when communicating with non-technical users and maintain a professional
tone even when delivering bad news or error messages.

Channel Configuration

Virtual Agent Channel Setup

Enable the Virtual Agent experience toggle in AI Agent Studio under “Select channels and status,” and activate the
AI Agents skill in the Assistant’s Skills setup page. Ensure the agent description is detailed enough for the
orchestrator to match user natural language queries to an agent and use a model provider other than NowLLM
(recommended for Virtual Agent integration). Test discovery by typing queries in Virtual Agent to validate that the
agent matches correctly.

                                                                                         47

---

<!-- page_48 -->
## Page 48

User Testing & Feedback Collection

Test with actual users before production deployment and collect feedback on clarity of agent responses, ease of
providing input, and satisfaction with outcomes. Measure adoption through usage frequency, successful
completion rates, and escalation rates to humans, while tracking user satisfaction using inferred CSAT from the AI
Value Framework.

Common Pitfalls
     •    Vague agent descriptions causing the orchestrator to select wrong agent
     •    Not informing users when actions complete (success or failure)
     •     Referring to users by role (“Service Desk Agent”) instead of “user” in prompts
     •    Not enabling Virtual Agent toggle when agent should be discoverable in VA
     •     Creating conversation dead-ends with no next steps or escalation options
     •    Not allowing users to refine agent responses iteratively
     •     Overly technical language in outputs for business users
     •    Not configuring supervised tools for high-risk actions
     •    Assuming users understand what agents can do without clear communication

Running and Scoring the Framework Assessment

This Well-Architected Review supports three complementary usage modes that align with the Agent Development
Lifecycle. Each mode serves different stakeholders and objectives.

Mode 1: Pre-Build Design Guidance (Preventive)

Use this framework before building new agents to incorporate best practices from the start and minimize post-
build remediation.

Target Audiences:

     •     AI architects designing new agentic workflows
     •    Prompt engineers structuring agent instructions
     •     Platform owners planning agent deployments
     •    Development teams building tools and integrations
     •     Business analysts defining use cases

When to Use:

     •     During ADLC Discover & Plan phase (use case qualification)
     •     During ADLC Design phase (architecture decisions)
     •     At project kickoff before any development work begins
     •    When scoping new automation opportunities

How to Use:

     •    Step 1: Review relevant Design Principles
           §   Before building, read Design Principles sections for pillars applicable to your planned workflow

                                                                                  48

---

<!-- page_49 -->
## Page 49

•    Step 2: Use Leading Practices as build reference
           §   Keep Leading Practices sections accessible during development as implementation guides
     •    Step 3: Convert Assessment Questions into design checklist
           §   Use assessment questions as proactive design requirements rather than reactive audits. Build
              these requirements into your development workflow from day one.
     •    Step 4: Set quality gates using Assessment Questions
           §   Integrate framework questions as quality gates in your ADLC process:

Expected Outcome:

If you integrate 60-70% of best practices during initial build:

     •     Post-build assessment likely scores 80-90% (Advanced maturity)
     •    Remediation reduced to quick wins (hours, not weeks)
     •     Faster time to production
     •     Higher quality from day one

The goal isn't perfection on the first attempt but rather to build a strong foundation that minimizes expensive post-
build rework.

Mode 2: Post-Build Assessment & Validation

Use this framework after building agents to validate production readiness and identify improvement opportunities.

Target Audiences

     •     Platform owners conducting pre-production reviews
     •    Governance teams approving deployments
     •     Operations teams validating readiness
     •    Compliance officers ensuring policy adherence
     •     AI or Data Stewards and AI Control Tower administrators

When to Use:

     •     After ADLC Build phase, before production deployment
     •    When evaluating existing production workflows for optimization
     •     Before major agent modifications or platform upgrades
     •     During security audits or compliance reviews
     •    When troubleshooting performance or cost issues

How to Use:

     •    Step 1: Conduct formal assessment and work through framework systematically
           §   Answer all questions for this specific workflow
           §   Mark N/A for features not applicable (external integrations, RAG, encryption)
           §  Be honest – this is diagnostic, not performative
           §   Involve cross-functional team (security, operations, business owner)
     •    Step 2: Calculate Score by following the methodology in Appendix A
           §   Multi-select questions: Count checked boxes

                                                                                    49

---

<!-- page_50 -->
## Page 50

§  YES/NO questions: 1 or 0 points
           §   Total checkmarks
           §   Calculate: Total checkmarks ÷ (Total possible - N/A questions)
           §   Determine maturity level (>90%, 80-90%, 70-80%, 60-70%, <60%)
     •    Step 3: Check Critical Pillar Requirement and regardless of overall score, verify
           §   Security (Pillar 2): ≥95% required
           §    Reliability (Pillar 3): ≥90% required
           §      If either fails: your workflow does NOT meet threshold for production, even with high overall score
           §   See Appendix A Section 5 for override logic and examples.
     •    Step 4: Review Assessment Results
        Analyze your scores to understand strengths and gaps:
           §    Identify lowest-scoring pillar – this indicates highest concentration of gaps
           §   Note score proximity to thresholds – 89% is one quick win from 90%
     •    Step 5: Route to Implementation Roadmap
       Based on your maturity level, follow appropriate remediation path (see Appendix A):
           §   90%: Deploy immediately
           §   80-90%: Quick wins available
           §   70-80%: Focused improvement needed
           §   <70%: Comprehensive remediation required
           §    Critical pillar failure: Address immediately regardless of overall score.
     •    Step 6: Document Findings and create assessment record including:
           §   Overall score and pillar-specific scores
           §   N/A justifications (why features not applicable)
           §    Identified gaps
           §   Remediation plan with ownership
           §   Target reassessment date

Mode 3: Continuous Improvement & Governance

Use this framework quarterly for ongoing optimization, governance, and compliance monitoring when the solution
is improved or your security posture becomes more stringent.

Summary: Choosing Your Mode

     •     Starting new agent project? → Mode 1 (Pre-Build Design Guidance)
     •    Agent built, ready for validation? → Mode 2 (Post-Build Assessment)
     •    Agent in production for 3+ months? → Mode 3 (Continuous Improvement)

All three modes reinforce each other:

     •     Pre-build guidance reduces post-build remediation
     •     Post-build assessment validates design decisions
     •     Continuous improvement drives sustained excellence
Most effective approach: Use all three modes as part of integrated governance practice.

                                                                                 50

---

<!-- page_51 -->
## Page 51

Appendix A: Assessment & Scoring Guide

Total Questions: 72

The assessment includes:

     •       Pillar 1: 12 questions – up to 26 checkboxes
     •       Pillar 2: 20 questions – up to 35 checkboxes
     •       Pillar 3: 13 questions – up to 17 checkboxes
     •       Pillar 4: 9 questions – up to 19 checkboxes
     •       Pillar 5: 9 questions – up to 12 checkboxes
     •       Pillar 6: 9 questions – up to 12 checkboxes

Total Maximum Score: 121 checkboxes (varies based on conditional N/A selections)

   Skip the Manual Math
   Rather than calculating scores by hand, an interactive version of this assessment is available through
   ServiceNow's AI Center of Excellence. The tool automatically scores your responses, applies N/A exclusions,
   flags critical pillar thresholds, and produces a gap list – all aligned to the methodology described in this
   appendix. Contact your ServiceNow Account Team or Impact Team to request access or to schedule an
   interactive session.

Design Principles and Leading Practices

Use Design Principles to answer the assessment questions and Leading Practices for more details. This format
makes it easy to reference supporting information when answering questions and is consistently structured
across all pillars.

Recommended Frequency
     •       Initial assessment after building but before production launch (conduct alongside Agentic Evaluations)
     •      Iterative reassessment during remediation until achieving production-ready maturity
     •     Quarterly reviews for established workflows
     •    Ad-hoc assessment after major changes, performance issues, or security incidents

How to Score Questions

Multi-Select Questions

Each checkbox = 1 point. Check all practices that apply to your workflow.

Example:

How do you ensure agent architecture follows design best practices? (Select all that apply)

     •   ✓ Each agent has clearly documented purpose distinguishing it from other agents

                                                                                                         51

---

<!-- page_52 -->
## Page 52

•   ✓ Agents kept at 15 tools or fewer unless performance testing justifies higher count
     •   ☐ Multiple prompt versions maintained in AI Agent Studio for experimentation/rollback
     •   ✓ Tools organized strategically in multi-agent workflows (by data domain, workflow phase, or shared
       dependencies)

Score: 3 out of 4 possible points

Standalone YES/NO Questions
     •    YES = 1 point
     •   NO = 0 points
     •    N/A = excluded from both numerator and denominator

Example:

Have you identified the critical Knowledge Base articles for your use case?

     •   ✓ YES - ☐ NO - ☐ N/A

Score: Yes checked = 1 point

N/A Handling

Questions marked N/A are excluded from BOTH numerator and denominator (not counted against you).

Example:

Have you identified the critical Knowledge Base articles for your use case?

     •   ☐ YES - ☐ NO - ✓ N/A
(Search retrieval tool not used in the use case being evaluated)

Score: Questions marked as N/A should be completely excluded from scoring

Calculating Your Score

Formula:

Score = Total checkmarks ÷ (Total possible checkmarks - N/A questions)

Example 1: Internal Workflow

     •     Total possible checkboxes: 121
     •    Checkboxes Marked N/A: 12
     •     Applicable checkboxes: 109
     •    Your checkmarks: 94
     •    Score 94 ÷ 109 = 86.2% Advanced

Example 2: Customer-Facing Workflow

                                                                                         52

---

<!-- page_53 -->
## Page 53

•     Total possible checkboxes: 121
     •    Checkboxes Marked N/A: 4
     •     Applicable checkboxes: 117
     •    Your checkmarks: 108
     •    Score 108 ÷ 117 = 92.3% Production Ready

Note: These are illustrative examples only. Actual scores depend on your specific workflow implementation and
feature usage.

Maturity Levels

 Score Range   Maturity Level   Assessment                 Recommended Action

 >90%          Production    Demonstrates comprehensive       Deploy with confidence. Minor gaps
              Ready         implementation of best practices     represent optimization opportunities,
                              across all applicable pillars. Meets    not blockers.
                                threshold for enterprise production
                             deployment.
 80-90%      Advanced -    Demonstrates strong foundational    Focus remediation on highest-impact
                    Prioritize      competency with identified         gaps to achieve Production Ready
               Quick Wins    improvement areas. Meets             status. Prioritize practices requiring
                                threshold for limited production      minimal effort for maximum
                             deployment.                      improvement.
 70-80%        Functional -    Demonstrates basic competency     Address systematic deficiencies in
            Room for      but exhibits notable gaps in           lowest-scoring pillars. Suitable for
              Improvement  systematic implementation.            limited production with enhanced
                              Requires focused improvement       monitoring. Develop remediation
                               before broad deployment.          roadmap before scaling.
 60-70%        Material       Demonstrates significant            Delay broad deployment. Conduct
               Remediation    architectural gaps across multiple    focused workshops on Security (Pillar 2)
               Required         pillars. Does not meet threshold for   and Reliability (Pillar 3) first. Requires
                               production deployment.               architectural redesign in deficient areas.
 <60%        Does Not      Demonstrates critical deficiencies   Do NOT deploy to production. Conduct
              Meet            that present unacceptable risk. Full   comprehensive architectural review.
                Threshold      stop on production deployment      Engage ServiceNow experts for guided
                                  required.                            remediation. Restart assessment after
                                                                      foundational rework.

Critical Pillar Requirements

Regardless of overall score, workflows must achieve:

     •     Security & Compliance (Pillar 2): ≥ 95% - Security controls are not negotiable
     •      Reliability (Pillar 3): ≥ 90% - Loops and failures are production-blocking

                                                                                      53

---

<!-- page_54 -->
## Page 54

Override Logic

A workflow scoring 92% overall but only 88% on Security does NOT meet the threshold for production
deployment.

Example Scenario:

     •     Overall Score: 92% (Production Ready range)
     •       Pillar 1: 95%
     •       Pillar 2: 88% ✗ (Below 95% requirement)
     •       Pillar 3: 94%
     •       Pillar 4: 90%
     •       Pillar 5: 96%
     •       Pillar 6: 93%

Result: Does NOT meet threshold - Security gaps block production deployment despite high overall score.

                                                                                   54

---

<!-- page_55 -->
## Page 55

Appendix B: Further Reading & Resources

ServiceNow Resources

Whitepapers
     •     AI Value Framework: How ServiceNow Measures the Value of AI (2025)
     •     Data Encryption on the ServiceNow AI Platform: Encryption for Data at Rest and Data in Transit (March
        2025, Zurich release)
     •     Responsible AI: How ServiceNow is Committed to Developing and Delivering Responsible AI Solutions
        (February 2026, Zurich release)
     •    ServiceNow Security Best Practices Guide: Key Considerations for Securing ServiceNow Instances
       (November 2025, Zurich release)
     •    ServiceNow Shared Responsibility Model (December 2025, Zurich release)

ServiceNow AI Agent Guides
     •   Now Assist AI Agents Prompting Guide (2025, Yokohama and Zurich releases) by Victor Chen
     •   MyNow – Includes AI Agent Implementation Guides for Get Started, Initiate, Plan, Execute and Deliver
       Phases

ServiceNow Product Documentation
     •   Now Assist AI Agents
     •     AI Control Tower
     •     Agentic Evaluations

ServiceNow Community Articles
Articles authored by ServiceNow Product Management or members of the ServiceNow AI CoE
     •    Advanced AI Agent Instructions Guide: ServiceNow Edition – Dan Andrews, ServiceNow
     •     AI Agent Practical Implementation: Lessons from the Field – Natalia Heel, ServiceNow AI CoE
     •     AI Agent Testing: Building Trust in Uncertainty – Xavier Gouy, ServiceNow AI CoE
     •     AI Agents FAQ and Troubleshooting – Victor Chen, ServiceNow
     •     Best Practices to Use Your Knowledge Articles with Now Assist – Ashley Snyder, ServiceNow
     •    Deploy AI Agents with Confidence Using Agentic Evaluations – Ashley Snyder, ServiceNow
     •     Enable MCP and A2A for Your Agentic Workflows – Victor Chen, ServiceNow
     •   How Governance Can Accelerate the Adoption of AI Agents – Edwin Jaspers, ServiceNow AI CoE
     •     Latest Access Control Security Enhancements for AI Agents – Victor Chen, ServiceNow
     •     Limit Assist Consumption by Designing AI Agents Which Avoid Loops – TJ Lincoln, ServiceNow AI CoE
     •   Now Assist for CSM: Agentic Workflows and AI Agents – Fernando Castro, ServiceNow
     •    ServiceNow AI Control Tower in the Zurich Release – Usman Sindhu, ServiceNow
     •     Try the Now Assist AI Agent MCP Client with These Official MCP Servers – Victor Chen, ServiceNow
     •    When to Use AI Agents: Rationalizing Use Cases for Workflows – TJ Lincoln, ServiceNow AI CoE

                                                                                     55

**Links on this page:**

- [papers AI Value Framework: How ServiceNow Measures the Value of AI (2 Data Encryption on the ServiceNow AI Platform: Encryption for Da](https://www.servicenow.com/standard/resource-center/white-paper/wp-ai-value-framework.html)
- [https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-data-encryption-with-servicenow.pdf](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-data-encryption-with-servicenow.pdf)
- [2025, Zurich release) Responsible AI: How ServiceNow is Committed to Developing and Delivering Responsible AI Solutions (February 2026, Zurich release](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-sn-responsible-genai.pdf)
- [February 2026, Zurich release) ServiceNow Security Best Practices Guide: Key Considerations for Securing ServiceNow Instances (November 2025, Zurich release](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/instance-security-best-practice.pdf)
- [November 2025, Zurich release) ServiceNow Shared Responsibility Model (D](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-shared-responsibility-model.pdf)
- [ceNow AI Agent Guides Now Assist AI Agents Prompting Guide (2 MyNow – Includes AI Agent Implementa](https://www.servicenow.com/community/now-assist-articles/now-assist-ai-agents-prompting-guide/ta-p/3386242)
- [Now Assi MyNow – Phases](https://mynow.servicenow.com/now/mynow/my-home/home)
- [ceNow Product Docu Now Assist AI Agents AI Control Tower](https://www.servicenow.com/docs/r/zurich/intelligent-experiences/na-ai-agents.html)
- [Now Assist AI Age AI Control Tower Agentic Evaluation](https://www.servicenow.com/docs/r/zurich/intelligent-experiences/ai-control-tower/ai-control-tower-home-page.html)
- [AI Control Tower Agentic Evaluations](https://www.servicenow.com/docs/r/zurich/intelligent-experiences/execute-aia-eval.html)
- [authored by ServiceNow Product Management or members o Advanced AI Agent Instructions Guide: ServiceNow Edition – AI Agent Practical Implementation: Lessons from the Field](https://www.servicenow.com/community/now-assist-articles/advanced-ai-agent-instructions-guide-servicenow-edition/ta-p/3346578)
- [Advanced AI Agent Instructions Guide: ServiceNow Edition AI Agent Practical Implementation: Lessons from the Field – AI Agent Testing: Building Trust in Uncertainty – Xavier Gouy](https://www.servicenow.com/community/now-assist-articles/ai-agent-practical-implementation-lessons-from-the-field/ta-p/3339826)
- [AI Agent Practical Implementation: Lessons fro AI Agent Testing: Building Trust in Uncertainty – AI Agents FAQ and Troubleshooting – Victor Ch](https://www.servicenow.com/community/now-assist-articles/ai-agent-testing-building-trust-in-uncertainty/ta-p/3351244)
- [AI Agent Testing: Building Trust in Unc AI Agents FAQ and Troubleshooting – Best Practices to Use Your Knowledge](https://www.servicenow.com/community/now-assist-articles/ai-agents-faq-and-troubleshooting/ta-p/3200454)
- [https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219](https://www.servicenow.com/community/knowledge-management-articles/best-practices-to-use-your-knowledge-articles-with-now-assist/ta-p/2824219)
- [https://www.servicenow.com/community/now-assist-articles/deploy-ai-agents-with-confidence-using-agentic-evaluations/ta-p/3428937](https://www.servicenow.com/community/now-assist-articles/deploy-ai-agents-with-confidence-using-agentic-evaluations/ta-p/3428937)
- [Deploy AI Agents with Confidence Using Agentic Ev Enable MCP and A2A for Your Agentic Workflows – How Governance Can Accelerate the Adoption of A](https://www.servicenow.com/community/now-assist-articles/introducing-ai-agent-fabric-enable-mcp-and-a2a-for-your-agentic/ta-p/3373907)
- [Enable MCP and A2A for Your Agentic Workflows – Victor Che How Governance Can Accelerate the Adoption of AI Agents – Latest Access Control Security Enhancements for AI Agents](https://www.servicenow.com/community/now-assist-articles/how-governance-can-accelerate-the-adoption-of-ai-agent/ta-p/3338799)
- [How Governance Can Accelerate the Adoption of AI Agents – Latest Access Control Security Enhancements for AI Agents – Limit Assist Consumption by Designing AI Agents Which Avoid](https://www.servicenow.com/community/now-assist-articles/latest-access-control-security-enhancements-for-ai-agents-and/ta-p/3374036)
- [https://www.servicenow.com/community/now-assist-articles/limit-assist-consumption-by-designing-ai-agents-which-avoid/ta-p/3450013](https://www.servicenow.com/community/now-assist-articles/limit-assist-consumption-by-designing-ai-agents-which-avoid/ta-p/3450013)
- [Limit Assist Consumption by Designing AI Agents Which Now Assist for CSM: Agentic Workflows and AI Agents – ServiceNow AI Control Tower in the Zurich Release – U](https://www.servicenow.com/community/csm-articles/now-assist-for-csm-agentic-workflows-and-ai-agents/ta-p/3341816)
- [Now Assist for CSM: Agentic Workflows and AI Agent ServiceNow AI Control Tower in the Zurich Release – Try the Now Assist AI Agent MCP Client with These O](https://www.servicenow.com/community/grc-blog/servicenow-ai-control-tower-in-the-zurich-release-mastering-ai/ba-p/3365258)
- [https://www.servicenow.com/community/now-assist-articles/try-the-now-assist-ai-agent-mcp-client-with-these-official-mcp/ta-p/3391677](https://www.servicenow.com/community/now-assist-articles/try-the-now-assist-ai-agent-mcp-client-with-these-official-mcp/ta-p/3391677)
- [Try the Now Assist AI Agent MCP Client with These Official MCP When to Use AI Agents: Rationalizing Use Cases for Workflows](https://www.servicenow.com/community/now-assist-articles/when-to-use-ai-agents-rationalizing-uses-cases-for-workflows/ta-p/3340584)

---

<!-- page_56 -->
## Page 56

Contact & Support

Feedback: Submit framework improvements via the ServiceNow Community

For Tailored Guidance: Contact your ServiceNow Account Team or Impact Team for an interactive session or to
request access to the automated scoring tool

© 2026 ServiceNow, Inc. All rights reserved.

This framework uses official ServiceNow documentation and leading practices. It should be adapted to your
specific requirements, regulatory constraints, and business objectives.

                                                                                      56

---
