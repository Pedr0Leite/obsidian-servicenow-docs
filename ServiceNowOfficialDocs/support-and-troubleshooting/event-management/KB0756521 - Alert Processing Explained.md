---
title: "Alert Processing Explained"
aliases:
  - KB0756521
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756521
kb_number: KB0756521
last_modified: 2026-04-23
---

## Alert Processing Explained

  

# Contents

1.  [Overview](#HEADING1 "Overview")
2.  [What is an Alert?](#HEADING2 "What is an Alert?")
3.  [Alert Processing Flow](#HEADING3 "Alert Processing Flow")
4.  [The Alert States and Processing](#HEADING4 "The Alert States and Processing")
5.  [Additional Information](#HEADING5 "Additional Information")

# 1\. Overview

-   This article will demonstrate details about what an alert is, how the alerts are created and handled by ServiceNow EM, the processing life cycle, etc.

# 2\. What is an Alert?

-   A notification to draw attention to one or more Events is what I call an **Alert**. Events trigger "alerts" to notify responsible parties to take actions before things go wrong. So the flow is as below

Data collection > Events > Alerts  
Lots of things > Some things > Few things  

-   Any event that meets or exceeds defined condition/thresholds that require immediate attention/action by 'service providers' (sysadmins, DBAs, network engineers, product managers, service managers, service desk) are converted to alerts. 
-   Please refer to [Event Processing](/kb_view.do?sys_kb_id=298dae8bdbcf73402be0a851ca96199d "Event Processing") for more information on how the events are handled and processed.

# 3\. Alert Processing Flow

-   The below diagram explains the alert processing flow based on different stages.  
     

![](sys_attachment.do?sys_id=6a844b0647052e50b8a4aa25126d43c6)

### Event Rules

-   The event rule mechanism is used to categorize and process the event based on certain criteria. Each rule is defined has conditions like the source of event or maintenance state, etc.
-   If the condition is passed we either continue with processing the event or "Ignore the event".
-   The outcome of processing is an Alert. 
-   Refer to [Event Rules](https://docs.servicenow.com/bundle/madrid-it-operations-management/page/product/event-management/concept/create-event-rules.html "Event Rules") for more information on event rules.

### Alerts

-   Post successful processing of events an alert record is generated.
-   The newly generated alert has 4 different states; Open, reopen, closed and flapping. 
-   Each state has the execution flow which is explained in detail in the next section.

### Event to Alert Association:

-   When an event is processed, system decides whether to create a new alert or get associated with the existing alert. This is decided by the value of the Message key. By default, each event is uniquely identified by the **Message Key**. 
-   If the message of the event is the same as of any existing alert, the event gets associated with the alert else it will create a new Alert.
-   If an alert is closed then it reopens of the alert is dependent on the value defined in the "Active interval (in seconds), within which a new event reopens a closed alert" property present under Event Management properties.
-   **If the Message Key is not populated**, a concatenation of the **Source**, **Type**, **Node**, **Resource**, and **Metric Name** fields are used and these fields populate the Message Key. 

# 4. The Alert States and Processing

-   There are 4 alert states; Open, Closed, Reopen, and flapping. All these states have different execution flow and code associated. Below are the details of each state.

### Open

-   The first stage in the processing of Alert is Open. When an event is processed successfully it creates an alert.
-   An alert is opened whenever an event is not ignored or its threshold is exceeded by an event rule, and de-duplication does not identify the event as belonging to an existing alert.
-   The Alerts are processed using the specific job named "`Event Management - Evaluate Scoped Alert Rules Managemen`"  
    Note - Only new users from Vancouver and later releases will see two scheduled jobs: `Event Management - Evaluate Scoped Alert Rules Management0` and `Event Management - Evaluate Scoped Alert Rules Management1`. Users upgrading from earlier family releases will continue with just one: `Event Management - Evaluate Scoped Alert Rules Management0`. Please do not modify the `sn_em_arm.alert_management.num_of_jobs` property.
-   During the evaluation process, [Alert Management](/kb_view.do?sys_kb_id=933c0d0bdbae33000be6a345ca961941 "Alert Management") rules are used to filter the alerts and perform the remediation action accordingly.
-   In case of any deletion business use cases, we recommend not to delete any open alert. Kindly close the alert first and then delete it. Also, note that Alerts with State as "Info" will close/resolve incidents.

### Closed

-   For an open alert if the Clear event is triggered then the corresponding alert associated is set to the "Closed" state.
-   Closing an alert also closes any related incident that is not already resolved or closed.
-   If there is no associated Incident, then no only state is changed to Closed and no further action is performed.

### Reopen

-   When new additional events are generated which on processing finds existing closed alert then the alert is reopened. An alert can be reopened manually.
-   Reopening of existing closed alert by new events is controlled by property "**evt\_mgmt.active\_interval**".
-   By default value of this property is 14400 sec. This means that if an alert is closed and a new event is generated within 4 hours which matches the same message key then the existing alert is reopened.  
      
    
-   When an alert is reopened, the related incident is processed as follows:  
    -   If the incident is not Resolved or Closed, a work note is added to indicate that the related alert was reopened.
    -   If the incident is Resolved or Closed, the incident is reopened, a new incident is created, or nothing is done, depending on the **evt\_mgmt.alert\_reopens\_incident property** value.  
        -   If the incident is reopened, work notes are added to the incident.
        -   If a new incident is created, any matching alert management rule, alert action rule, and task template apply to the incident.
        -   If there is no matching alert rule or template, fields from the existing incident are copied to a new incident.
-   The business rule that gets executed post alert reopen is "**Reopen associated closed incident**"
-   This BR calls for script include "**EvtMgmtAlertManagementAlertReopenHandler**" which again invoke the Alert Management process to find the correct rule and perform the remediation action.

### Flapping

-   Flapping is a state when multiple open-closes events are generated for an associated closed alert. 
-   The flapping state entry is determined using the value configured for "**evt\_mgmt.flap\_interval**" and "**evt\_mgmt.flap\_frequency**" .
-   An alert enters the flapping state when its **current Flap Count** value reaches or exceeds the given evt\_mgmt.flap\_frequency property value within the time period specified by the evt\_mgmt.flap\_interval property.
-   There a scheduled Job "**Event Management - close flapping alerts**" which executes every 5 minutes and processes the flapping alerts.

# 5\. Additional Information

### Acknowledging Alert

-   It denotes that the alert is known, and can temporarily be ignored.
-   Acknowledging the alert does not assign it to you, nor does it create a task like an incident or change request. It simply lets other operators know that you are aware of the issue. After you acknowledge it, you will take further action during the triage stage.

### Auto Closing Alert

-   evt\_mgmt.alert\_auto\_close\_interval - An interval (in hours), within which open alerts will be automatically closed; Setting to 0 disables the feature.
-   evt\_mgmt.alert\_closes\_incident - Closing the alert will Resolve Incident or Close Incident or Do nothing.
-   evt\_mgmt.alert\_reopens\_incident - Reopening alert will Create New Incident or Reopen Incident or Do nothing
-   evt\_mgmt.incident\_closes\_alert - If true then resolving an incident closes the associated alerts, else no action will taken.

### Points to focus

-   Business rules created on alert tables should not take more than a few milliseconds. In place of using a business rule, consider if the same functionality can be achieved using a job.
-   Do not use business rules to associate an alert with a CI. Use event rules to do binding instead of using business rules.
