---
title: "Files still left in Changed Files list after committing a scoped application to source control"
aliases:
  - KB0695379
tags:
  - servicenow
  - support-kb
  - source-control
  - scoped-applications
  - update-sets
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695379
kb_number: KB0695379
last_modified: 2024-04-07
---

## Files still left in Changed Files list after committing a scoped application to source control

  

### Issue

# Symptoms

* * *

After using the Commit Changes feature in the Source Control menu in Studio, the commit completes successfully, but some of the changed files are still appearing in the list and the Commit Changes option is still available.

# Release

* * *

All Supported Releases

# Cause

* * *

When an application is committed to source control, the system searches for sys\_update\_xml records in order to determine what local changes are being committed. When the commit is finished, the system deletes these sys\_update\_xml records. However, the system will only remove them if they are inside a valid update set that is part of the application.

If files are still appearing in this list after committing, it indicates an issue with the update set they are in. Find these updates by going to the sys\_update\_xml table and searching for records where the Application field is equal to the affected application. Then, investigate the update sets that these updates are in. If the Application field on these update sets does not contain a valid value, or if they are part of another application, they will not be cleaned up.

Usually, the updates are in the wrong update set due to being moved manually. It is strongly discouraged to move updates manually between update sets.

# Resolution

* * *

In order to resolve the issue and remove the changes from the Changed Files list, you must manually delete the sys\_update\_xml records for these files. Alternatively, you can move them into a valid update set that is part of the application, and then commit again to have the system clean them up.

## Related

- [[KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository]]
- [[KB0695169 - Changes to a scoped application are not being applied when the update is installed]]
- [[KB0715422 - How to go back to using the application repository after commiting changes to an application via update set]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695169 - Changes to a scoped application are not being applied when the update is installed|Changes to a scoped application are not being applied when the update is installed]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository|Resolve \"The operation encountered an unexpected error\" when linking source control to a Git repository]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0715422 - How to go back to using the application repository after commiting changes to an application via update set|How to go back to using the application repository after commiting changes to an application via update set]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687531 - Authorship of application was lost after clone|Authorship of application was lost after clone]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
