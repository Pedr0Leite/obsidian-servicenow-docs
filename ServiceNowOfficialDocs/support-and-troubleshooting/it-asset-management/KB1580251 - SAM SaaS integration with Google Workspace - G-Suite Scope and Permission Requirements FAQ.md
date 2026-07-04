---
title: "SAM SaaS integration with Google Workspace - G-Suite Scope and Permission Requirements FAQ"
aliases:
  - KB1580251
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1580251
kb_number: KB1580251
last_modified: 2026-05-08
---

## SAM SaaS integration with Google Workspace - G-Suite Scope and Permission Requirements FAQ

  

### Summary

[Docs: SaaS license management - Integrating with Google Workspace](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-gsuite.html?section=integrate-with-gsuite)

The Google Workspace integration has 3 main processes:  
1\. Download all user subscriptions  
2\. Fetch the activity of all users to determine the usage of the products.  
3\. Reclaim users that have low usage.

  
**Q. https://www.googleapis.com/auth/admin.directory.user** 

**Why is write access needed?**

**A.** As part of the reclaim process, we use the [Google Workspace Admin console Reference - Method: users.delete](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/delete) API to delete the user record which requires the https://www.googleapis.com/auth/admin.directory.user scope.

**Q. https://www.googleapis.com/auth/admin.datatransfer** 

**Are data transfers in the scope of the SaaS connection to support SAM pro?**

**A.** For the reclamation process, the following process is followed to retain the data of the user record which is being reclaimed, to prevent data loss.  
#1. Transfer all the data (which the user to be reclaimed owns) to the authenticated admin.  
#2. Once the transfer is successful, delete the user

**Q. https://www.googleapis.com/auth/admin.reports.usage.readonly** 

**What information is required from the Reports API? Some of these reports contain highly sensitive data. What information will be pulled into ServiceNow from this API?**

**A.** The Reports API is used to fetch activity data namely, the number of entities updated by users and the last activity timestamp of those entities.

The following parameters are fetched in the API call:  
accounts:last\_login\_time,accounts:last\_sso\_time,gmail:last\_access\_time,gmail:last\_imap\_time,gmail:last\_interaction\_time,gmail:last\_pop\_time,gmail:last\_webmail\_time,docs:num\_owned\_google\_documents\_created,docs:num\_owned\_google\_documents\_edited,docs:num\_owned\_google\_documents\_trashed,docs:num\_owned\_google\_documents\_viewed,docs:num\_owned\_google\_drawings\_created,docs:num\_owned\_google\_drawings\_edited,docs:num\_owned\_google\_drawings\_trashed,docs:num\_owned\_google\_drawings\_viewed,docs:num\_owned\_google\_forms\_created,docs:num\_owned\_google\_forms\_edited,docs:num\_owned\_google\_forms\_trashed,docs:num\_owned\_google\_forms\_viewed,docs:num\_owned\_google\_presentations\_created,docs:num\_owned\_google\_presentations\_edited,docs:num\_owned\_google\_presentations\_trashed,docs:num\_owned\_google\_presentations\_viewed,docs:num\_owned\_google\_spreadsheets\_created,docs:num\_owned\_google\_spreadsheets\_edited,docs:num\_owned\_google\_spreadsheets\_trashed,docs:num\_owned\_google\_spreadsheets\_viewed,drive:num\_google\_documents\_created,drive:num\_google\_documents\_edited,drive:num\_google\_documents\_trashed,drive:num\_google\_documents\_viewed,drive:num\_google\_drawings\_created,drive:num\_google\_drawings\_edited,drive:num\_google\_drawings\_trashed,drive:num\_google\_drawings\_viewed,drive:num\_google\_forms\_created,drive:num\_google\_forms\_edited,drive:num\_google\_forms\_trashed,drive:num\_google\_forms\_viewed,drive:num\_google\_presentations\_created,drive:num\_google\_presentations\_edited,drive:num\_google\_presentations\_trashed,drive:num\_google\_presentations\_viewed,drive:num\_google\_sites\_created,drive:num\_google\_sites\_edited,drive:num\_google\_sites\_trashed,drive:num\_google\_sites\_viewed,drive:num\_google\_spreadsheets\_created,drive:num\_google\_spreadsheets\_edited,drive:num\_google\_spreadsheets\_trashed,drive:num\_google\_spreadsheets\_viewed
