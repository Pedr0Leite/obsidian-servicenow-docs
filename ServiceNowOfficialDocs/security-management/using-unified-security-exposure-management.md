---
title: Using Unified Security Exposure Management
description: Unified Security Exposure Management provides a comprehensive platform for managing vulnerabilities and ensuring compliance across your organization. By unifying workflows across Vulnerability Response \(VR\), Application Vulnerability Response \(AVR\), Container Vulnerability Response \(CVR\), and Configuration Compliance \(CC\), you can view all findings in one place, streamline workflows and improve overall efficiency.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/using-unified-security-exposure-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Using Unified Security Exposure Management

Unified Security Exposure Management provides a comprehensive platform for managing [[vulnerabilities|vulnerabilities]] and ensuring compliance across your organization. By unifying workflows across [[vuln-landing-page|Vulnerability Response]] \(VR\), [[avr-landing|Application Vulnerability Response]] \(AVR\), [[cvr-landing|Container Vulnerability Response]] \(CVR\), and [[vr-config-compliance-landing|Configuration Compliance]] \(CC\), you can view all findings in one place, streamline workflows and improve overall efficiency.

-   **[[sem-create-dashboard|Create a dashboard in the Findings view page]]**  
As a vulnerability manager and analyst, create a configured dashboard using the [[sem-visualization-library|visualization library]] widgets, and use the active widgets to drill down to specific findings.
-   **[[now-assist-review-vulnerability-exposure-data|Evaluate vulnerability exposure data with Security Exposure 360]]**  
Use the Security Exposure 360 agentic workflow to review vulnerability data about your environment. Vulnerability analysts and remediation owners can enter questions in plain language and receive comprehensive answers about host, container, and test results vulnerabilities.
-   **[[exploring-ai-security-exposure|Exploring AI Security Exposure Management]]**  
AI Security Exposure Management is a part of the Unified Security Exposure Management product suite of applications. AI Security Exposure Management integrates with third-party AI security products to help you manage various types of potential AI exposure across your environment.
-   **[[sem-insights-skill|Generate vulnerability insights with generative AI]]**  
Use the Security Exposure Management \(SEM\) Insights generative AI skill to provide contextual summaries and actionable recommendations in the Security Exposure Management \(SEM\) Workspace. Use insights based on exposure data, [[threat-intel-landing-page|threat intelligence]], remediation status, and asset context to surface dynamic insights for Findings views. Help admins, analysts, and vulnerability managers prioritize critical risks and take immediate remediation actions.
-   **[[retrieve-vr-data|Retrieve Vulnerability and exposure data with generative AI]]**  
Chat with an AI agent to get help with your questions about Vulnerability Response host and Application Vulnerability Response findings \(vulnerable items and application vulnerable items\).
-   **[[assess-exposure-vr-aiagent|Assess your vulnerability exposure with generative AI]]**  
Chat with an AI agent to help you assess the potential exposure of your configuration items and your business services to vulnerabilities.
-   **[[dedupe-host-vi-now-assist-vulnerability-response|Identify duplicate vulnerable items with generative AI]]**  
Use the Vulnerable item de-duplication generative AI skill to identify the primary \(first-found\) vulnerable items for configuration items along with duplicate vulnerable items that are imported by your vulnerability scanners.
-   **[[now-assist-vr-generating-approvals|Approval recommendations using generative AI]]**  
Learn more about the how the Approval Recommendation generative AI skill arrives at its approval recommendations and the sources it uses to generate them.
-   **[[solutions-now-assist-vulnerability-response|Suggest vulnerability solutions with generative AI]]**  
Use generative the Approval Recommendation generative AI skill to help your analysts find potential preferred solutions from third-party vendors for the vulnerabilities on your assets.
-   **[[sla-targets-vr-aiagent|Analyze vulnerability remediation status with generative AI]]**  
Chat with an AI agent to help you gain insights into your monthly remediation compliance metrics for vulnerable items.
-   **[[using-now-assist-api-connector|Creating an API connector with generative ai]]**  
Use the SPC Setup Connector generative AI skill in USEM to help your developers quickly and automatically create an API connector that you can publish and use in the [[spc-landing|Security Posture Control]] workspace. This skill automatically selects an API template, populates request and header parameters, and maps sample response attributes to SPC attributes based on API documentation you provide.
-   **[[sem-reclassify-unclassed-hardware|Reclassify unclassed hardware]]**  
Reclassify unclassed hardware by updating the lookup rules.
-   **[[sem-workspace-bulk-edit-overview|Bulk edit in the Security Exposure Management Workspace]]**  
In the [[sem-workspace-user-interface|Security Exposure Management Workspace]], the bulk edit feature enables you to update multiple findings simultaneously, streamlining the management and remediation process.
-   **[[sem-ws-list-view|Use the List view in the Security Exposure Management Workspace]]**  
As a vulnerability manager, security manager and analysts, you can view remediation progress on records, drill down into findings, and view the status of their approval requests and exceptions.
-   **[[sem-create-remediation-task|Create a remediation task manually in the Security Exposure Management Workspace]]**  
You can create remediation tasks manually from the findings on the List page of Security Exposure Management Workspace. You can also create remediation tasks from the drill-down lists that appear when you click on the visualizations on the Home page.
-   **[[sem-enable-disable-imports-qualys|Enable or disable the import of test results for a Qualys test group]]**  
In Security Exposure Management Workspace control the import of the test results for the tests in a Qualys test group by using the **Enable/Disable import** button, which is available in the test group's record view.
-   **[[sem-modify-reset-severity|Modify the severity for a CVE or TPE]]**  
As a vulnerability manager or analyst, you can modify the severity level of Common Vulnerability Entry \(CVE\) or Third-party Entry \(TPE\) in the Security Exposure Management Workspace.
-   **[[sem-ws-remed-eff-rcd|Use Remediation Effort records]]**  
When Vulnerability managers and analysts create remediation efforts \(REs\), remediation Tasks \(VUL\) are automatically assigned to IT teams for remediation.
-   **[[sem-approve-requests|Approve or reject requests in the Security Exposure Management Workspace]]**  
Approve or reject requests that are submitted by remediation owners.
-   **[[sem-create-compensatory-control|Add a compensating control to the library]]**  
As a Vulnerability Manager or Analyst, add a list of compensatory controls to the Compensating Controls library in the Security Exposure Management Workspace, which can be applied for the risk reduction of host vulnerable items and remediation tasks.
-   **[[sem-create-remediation-task-examples|Examples for remediation task creation in the Security Exposure Management Workspace]]**  
When you create remediation tasks manually in the Security Exposure Management Workspace, records are grouped into a remediation task based on the grouping criteria you select.
-   **[[sem-exception-management-overview|Exception Management Overview]]**  
When your organization can't comply with a published finding or security policy, standard, or guideline, you can request an exception. Exception management entails requesting, reviewing, approving, or rejecting exceptions to a finding or remediation task \(RT\) that can’t be remediated.
-   **[[sem-approval-view|Unified Approvals View]]**  
The approval process in Security Exposure Management for vulnerability and compliance exceptions is unified to simplify workflows, improve visibility, and streamline actions for Approvers.
-   **[[employee-center-vr-overview|Employee service center for Vulnerability Response]]**  
Employee Service Center provides a standardised approval experience and process for Business Unit Heads, Service Owners, and IT Heads, who may not regularly log in to USEM. It enables them to manage approvals from a central [[location|location]], such as Employee Center Approval Requests, ensuring that requests are routed to the right approvers, decisions are tracked transparently, and actions are completed efficiently. This improves operational efficiency, accountability, and the overall approver experience.
-   **[[sem-approval-rules-overiew|Unified Approval Rules Overview]]**  
The approval rules and approval configuration are unified to provide a consistent approach to managing approval workflows.
-   **[[sem-ws-CRs|Create a change request in the Remediation view]]**  
From a remediation task \(VUL, AVUL, CVUL, or CRG\), create a change request. Alternatively, add a remediation task to an existing change request.

