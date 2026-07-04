---
title: "How to make template creation menu from Toggle template bar applicable for uses with 'sn_hr_core.basic' role"
aliases:
  - KB0696045
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696045
kb_number: KB0696045
last_modified: 2024-04-07
---

## How to make template creation menu from Toggle template bar applicable for uses with 'sn\_hr\_core.basic' role

  

### Issue

  
  

# Description

* * *

According to the documentation, only users with 'sn\_core\_hr.admin' role can create or modify HR Case templates.

[https://docs.servicenow.com/](https://docs.servicenow.com/)

Some customers need general HR users which just have 'sn\_hr\_core.basic' to create HR Case template.

# Procedure

* * *

The workaround for this is creating the following ACL Rules.

1.  Log in as admin.
2.  Create the following ACL Rules.

<table><tbody><tr><td><strong>Name&nbsp;</strong></td><td><strong>Operation&nbsp;</strong></td><td><strong>Scope&nbsp;</strong></td><td><strong>&nbsp;Type</strong></td></tr><tr><td>&nbsp;sys_template.*</td><td>&nbsp;Create</td><td>&nbsp;Global</td><td>&nbsp;record</td></tr><tr><td>&nbsp;sys_template.*</td><td>&nbsp;Write</td><td>&nbsp;Global</td><td>&nbsp;record</td></tr><tr><td>&nbsp;sys_template.*</td><td>&nbsp;Read</td><td>&nbsp;Global</td><td>&nbsp;record</td></tr><tr><td>&nbsp;sn_hr_core_case.*</td><td>&nbsp;save_as_template</td><td>&nbsp;Human Resources:core</td><td>&nbsp;record</td></tr><tr><td>&nbsp;sn_hr_core_case</td><td>&nbsp;save_as_template</td><td>&nbsp;Human Resources:core</td><td>&nbsp;record</td></tr></tbody></table>

#   
  
Applicable Versions

* * *

Kingston Patch 7
