---
title: "The Microsoft Azure AD Spoke cannot be used to Manage Mail-Enabled Security Groups"
aliases:
  - KB0999092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999092
kb_number: KB0999092
last_modified: 2025-01-02
---

## The Microsoft Azure AD Spoke cannot be used to Manage Mail-Enabled Security Groups

  

### Summary

The Microsoft Azure AD Spoke has Actions such as 'Add User to Group' and 'Remove User from Group'. These Actions cannot be used to manage mail-enabled Security Groups. The cause of this is that in Azure AD Mail-enabled security groups cannot be managed or updated via API and are read-only:

[Working with groups in Microsoft Graph](https://docs.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0 "Working with groups in Microsoft Graph")

![](sys_attachment.do?sys_id=a13b4e6cdb73b45080073ca8f4961930)

### Release

This is a limitation on the Microsoft Azure side. There is some indication that the limitation was put in place in late 2021 (i.e previously it was possible to manage Mail-Enabled Security groups via API calls), however, we do not have definite information on that and further questions would need to be directed to Microsoft support.
