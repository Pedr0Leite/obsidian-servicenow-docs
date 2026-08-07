---
title: Configure the Impact Store Application
description: The tasks are outlined that are required to install and then configure the Impact Store Application using Guided Setup.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/configuring-impact-platform.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring Impact, Impact]
tags:
  - impact
  - type-concept
---

# Configure the Impact Store Application

The tasks are outlined that are required to install and then configure the Impact Store Application using Guided Setup.

Guided setup provides a sequence of tasks that [[io-help|help]] you configure the Impact Store Application in your ServiceNow instance.

The configuration and connection steps must be performed for each instance to connect to the [[impact-landing-page|Impact]] Delivery Instance for multi-instance configurations.

Automated registration, the preferred method, initiates the connection and the registration to the Impact Delivery Instance provider instance into combined tasks.

**Note:** Regulated and GCC customers are required to perform Manual registration. See [[use_manual_registration_configure_impact_store_application|Use manual registration to configure the Impact Store Application]].

Follow the individual topics for each step of the Impact Guided setup.

1.  [[install-impact-innovation-lab|Install Impact]]  
Follow these instructions to install the Impact Store Application.
2.  [[guided-setup-impact-in-app|Run Impact Guided Setup]]  
Use Impact Guided Setup to follow a sequence of tasks that help you configure the Impact Store Application on your ServiceNow instance.
3.  [[onboard_users_impact_store_application|Use Guided Setup to onboard users to the Impact Store Application]]  
Onboard new and existing users to the Impact Store Application.
4.  [[assign-users-scan-engine-groups|Assign users to Platform Health groups]]  
In addition to assigning Impact users to groups, [[platform-health-idi|Platform Health]] users must also be part of a group for the Scan Engine feature.
5.  [[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]]  
Use Impact Guided Setup to set up the minimum required configuration options in order to run the first system scan.
6.  [[run-scan-engine|Run your first scan with the Scan Engine]]  
An initial full Scan Engine completion is required to set a baseline from a series of tasks performed that tune the instance environment to complete future scans quickly and efficiently.
7.  [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]  
The automated registration process simplifies the configuration process and connects your Impact Store Application with data from the Impact Delivery Instance.
8.  [[verify-impact-data-connection|Verify Impact data connection]]  
During Impact Guided Setup automated registration, a status is provided to indicate a successful connection. Use the Verify the Connection step to track the progress.
9.  [[initiate-migration-idi|Initiate data migration from IDI]]  
After the connection is established between your Impact Store Application and the Impact Delivery Instance, next migrate your data.
10. [[instance-integration-scan-engine|Scan Engine integrations]]  
Scan Engine integrates with other ServiceNow instances and external agile systems to synchronize definitions, manage exception reasons, create user stories, and enforce governance over app deployments.
11. [[hop-access-impact-squad|Grant temporary instance access to your Impact Squad]]  
Familiarize yourself with your ServiceNow [[impact-squad|Impact Squad]], a dedicated team of experts ready to assist in tackling your team's unique transformation challenges. View or grant your Impact squad 30 day read-only access to your instance to support you with Impact features.

**Parent Topic:**[[configuring-impact|Configuring Impact]]

## Related

- [[use_manual_registration_configure_impact_store_application|Use manual registration to configure the Impact Store Application]]
- [[install-impact-innovation-lab|Install Impact]]
- [[guided-setup-impact-in-app|Run Impact Guided Setup]]
- [[onboard_users_impact_store_application|Use Guided Setup to onboard users to the Impact Store Application]]
- [[assign-users-scan-engine-groups|Assign users to Platform Health groups]]
- [[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]]
- [[run-scan-engine|Run your first scan with the Scan Engine]]
- [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]
- [[verify-impact-data-connection|Verify Impact data connection]]
- [[initiate-migration-idi|Initiate data migration from IDI]]
- [[instance-integration-scan-engine|Scan Engine integrations]]
- [[hop-access-impact-squad|Grant temporary instance access to your Impact Squad]]
- [[configuring-impact|Configuring Impact]]
- [[io-help|Help]]
- [[impact-landing-page|Impact]]
- [[platform-health-idi|Platform Health]]
- [[impact-squad|Impact Squad]]
