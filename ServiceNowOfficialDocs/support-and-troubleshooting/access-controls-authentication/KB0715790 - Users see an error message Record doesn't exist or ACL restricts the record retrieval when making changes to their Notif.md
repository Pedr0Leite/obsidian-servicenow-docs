---
title: "Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings"
aliases:
  - KB0715790
tags:
  - servicenow
  - support-kb
  - acl
  - cmn_notif_message
  - notifications
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715790
kb_number: KB0715790
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Users see an error message "Record doesn't exist or ACL restricts the record retrieval" when making changes to their Notifications settings

# Release

* * *

All 

# Cause

* * *

The ability to make changes to your notification settings requires CREATE access to the cmn\_notif\_message. This is the table where your settings are stored. It is likely that your users are not getting the required permissions.

# Resolution

* * *

Unless you've made changes to the ACLs for this table, it is likely there will be only 1 CREATE ACL for cmn\_notif\_message. Review the conditions and make the necessary adjustments to allow your users to pass.

## Related

- [[KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif]] - same error message, different underlying ACL
- [[KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[access-control-rules]] - official docs on ACL rule evaluation
