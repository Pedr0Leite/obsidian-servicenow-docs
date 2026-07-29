---
title: "Understanding Event Management"
aliases:
  - KB0756800
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756800
kb_number: KB0756800
last_modified: 2025-08-31
---

## Understanding Event Management

  

## Contents

1.  [Overview](#OVERVIEW "Overview")
2.  [Prerequisite and Setup](#HEADING_2 "Prerequisite and Setup")
3.  [Understanding Event Management](#HEADING_3 "Understanding Event Management")
4.  [Managing and monitoring Alerts](#HEADING_4 "Managing and monitoring Alerts")
5.  [Connectors and Listeners](#HEADING_5 "Connectors and Listeners")
6.  [Domain Separation in Event Management](#HEADING_6 "Domain Separation in Event Management")
7.  [Troubleshooting  Guide](#HEADING_7 "Troubleshooting  Guide")

### 1\. Overview.

-   This article will demonstrate the procedure to set up and configure the Event Management Module in an environment. Using this article, we will understand events generation & processing, dealing with alerts and alert remediation, etc.
-   The purpose of this document to showcase all event management related modules at the same place and help TSE's with understanding the flow of data, get details of the code associated, and other details related to working and configuration.
-   This is the initial version of the document and the goal is to keep improving the documents as and when required based on the feedback and suggestions received.

### 2\. Prerequisite and Setup.

-   **Required Plugins**  
    -   Plugin Name: **Event Management**
    -   Plugin ID: **com.glideapp.itom.snac  
        **
-   **Event Management SetUp  
    **  
    -   **[Event Management SetUp](https://docs.servicenow.com/bundle/london-it-operations-management/page/product/event-management/concept/c_EMConfiguration.html#c_EMConfiguration "Event Management SetUp")**
    -   [**Event Management Setup Demo - Youtube**](https://www.youtube.com/watch?v=Vh8E_AlmcPY&list=PLCOmiTb5WX3p7hJP68kQu3nXPCwwGtXK0&index=15 "Event Management Setup Demo - Youtube")

### 3\. Understanding Event Management.

-   [Events](/kb_view.do?sysparm_article=KB0756665 "Events")
-   [Components installed with Event Management](https://docs.servicenow.com/csh?topicname=r_InstalledWithEventManagement.html&version=latest "Components installed with Event Management")
-   [Event Rules](https://docs.servicenow.com/csh?topicname=create-event-rules.html&version=latest "Event Rules")
-   [Alert binding to CIs with event rules](https://docs.servicenow.com/csh?topicname=r_EMHowAlertsBindCI.html&version=latest "Alert binding to CIs with event rules")
-   [Set a threshold to suppress alert generation](https://docs.servicenow.com/csh?topicname=t_EMISetThresholdEvent.html&version=latest "Set a threshold to suppress alert generation")
-   [Event Field Mapping Configuration](https://docs.servicenow.com/csh?topicname=c_EMEventFieldMapping.html&version=latest "Event Field Mapping Configuration")

### 4\. Managing and Monitoring Alerts.

-   [Alert Processing Explained](/kb_view.do?sysparm_article=KB0756521 "Alert Processing Explained")
-   [Alert Management Rules](/kb_view.do?sysparm_article=KB0753955 "Alert Management Rules")
-   [Alert Grouping](/kb_view.do?sysparm_article=KB0756804 "Alert Grouping")
-   [Event Management - Impact calculation explained](/kb?id=kb_article_view&sysparm_article=KB1157218)

### 5\. Connectors and Listeners.

-   [ServiceNow supported Connectors and Listeners.](https://docs.servicenow.com/csh?topicname=connectors-and-listeners.html&version=latest "ServiceNow supported Connectors and Listeners.")

### 6\. Domain Separation

-   [Event Management supported Application for Domain Separation](https://docs.servicenow.com/csh?topicname=t_EMConfigureDomainSeparation.html&version=latest "Event Management supported Application for Domain Separation").

### 7\. Troubleshooting Guide

-   [Events in stuck in the "Ready" state.](/kb_view.do?sysparm_article=KB0722851 "Events in stuck in \"Ready\" state.")
