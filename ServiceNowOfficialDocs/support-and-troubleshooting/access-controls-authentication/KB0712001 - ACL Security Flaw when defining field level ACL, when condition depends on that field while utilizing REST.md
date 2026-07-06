---
title: "ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST"
aliases:
  - KB0712001
tags:
  - servicenow
  - support-kb
  - acl
  - field-level-acl
  - GlideRecordSecure
  - REST
  - Table-API
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712001
kb_number: KB0712001
last_modified: 2024-10-09
---

## ACL Security Flaw when defining field level ACL, when condition depends on that field while utilizing REST

  

### Issue

# Symptoms

* * *

ACL allows for changes to a field that should be locked down using a field level write ACL. While the ACL is respected on the form view, when transacting via REST (Table API) or GlideRecordSecure, these field level ACLs are not respected. 

# Release

* * *

Istanbul and Jakarta. This issue is fixed in Kingston. 

# Cause

* * *

The root cause of the issue is PRB660114. Although the description does not explain this exact situation, the fix provided in this problem resolves the issue mentioned in this knowledge article. 

# Resolution

* * *

Upgrade to a fixed version as mentioned in PRB660114. There were several fixes done to GlideRecordSecure (GRS) for this PRB660114. The part of the problem that is relevant to the issue mentioned in this knowledge article is that previously GlideRecordSecure would read the current values of the record (including values changed by the user) when evaluating ACLs. After the fix, the values from the original record are used when evaluating the ACLs.

## Related

- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[KB0728016 - A user with a specific role does not have access to a table even when an ACL grants that role the required access]]
- [[c_GlideRecordAPI]] - official GlideRecord/GlideRecordSecure server-side API reference
- [[access-control-rules]] - official docs on ACL rule evaluation
- [[c_TableAPI]] - official Table API (REST) reference
