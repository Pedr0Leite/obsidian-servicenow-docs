---
title: "Authorship of application was lost after clone"
aliases:
  - KB0687531
tags:
  - servicenow
  - support-kb
  - clone
  - application-development
  - update-sets
  - authorship
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687531
kb_number: KB0687531
last_modified: 2025-04-08
---

## Authorship of application was lost after clone

  

### Issue

Authorship of an application was lost after clone, and you can no longer publish the application to your Repository.

### Release

Geneva+

### Cause

When cloning, if the source instance has a different version of the application than the target instance, authorship may be lost.

### Resolution

A restore from backup is the quickest and safest method to restore authorship to the application. In some cases, Customer Support is able to restore Authorship for you; however, there are risks involved. The most optimal option is restoring from backup to when the application had authorship. Engage Customer Support if further assistance is needed.

To prevent this in the future, refer to the following [Docs page](https://docs.servicenow.com/csh?topicname=preserve-applications-during-clone.html&version=latest).

## Related

- [[KB0538768 - Determining if the properties from the source were copied over a target]] - another clone-related configuration loss
- [[using-system-update-sets]] - official docs on update sets for moving customizations between instances
- [[update-sets-reference]] - official docs on update set reference

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695169 - Changes to a scoped application are not being applied when the update is installed|Changes to a scoped application are not being applied when the update is installed]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository|Resolve \"The operation encountered an unexpected error\" when linking source control to a Git repository]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695379 - Files still left in Changed Files list after committing a scoped application to source control|Files still left in Changed Files list after committing a scoped application to source control]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0715422 - How to go back to using the application repository after commiting changes to an application via update set|How to go back to using the application repository after commiting changes to an application via update set]]