## Related

- [[sem-create-dashboard|Create a dashboard in the Findings view page]]
- [[now-assist-review-vulnerability-exposure-data|Evaluate vulnerability exposure data with Security Exposure 360]]
- [[exploring-ai-security-exposure|Exploring AI Security Exposure Management]]
- [[sem-insights-skill|Generate vulnerability insights with generative AI]]
- [[retrieve-vr-data|Retrieve Vulnerability and exposure data with generative AI]]
- [[assess-exposure-vr-aiagent|Assess your vulnerability exposure with generative AI]]
- [[dedupe-host-vi-now-assist-vulnerability-response|Identify duplicate vulnerable items with generative AI]]
- [[now-assist-vr-generating-approvals|Approval recommendations using generative AI]]
- [[solutions-now-assist-vulnerability-response|Suggest vulnerability solutions with generative AI]]
- [[sla-targets-vr-aiagent|Analyze vulnerability remediation status with generative AI]]
- [[using-now-assist-api-connector|Creating an API connector with generative ai]]
- [[sem-reclassify-unclassed-hardware|Reclassify unclassed hardware]]
- [[sem-workspace-bulk-edit-overview|Bulk edit in the Security Exposure Management Workspace]]
- [[sem-ws-list-view|Use the List view in the Security Exposure Management Workspace]]
- [[sem-create-remediation-task|Create a remediation task manually in the Security Exposure Management Workspace]]
- [[sem-enable-disable-imports-qualys|Enable or disable the import of test results for a Qualys test group]]
- [[sem-modify-reset-severity|Modify the severity for a CVE or TPE]]
- [[sem-ws-remed-eff-rcd|Use Remediation Effort records]]
- [[sem-approve-requests|Approve or reject requests in the Security Exposure Management Workspace]]
- [[sem-create-compensatory-control|Add a compensating control to the library]]
- [[sem-create-remediation-task-examples|Examples for remediation task creation in the Security Exposure Management Workspace]]
- [[sem-exception-management-overview|Exception Management Overview]]
- [[sem-approval-view|Unified Approvals View]]
- [[employee-center-vr-overview|Employee service center for Vulnerability Response]]
- [[sem-approval-rules-overiew|Unified Approval Rules Overview]]
- [[sem-ws-CRs|Create a change request in the Remediation view]]
- [[vulnerabilities|Vulnerabilities]]
- [[vuln-landing-page|Vulnerability Response]]
- [[avr-landing|Application Vulnerability Response]]
- [[cvr-landing|Container Vulnerability Response]]
- [[vr-config-compliance-landing|Configuration Compliance]]
- [[sem-visualization-library|Visualization library]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[spc-landing|Security Posture Control]]
- [[sem-workspace-user-interface|Security Exposure Management Workspace]]
- [[location|Location]]
