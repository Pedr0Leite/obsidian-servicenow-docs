---
title: "Certain fields are visible to non-admin users only when the fields not empty."
aliases:
  - KB0759218
tags:
  - servicenow
  - support-kb
  - acl
  - reference-fields
  - sys_reference_row_check
  - system-properties
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759218
kb_number: KB0759218
last_modified: 2024-01-28
---

## Certain fields are visible to non-admin users only when the fields not empty.

  

### Issue

Some of the fields are visible to non-admin users only when the fields not empty. When they are not empty, they will be visible without any issue.

### Release

All

### Cause

This behavior can be seen when the system property 'glide.sys\_reference\_row\_check' is set to true. 

If this property value is set to true, it will check the ACL conditions/script for reference fields as well. For example: assume that in an ACL on 'sys\_user\_group.Name', there is a condition as 'Active is true'. So, as per the property 'glide.sys\_reference\_row\_check', the users can read the Assignment group reference field that refers to the sys\_user\_group table only when the group selected in that field is Active. When the Assignment group value is empty, the active field on sys\_user\_group would be evaluated to false on this field. Hence, the users are not able to see the Assignment group when it is empty. 

### Resolution

This behavior is expected one. The customers need to evaluate the business requirement and change the value of this property accordingly.

Refer the below product documentation to know more about this property.

[Apply ACL script conditions to reference fields](https://docs.servicenow.com/csh?topicname=r_ContScriptCondAppRefFld.html&version=latest "Apply ACL script conditions to reference fields")

## Related

- [[KB0785309 - Reference Fields in a form are not visible if the user does not have read access on the Referenced table's recorddisplay]] — another reference-field ACL visibility issue
- [[KB0749738 - SLA Definition field value is not displaying on task sla list or related lists for some users]] — similar field-visibility ACL scenario
- [[r_ContScriptCondAppRefFld]] — official docs on applying ACL script conditions to reference fields
