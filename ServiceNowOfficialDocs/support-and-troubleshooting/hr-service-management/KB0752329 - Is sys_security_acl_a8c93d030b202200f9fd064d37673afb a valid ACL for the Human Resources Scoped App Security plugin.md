---
title: "Is sys_security_acl_a8c93d030b202200f9fd064d37673afb a valid ACL for the \"Human Resources Scoped App: Security\" plugin?"
aliases:
  - KB0752329
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752329
kb_number: KB0752329
last_modified: 2024-04-07
---

## Is sys\_security\_acl\_a8c93d030b202200f9fd064d37673afb a valid ACL for the "Human Resources Scoped App: Security" plugin?

  

### Issue

# Overview

Is sys\_security\_acl\_a8c93d030b202200f9fd064d37673afb a valid ACL for the "Human Resources Scoped App: Security" plugin?

# Response

This ACL (sys\_security\_acl\_a8c93d030b202200f9fd064d37673afb) got removed from Security plugin in **London**, hence not supposed to be installed on **London** or later instances.

An equivalent ACL was added to com.sn\_hr\_core plugin to maintain security - "sys\_security\_acl\_24ee8c39534203002b76da86a11c088e".

If this newer ACL is present then it should be safe to remove the older ACL.
