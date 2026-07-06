---
title: "Discovery failing on Error: Missing expression after unary operator"
aliases:
  - KB0783025
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783025
kb_number: KB0783025
last_modified: 2024-04-07
---

## Discovery failing on Error: Missing expression after unary operator

  

### Issue

Discovery failing on Error: Missing expression after unary operator  
  
When I run discovery I notice the error:   
"Error: Missing expression after unary operator '-'.At line:1 char:2+ -E <<<< xecutionPolicy ByPass -NonInteractive -WindowStyle Hidden -command &"

### Cause

The error happens when running the command '-ExecutionPolicy ByPass -NonInteractive -WindowStyle Hidden' so you can test this by running the following command on the affected MID Server and check the output text file to see if it has the same error or not.  
  
\# powershell -ExecutionPolicy ByPass -NonInteractive -WindowStyle Hidden > C:\\SampleFolder\\output.txt  
  
Observe the Powershell version that your MID Server is using?

PowerShell version 1.0 running on remote mid server or remote host.

Minimum pre-requisite for PowerShell is v2.0

### Resolution

Ask if PowerShell can be upgraded to 2.0 or higher to satisfy Discovery requirements.  
  
Confirm after upgrade PowerShell 2.0 or higher resolved the issue.
