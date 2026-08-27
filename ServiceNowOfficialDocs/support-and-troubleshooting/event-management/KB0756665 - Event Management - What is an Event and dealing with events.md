---
title: "Event Management - What is an Event and dealing with events"
aliases:
  - KB0756665
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756665
kb_number: KB0756665
last_modified: 2025-03-19
---

## Event Management - What is an Event and dealing with events

  

## Table of Contents

-   [Overview](#OVERVIEW)
-   [Introduction to Event Management](#INTRODUCTION_TO_EVENT_MANAGEMENT)
-   [What is an Event?](#EVENTS)
-   [Event Sources](#mcetoc_1fvqv1dnf6i)
-   [Event Processing Flow.](#mcetoc_1fvqv1dnf6j)  
    -   [Scheduled Job - Event Management Process events](#mcetoc_1fvqv1dnf6k)
-   [Additional Information](#OVERVIEW)

## Overview

-   This article will demonstrate details about what is an event, how the events are created, handled by ServiceNow EM, different event sources, etc.

## Introduction to Event Management

-   The Event Management application **consolidates events integrated from different monitoring tools** (e.g. SCOM, Nagios, SolarWinds, etc.), performs processing of the events to produce actionable alerts.
-   It monitors the health of business services and infrastructure using a single management console and responds appropriately to any issues that come up. It also provides intelligent event and "alert analysis" to ensure continuity of your business service performance.
-   Using Event Management and Service Mapping you can **identify which service is affected by an event**.

## What is an Event?

-   _Events_ are the way to monitor a system's health. 
-   In the ServiceNow system, an event is a notification from a CI in your IT system or cloud about an issue, the IT team should be aware of. Like a failure or warning.  It is a record collected from an external monitoring solution and relates them to your CI's - with some additional logic to rate/qualify these events. On successful processing, events generate actionable alerts.
-   Applications, servers, and network gear generate various types of log messages which would further enrich ITOM Event Management for event grouping and correlation.
-   Alerts can be \[automatically\] related to CIs and if the CIs are related to business services then the severity of the alerts can be used to detect the impact on the business services
-   You can use Alert Rules to automate the creation of incidents (or other tasks) and automate the remediation (or repair) of problems reported by alerts.

## Event Sources

-   Events can be sent to instances directly or via Mid Server using connectors. Some examples are:  
    -   **[External Monitoring Tools like SCOM, Nagios, SolarWinds, etc](https://docs.servicenow.com/csh?version=latest&topicname=connectors-and-listeners.html "External Monitoring Tools like SCOM, Nagios, SolarWinds, etc").**
    -   [**SNMP Trap Listener**](https://docs.servicenow.com/csh?version=latest&topicname=t_EMSNMPTrapEvent.html "SNMP Trap Listener") - Use a monitoring tool to send SNMP traps, rather than sending them directly from devices.
    -   **Web Service or Rest API Integration** - Using a web service API for integration can reduce the number of event rules needed. This action avoids having to transform events (prepared data is sent in an event to the instance).
    -   **CloudWatch** - Use dedicated credentials for integrating CloudWatch with ServiceNow.
    -   **Email**\- Use email only if the source has a low volume and other options are not available, such as, running a script or forwarding an SNMP trap.  
          
        
-   Using these mechanisms, an event record is created in the ServiceNow **em\_event** table which feeds data to Event Management Flow.

## Event Processing Flow.

-   Event Management flow involves processing the events using Scheduled Job, Event rules, etc. The below diagram explains the flow.

![](sys_attachment.do?sys_id=40304f1fdbaec510ae812509139619d9)

### Scheduled Job - Event Management Process events

-   Events are stored in the em\_event table with status = Ready and are processed by scheduled Job \[sys\_trigger\] Event Management Process events which execute every 5 seconds. Therefore, the "Next action" should be a few seconds from now.  
    
     **Note:** If "Next action" is a time in the past, then likely the job is stuck. If the job was claimed by a passive node, then the job is stuck as well.
    
-   This Job calls process(); function of EvtMgmtEventProcessor java class which process events in all buckets. if multi-node processing is enabled, this node is going to process the buckets between lower and upper limits.  
      
    **Tip - Buckets**  
    -   Events coming into service now have a specific bucket between 0 - 99 assigned. When Multi-Node Event Processing is enabled, on each node, the bucket range will be divided evenly among the scheduled jobs.
    -   Ex: if number of scheduled jobs processing events is 4, then each job is responsible for processing each event in a specific range: \[0 - 24\], \[25 - 49\], \[50 - 74\], \[75 - 99\].

#### Multinode Event Processing

-   if "Enable multi-node event processing = true", the system creates jobs as per this formula  
    
    (<number\_of\_jobs\_configured> \* (1 + <active\_worker\_nodes>))
    
-   For example, an instance with 6 active worker nodes configured to have 4 jobs processing events per node would have (4 \* (1 + 6)) = 28.
-   The 1 above, added to the number of active worker nodes, is because a job is also created for the system "Active Nodes".

#### Event Rules

-   Event rule mechanism is used to categorize and process the event based on certain criteria. Each rule is defined has conditions like the source of event or maintenance state, etc.
-   If the condition is passed we either continue with processing the event or "Ignore the event".
-   The outcome of processing is an Alert. 
-   Refer [Event Rules](https://docs.servicenow.com/bundle/madrid-it-operations-management/page/product/event-management/concept/create-event-rules.html "Event Rules") for more information on event rules.

#### Event Field Mapping

-   Event Management provides default event field mappings for commonly used system monitoring tools. It is used to map values from specific fields to values in other fields.
-   Event Management stores event field mappings in the Event Field Mapping \[**em\_mapping\_rule**\] table.
-   **The mappings apply after event rule processing and prior to alert generation**. The mapping values from the Event Mapping Pair \[em\_mapping\_pair\] table apply to the alert. **The original event severity remains unchanged**.
-   For example, if the events came from Solaewinds with the field "Status" that get the values "Up, Down, Warning" etc and you want the alert Severity to hold the value, then create an event field mapping rule that maps the field Status to Severity, with values between 0-5 which denotes the Severity field values of Alert record. Below is one such example of mapping.

![](sys_attachment.do?sys_id=8c304f1fdbaec510ae812509139619ec)

 **Note:**

-   The Source system sends the values which are part of the Additional Info field payload which is then used for processing.
-   If there is an issue with mapping or value passed, for a field which is a mandatory field on event form\[ For Ex Severity\] then the event will not be created and the event goes to an error state.

#### Alerts

-   A notification to draw attention to one or more Events is we consider as Alert. Refer "[Alert Processing Explained](/kb_view.do?sys_kb_id=9cc300eadb4b7b0cfff8a345ca9619a9 "Alert Processing Explained")" document for more details on Alerts and their processing.

## Additional Information

-   [Event Management configuration preferences](https://docs.servicenow.com/csh?version=latest&topicname=r_EMBestPractice.html "Event Management configuration preferences")
