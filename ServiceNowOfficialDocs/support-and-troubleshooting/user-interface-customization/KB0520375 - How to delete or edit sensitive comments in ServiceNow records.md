---
title: "How to delete or edit sensitive comments in ServiceNow records"
aliases:
  - KB0520375
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0520375
kb_number: KB0520375
last_modified: 2026-01-16
---

## How to delete or edit sensitive comments in ServiceNow records

  

### Issue

When comments or work notes contain sensitive information in ServiceNow records, you may need to edit or delete them from journal entries, audit records, and email entries to maintain data privacy. This process requires administrator privileges and cannot be performed by regular users.

### Release

  All supported releases

### Resolution

### Prerequisites

-   **Required permissions**: Admin access or a role with elevated privileges to modify system tables.
-   If you are a regular user who needs to remove a comment, contact your ServiceNow administrator with the record details.

**Warning**: Viewing the entire sys\_audit table may retrieve a large number of records and can seriously affect instance performance during the query.

### Get the record sys\_id

1.  Right-click on the record and select **Copy URL to Clipboard** to obtain the unique sys\_id.
2.  Copy the sys\_id from the URL. For example, in https://<instance>.service-now.com/nav\_to.do?uri=incident.do?sys\_id=85befb1c4a34bb12013b216a9fd5fee8, the sys\_id is 85befb1c4a34bb12013b216a9fd5fee8.

### Update the journal entry

1.  Go to the journal entry using one of these methods:
    -   Enter the URL with your sys\_id: https://<instance>.service-now.com/sys\_journal\_field\_list.do?sysparm\_query=element\_id=85befb1c4a34bb12013b216a9fd5fee8
    -   Go to **System Definition** > **Tables** \> **Journal Field** and search for your record sys\_id.
2.  Locate the journal entry containing the sensitive information.
3.  Modify the record and select **Update** or **Delete**.

### Update the audit entry

1.  Go to the audit entry using one of these methods:
    -   Enter the URL with your sys\_id: https://<instance>.service-now.com/sys\_audit\_list.do?sysparm\_query=documentkey=85befb1c4a34bb12013b216a9fd5fee8
    -   Go to **System Definition** > **Tables** \> **Audit** and search for your record sys\_id.
2.  Locate the audit entry containing the sensitive information.
3.  Modify the record and select **Update** or **Delete.**

### Rebuild the history set

This step is only required when you do not use direct auditing and the glide.sys.activity\_using\_audit\_direct property is set to false (default value if the system property does not exist on the instance).

1.  Go to the History Set records using one of these methods:
    -   Enter the URL with your sys\_id: https://<instance>.service-now.com/sys\_history\_set\_list.do?sysparm\_query=id=85befb1c4a34bb12013b216a9fd5fee8
    -   Go to **System Definition** > **Tables** \> **History Set** and search for your record sys\_id.
2.  Select **Delete** for each History Set. This deletes the History Set, not the audit data.

The History Set rebuilds with the corrected audit and journal information when a user views the item.

### Update the email entry

1.  Go to the email entry using one of these methods:
    -   Enter the URL with your sys\_id: https://<instance>.service-now.com/sys\_email\_list.do?sysparm\_query=instance=85befb1c4a34bb12013b216a9fd5fee8
    -   Go to **System Definition** > **Tables** \> **Email** and search for your record sys\_id.
2.  Locate the email entry containing the sensitive information.
3.  Modify the record and select **Update** or **Delete**.

### Update the email history

1.  Go to the email history line entries using one of these methods:
    -   Enter the URL: /history.do?sysparm\_table=sys\_email&sysparm\_sys\_id=\[email sys\_id\]&sysparm\_nostack=true
    -   Go to **System Definition** > **Tables** \> **History Line** and search for entries related to your email record.
2.  Locate the history line entries containing sensitive information.
3.  Delete or modify these entries to remove the sensitive information.

### Troubleshooting

#### **Cannot find the journal entry**

-   Verify you are using the correct sys\_id.
-   Check if the comment was added to a different field than expected.
-   Confirm that you have the necessary permissions to view the sys\_journal\_field table.

#### **Cannot modify or delete entries**

-   Verify you have administrator privileges or the appropriate role.
-   Contact your system administrator if you need assistance.

## FAQ

### Why can't regular users edit their own comments?

ServiceNow restricts this capability to administrators to maintain data integrity and audit compliance. Allowing users to edit their own comments would require careful implementation of audit logging to track all changes. 

### How can regular users request comment deletion?

If you added a comment in error, contact your ServiceNow admin. Provide the admin with:

-   The record number
-   The specific comment that needs to be removed
-   The reason for removal

### Important notes

-   If history rebuilding is not possible on a record, the reference is likely broken.
-   When modifying a comment, do not delete the old one. Instead, make modifications in both the sys\_journal\_field and sys\_audit tables against the same record.
-   After modifications, rebuild the sys\_history\_set to load the updated comment in the record.

### Related Links
