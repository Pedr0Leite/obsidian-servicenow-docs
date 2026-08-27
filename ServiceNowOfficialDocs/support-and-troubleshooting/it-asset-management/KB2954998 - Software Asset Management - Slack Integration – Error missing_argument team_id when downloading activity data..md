---
title: "Software Asset Management - Slack Integration – Error \"missing_argument: team_id\" when downloading activity data."
aliases:
  - KB2954998
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2954998
kb_number: KB2954998
last_modified: 2026-04-23
---

## Software Asset Management - Slack Integration – Error "missing\_argument: team\_id" when downloading activity data.

  

### Issue

When SAM Pro tries to download activity data from Slack workspaces, the integration returns the following error in the outbound logs:  
{"ok":false,"error":"missing\_argument","arg":"team\_id"}

Refer to the section "Execute Jobs and Review the Logs:" within the below KB to enable the debug on the instance and verify the outbound logs for the error response.

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2977963](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2977963)  

This error says that SAM Pro is using the enterprise grid token to query workspace level activity a configuration that slack does not support. When a grid level token is used to request workspace activity, Slack requires a team\_id parameter to identify the target workspace. If that parameter is absent, Slack rejects the request.

### Release

ALL

### Cause

One or more workspaces that have download activity enabled do not have a dedicated workspace level app and token configured in the Slack Workspace Tokens table. As a result, SAM Pro falls back to the grid token, which Slack rejects for workspace activity calls.

### Resolution

For each workspace where you want to download activity, complete the following:  
1\.    Create a Slack app in the target workspace (not at the Enterprise Grid level).  
2\.    Install the app in that workspace and obtain its OAuth token.  
3\.    In SAM Pro, navigate to the Slack integration configuration and open the Slack Workspace Tokens table.  
4\.    Add a row for the workspace with the token obtained in step 2.  
5\.    Save the connection and run Validate to confirm the error is resolved.

If activity data is not required, disable the feature to stop the failing API calls:  
1\.    Open the Slack integration connection in SAM Pro.  
2\.    Locate the Download Activity option and uncheck it.  
3\.    Save the connection and click Validate to confirm no errors remain.
