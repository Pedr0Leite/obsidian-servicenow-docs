---
title: Configuring an exception rule
description: You can request an exception for findings that can't be remediated or deferred immediately. By automating the finding deferral process, you can defer the matching findings based on the rule when the system identifies them.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-configure-exception-rule.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure rules to manage findings, Implement, Unified Security Exposure Management, Security Operations]
---

# Configuring an exception rule

You can request an exception for findings that can't be remediated or deferred immediately. By automating the finding deferral process, you can defer the matching findings based on the rule when the system identifies them.

-   **[[sem-create-exception-rule|Create an exception rule]]**  
Create a rule to automatically request an exception for a specific condition for a group findings, such as a rule with a condition that is based on the vulnerability severity of these findings. With this rule, you can defer new and existing findings automatically if they match the approved rule condition.
-   **[[sem-approve-ex-rule-request|Approve an exception rule request]]**  
Assess exception rule requests from users so that you can approve or reject these requests.
-   **[[sem-activate-ex-rule|Activating an exception rule]]**  
A rule is activated on its "Valid from" date. After activation, it automates the exception process for findings.
-   **[[sem-reopen-ex-rule|Reopen an exception rule]]**  
Reopen an exception rule that has been rejected, but you want to resubmit. Reopening the rule moves it to the Draft state.
-   **[[sem-update-approved-ex-rule|Update an approved exception rule]]**  
Cancel an approved rule to be able to update it. For example, before you can modify any dates or add a condition to an approved rule, you must cancel it so that the remediation task finding is deleted, and the findings move to the Open state.
-   **[[sem-delete-ex-rule|Delete an exception rule]]**  
Delete an exception rule that is not required anymore. For example, you can delete a rule if you don't want to defer a finding during ingestion.

**Parent Topic:**[[sem-configure-rules-manage-findings|Configure rules to manage findings]]

**Related topics**  


[[sem-exception-rules-overview|Deferring findings automatically without manual intervention using exception rules]]

## Related

- [[sem-create-exception-rule|Create an exception rule]]
- [[sem-approve-ex-rule-request|Approve an exception rule request]]
- [[sem-activate-ex-rule|Activating an exception rule]]
- [[sem-reopen-ex-rule|Reopen an exception rule]]
- [[sem-update-approved-ex-rule|Update an approved exception rule]]
- [[sem-delete-ex-rule|Delete an exception rule]]
- [[sem-configure-rules-manage-findings|Configure rules to manage findings]]
- [[sem-exception-rules-overview|Deferring findings automatically without manual intervention using exception rules]]
