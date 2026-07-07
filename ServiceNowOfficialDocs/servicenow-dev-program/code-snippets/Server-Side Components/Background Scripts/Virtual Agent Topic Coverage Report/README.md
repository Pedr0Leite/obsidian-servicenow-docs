---
title: "Virtual Agent Topic Coverage Report"
aliases:
  - Virtual Agent Topic Coverage Report
tags:
  - servicenow-dev-program
  - code-snippet
  - virtual-agent-topic-coverage-report
  - background-scripts
---

# Virtual Agent Topic Coverage Report

A background script that analyzes Virtual Agent topic configuration health by identifying inactive, unpublished, or unused topics.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. (Optional) Modify `daysBack` variable to set the usage analysis timeframe (default: 30 days)
4. Click "Run script"

## What It Does

The script:
1. Queries all Virtual Agent topics in the system
2. Checks each topic's active and published status
3. Counts conversations per topic over the past 30 days (configurable)
4. Displays inactive topics, unpublished topics, and zero-usage topics
5. Helps identify topics that need attention before go-live or during health checks

## Report Categories

**Inactive Topics**: Topics where the "Active" checkbox is unchecked. These topics are disabled and won't respond to user inputs even if published.

**Unpublished Topics**: Topics where the "Published" checkbox is unchecked. These are draft topics not yet available to end users.

**Topics with Zero Usage**: Topics that are both active and published but have had no conversations in the specified timeframe. May indicate topics that need better training phrases or are not discoverable by users.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
