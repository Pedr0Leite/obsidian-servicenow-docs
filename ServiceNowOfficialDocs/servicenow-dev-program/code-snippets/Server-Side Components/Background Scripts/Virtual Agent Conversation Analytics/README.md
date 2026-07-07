---
title: "Virtual Agent Conversation Analytics"
aliases:
  - Virtual Agent Conversation Analytics
tags:
  - servicenow-dev-program
  - code-snippet
  - virtual-agent-conversation-analytics
  - background-scripts
---

# Virtual Agent Conversation Analytics

A background script that analyzes Virtual Agent conversation logs to identify the most common topics over a configurable time period.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. (Optional) Modify `daysBack` variable to set the analysis timeframe (default: 7 days)
4. Click "Run script"

## What It Does

The script:
1. Queries Virtual Agent conversation logs from the past 7 days (configurable)
2. Counts conversations by topic
3. Displays the top 10 most common topics with conversation counts
4. Helps identify which Virtual Agent topics are most frequently used

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
