---
title: "Alert Management Explained"
aliases:
  - KB0753955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753955
kb_number: KB0753955
last_modified: 2025-05-31
---

## Alert Management Explained

  

### Issue

How does Alert Management Work?

### Release

 All Releases 

### Resolution

## Table of Contents

-   [Overview](#mcetoc_1g2amkl53j9)
-   [Introduction to Alert Management](#mcetoc_1g2amkl53ja)
-   [Alert Processing Flow](#mcetoc_1g2amkl53jb)
-   [Alert Management Rule](#mcetoc_1g2amkl53jc)
-   [Alert Info](#mcetoc_1g2amkl53jd)
-   [Alert Filter](#mcetoc_1g2amkl53je)
-   [Actions](#mcetoc_1g2amkl53jf)
-   [Migrating Alert Action rules to Alert Management rules](#mcetoc_1g2amkl53jg)
-   [Alert Management Troubleshooting](#mcetoc_1g2amkl53jh)

### Overview

-   This article will demonstrate the procedure to set up and configure the Alert Management Rules in an environment. Using this article, we will understand Alert Filters, Remediation Flows, etc.
-   Along with configuration, additional best practices related to the implementation and use-cases are also discussed in this article.

### Introduction to Alert Management

![](sys_attachment.do?sys_id=74b42d8e473926507947e551336d4317)

-   Alert Management is a new feature introduced in the London release of ServiceNow replacing the existing "Alert Action Rule" Feature.  
      
    
-   The Purpose of Alert Management is to integrate the Alert Rules with [Flow Designer](https://docs.servicenow.com/csh?topicname=flow-designer.html&version=latest), which enables you to use user-defined sub-flows to resolve the cause of the alert. Several sub-flows are provided with the base instance. Such as "open an incident", "create knowledge base(KB)" etc.  
      
    
-   As alerts generate, you can view more information about them, acknowledge them, and take action to resolve them and you can respond to an alert 2 ways.  
    1.  Manually Response: Manual response involves manually remediating the alert to acknowledge it and perform the remediation action.  
          
        
    2.  Automatic Response via Alert Action Rule: It uses Business Rules, user-defined subflows to   
        -   Acknowledge an alert that requires attention.
        -   Create an incident or security incident.
        -   Close the alert.
        -   Resolve any incident that is related to the alert.
        -   Reopen the alert.
            
-   With the Implementation of Alert Management Rules, you can continue to use existing alert action rules, but you cannot modify them. You cannot create new alert action rules. You can migrate alert action rules to alert management rules.  
      
    
-   To see the feature, follow below steps  
      
    -   Navigate to **Event Management** > **Rules** > **Alert Management**
    -   It opens a list view and displays all Alert Management Rules available OOTB as below.  
          
        ![](sys_attachment.do?sys_id=f4b42d8e473926507947e551336d4339)

### Alert Processing Flow

-   The Alert Management Rules executes on the alert records created on the **Alert** \[em\_alert\] table.  
      
    
-   The Major flow of Alert Management Rule execution is as follows:  
      
    -   Event coming into the system - The **Event Processor** process the event and inserts an alert record on the em\_alert table.
    -   Once the Alert is created, the **Alert Management Processor** tries to match Alert Management rules according to defined filter, if the rule is matched the then the remediation sub-flow, workflow or launch application action is executed.  
          
        ![](sys_attachment.do?sys_id=38b4e98e473926507947e551336d43aa)

### Alert Management Rule

-   An Alert Management Rule is consists of 3 sections: Alert-Info, Alert Filter and Actions. To create a new alert management rule follow the below steps.  
    -   Navigate to **Event Management** > **Rules** > **Alert Management**
    -   Click on New Button.
    -   All the rules are stored on "**em\_alert\_management\_rule**" table  
        -   **Note** - The role **evt\_mgmt\_admin** is required to create new Alert Management Rules.  
              
            
-   Let's understand all the sections and the fields present in the sections in detail.  
      
    -   Alert-Info
    -   Alert Filter
    -   Actions

### Alert Info

-   -   The Alert-Info is the first screen on the Alert Management Rule where we provide the Name, Order, State, etc.  
          
        ![](sys_attachment.do?sys_id=b0b42d8e473926507947e551336d433e)

-   Here the field of most importance is "Multiple Alert Rules". Below are the details of both options.  
    -   Search for additional rules — After the execution of the current rule, the system continues to execute other matching rules by the order of the rules of priority, where the lower number has a higher priority.
    -   Stop the search for additional rules — do not search for any other rules after the execution of the current rule.  
          
        

**Use case - Why the Alert management rule is not executing**.

-   When we see a use case where an alert rule should execute based on the filter condition but it is not executing, in that case, check if there is any other alert rule with execution order less than the current one that matches the same filter condition and has Multiple Alert Matches - Stop search for additional rules value set
-   If it has the value set, then the system executes the current rule, perform the remediation action and stops further processing. Thus no other Alert Management rules are executed even though it matches the condition.
-   Refer "[Querying Alert Rule](https://support.servicenow.com/kb_knowledge.do?sys_id=b14537d9dbd9f78854250b55ca961935 "Querying Alert Rule")" article to query the Alert Management list view to find alerts with a specific filter condition.

### Alert Filter

-   The Alert Filter section defines an alert filter on which this alert management rule is applied, plus you can specify related list conditions, such as a number of secondary alerts.
-   Use the conditions in the RELATED LIST CONDITIONS area to apply an additional filter to further define which alerts match this rule.   
    For example, the alert filter might match an alert that is part of a group. Using the conditions in the RELATED LIST CONDITIONS area, you can create a filter to match only the primary alert or to match only secondary alerts, as required. Refer "[Add Related List Conditions](https://docs.servicenow.com/csh?topicname=create-related-list-query.html&version=latest "Add Related List Conditions")" for more details.

  
![](sys_attachment.do?sys_id=fcb42d8e473926507947e551336d431b)  
  

-   Let's focus on "**Rule is activated when"** field values. This value determines when to activate the rule. **The rule executes on the update of an open alert** when:
    -   Alert Matches To Filter - When the content of the alert matches the filter. On every update of the alert and when the filter is matched, the rule runs and is applied to the alert for every update.
    -   Alert Changes to Filter - The rule will be applied **only once** when content changes to the alert cause the alert to match the filter. On the following updates of the alert, if the filter is matched, the rule is no longer applied. If the alert was closed and then reopen if the filter is matched, the rule is applied. Thereafter, when there is an update of the alert and alert continues to match the filter, the rule is no longer applied.
-   Let's consider an example Here.

1.  There exists an alert with Severity = Major.
2.  We have an Alert rule with "Rule is activated when" value set to **Alert Changes to the filter** and filter condition contains Severity = Critical then in that case

-   -   If a new critical event is generated and that changes the severity of the alert from Major to Critical then, in that case, the alert filter condition \[Severity = Critical\] is matched and Remediation action is will be executed.
    -   In the same use case if another new event is generated that changes the severity of the alert back to Major from critical then this rule is not applied. If there is a change in \[Major\] attribute(s) in the alert that feeds the filter condition then only the rule is applied. \[Here the thing to notice is that this rule is applied each time the severity changes from some value to Critical\].
    -   After some time if another event generated changes the severity of severity to critical then in that case as well the rule is triggered and remediation subflow is executed. 
    -   In the same example, another event is generated that changes the **Description** value of the field then, as there is a change in the Description value and not in the severity value, this rule is not applied and no remediation action is performed.
-      
    -   But if the "Rule is activated when" set to "**Alert matches filter**" and the filter condition is the same \[Severity = Critical\] then the change in the Description will also trigger the Alert Management Rule.
    -   Every time when an alert is updated, if the filter "**matches**" the condition, the alert rule is triggered and remediation action is executed which means that even if you do not make any changes to the attribute(s) used in the condition filter, if the condition is matching then the rule will always execute.  
          
        **Note** -_Pay attention to the Automatic Execution Limit that is defined for each remediation action. If the execution limit is 1 then the rule may be applied but nothing will happen._ This limit is reset when the alert is reopened.  
          
        
-   **Use Case - Alert condition is matching still no remediation action is performed.  
    **  
    -   In a scenario when we see that the Alert filter condition is matching but still no incident is created or no workflow is executed then the thing to verify is the case. **Alert filter condition is case sensitive.** If the condition value does not match the case of the string then filter execution fails and no remediation flow is triggered. 
    -   For example, if the alert filter condition is configured as "Description = NRTEST" then alert description should contain NRTEST and not NRtest or nrtest, nrTest, etc.

-   -   -   **Note**: If **Active** is selected in the Alert-Info tab, it is mandatory to specify at least one remediation action. If no remediation actions are defined then the rule will automatically become inactive.

### Actions

-   The Alert Action tab specifies the action to be performed when an alert filter condition is passed. OOTB there are actions allowed.  
      
    -   Remediation Subflows — Execute a subflow provided with the base system or a subflow that was previously created and published.
    -   Remediation Workflows — Execute a workflow that you previously published.
    -   Launch Applications — Open applications and browsers that you configure.  
          
        Note - To know more about Flow Designer, Subflows, etc. please see "[Flow Designer](https://docs.servicenow.com/csh?topicname=flow-designer.html&version=latest "Flow Designer")"  
          
        ![](sys_attachment.do?sys_id=b4b42d8e473926507947e551336d4310)  
          
          
        
    -   OOTB multiple subflows are provided that provide an option to create an incident, attach knowledge article, close alert, etc. Below are the details related to how to add subflow and various configuration options associated.  
          
        1.  Navigate to **Actions** > **Remediation Subflow**, double click on the cell below "Subflow" label.
        2.  It gives an option to add text to search the subflow or you can click on the Search icon.
        3.  The search option displays all the OOTB available subflows that are published. Select the desired one and click save on the cell window.
        4.  It relates the subflow record with the Alert Rule. These relationships are stored on **em\_alert\_man\_m2m\_rule\_flow** table.  
              
            
-   **Things to note**  
      
    -   **Execution Options**  
          
        **Automatic** - The subflow is executed automatically whenever the rule is matched.  
        **Manual** -  The execution of subflow is linked with manual actions. Ex: Executing subflow by manually selecting "Quick Response" UI Action.  
        **Both** - When the rule is matched, the subflow is executed automatically and you can optionally execute the subflow again manually by using Quick Response UI Action.  
          
        
    -   **Automatic Execution Limit  
          
        **An integer value that is used to configure the maximum number of times a subflow can be executed. If the subflow execution is called beyond the number configured on the field then subflow execution will be skipped and no remediation action is performed.  
          
        
    -   You can add any number of workflows/sub-flows to the actions however **each subflow can be added only once**. if you try adding the same subflow twice the system triggers an error as below.  
          
          
        ![](sys_attachment.do?sys_id=60b4e98e473926507947e551336d43a8)  
          
        
    -   **The subflows cannot be executed in a specific order.** The execution of subflows is in **an asynchronous way**.
    -   To create custom subflow, it is recommended to copy OOTB subflow and OOTB actions wherever possible to avoid any issue occurred due to incorrect syntax and naming issues.
    -   These custom subflows needs to be tested properly and make sure it is Active and Published. 

-   Using similar steps and configurations, the Remediation workflow and Launch Application can be selected. For more details refer [Create alert management rules](https://docs.servicenow.com/csh?topicname=create-alert-management-rule.html&version=latest "Create alert management rules")  
      
    
-   **Use Case - No Incident is created for CI which is back to Production Mode from Maintenance Mode.  
      
    **  
    -   When a CI is in maintenance mode and alert is generated for it but no incident is created because of the validation check present in the subflow.  
          
        ![](sys_attachment.do?sys_id=30b42d8e473926507947e551336d4315)  
          
        
    -   However when CI is back to production mode and in that case, if an alert is generated, it is expected it should create an Incident for it but no incident is generated. This is because of the value of the field "**Automatic Execution Limit**" present on the Alert Management Rule for selected subflow. 
    -   When the Alert Rule gets executed for CI in maintenance mode, it successfully calls the subflow but due to validation, it won't create any incident thus the attempt is wasted. When CI is back to Production Mode and alert is generated, as the subflow execution already executed for the specified number of times (1), it won't execute beyond the specific number thus no Remediation subflow is executed for it.
    -   Thus in such cases, it is recommended to add Maintenance = False filter condition to alert rule to avoid wasting execution attempt.   
          
        
-   Alert management rules that are **not configured to perform any action** are **skipped** and the rule is automatically set to inactive.

### Migrating Alert Action rules to Alert Management rules

-   Alert Management supports the execution of alert action rules.
-   Post Upgrade to London and above **old alert action rules continue to work but cannot be modified and are read-only.**
-   If you want to make any modification to the rule then the rule needs to be migrated to Alert Management Rule. Note that a rule can be migrated only once
-   The filter is mapped with Filter and actions are mapped with actions. If the alert action rule has some incident template defined then it will be performed by OOTB "create task(legacy)" subflow.
-   The input to the legacy subflow is provided by the templates from the alert action rule. On ListView, if we add the template fields we can see the values.  
      
    ![](sys_attachment.do?sys_id=f8b42d8e473926507947e551336d4312)

-   See [Migrate alert action rule to alert management rule](https://docs.servicenow.com/csh?topicname=t_EMCreateAlertRule.html&version=latest#t_EMCreateAlertRule "Migrate alert action rule to alert management rule") for more details.
-   See [KB0751453 - Import Export Alert Management Rule](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751453 "KB0751453 - Import Export Alert Management Rule") to know how to migrate OOTB Alert Management Rules from one instance to another.
-   See [KB0752233 - Import Export Alert Management Rule with Custom Subflow](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752233 "KB0752233 - Import Export Alert Management Rule with Custom Subflow") to know how to migrate Alert Management Rules with custom subflow from one instance to another.

### Alert Management Troubleshooting

-   **Possible root causes observed with Alert Management**.  
      
    
-   Make sure the Alert Management Job Event Management - Evaluate Scoped Alert Rules Management0 is running/active. 
-   The script included called is EvtMgmtAlertMgmtJobWrapper. Verify if it is customized or is it OOTB.
-   Also sometimes useful to go to sa\_hash.last\_calculated\_alert\_management\_job field updated is last minute.

Note - In few instances, it's observed that the old deprecated job \[Event Management - Evaluate Alert Management Rules\] continues to run. Make sure you follow the right process to enable the right job and disable the deprecated one.   
![](sys_attachment.do?sys_id=7cb42d8e473926507947e551336d433b)  
  

-   Verify whether the Alert Management Content Plugin is installed. This plugin contains all the OOTB sub-flows provided OOTB.
-   Alert Rule that supposed to be fire should be **active and published**.
-   Pay attention to the "**Multiple alert rules**" field value. Specifically, the stop searching for additional rules value.
-   Remediation action subflow can be set to execute Automatic, manual or both. If it is set to manual, then the flow will only exeucte when the "**Quick Response**" UI action is selected. The quick response UI action shows only those subflows which are set to execute as both or manual.
-   For new custom subflow, we recommend using an alert management template, copy it and save. Here you are free to modify or add the actions as you wish. You can copy any other OOTB subflows available and modify it.
-   Make sure for the custom subflow, all the names look correct, the main issue is with the names. Post modifications, test it and publish.
-   You can copy the actions and use the actions to the subflows, the custom actions will be available under the Global option of Add Action menu on flow designer.  
      
    

**Validate Subflow execution**.  
  

-   On Alert processing, it is expected to perform certain actions based on the alert rule defined. The details of the subflow execution can be seen in the alert execution tab.
-   This tab has the details about, Name of Alert Management Rule, Action Name, the flow designer execution link, related task, and log.
-   The Log tab shows the success or failure of the flow. 

  
![](sys_attachment.do?sys_id=b0b42d8e473926507947e551336d4337)  
  

-   In case of failed execution, when we click on the subflow links, it opens the flow designer and displays error for the failed step. Thus based on the failed step, the cause can be identified.

  
![](sys_attachment.do?sys_id=b8b42d8e473926507947e551336d4319)  
  

-   **Use Case - Alert rule matches the condition but still, no Incident is created.  
      
    **
    -   In a scenario when events are generating alerts but **no Alert Rule** is getting executed. On clicking the "Preview" button on Alert Rule filter, we see the alert getting listed in the result but still, no rule is executed. This situation occurs due to event creation time.
    -   In a situation when we have 2 events that come in the same minute and are bound to the same alert: one with resolution state new and another with resolution state closing and these 2 events are processed in the same processing cycle, then the alert management rule is not executed and an incident is not created.
    -   Here the relevant alert is created and immediately closed. In such cases, Alert Management rules are not applied by purpose. In general, the Alert Management rules are not applied to closed alerts.
    -   We have a special treatment to support such kind scenarios where the alert is rapidly closed as we want to reduce the noise and do not open irrelevant incidents.  
          
        
-   **Use Case – Alert rule matches the condition, but incident creation is delayed  
    **
    -   Alert management rules run 5 seconds after an alert is updated, resetting the timer if updates occur within that window.
    -   This delay ensures remediation actions, such as incident creation, are triggered only when the issue is clear and stable, reducing duplicates and unnecessary noise.
    -   To change the default 5-second delay, create the **evt\_mgmt.alert\_rule\_delay** property on the All > System Properties > All Properties and change the value.
