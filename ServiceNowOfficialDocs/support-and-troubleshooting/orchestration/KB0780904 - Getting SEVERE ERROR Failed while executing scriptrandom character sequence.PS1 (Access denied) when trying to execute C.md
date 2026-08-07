---
title: "Getting SEVERE *** ERROR *** Failed while executing script<random character sequence>.PS1 (Access denied) when trying to execute Custom Powershell Script"
aliases:
  - KB0780904
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780904
kb_number: KB0780904
last_modified: 2024-04-08
---

## Getting SEVERE \*\*\* ERROR \*\*\* Failed while executing script.PS1 (Access denied) when trying to execute Custom Powershell Script

  

### Issue

When running a Custom Powershell script using a Custom Orchestration Activity, it is generating the following error below.

Getting SEVERE \*\*\* ERROR \*\*\* Failed while executing script<random character sequence>.PS1 (Access denied)

### Cause

This issue could be due to Permission or Credentials related.

### Resolution

1.  Check whether the service account running the MID server service has permission to run the script in windows\\temp.
2.  Test couple of simple PowerShell command like "ls"
3.  Check to see if there is a Credential tag on the Custom Activity and make sure that the same tag exists on the credential table.
4.  Test the credential with the target IP to make sure that the credentials works.
5.  On this particular issue, the error was generating due to a broken credential record.
