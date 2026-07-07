---
title: "Changes to a scoped application are not being applied when the update is installed"
aliases:
  - KB0695169
tags:
  - servicenow
  - support-kb
  - scoped-applications
  - update-sets
  - application-repository
  - upgrade-history
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695169
kb_number: KB0695169
last_modified: 2024-04-07
---

## Changes to a scoped application are not being applied when the update is installed

  

### Issue

# Symptoms

* * *

Changes that were made to a scoped application are not taking effect when the updated version of the application is installed.

# Release

* * *

All Supported Releases

# Cause

* * *

This is usually due to local customizations. If any changes have been made to a record locally, the system will skip this record when installing an update to the application. Thus, if any changes were made to that record in the app, they will not be applied. You can review the Skipped Changes list by going to the Upgrade History module and opening the entry for your recent application installation. From there you can use the "Revert to Base System" UI action to apply the base system version of the record from your application.

You can also determine if local changes were made by looking for sys\_update\_xml (Customer Update) records for the affected record. You will often find updates in the Default update set if inadvertent changes were made locally.

# Resolution

* * *

Use the Skipped Changes list on the Upgrade History module to review records that were skipped during the installation/update. From there you can use the "Revert to Base System" UI action to apply the base system version of the record from your application.

## Related

- [[KB0715422 - How to go back to using the application repository after commiting changes to an application via update set]]
- [[KB0695379 - Files still left in Changed Files list after committing a scoped application to source control]]
- [[KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository]]
- [[customizations-tracked-update-sets]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0715422 - How to go back to using the application repository after commiting changes to an application via update set|How to go back to using the application repository after commiting changes to an application via update set]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695379 - Files still left in Changed Files list after committing a scoped application to source control|Files still left in Changed Files list after committing a scoped application to source control]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687531 - Authorship of application was lost after clone|Authorship of application was lost after clone]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository|Resolve \"The operation encountered an unexpected error\" when linking source control to a Git repository]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
