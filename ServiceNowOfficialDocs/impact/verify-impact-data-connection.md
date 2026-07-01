---
title: Verify Impact data connection
description: During Impact Guided Setup automated registration, a status is provided to indicate a successful connection. Use the Verify the Connection step to track the progress.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/verify-impact-data-connection.html
release: australia
topic_type: task
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Configure the Impact Store Application, Configuring Impact, Impact]
tags:
  - impact
  - type-task
---

# Verify Impact data connection

During [[impact-landing-page|Impact]] Guided Setup automated registration, a status is provided to indicate a successful connection. Use the Verify the Connection step to track the progress.

## Before you begin

[[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]] before this procedure.

Role required: impact app admin, impact admin \(IDI\)

## Procedure

1.  Navigate to **All** &gt; **Impact** &gt; **Configuration** &gt; **Guided Setup** &gt; **Verify the Connection**.

    The Verify connection table loads. Once the connection has been initiated, the status updates in the Provider connections record.

    **Note:** \[Omitted image "verify-connection-status.png"\] Alt text: Verify connection table with the success statuses, Active Replication showing.

2.  Verify that the inbound and outbound statuses update to **Active Replication**.

<table id="table_fbs_gqq_zfc"><thead><tr><th>

Status

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Outbound status

</td><td>

-   **Active replication**: Status with successful connection and registration.
-   **Not onboarded**: The status before a successful connection to IDI and registration is completed.


</td></tr><tr><td>

Inbound status

</td><td>

-   **Active replication**: Status with successful connection and registration.
-   **Not onboarded**: The status before a successful connection to IDI and registration is completed.


</td></tr></tbody>
</table>    **Warning:** If either status does not update to Active Replication, contact your Impact Customer Success Manager for further assistance. In some cases, you may be instructed to continue with the manual registration process. See [[initiate-the-connection-impact-delivery-instance|Initiate the connection to Impact data with manual registration]] for manual registration.


## What to do next

[[initiate-migration-idi|Initiate data migration from IDI]]

**Parent Topic:**[[configuring-impact-platform|Configure the Impact Store Application]]

**Previous topic:**[Use automated registration to connect to the Impact Delivery Instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/start-automated-registration-IDI.md)

**Next topic:**[Initiate data migration from IDI](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/initiate-migration-idi.md)

## Related

- [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]
- [[initiate-the-connection-impact-delivery-instance|Initiate the connection to Impact data with manual registration]]
- [[initiate-migration-idi|Initiate data migration from IDI]]
- [[configuring-impact-platform|Configure the Impact Store Application]]
- [[impact-landing-page|Impact]]
