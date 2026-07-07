---
title: "The non-admin users are not able to access to a table"
aliases:
  - KB0753582
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - table-acl
  - read-acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753582
kb_number: KB0753582
last_modified: 2024-01-28
---

## The non-admin users are not able to access to a table

  

### Issue

The non-admin users are not able to access to a table.

### Release

All releases. This would be applied to both OOB tables and custom tables.

### Cause

The issue should be caused by either or two of the following reasons:

1\. There is no any base system STAR (\*) table level read ACL with record Type for the affected table.

2\. There is no any read ACL with its name matches the table name for the affected table.

According to the documentation [https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest](https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest), the user must first pass the table ACL rule. Since the base system includes STAR (\*) table ACL rules that match every table, the user must always pass at least one table ACL rule. The base system provides additional table ACL rules to control access to specific tables.   
  
Table ACL rules are processed in the following order:   
1\. Match the table name. For example, incident.   
2\. Match the parent table name. For example, task.   
3\. Match any table name (\*). For example, \*.   
  
If a user fails all table ACL rules, the user cannot access the fields in any table. If a user passes a table ACL rule, the system then evaluates the field ACL rules.

### Resolution

The issue can be resolved in the following ways:

1.  Create at least one base system STAR (\*) table level read ACL with record Type for the affected table.
2.  Create at least one read ACL with its name matches the table name for the affected table.

### Related Links

Please refer to the documentation [https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest](https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest) to get a better understanding about how ACLs are working on a table.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — the two-gate table/field ACL evaluation model this article assumes
- [[KB0749738 - SLA Definition field value is not displaying on task sla list or related lists for some users]] — same table-level read ACL root cause
- [[KB0813250 - User with no read access to a Table see a blank form instead of a security message (Security constraints prevent access ]] — related consequence of missing table read access
- [[acl-rule-types]] — official docs on ACL rule types and matching order

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0749738 - SLA Definition field value is not displaying on task sla list or related lists for some users|SLA Definition field value is not displaying on task sla list or related lists for some users]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
