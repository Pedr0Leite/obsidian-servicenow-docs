---
title: "Password Enrollment Error: \"Cannot set property 'value' of undefined\"
aliases:
  - KB0749393
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749393
kb_number: KB0749393
last_modified: 2024-04-07
---

## Password Enrollment Error: "Cannot set property 'value' of undefined"

  

### Issue

# Symptoms

When user tried to enroll themselves for question/answer for password reset, after clicking submit nothing happen and pop-up error says:

"Cannot set property 'value' of undefined"

# Release

Usually happens when upgrading to newer releases like K, L, M, etc. 

# Cause

The "enroll" module should link to the "$pwd\_enrollment\_form\_container" UI Page.

# Resolution

1) Go to your list of modules (table = sys\_app\_module.LIST)

2) Find you enroll module

3) Look for the 'arguments' field

4) Insure that it says "$pwd\_enrollment\_form\_container"

NOTE: Notice that there is "$" sign in front, that is required. If it is not there, please add it.
