---
title: Link to related records
description: A notification can link to a related record by specifying a reference field in front of the $\{URI\} or $\{URI\_REF\} parameters.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_LinkToRelatedRecords.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Links to records, Create an email notification, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Link to related records

A notification can link to a related record by specifying a [[reference-email-admin|reference]] field in front of the**$\{URI\}** or **$\{URI\_REF\}** [[r_DirectJDBCProbeParameters|parameters]].

Format the related record link as follows:

-   `${<reference field that contains the related record you want to display>.URI}`
-   `${<reference field that contains the related record you want to display>.URI_REF}`

For example:

<table id="table_z4t_qxp_rq"><thead><tr><th>

Related record to provide link to

</th><th>

Notification record table

</th><th>

Reference field

</th><th>

Samples

</th></tr></thead><tbody><tr><td>

Related task record to be approved from an approval notification

</td><td>

Approval \[sysapproval\_approver\]

</td><td>

Approval for \[sysapproval\]

</td><td>

-   $\{sysapproval.URI\}
-   $\{sysapproval.URI\_REF\}

</td></tr><tr><td>

Related problem record in an incident notification

</td><td>

Incident

</td><td>

Problem \[problem\_id\]

</td><td>

-   $\{problem\_id.URI\}
-   $\{problem\_id.URI\_REF\}

</td></tr></tbody>
</table>For example, the following notification template produces the email links in the picture below:

```
Click here to view Incident: ${URI_REF}
Click here to view Related Problem: ${problem_id.URI_REF}
```

\[Omitted image "RelatedRecordLink.png"\] Alt text: Related record link.

**Parent Topic:**[[c_EnablingLinksToServiceNowRecords|Links to records in email notifications]]

## Related

- [[c_EnablingLinksToServiceNowRecords|Links to records in email notifications]]
- [[reference-email-admin|Reference]]
- [[r_DirectJDBCProbeParameters|Parameters]]
