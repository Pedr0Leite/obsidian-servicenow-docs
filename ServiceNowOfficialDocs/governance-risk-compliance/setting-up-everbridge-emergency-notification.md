---
title: Setup steps for emergency notification
description: Setting up the Emergency Notification feature requires you, as a BCM admin, to configure certain pre-requisite data. The setup steps help you to establish a consistent connection with Everbridge and a successful notification delivery workflow on the Everbridge side.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/setting-up-everbridge-emergency-notification.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Integrating Crisis Management with Everbridge, Using BCM Classic Workspace, Manage, Business Continuity Management, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-concept
---

# Setup steps for emergency notification

Setting up the Emergency Notification feature requires you, as a BCM admin, to configure certain pre-requisite data. The setup steps help you to establish a consistent connection with Everbridge and a successful notification delivery workflow on the Everbridge side.

These configurations are required to be set up for different users to use the Crisis Management workspace for sending an emergency notification and monitoring the notification workflow:

-   To create a connection and authenticate your credentials with Everbridge, see [[setup-connection-everbridge|Create connection and authenticate credential with Everbridge]].
-   To get the delivery details of the contacts from Everbridge and use them to send notification, see [[setup-delivery-channel-everbridge|Import delivery channels from Everbridge]].
-   To get the details about the type of contacts from Everbridge, see [[record-types-everbridge|Import record types from Everbridge]].
-   To pre-configure a notification template to send an email or SMS to your contacts, see [[setup-notification-template-bcm|Define a template for emergency notification]].
-   To create contacts for sending the notification, see [[create-contact-rules-emergency-notifications|Create contacts for emergency notifications]].
-   To set up rules in filtering the contacts from the user table, see [[contact-import-sync-rule|Create contact import rules]].
-   To create a group of contacts, see [[create-notification-contact-group|Create a notification contact group]].

Here is a flow diagram that shows how the different setup steps are connected for the integration:

\[Omitted image "SetupFlowDiagram.png"\] Alt text: Emergency notification setup flow.

## Related

- [[setup-connection-everbridge|Create connection and authenticate credential with Everbridge]]
- [[setup-delivery-channel-everbridge|Import delivery channels from Everbridge]]
- [[record-types-everbridge|Import record types from Everbridge]]
- [[setup-notification-template-bcm|Define a template for emergency notification]]
- [[create-contact-rules-emergency-notifications|Create contacts for emergency notifications]]
- [[contact-import-sync-rule|Create contact import rules]]
- [[create-notification-contact-group|Create a notification contact group]]
