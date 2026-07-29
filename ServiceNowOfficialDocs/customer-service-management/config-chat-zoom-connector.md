---
title: Configure Chat Zoom Connector
description: Install and set up the Chat Zoom Connector application to interact with customers using Zoom meetings initiated from a chat.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-chat-zoom-connector.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Chat Zoom Connector, Chat channel, Enable communication channels, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Configure Chat Zoom Connector

Install and set up the Chat Zoom Connector application to interact with customers using Zoom meetings initiated from a chat.

## Before you begin

Role required: admin

## About this task

This task provides general steps to set up the Chat Zoom Connector application for initiating Zoom meetings from a chat.

## Procedure

1.  Integrate the Zoom account of your company with your ServiceNow instance using the Zoom spoke.

    For more information, see [Set up the Zoom spoke](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/setup-zoom.md).

2.  Set up the Notify Zoom connector in Zoom for associating the Notify communication channel with Zoom meetings.

    The conference call details of the Zoom meetings are stored in the Notify Conference Calls \[notify\_conference\_call\] table. For more information, see [Set up Notify Zoom connector](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/setup-notify-zoom-connector.md).

3.  Install the Chat Zoom Connector application.

    For more information, see [Install a ServiceNow Store application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_InstallApplications.md).

    **Note:** The Chat Zoom Connector application installs the CSMZoomInteractionImpl script include, which is preconfigured for the Customer Service application. It also installs the sn\_chat\_zoom.ZoomInteractionExtPoint extension point, which enables the copying of any application-specific fields from the parent chat interaction record to the Zoom interaction record. For more information, see [[config-chat-zoom-ext-pt|Configure application-specific field values for Zoom interactions]].

4.  Activate the Zoom quick action.

    For more information, see [[activate-chat-zoom-quick-action|Activate the quick action for Zoom meetings]].


**Related topics**  


[[chat-zoom-connector|Chat Zoom Connector]]

[[using-chat-zoom-connector|Using Chat Zoom Connector]]

## Related

- [[config-chat-zoom-ext-pt|Configure application-specific field values for Zoom interactions]]
- [[activate-chat-zoom-quick-action|Activate the quick action for Zoom meetings]]
- [[chat-zoom-connector|Chat Zoom Connector]]
- [[using-chat-zoom-connector|Using Chat Zoom Connector]]
