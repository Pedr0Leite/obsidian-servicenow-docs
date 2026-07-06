---
title: "Does not have access to performance_dashboards_main.do blank"
aliases:
  - KB0715670
tags:
  - servicenow
  - support-kb
  - pdb_user
  - performance-analytics
  - dashboards
  - roles
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715670
kb_number: KB0715670
last_modified: 2023-09-05
---

## Does not have access to performance\_dashboards\_main.do blank

  

### Issue

User navigates to "_**performance\_dashboards\_main.do"**_ and gets a blank page

![](/sys_attachment.do?sys_id=c88d61a2930db1d0080af35d6cba10b3)

### Resolution

User must have the "_**pdb\_user**_" role in order to view data for page "_**performance\_dashboards\_main.do"**_

This role is required by our code written in the backend. Admins can override this rule.

Therefore to address this issue you need to assign the "_**pdb\_user**_" role to the affected user

# ![](/sys_attachment.do?sys_id=377d61a2930db1d0080af35d6cba10b0)

## Related

- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[KB0743902 - Unable to view all sys_user_preferences records as an Admin, seeing security constraints message]]
