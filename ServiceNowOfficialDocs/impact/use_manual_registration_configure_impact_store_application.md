---
title: Use manual registration to configure the Impact Store Application
description: Manual registration is generally used by advanced users or to obtain configuration support from your Impact Squad. Regulated and GCC customers are also required to use manual registration.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/use\_manual\_registration\_configure\_impact\_store\_application.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Impact reference, Impact]
tags:
  - impact
  - type-task
---

# Use manual registration to configure the Impact Store Application

Manual registration is generally used by advanced users or to obtain configuration support from your [[impact-squad|Impact Squad]]. Regulated and GCC customers are also required to use manual registration.

## Before you begin

Refer to [[configuring-impact-platform|Configure the Impact Store Application]] for prerequisite configuration steps.

**Important:**

Follow the individual topics for each step of the [[impact-landing-page|Impact]] Guided setup. Manual registration is performed in place of the automated registration step 8, [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]].

If the automated registration failed, contact your Impact Squad, as the manual configuration may also fail to complete successfully.

1.  [[install-impact-innovation-lab|Install the Impact Store Application from the ServiceNow Store]]

    Follow these instructions to install the Impact Store Application.

2.  [[guided-setup-impact-in-app|Use Guided Setup for Impact Store Application configuration]]

    Use Impact Guided Setup to follow a sequence of tasks that [[io-help|help]] you configure the Impact Store Application on your ServiceNow instance.

3.  [[onboard_users_impact_store_application|Use Guided Setup to onboard users to the Impact Store Application]]

    Onboard new and existing users to the Impact Store Application.

4.  [[assign-users-scan-engine-groups|Assign users to Scan Engine groups]]

    In addition to assigning Impact users to groups, the [[platform-health-idi|Platform Health]] users must also be part of a group.

5.  [[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]]

    Use Impact Guided Setup to set up the minimum required configuration options to run the first system scan.

6.  [[run-scan-engine|Run your first scan with the Scan Engine]]

    An initial full Scan Engine completion is required to set a baseline from a series of tasks performed that tune the instance environment to complete future scans quickly and efficiently.


Impact

Role required: admin, any Impact role

## Procedure

1.  Complete pre-requisite steps of the Impact Guided setup, as mentioned in the **Before you begin** section.

2.  Complete the manual connection steps:

    1.  [[initiate-the-connection-impact-delivery-instance|Initiate the connection to Impact data with manual registration]].

    2.  [[connect-instance-impact-store-app|Use manual registration to establish the connection to the provider instance]] with Service Bridge registration

3.  Return to Guided Setup to [[verify-impact-data-connection|Verify Impact data connection]]

4.  [[initiate-migration-idi|Initiate data migration from IDI]] that migrates data from IDI to the Impact Store Application.


1.  [Initiate the connection to Impact data with manual registration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/initiate-the-connection-impact-delivery-instance.md)  
Establish a connection between your Impact Store Application and the Impact Delivery Instance to allow the exchange of data.
2.  [Use manual registration to establish the connection to the provider instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/connect-instance-impact-store-app.md)  
The named contact administrator will establish a secure connection to the Impact Delivery Instance \(provider instance\) to transmit data with the Impact Store Application.

**Parent Topic:**[[impact-reference|Impact reference]]

## Related

- [[configuring-impact-platform|Configure the Impact Store Application]]
- [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]
- [[install-impact-innovation-lab|Install Impact]]
- [[guided-setup-impact-in-app|Run Impact Guided Setup]]
- [[onboard_users_impact_store_application|Use Guided Setup to onboard users to the Impact Store Application]]
- [[assign-users-scan-engine-groups|Assign users to Platform Health groups]]
- [[configure-initial-scan-engine-settings|Activate Scan Engine and review settings]]
- [[run-scan-engine|Run your first scan with the Scan Engine]]
- [[initiate-the-connection-impact-delivery-instance|Initiate the connection to Impact data with manual registration]]
- [[connect-instance-impact-store-app|Use manual registration to establish the connection to the provider instance]]
- [[verify-impact-data-connection|Verify Impact data connection]]
- [[initiate-migration-idi|Initiate data migration from IDI]]
- [[impact-reference|Impact reference]]
- [[impact-squad|Impact Squad]]
- [[impact-landing-page|Impact]]
- [[io-help|Help]]
- [[platform-health-idi|Platform Health]]
