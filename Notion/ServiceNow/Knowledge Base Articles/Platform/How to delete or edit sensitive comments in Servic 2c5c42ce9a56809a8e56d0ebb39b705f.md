---
aliases:
  - "How to delete or edit sensitive comments in Servic"
tags:
  - knowledge-base
  - platform
  - security
  - data-privacy
  - audit
---

# How to delete or edit sensitive comments in ServiceNow records

### **Issue**

When comments or work notes contain sensitive information in ServiceNow records, you may need to edit or delete them from journal entries, audit records, and email entries to maintain data privacy. This process requires administrator privileges and cannot be performed by regular users.

### **Release**

All supported releases

### **Resolution**

### **Prerequisites**

- Required permissions: Administrator access or a role with elevated privileges to modify system tables
- If you are a regular user who needs to remove a comment, you must contact your ServiceNow administrator with the record details

> Warning: Viewing the entire sys_audit table may retrieve a large number of records and can seriously affect instance performance during the query.
> 

### **Get the record's sys_id**

1. Right-click on the record and select Copy URL to Clipboard to obtain the unique sys_id.
2. Copy the sys_id from the URL. For example, in `https://<instance>.service-now.com/nav_to.do?uri=incident.do?sys_id=85befb1c4a34bb12013b216a9fd5fee8`, the sys_id is `85befb1c4a34bb12013b216a9fd5fee8`.

### **Update the journal entry**

1. Navigate to the journal entry using one of these methods:
    - Enter the URL with your sys_id: `https://<instance>.service-now.com/sys_journal_field_list.do?sysparm_query=element_id=85befb1c4a34bb12013b216a9fd5fee8`
    - Or navigate to System Definition > Tables > Journal Field and search for your record's sys_id
2. Locate the journal entry containing the sensitive information.
3. Modify the record and select update or delete.

### **Update the audit entry**

1. Navigate to the audit entry using one of these methods:
    - Enter the URL with your sys_id: `https://<instance>.service-now.com/sys_audit_list.do?sysparm_query=documentkey=85befb1c4a34bb12013b216a9fd5fee8`
    - Or navigate to System Definition > Tables > Audit and search for your record's sys_id
2. Locate the audit entry containing the sensitive information.
3. Modify the record and select update or delete.

### **Rebuild the history set**

This is only required when you do not use direct auditing and the System Property glide.sys.activity_using_audit_direct is set to false (default value if the System Property does not exist on the instance).

1. Navigate to the History Set records using one of these methods:
    - Enter the URL with your sys_id: `https://<instance>.service-now.com/sys_history_set_list.do?sysparm_query=id=85befb1c4a34bb12013b216a9fd5fee8`
    - Or navigate to System Definition > Tables > History Set and search for your record's sys_id
2. Select the Delete button for each History Set. This deletes the History Set, not the audit data.
3. The History Set will be rebuilt with the corrected audit and journal information when a user views the item.

### **Update the email entry**

1. Navigate to the email entry using one of these methods:
    - Enter the URL with your sys_id: `https://<instance>.service-now.com/sys_email_list.do?sysparm_query=instance=85befb1c4a34bb12013b216a9fd5fee8`
    - Or navigate to System Definition > Tables > Email and search for your record's sys_id
2. Locate the email entry containing the sensitive information.
3. Modify the record and select update or delete.

### **Update the email history**

1. Navigate to the email history line entries using one of these methods:
    - Enter the URL: `/history.do?sysparm_table=sys_email&sysparm_sys_id=[email sys_id]&sysparm_nostack=true`
    - Or navigate to System Definition > Tables > History Line and search for entries related to your email record
2. Locate the history line entries containing sensitive information.
3. Delete or modify these entries to remove the sensitive information.

# **Troubleshooting**

### **Cannot find the journal entry**

- Verify you are using the correct sys_id
- Check if the comment was added to a different field than expected
- Ensure you have the necessary permissions to view the sys_journal_field table

### **Cannot modify or delete entries**

- Verify you have administrator privileges or the appropriate role
- Contact your system administrator if you need assistance

# **FAQ**

### **Why can't regular users edit their own comments?**

ServiceNow restricts this capability to administrators to maintain data integrity and audit compliance. While users can see the need to edit their own comments, allowing this would require careful implementation of audit logging to track all changes.

### **How can regular users request comment deletion?**

If you've added a comment in error, contact your ServiceNow administrator with:

- The record number
- The specific comment that needs to be removed
- The reason for removal

### **Important notes**

- If history rebuilding is not possible on a record, the reference is likely broken.
- When modifying a comment, don't delete the old one. Instead, make modifications in both the sys_journal_field and sys_audit tables against the same record.
- After modifications, rebuild the sys_history_set to load the updated comment in the record.

**Related Links**

## Related

- [[Platform]]
- [[Knowledge Base Articles]]
- [[Security & ACL]]
- [[Confidential Attachments]]