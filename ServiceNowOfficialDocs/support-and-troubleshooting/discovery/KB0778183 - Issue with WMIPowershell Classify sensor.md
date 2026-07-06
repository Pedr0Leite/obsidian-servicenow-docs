---
title: "Issue with WMI/Powershell: Classify sensor"
aliases:
  - KB0778183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778183
kb_number: KB0778183
last_modified: 2024-04-07
---

## Issue with WMI/Powershell: Classify sensor

  

### Issue

The Following Error is returned on (some) Windows Servers during a typical Discovery in the Discovery Log:

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

  

The Windows Server will fail to classify

### Release

New York - patch 0(possibly others)

### Cause

There are GPO (Group Policy Objects) in the customer's environment that can specifically cause this error. These are things that are somewhat out of our control, but there are some things that we can do to diagnose.

### Resolution

1.  Compare the different CIs for the Windows Servers - see if any of them are not throwing this error and are being classified
2.  If there are servers that this is not happening to, then the most likely course of action is to compare the working Hosts to the Non Working Hosts. There is a command that you can run to print out the GPOs for each host and then you can compare them: gpresult/h report.html (returns an html file with the results).
3.  Eliminate any GPOs on the non working host that to not appear on the working host (remember that this would only apply to the GPOs that the Windows credential account for Service Now Discovery is tied to (ignore all other users from the report).
4.  (Optional) As a fallback you can always revert back to legacy WMI by setting the following property in ecc\_agent\_property.LIST: mid.use\_legacy\_wmi = "true"
