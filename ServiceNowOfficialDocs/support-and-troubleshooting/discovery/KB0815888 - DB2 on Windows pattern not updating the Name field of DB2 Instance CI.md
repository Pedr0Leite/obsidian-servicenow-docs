---
title: "\"DB2 on Windows\" pattern not updating the Name field of DB2 Instance CI"
aliases:
  - KB0815888
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815888
kb_number: KB0815888
last_modified: 2024-04-08
---

## "DB2 on Windows" pattern not updating the Name field of DB2 Instance CI

  

### Issue

When running Discovery on a server that hosts DB2 Instance, the _Name_ field of the instance (cmdb\_ci\_db2\_instance) **is not updated or modified.** Even though the discovery run completed without issue.

### Release

Any

### Cause

Below is the logic used during DB2 instance discovery.

1.  IP Based Discovery (Horizontal) is scheduled to run against the server/host that hosts DB2 Instance.
2.  Name modification is commonly done via the Extension Section of DB2 on Windows Pattern. This is done to override the default naming of **DB2@hostname**, which is confusing if you have multiple DB2 instances running on the same host.
3.  The host along with DB2 Instance CIs seem to update successfully by the discovery, run from point #1 above.
4.  However, when checking DB2 Instance CI, the "Name" field is not updated with the customised name format.

During the IRE processing, DB2 instance uses '_DB2 Instance rule by ServiceWatch'_ reconciliation _rule._  This rule will block update on the DB2 Instance CI if the source is not ServiceWatch.

### Resolution

**This is expected behavior**

It is also mentioned in the [documentation](https://docs.servicenow.com/csh?topicname=r_SupportedApplications.html&version=latest "documentation") that DB2 Instance should be only discovered using **Service Mapping (Top Down)**.

Some customers might only have Discovery plugin installed in their environment. Out of the box, DB2 on Windows Pattern is not triggered when running Horizontal Discovery.

If the customer want to use this pattern for Horizontal Discovery, Reconciliation rule '_DB2 Instance rule by ServiceWatch'_ needs to be disabled.
