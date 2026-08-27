---
title: Data Discovery roles
description: You can assign Data Discovery roles to limit user access to certain data types.View, create, and modify, data patterns and related jobs.Read data patterns and target tables.Read data patterns, discovery jobs, and the data\_classification table when an enabled specific pattern finding is classified.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/data-discovery/data-discovery-roles.html
release: australia
product: Data Discovery
classification: data-discovery
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exploring Data Discovery \(Classic\), Data Discovery, Platform Privacy]
tags:
  - platform-security
  - data-discovery
  - pii
  - scanning
  - compliance
  - type-reference
---

# Data Discovery roles

You can assign Data Discovery roles to limit user access to certain data types.

## Data discovery administrator \[sn\_data\_discovery.data\_discovery\_admin\]

View, create, and modify, data patterns and related jobs.

-   Data patterns:
    -   Create
    -   Read
    -   Update
    -   Delete
-   Active data patterns:
    -   Delete
    -   Read
-   Jobs:
    -   Create
    -   Read
    -   Update
    -   Delete
    -   Schedule
    -   Pause
    -   Resume
    -   Cancel
-   Target tables:
    -   Create
    -   Read
    -   Write
-   Granular [[sc-configuration|configuration]]:
    -   Create
    -   Read
    -   Update
    -   Delete
-   [[granular-findings|Granular findings]]:
    -   Create
    -   Read
    -   Actions

        **Note:** [[users|Users]] with this role may only take the ignore action


### Contains Roles

List of roles contained within the role.

-   data\_classification\_auditor
-   data\_classification\_admin
-   sn\_data\_discovery.data\_discovery\_api\_processor

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

Admins are automatically assigned this role on product installation.

**Note:** Avoid granting an admin role when more specialized roles are available.

## Data discovery auditor \[sn\_data\_discovery.data\_discovery\_auditor\]

Read data patterns and target tables.

-   Read data patterns
-   Read active data patterns
-   Read [[data-discovery-jobs|Data Discovery jobs]]
-   Read target tables
-   Review granular configuration
-   [[dds-review-granular-findings|Review granular findings]]

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

None.

## Data classification administrator \[data\_classification\_admin\]

Read data patterns, discovery jobs, and the data\_classification table when an enabled specific pattern finding is classified.

### Contains Roles

The [[data-classification|Data classification]] role contains the List of roles contained within the data\_classification\_auditor role.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** For more information about the Data Classification admin role, see [Installing Data Classification plugin demo data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-classification/install-data-classification-plugin-demo-data.md).

## Related

- [[sc-configuration|Configuration]]
- [[granular-findings|Granular Findings]]
- [[users|Users]]
- [[data-discovery-jobs|Data Discovery jobs]]
- [[dds-review-granular-findings|Review granular findings]]
- [[data-classification|Data Classification]]
