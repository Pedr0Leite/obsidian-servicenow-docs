---
title: "User with \"knowledge_manager\" role cannot see the knowledge list-view (kb_knowledge.list)"
aliases:
  - KB0996939
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996939
kb_number: KB0996939
last_modified: 2024-08-28
---

## User with "knowledge\_manager" role cannot see the knowledge list-view (kb\_knowledge.list)

  

### Issue

The user reporting the issue was an "admin" user, and they reported that they provided several other users with the "knowledge\_manager" role. Those users to whom the role was given were unable to view the kb\_knowledge list-view. The admin user wanted to know why this was.

Note: when the users who were given the "knowledge\_manager" role opened the kb\_knowledge list-view, they saw the below message:

_Number of rows removed from this list by Security constraints: 20_

### Cause

There was no "read" operation ACL for the table-level of kb\_knowledge.

### Resolution

The admin user had a field-level ACL for kb\_knowledge (e.g. "kb\_knowledge.\*") with operation = read, but they did not have a table-level ACL (e.g. "kb\_knowledge.NONE") for operation = read.

Once the user created the kb\_knowledge.NONE table-level ACL for operation = read, and cleared the cache (in the left-navigator, type "cache.do" and hit Enter, as ACL results always cache), the issue was resolved. All users with the "knowledge\_manager" role were now able to see the kb\_knowledge list-view with no security restraints.
