---
title: "Community content approval"
aliases:
  - KB0995395
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995395
kb_number: KB0995395
last_modified: 2024-08-10
---

## Issue

After installing the CSM Community plugin, how can Community content which is "under review" be approved?

## Resolution

Approvers can go to the sysapproval\_approver table and filter where Source table=sn\_communities\_content to see the approval requests:  
/sysapproval\_approver\_list.do?sysparm\_query=source\_table%3Dsn\_communities\_content&sysparm\_view=  
  
Also see:  
https://community.servicenow.com/community?id=community\_question&sys\_id=434c76671bc4d49cd01143f6fe4bcb01

A couple of workarounds that can be considered are:

1\. Add a 'New Content Approvals' menu item under the Community application menu, just like 'Forum Membership Approvals'. The implementation is a customization which is out of scope of Technical Support.  
2\. Add the approver\_user role to the user or the Community Administrators group, so that the Self-Service / My Approvals menu items appears for community admins.
