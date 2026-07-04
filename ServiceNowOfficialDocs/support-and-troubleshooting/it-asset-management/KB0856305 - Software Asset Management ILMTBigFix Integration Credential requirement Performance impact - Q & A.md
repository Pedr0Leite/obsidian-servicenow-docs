---
title: "Software Asset Management ILMT/BigFix Integration: Credential requirement / Performance impact - Q & A"
aliases:
  - KB0856305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856305
kb_number: KB0856305
last_modified: 2025-01-02
---

## Software Asset Management ILMT/BigFix Integration: Credential requirement / Performance impact - Q & A

  

### Summary

**Question:**

To set up ILMT/BigFix Integration, what are the role requirements for the credential created in ILMT/BigFix ?

**Answer:**

You will need the **Software Asset Manager** or **Administrator** role.

More details here:  
[https://www.ibm.com/support/knowledgecenter/SS8JFY\_9.2.0/com.ibm.lmt.doc/Inventory/planinconf/c\_roles.html](https://www.ibm.com/support/knowledgecenter/SS8JFY_9.2.0/com.ibm.lmt.doc/Inventory/planinconf/c_roles.html)

  

**Question:**

What would be the performance impact during the inventory query in Bigfix ?

**Answer:**

The queries from SN are batched in sets of 1000s so there should be minimal impact.

  

**Question:**

Can the data pull be scheduled ?

**Answer:**

Yes. The job is scheduled by default.

Please check in:

Integration - ILMT / BigFix Inventory > Scheduled Import > the job is called "SAM - IBM Data Import"

### Related Links

[Create a connection to ILMT/BigFix Inventory](https://docs.servicenow.com/csh?topicname=set-up-ibm-platform.html&version=latest "Create a connection to ILMT/BigFix Inventory")
