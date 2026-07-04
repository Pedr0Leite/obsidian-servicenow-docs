---
title: "SAM licenses consumed by inactive users and retired computers or servers"
aliases:
  - KB2579752
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2579752
kb_number: KB2579752
last_modified: 2026-05-22
---

## SAM licenses consumed by inactive users and retired computers or servers

  

### Issue

In Software Asset Management (SAM), licenses may appear overutilized when inactive users or retired computers and servers continue to consume license counts. This article explains how to identify and remove these records and how to view license consumption details.

  

### Release

All

### Resolution

Step 1 — Review your current license counts

Navigate to the following URL on your instance to view active subscription entitlements and license counts by segment:

`/itam_licensing_resource_counts_list.do?sysparm_query=is_aggregated%3Dtrue%5Eactive_subscription_entitlement%3Dtrue`

This view is populated when the scheduled job SAM/CI - Populate Licensing Data runs, which uses the SAMLicensingUtility script.

Step 2 — Remove installs from retired devices

By default, the system counts licenses for servers and end-user computers based on devices that have software installs and were last discovered within 90 days. Retired status is not considered in this count.

To stop retired devices from consuming licenses, remove the software installs from those devices. To review the list of devices currently being counted, navigate to:

`/itam_ci_usage_list.do`

Step 3 — Clean up inactive subscription records

For subscription-based licensing, the system counts records in the subscription table by default. The active or inactive status of the associated user is not evaluated.

To reduce overutilization, delete inactive records from the samp\_sw\_subscription table. Navigate to:

`/samp_sw_subscription_list.do`

Filter for inactive records and delete them.

Step 4 — Remove subscriptions without an associated profile

Subscriptions without an associated profile may also contribute significantly to license overconsumption. Review the subscription list (same URL as Step 3), filter for records with no profile, and remove them.
