---
title: Initiate data migration from IDI
description: After the connection is established between your Impact Store Application and the Impact Delivery Instance, next migrate your data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/initiate-migration-idi.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure the Impact Store Application, Configuring Impact, Impact]
tags:
  - impact
  - type-task
---

# Initiate data migration from IDI

After the connection is established between your [[impact-landing-page|Impact]] Store Application and the Impact Delivery Instance, next migrate your data.

## Before you begin

**Note:** [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]] prior to migrating data.

Role required: impact app admin, admin

## Procedure

1.  Navigate to **All** &gt; **Impact** &gt; **Configuration** &gt; **Guided Setup** &gt; **Initiate sync &amp; migration**.

2.  Select **Initiate migration** from the listed tasks.

3.  On the Impact Data Migration overviews table, select **Start Data Migration**.

    \[Omitted image "initiate-data-migration.png"\] Alt text: Initiate migration step with the Start data migration button highlighted.

4.  Check the migration status for each table in the Impact Data Migration Overviews table.

5.  Refresh the page to re-populate the migration statuses in the table data.

    The **Overall Migration Status** for each table will update to `Completed` when successfully transferred. Reach out to your [[impact-squad|Impact Squad]] if you require assistance or a table failed to migrate.

6.  Select **Mark as Complete** on the Initiate Migration page when the data transfer is complete.


## What to do next

-   [[hop-access-impact-squad|Grant temporary instance access to your Impact Squad]]
-   See [[instance-integration-scan-engine|Scan Engine integrations]] to connect instances and external agile systems to synchronize definitions, manage exception reasons, create user stories, and enforce governance over app deployments.
-   With successful connection and registration, see [[impact-in-app|Using Impact]] to get started with your Impact Store Application.

**Parent Topic:**[[configuring-impact-platform|Configure the Impact Store Application]]

**Previous topic:**[[verify-impact-data-connection|Verify Impact data connection]]

**Next topic:**[Scan Engine integrations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/impact/instance-integration-scan-engine.md)

## Related

- [[start-automated-registration-IDI|Use automated registration to connect to the Impact Delivery Instance]]
- [[hop-access-impact-squad|Grant temporary instance access to your Impact Squad]]
- [[instance-integration-scan-engine|Scan Engine integrations]]
- [[impact-in-app|Using Impact]]
- [[configuring-impact-platform|Configure the Impact Store Application]]
- [[verify-impact-data-connection|Verify Impact data connection]]
- [[impact-landing-page|Impact]]
- [[impact-squad|Impact Squad]]
