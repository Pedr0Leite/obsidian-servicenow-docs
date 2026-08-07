---
title: "HR Life Cycle Records not Displaying SLA Timeline"
aliases:
  - KB0779092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779092
kb_number: KB0779092
last_modified: 2024-04-08
---

## HR Life Cycle Records not Displaying SLA Timeline

  

### Issue

Users with sn\_hr\_le.case\_reader are not able to see SLA timeline on HR life cycle records.

### Release

London and above

### Cause

This is expected behavior as SLAs are viewable only if the user has the ITIL role.

### Resolution

There are 3 possible solutions for this:

1.  The HR admin can decided if they want to provide the ITIL role to the users (This will allow the users to see data from any table within the scope of ITIL change, problem, incident, etc)
2.  Create an ACL that only allows the users with the sn\_hr\_le.case\_reader to see the SLAs that correlate with the HR life cycle record
3.  Create a before query business rule that will only allow the user with sn\_hr\_le.case\_reader to see the SLAs that correlate with the HR life cycle record
