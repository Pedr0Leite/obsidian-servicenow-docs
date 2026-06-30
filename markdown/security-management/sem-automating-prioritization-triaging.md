---
title: Automating prioritization and triaging
description: Automate prioritization and triaging of findings using rules and severity mapping.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-automating-prioritization-triaging.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Security Exposure Management workflow, Explore, Unified Security Exposure Management, Security Operations]
---

# Automating prioritization and triaging

Automate prioritization and triaging of findings using rules and severity [[mapping-logrhythm|mapping]].

-   **[[sem-associate-finding-configuration-item-using-lookup-rules|Associating finding with a configuration item using lookup rules]]**  
Unified Security Exposure Management uses lookup rules to associate imported third-party exposure findings with configuration items \(CIs\) in the Configuration Management Database \(CMDB\). These rules match asset data to existing CIs, enabling accurate remediation.
-   **[[sem-categorizing-findings-discovered-items|Categorizing findings and discovered items using classification rules]]**  
Classification groups automate the classification of entities or records based on the classification rules defined in the group. The condition for each rule is evaluated in order, and the first matching rule is used.
-   **[[sem-prioritizing-vulnerabilities-other-findings|Prioritizing vulnerabilities and other findings using roll-up calculators]]**  
After assessing risk calculators, use the roll-up calculators to configure how the cumulative risk scores are computed for remediation tasks and other higher entities.
-   **[[sem-assigning-findings-to-remediation-teams|Assigning findings to remediation teams using assignment rules]]**  
Assignment rules automatically assign findings, such as vulnerable items, application [[vulnerabilities|vulnerabilities]], container vulnerabilities, and configuration test results, to the appropriate groups for remediation. This streamlined triage ensures that tasks are directed to the appropriate teams, and enhances consistency and visibility across security and compliance programs.
-   **[[sem-defining-your-own-sla|Defining your own service level agreements \(SLAs\) using remediation target rules]]**  
Remediation target rules set the expected time frame for addressing findings, similar to how service level agreements \(SLAs\) set deadlines for fixing vulnerabilities. You can also send notifications to users and groups when target dates are approaching and when they are past due.
-   **[[sem-exception-rules-overview|Deferring findings automatically without manual intervention using exception rules]]**  
Exception rules for [[sem-workspace-user-interface|Security Exposure Management Workspace]] enable you to automate the deferral process for findings. Request an exception for the findings that can't be remediated or deferred immediately, by identifying the impacted vulnerabilities, configuration items \(CIs\), or VIs. Defer the matching findings based on the rule when the system identifies them by automating the finding deferral process.
-   **[[sem-grouping-multiple-findings-remediation-tasks-processing|Grouping multiple findings as remediation tasks for easy processing using remediation task rules]]**  
Remediation tasks help vulnerability analysts and remediation teams manage findings in bulk. By [[sem-configure-remediation-task-rules|configuring remediation task rules]], you can automatically group findings into remediation tasks, eliminating the need for manual task creation and streamlining remediation efforts.
-   **[[sem-closing-stale-findings-automatically|Closing stale detections and findings automatically using auto-close rules]]**  
Auto-close rules automatically close stale detections and findings based on predefined criteria. These rules ensure that redundant or unwanted findings are marked as closed, helping to maintain an accurate and up-to-date record of the organization's security posture. By automating this process, the rules reduce manual effort and enable teams to focus on active and critical vulnerabilities.
-   **[[sem-deleting-stale-findings-automatically|Deleting stale findings automatically using auto-delete rules]]**  
Auto-delete rules automatically remove findings from the system based on predefined criteria. These rules help manage the life-cycle of vulnerabilities by ensuring that resolved or outdated findings are removed, reducing clutter and maintaining a clean, up-to-date database. This automation streamlines the vulnerability management process and ensures that teams focus on current and relevant issues.
-   **[[sem-controlling-ingestion-volume-automatic-exclusion|Controlling the ingestion volume with automatic exclusion]]**  
Exclusion rules provide a way to filter or exclude detections from getting converted into VITs during the ingestion process in [[vuln-landing-page|Vulnerability Response]].
-   **[[sem-ci-creation-using-IRE|Creating CIs using the Identification and Reconciliation engine]]**  
You can create configuration items \(CIs\) in the Configuration Management Database \(CMDB\) using the Identification and Reconciliation engine \(IRE\) API. By using the IRE API to create CIs, you can prevent duplicate CIs from being created and you can reconcile CI attributes by allowing only authoritative [[data-sources|data sources]] to write to CMDB.

## Related

- [[sem-associate-finding-configuration-item-using-lookup-rules|Associating finding with a configuration item using lookup rules]]
- [[sem-categorizing-findings-discovered-items|Categorizing findings and discovered items using classification rules]]
- [[sem-prioritizing-vulnerabilities-other-findings|Prioritizing vulnerabilities and other findings using roll-up calculators]]
- [[sem-assigning-findings-to-remediation-teams|Assigning findings to remediation teams using assignment rules]]
- [[sem-defining-your-own-sla|Defining your own service level agreements \(SLAs\) using remediation target rules]]
- [[sem-exception-rules-overview|Deferring findings automatically without manual intervention using exception rules]]
- [[sem-grouping-multiple-findings-remediation-tasks-processing|Grouping multiple findings as remediation tasks for easy processing using remediation task rules]]
- [[sem-closing-stale-findings-automatically|Closing stale detections and findings automatically using auto-close rules]]
- [[sem-deleting-stale-findings-automatically|Deleting stale findings automatically using auto-delete rules]]
- [[sem-controlling-ingestion-volume-automatic-exclusion|Controlling the ingestion volume with automatic exclusion]]
- [[sem-ci-creation-using-IRE|Creating CIs using the Identification and Reconciliation engine]]
- [[mapping-logrhythm|Mapping]]
- [[vulnerabilities|Vulnerabilities]]
- [[sem-workspace-user-interface|Security Exposure Management Workspace]]
- [[sem-configure-remediation-task-rules|Configuring remediation task rules]]
- [[vuln-landing-page|Vulnerability Response]]
- [[data-sources|Data Sources]]
