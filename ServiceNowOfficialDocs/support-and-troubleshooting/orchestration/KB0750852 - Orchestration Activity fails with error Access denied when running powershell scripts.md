---
title: "Orchestration Activity fails with error Access denied when running powershell scripts"
aliases:
  - KB0750852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750852
kb_number: KB0750852
last_modified: 2024-04-07
---

## Orchestration Activity fails with error Access denied when running powershell scripts

  

### Issue

# Symptoms

Powershell activity fails without trying any credentials from credentials table with Access denied

06/03/19 14:09:02 (596) ECCSender.1 Sending ecc\_queue.550ae779dbf5f300cb5671968c961979.xml&#13;  
06/03/19 14:09:12 (081) Worker-Standard:PowershellProbe-330a6b79dbf5f300cb5671968c9619f8 Worker starting: Powershell source: 10.27.247.48&#13;  
06/03/19 14:09:12 (097) Worker-Standard:PowershellProbe-330a6b79dbf5f300cb5671968c9619f8 SEVERE \*\*\* ERROR \*\*\* Failed while executing script11891173026142638.PS1 (Access denied)&#13;  
06/03/19 14:09:12 (097) Worker-Standard:PowershellProbe-330a6b79dbf5f300cb5671968c9619f8 Enqueuing: D:\\servicenow\_midserver\\agent\\work\\monitors\\ECCSender\\output\_2\\ecc\_queue.330a6b79dbf5f300cb5671968c9619f8.xml&#13;  
06/03/19 14:09:12 (097) Worker-Standard:PowershellProbe-330a6b79dbf5f300cb5671968c9619f8 Worker completed: Powershell source: 10.27.247.48 time: 0:00:00.016&#13;

# Release

All releases

# Cause

1.  This happens if you have defined a credential tag in the activity and there is no credential with the tag in the credentials table.
2.  If a credential tag is defined in the activity, we always query for the tag and will ignore all the credentials even when you have a valid credentials.

# Resolution

\-Make sure that the tag defined in the orchestration activity is present in credentials table.
