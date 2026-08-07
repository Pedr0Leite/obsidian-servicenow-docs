---
title: Configure rules to manage findings
description: By configuring rules, you can automate, organize, and manage the lifecycle of findings. The rules help ensure scalability, data consistency, and faster response times by reducing manual intervention across large volumes of vulnerability data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-configure-rules-manage-findings.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Implement, Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Configure rules to manage findings

By configuring rules, you can automate, organize, and manage the lifecycle of findings. The rules help ensure scalability, data consistency, and faster response times by reducing manual intervention across large volumes of vulnerability data.

-   **[[sem-configure-lookup-rules|Configuring lookup rules]]**  
By configuring lookup rules, you can map security exposure data to the correct configuration items \(CIs\) in the CMDB. This [[mapping-logrhythm|mapping]] is a critical function because associating exposure findings with the right assets is essential for proper risk assessment, assignment, and remediation workflows.
-   **[[sem-configure-classification-rules|Configuring classification rules]]**  
By configuring classification rules, you can ensure consistent categorization and processing of [[vulnerabilities|vulnerabilities]], [[cj-discovered-items|discovered items]] and other finding related entities based on key attributes. This helps the system route findings to the correct tables, apply the appropriate grouping, assignment, and remediation rules, enhance reporting accuracy, and determine which business logic to use \(such as prioritization and remediation targets\).
-   **[[sem-configure-risk-rules|Configuring roll-up calculator rules]]**  
Configure roll-up calculator rules to compute the cumulative risk score for remediation tasks and imported vulnerabilities.
-   **[[sem-configure-assignment-rules|Configuring assignment rules]]**  
By configuring assignment rules, you can automate the process of routing findings to the appropriate teams or individuals. By defining assignment criteria based on vulnerability attributes or affected assets, you can ensure timely and accurate ownership for remediation efforts.
-   **[[sem-configure-remediation-target-rules|Configuring remediation target rules]]**  
By configuring remediation target rules, you can set the expected time frame for addressing findings, similar to how service level agreements \(SLAs\) set deadlines for fixing vulnerabilities.
-   **[[sem-configure-exception-rule|Configuring an exception rule]]**  
You can request an exception for findings that can't be remediated or deferred immediately. By automating the finding deferral process, you can defer the matching findings based on the rule when the system identifies them.
-   **[[sem-vuln-calc-define-risk-rule-fields|Define fields and weights for the risk rule for Unified Security Exposure Management risk calculators]]**  
Customize risk rule parameters and weights to generate risk scores that reflect your organization's specific finding and asset data. By selecting relevant fields for the risk rule, you can create an effective risk scoring framework that meets your organization's unique needs.
-   **[[sem-configure-remediation-task-rules|Configuring remediation task rules]]**  
By configuring remediation task rules, you can automatically group findings based on filter conditions.
-   **[[sem-configure-auto-close-rules|Configuring auto-close rules]]**  
By configuring auto-close rules, you can automate the process of closing stale detections and findings associated with retired configuration items \(CIs\).
-   **[[sem-configure-auto-delete-rules|Configuring auto-delete rules]]**  
By configuring auto-delete rules, you can automate the process of deleting older findings and remediation tasks.
-   **[[sem-configure-exclusion-rules|Configuring exclusion rules]]**  
By configuring exclusion rules, you can filter or exclude detections from being converted into vulnerable items \(VITs\) during ingestion. This filtering helps streamline vulnerability management by reducing noise and prioritizing critical issues.
-   **[[sem-unassign-approval-rules|Approval workflow configurations for unassign request]]**  
You can design the approval workflow for the removal of assignments from vulnerable items \(VIs, VITs\), remediation tasks, application vulnerable items \(AVITs\), and container vulnerable items \(CVITs\) for you and your group.

## Related

- [[sem-configure-lookup-rules|Configuring lookup rules]]
- [[sem-configure-classification-rules|Configuring classification rules]]
- [[sem-configure-risk-rules|Configuring roll-up calculator rules]]
- [[sem-configure-assignment-rules|Configuring assignment rules]]
- [[sem-configure-remediation-target-rules|Configuring remediation target rules]]
- [[sem-configure-exception-rule|Configuring an exception rule]]
- [[sem-vuln-calc-define-risk-rule-fields|Define fields and weights for the risk rule for Unified Security Exposure Management risk calculators]]
- [[sem-configure-remediation-task-rules|Configuring remediation task rules]]
- [[sem-configure-auto-close-rules|Configuring auto-close rules]]
- [[sem-configure-auto-delete-rules|Configuring auto-delete rules]]
- [[sem-configure-exclusion-rules|Configuring exclusion rules]]
- [[sem-unassign-approval-rules|Approval workflow configurations for unassign request]]
- [[mapping-logrhythm|Mapping]]
- [[vulnerabilities|Vulnerabilities]]
- [[cj-discovered-items|Discovered Items]]
