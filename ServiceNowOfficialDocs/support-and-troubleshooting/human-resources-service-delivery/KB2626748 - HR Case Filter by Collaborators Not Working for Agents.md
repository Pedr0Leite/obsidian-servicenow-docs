---
title: "HR Case Filter by Collaborators Not Working for Agents"
aliases:
  - KB2626748
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2626748
kb_number: KB2626748
last_modified: 2026-01-03
---

## HR Case Filter by Collaborators Not Working for Agents

  

### Issue

Filtering the HR Case table using Collaborators is (dynamic) me does not return expected results for non-admin users.  
HR agents cannot view cases where they are set as collaborators, even though they are listed in the field.  
Functionality works for admin users but fails for standard HR agents.  
  

### Release

Any Release

### Cause

The issue occurs because the collaborators field in the `sn_hr_core_case` table lacks the necessary ACL permissions for non-admin users. Specifically, the query\_range access is missing, which prevents the filter from evaluating correctly. When the system checks ACLs during query execution, it ignores the collaborators field for users without this permission

### Resolution

To resolve this, ensure that the ACL configuration for the collaborators field allows non-admin users to query it. The filter relies on the ability to perform a range query on this field, which is controlled by the query\_range operation in ACLs.

Start by reviewing the ACLs for the `sn_hr_core_case` table and confirm whether the collaborators field has the required permissions. If the ACL does not include query\_range, create or update an ACL to grant this access to the appropriate HR roles (for example, `sn_hr_core.agent`). Once this permission is in place, the dynamic filter will work as expected, and HR agents will be able to see cases where they are collaborators.

After applying the ACL changes, test the filter by logging in as an HR agent and using Collaborators is (dynamic) me on the HR Case table. If configured correctly, the cases should now appear without requiring admin privileges.
