---
title: Configure Scan Engine instance integration settings
description: You can view and configure a variety of information, formatted into lists, that the Scan Engine uses to implement its various scanning types.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/add-view-scan-engine-related-lists.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure Scan Engine properties, Activate Scan Engine and review settings, Configure the Impact Store Application, Configuring Impact, Impact]
tags:
  - impact
  - type-concept
---

# Configure Scan Engine instance integration settings

You can view and configure a variety of information, formatted into lists, that the Scan Engine uses to implement its various scanning types.

Role required: Scan Engine admin and [[impact-landing-page|Impact]] admin.

## System properties

These are the properties specifically created by the Scan Engine application upon installation. Modification of these properties is performed using standard procedures in ServiceNow.

## My SN Instances

Each record indicates an instance connected to the current instance through API integrations.

**Note:** You must configure this to take advantage of exception processing, definition syncing, and user story tracking in Production.

1.  To add an instance to the list, select **New**.
2.  Configure the following fields and settings.

<table id="table_aj5_vx4_ghc"><thead><tr><th>

Field/Setting

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Instance Name

</td><td>

The name of the instance.

</td></tr><tr><td>

Instance URL

</td><td>

The URL of the instance.

</td></tr><tr><td>

Environment

</td><td>

The instance environment:

 -   Development
-   Production
-   Test
 **Important:** Only one instance can be listed as Production. Otherwise, the integration will fail.

</td></tr><tr><td>

Validated

</td><td>

-   Indicates whether the instance has been successfully validated using the UI Action provided in the configuration interface.
-   You can use the **Validate Connection** action available on the instance configuration form to attempt a live connection to the target instance using the defined credentials and connection parameters. If successful, the instance is flagged as Validated = true.


</td></tr><tr><td>

Connection Status

</td><td>

-   Represents the current state of connectivity between local and remote instances.
-   This field is automatically updated based on the results of the validation process. It reflects the outcome of the live connection test and cannot be edited.
-   The following values are supported:

    -   Approvals not configured in production
    -   Authentication method is not configured
    -   Connection Valid
    -   Connection Invalid
    -   API User is missing role
    -   User not setup on target instance
These values [[io-help|help]] diagnose integration issues, as well as help with corrective actions.

</td></tr><tr><td>

Authentication Type

</td><td>

The instance’s authentication type:

 -   Basic
-   OAuth


</td></tr><tr><td>

API Credential Config

</td><td>

-   This field references the credential record used for authentication when **Basic** is selected as the Authentication Type.
-   It typically points to a Basic Auth credential stored securely in the system.


</td></tr><tr><td>

OAuth Application Registry

</td><td>

-   The OAuth application registry used for cross-instance integrations.
-   This field is only available if **OAuth** was selected as the **Authentication Type**.


</td></tr><tr><td>

OAuth User Profile

</td><td>

The OAuth user profile used for cross-instance integrations.

</td></tr></tbody>
</table>
**Note:** See [[instance-integration-scan-engine|Scan Engine integrations]] for details on integration setup.

**Parent Topic:**[[configure-scan-engine-properties|Configure Scan Engine properties]]

## Related

- [[instance-integration-scan-engine|Scan Engine integrations]]
- [[configure-scan-engine-properties|Configure Scan Engine properties]]
- [[impact-landing-page|Impact]]
- [[io-help|Help]]
