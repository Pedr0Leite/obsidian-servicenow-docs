---
title: "SLA condition evaluation"
aliases:
  - KB0547389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547389
kb_number: KB0547389
last_modified: 2026-06-03
---

## SLA condition evaluation

  

### Issue

This article expands on some of the details for SLA condition evaluations.  
  

### SLA definitions

The [SLA Definitions](https://docs.servicenow.com/csh?topicname=c_SLADefinitions.html&version=latest "SLA Definitions") contain conditions that control when an SLA record is:

-   Created for a particular task
-   Updated as it moves through its lifecycle to completion

See [Understanding SLA Conditions (KB0547356)](/kb_view.do?sysparm_article=KB0547356 "Understanding SLA Conditions (KB0547356)") for more information. See [product documentation](https://docs.servicenow.com/csh?topicname=c_SLADefinitions.html&version=latest "product documentation") for more descriptions of SLA definitions.

**  
Note:** The SLA engine uses the **Stage** field to represent the state for SLA records.  
  

### Evaluating conditions

The SLA engine does two passes to evaluate SLA definitions and their conditions based on a task. The SLA engine checks:

-   Pass 1: SLA definitions that do not have active SLA records associated to the task
-   Pass 2: All active SLA records associated to the task  
      
    

Pass 1: Checks the SLA definitions that do not have active SLA records associated to the task

The SLA engine determines if the SLA definition applies to the task and if it needs to create a SLA record. If it needs to create the SLA record, it also needs to decide the stage of the SLA record (**In Progress** or **Paused**).

\- Condition checks:

1.  If the **Start** condition is **true** and the **Stop** condition is **true**, do nothing. The SLA would be measuring nothing, as the **Stop** condition overrides the **Start** condition, so do not create an SLA record.
2.  If the **Start** condition is **true** and the **Stop** condition is **false**, create a new SLA record for this task, using the SLA definition. Set the SLA record and set it to the **In Progress** stage.
3.  If the **Pause** condition is **true**, immediately pause the new SLA record.  
      
    

Pass 2: Checks all active SLA records associated to the task

The engine determines if the SLA records are changing stage.

\- Condition checks:

1.  If the **Stop** condition is **true**, change the SLA stage to **Completed**.
2.  If the **Start** condition is **false** and the **Stop** condition is **false**, the SLA changes to **Cancelled**. (The definition did apply, but does not apply any longer and was not properly finished, so it is **Cancelled**.)
3.  If the **Pause** condition is **true** and the SLA stage is **In Progress**, pause the SLA.
4.  If the **Pause** condition is **false** and SLA stage is **Paused**, unpause the SLA.   

### Related Links

-   [Troubleshooting service level agreements (SLAs)](/kb_view.do?sysparm_article=KB0523638 "Troubleshooting service level agreements (SLAs)")
-   [Understanding SLA times: actual elapsed time and business elapsed time (KB0547270)](/kb_view.do?sysparm_article=KB0547270 "Understanding SLA times: actual elapsed time and business elapsed time (KB0547270)")
-   [Understanding SLA Conditions (KB0547356)](/kb_view.do?sysparm_article=KB0547356 "Understanding SLA Conditions (KB0547356)")
