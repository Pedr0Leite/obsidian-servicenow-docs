---
title: "Resolve \"The operation encountered an unexpected error\" when linking source control to a Git repository"
aliases:
  - KB0695295
tags:
  - servicenow
  - support-kb
  - source-control
  - git
  - scoped-applications
  - application-development
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695295
kb_number: KB0695295
last_modified: 2026-06-23
---

## Resolve "The operation encountered an unexpected error" when linking source control to a Git repository

  

### Issue

Resolve an error that appears when attempting to link source control to a Git repository:

"The operation encountered an unexpected error. Check the node log file."

Checking the node logs shows the following exception:

```
SEVERE *** ERROR *** Error occurred while exporting application
com.glide.sourcecontrol.SourceControlException: org.eclipse.jgit.api.errors.TransportException: http://12.34.567.890/example.git:
insufficient data written
```

### Release

All supported releases

### Cause

This error typically occurs when attempting to link to a self-hosted Git repository on a local server within your network. If the firewall is not configured to allow inbound communication from ServiceNow servers, the repository is unreachable from the ServiceNow instance.

### Resolution

There are three options for resolving this issue:

-   **Make the repository server internet-accessible.** Configure the firewall to allow inbound communication from ServiceNow servers so that the repository is reachable from the internet.
-   **Set up a proxy with ServiceNow.** If the repository cannot be made internet-accessible, submit a case through Now Support to work with ServiceNow on setting up a proxy connection.
-   **Use a hosted repository service.** Migrate to a secure hosted repository service such as GitHub, GitLab, or Bitbucket.

## Related

- [[KB0695379 - Files still left in Changed Files list after committing a scoped application to source control]]
- [[KB0695169 - Changes to a scoped application are not being applied when the update is installed]]
- [[KB0715422 - How to go back to using the application repository after commiting changes to an application via update set]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695379 - Files still left in Changed Files list after committing a scoped application to source control|Files still left in Changed Files list after committing a scoped application to source control]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687531 - Authorship of application was lost after clone|Authorship of application was lost after clone]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695169 - Changes to a scoped application are not being applied when the update is installed|Changes to a scoped application are not being applied when the update is installed]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0715422 - How to go back to using the application repository after commiting changes to an application via update set|How to go back to using the application repository after commiting changes to an application via update set]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0720035 - Error calling Scoped Outbound REST message|Error calling Scoped Outbound REST message]]
