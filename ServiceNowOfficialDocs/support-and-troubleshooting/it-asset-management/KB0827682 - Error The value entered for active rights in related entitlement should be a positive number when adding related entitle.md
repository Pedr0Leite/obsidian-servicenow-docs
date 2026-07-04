---
title: "Error \"The value entered for active rights in related entitlement should be a positive number\" when adding related entitlement for Maintenance/Microsoft SA Entitlements"
aliases:
  - KB0827682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827682
kb_number: KB0827682
last_modified: 2024-04-08
---

## Error "The value entered for active rights in related entitlement should be a positive number" when adding related entitlement for Maintenance/Microsoft SA Entitlements

  

### Issue

Following Documents for Maintenance Entitlements or Microsoft SA Entitlements:

  

Record software rights for a Microsoft Software Assurance  
[https://docs.servicenow.com/csh?topicname=create-entitlement-microsoft-sa.html&version=latest](https://docs.servicenow.com/csh?topicname=create-entitlement-microsoft-sa.html&version=latest)

Record software rights for maintenance entitlements  
[https://docs.servicenow.com/csh?topicname=Record-software-rights-non-microsoft.html&version=latest](https://docs.servicenow.com/csh?topicname=Record-software-rights-non-microsoft.html&version=latest)

  

In Step 5, when trying to add the related entitlement and save, an error message may pop up "The value entered for active rights in related entitlement should be a positive number".

  

This message means that you need to manually enter a number for the active rights in the added related entitlement, otherwise the related entitlement cannot be added and the error message would display.

  

The purpose of entering active rights number manually is for the flexibility when you want only portion of the rights to be associated with Maintenance/Microsoft SA entitlements.

  

This step has not been mentioned in the Document and might cause some confusions.
