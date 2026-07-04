---
title: "Unable to delete samp_sw_subscription records"
aliases:
  - KB2660795
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2660795
kb_number: KB2660795
last_modified: 2025-12-01
---

## Unable to delete samp\_sw\_subscription records

  

### Issue

An admin user is unable to delete \[samp\_sw\_subscription\] records despite the sam\_admin and admin roles.

### Release

This is not release specific.

### Cause

The Delete ACL includes a condition which was introduced as a fix to a problem, where integration subscriptions were deleted, causing unexpected counts on Software Models.

<condition table="samp\_sw\_subscription">sourced\_from\_integration=no^EQ<item endquery="false" field="sourced\_from\_integration" goto="false" newquery="false" operator="=" or="false" value="no"/>  
<item endquery="true" field="" goto="false" newquery="false" operator="=" or="false" value=""/>  
</condition>  
https://instance.service-now.com/sys\_security\_acl.do?sys\_id=49a714b687700300562e4127f5cb0b74

### Resolution

This is the expected behaviour in the current design.
