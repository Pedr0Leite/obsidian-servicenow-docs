---
title: "For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page"
aliases:
  - KB0695387
tags:
  - servicenow
  - support-kb
  - acl
  - access-control-list
  - approvals
  - sysapproval_approver
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695387
kb_number: KB0695387
last_modified: 2024-04-07
---

## For users with the itil, catalog, or approval\_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page

  

### Issue

# Symptoms

* * *

When a user with the itil, catalog, or approval\_admin role accesses the My Approvals module, a message is displayed:

Security constraints prevent access to requested page

# Release

* * *

All releases.

# Cause

* * *

The out-of-box table-level read ACL for sysapproval\_approver may have been deactivated or modified.

# Resolution

* * *

1.  Elevate to the security\_admin role.
2.  Restore the out-of-box table-level read ACL for sysapproval\_approver by reactivating it if it was deactivated and/or restoring the script value to its original value:  
    
    if (gs.getProperty("glide.approvals.restrict\_by\_record", "false") == "true")
    
        answer = gs.hasRole('approval\_admin') || gs.hasRole('itil') || gs.hasRole('catalog') || (isApprovalMine(current) && hasAccessToDocument(current));
    
    else
    
        answer = gs.hasRole('approval\_admin') || gs.hasRole('itil') || gs.hasRole('catalog') || isApprovalMine(current) || hasAccessToDocument(current);  
      
    
    3\. Save the ACL record.

## Related

- [[KB0749174 - Customization considerations for Access Controls (ACLs)]] - guidance on safely modifying OOB ACLs like this one
- [[KB0727211 - FAQ Can an ACL work on the list view and be bypassed on the related list (or vice versa)]]
- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[access-control-rules]] - official docs on ACL rule evaluation
- [[c_ApprovalEngines]] - official docs on approval engine configuration

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access|A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message|Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0749174 - Customization considerations for Access Controls (ACLs)|Customization considerations for Access Controls (ACLs)]]
