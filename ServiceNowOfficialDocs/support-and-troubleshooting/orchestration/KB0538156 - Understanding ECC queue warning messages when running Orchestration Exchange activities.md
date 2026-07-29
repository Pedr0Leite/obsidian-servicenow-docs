---
title: "Understanding ECC queue warning messages when running Orchestration Exchange activities"
aliases:
  - KB0538156
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538156
kb_number: KB0538156
last_modified: 2025-01-30
---

## Understanding ECC queue warning messages when running Orchestration Exchange activities

  

### Issue

These warnings appear whenever running the Orchestration Exchange activities. These messages appear in the ECC Queue **Payload** field for Exchange-generated records with a Queue value of **Input.** 

### Example message

Messages appear at the top of the **Payload** field within **<output>** tags.

WARNING: Some imported command names include unapproved verbs which might make  
them less discoverable. Use the Verbose parameter for more detail or type  
Get-Verb to see the list of approved verbs.  
WARNING: Some imported command names include unapproved verbs which might make  
them less discoverable. Use the Verbose parameter for more detail or type  
Get-Verb to see the list of approved verbs.  
  
    
  
ModuleType Name ExportedCommands  
\---------- ---- ----------------  
Script tmp\_7bb90290-805f-4636... {Get-IRMConfiguration, New-MailUser, En...  
&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt; AuditEnabled, Value = True

### Resolution

No action is needed to resolve these warnings. These warnings are expected because Exchange activities establish a session with the Exchange server using Powershell Remoting.
