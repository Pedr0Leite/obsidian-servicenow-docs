---
title: Questionnaire support in Exception Management via Smart Assessment
description: Configure advanced questionnaires as part of the exception management process using Smart Assessment. This enables Remediation Owners to provide more detailed context for Exception Requests and enables Approvers to configure conditional questions to gather information for informed decision making.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-smart-assessment-exp-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exception Management Overview, Use, Unified Security Exposure Management, Security Operations]
---

# Questionnaire support in Exception Management via Smart Assessment

Configure advanced questionnaires as part of the exception management process using Smart Assessment. This enables Remediation Owners to provide more detailed context for Exception Requests and enables Approvers to configure conditional questions to gather information for informed decision making.

## Roles Required

**Smart Assessment Template Reader**: **sn\_vul\_cmn.smart\_assessment\_template\_manager** \(Vulnerability admin and Template reader\) enables admins to create and edit templates.

**Smart Assessment actor**: **sn\_vul\_cmn.smart\_assessment\_actor** enables you \(Remediation Owners and Admins\) to fill out the questionnaires/assessments.

**Smart Assessment reader**: **sn\_vul\_cmn.smart\_assessment\_reader** enables you \(Approver\) to read the submitted questionnaire responses.

Pre-requisite: The smart assessment plug-ins must be installed as the Smart Assessment is a dependency.

You can configure questionnaires as part of the Exception Management process using Smart Assessment. It enables Vulnerability Admins/Manager to configure conditional questions to gather the right information needed for informed decision-making, while enabling Remediation Owners to provide more detailed context for exception requests. This enhances collaboration between the Vulnerability Management and Remediation teams by streamlining the approval process and ensuring clarity and completeness of exception justifications.

In the **Exception Management Configuration** screen from any of the four options- **[[vuln-landing-page|Vulnerability Response]]**, **[[avr-landing|Application Vulnerability Response]]**, **[[cvr-landing|Container Vulnerability Response]]**, and **[[vr-config-compliance-landing|Configuration Compliance]]** you can select the Assessment for Compensating Control, request exception and false positive records.

You can use the **Smart Assessment** to manage the Questionnaires in [[sem-workspace-user-interface|Security Exposure Management Workspace]].

Templates can be accessed/edited by the Smart Assessment Template Reader: **sn\_vul\_cmn.smart\_assessment\_template\_manager**.

-   **[[sem-compensating-controls-approval-rule|Questionnaire Configuration form fields]]**  
You can define distinct questionnaire for a distinct collection of [[vulnerabilities|vulnerabilities]] or remediation tasks by filtering the vulnerabilities or remediation tasks respectively.
-   **[[sem-configure-assessment-template|Configure an assessment template]]**  
Assessment templates contain the questions prompted during the request process \(such as, when requesting an exception\). The above-mentioned preconfigured templates are provided with smart assessment. You can also create your own templates as required.
-   **[[sem-ques-for-false-positive-or-request-exp|Use case for False positive or Request Exception Questionnaire]]**  
Scenario when the [[questionnaire-for-false-positive-or-request-exception-in-vr|questionnaire for False Positive or Request Exception]] is raised but not filled completely.

**Parent Topic:**[[sem-exception-management-overview|Exception Management Overview]]

## Related

- [[sem-compensating-controls-approval-rule|Questionnaire Configuration form fields]]
- [[sem-configure-assessment-template|Configure an assessment template]]
- [[sem-ques-for-false-positive-or-request-exp|Use case for False positive or Request Exception Questionnaire]]
- [[sem-exception-management-overview|Exception Management Overview]]
- [[vuln-landing-page|Vulnerability Response]]
- [[avr-landing|Application Vulnerability Response]]
- [[cvr-landing|Container Vulnerability Response]]
- [[vr-config-compliance-landing|Configuration Compliance]]
- [[sem-workspace-user-interface|Security Exposure Management Workspace]]
- [[vulnerabilities|Vulnerabilities]]
- [[questionnaire-for-false-positive-or-request-exception-in-vr|Questionnaire for False positive or Request Exception]]
