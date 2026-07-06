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
