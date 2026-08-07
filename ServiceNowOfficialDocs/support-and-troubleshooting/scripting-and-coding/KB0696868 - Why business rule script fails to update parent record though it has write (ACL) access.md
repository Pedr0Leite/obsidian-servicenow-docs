---
title: "Why business rule script fails to update parent record though it has write (ACL) access?"
aliases:
  - KB0696868
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696868
kb_number: KB0696868
last_modified: 2024-01-28
---

## Why business rule script fails to update parent record though it has write (ACL) access?

  

### Issue

# Symptoms

* * *

Before update business rule was setup on child table to update associated parent table record with data from child record up on closure of child record.

For example, lets consider below scenario,

-   Custom table "ABC" extends "task" table. ("ABC record can have parent record like incident/problem/change request")
-   Set up a before update business rule on "ABC" table
-   In the business rule script, get the parent record via GlideRecord API and then update it with the closure details from the child record ( "ABC" record).
-   Checking the read/write ACL on parent record, looks good, but business rule fails to update the parent record.

# Release

* * *

Any supported release.

# Cause

* * *

Before query business rule was set up on the specific parent table ( for example incident/problem/change request) and which was allowing the visibility of the record to certain group of users.

Hence, before update business rule was unable to update it, since the GlideRecord query fails to get the record for update. 

# Resolution

* * *

Review the custom before query business rule on parent table and modify it as per the business requirement so that custom before update business rule set up on child table could update the parent record as expected.

# Additional Information

* * *

[Business Rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business Rules")

[Debugging business rules](https://docs.servicenow.com/csh?topicname=r_DebuggingBusinessRules.html&version=latest "Debugging business rules")
