---
title: "Issue with Windows Classify cannot discover Windows"
aliases:
  - KB0778397
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778397
kb_number: KB0778397
last_modified: 2024-04-08
---

## Issue with Windows Classify cannot discover Windows

  

### Issue

When Discovering a Windows host, the following error is returned:

TypeError: Cannot read property "0" from undefined  
Stack: at discovery\_sensor.b11453f50a0a0ba500a72547a687189e:158 (anonymous)  
at discovery\_sensor.b11453f50a0a0ba500a72547a687189e:66 (anonymous)  
at discovery\_sensor.b11453f50a0a0ba500a72547a687189e:45 (anonymous)  
at sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script:194 (anonymous)  
at sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script:149 (anonymous)  
at sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script:112 (anonymous)  
at sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script:25 (anonymous)  
at sys\_script\_include.d22e7bdbc0a8016500a18e024bfc9aa3.script:4 (anonymous)  
at discovery\_sensor.b11453f50a0a0ba500a72547a687189e:1  
at sys\_script\_include.78dfb2dd536002001f175f43911c087d.script:13 (anonymous)  
at sys\_trigger.e09ce071db933300e822748e0f9619da:2  
(sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script; line 56)

  

After testing every possible scenario and not being successful in determining whether there is a GPO or some sort of policy or configuration issue on the host, you may need to look elsewhere for the root cause of this error.

### Release

All Versions.

### Cause

The customer may have a Symnatec or McAfee Host Intrusion Policy that is blocking access to the application. Please instruct the customer to review these policies as they pertain to the hosts in question, as they may be particularly blocking powershell on specific hosts

### Resolution

Please disable the Symantec or McAfee Host Intrusion Policies that may be blocking PowerShell access
