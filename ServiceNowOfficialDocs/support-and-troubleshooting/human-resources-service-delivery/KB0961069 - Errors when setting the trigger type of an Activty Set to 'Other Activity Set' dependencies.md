---
title: "Errors when setting the trigger type of an Activty Set to 'Other Activity Set' dependencies"
aliases:
  - KB0961069
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961069
kb_number: KB0961069
last_modified: 2026-03-17
---

## Errors when setting the trigger type of an Activty Set to 'Other Activity Set' dependencies

  

### Issue

After upgrading to Quebec, you might not be able to set the Trigger Type of an Activity Set to 'Other Activity Set'. The following error is displayed and the record is not saved:

**There was an unexpected error. Navigate to System Logs > System Log > Errors for further information. If needed, contact your system administrator.**

![](sys_attachment.do?sys_id=5fd40777936fbe50f538fb2d6cba10a3)

### Release

Quebec and higher

### Cause

The following errors can be seen in the system logs:

`org.mozilla.javascript.EcmaError: Cannot find function getActivitySetTriggerType in object [object Object].`   
`Caused by error in sys_script.5703ffa253920010b814ddeeff7b1255.script at line 1`   
`​`   
`==> 1: (function executeRule(current, previous /*null when async*/) {`   
`2: var errMsg = '';`   
`3: // Cannot set activity set's trigger type from rescind to something else (from backend)`   
`4: if(!current.isNewRecord() && previous.trigger_type == 'rescind' && current.trigger_type != 'rescind') {`  
  
`org.mozilla.javascript.EcmaError: Cannot find function getActivitySetTriggerType in object [object Object].`   
`Caused by error in sys_script.5703ffa253920010b814ddeeff7b1255.script at line 1`  
​  
`==> 1: (function executeRule(current, previous /*null when async*/) {`   
`2: var errMsg = '';`   
`3: // Cannot set activity set's trigger type from rescind to something else (from backend)`   
`4: if(!current.isNewRecord() && previous.trigger_type == 'rescind' && current.trigger_type != 'rescind') {`   
  
`org.mozilla.javascript.EcmaError: Cannot find function getActivitySetTriggerType in object [object Object].`   
`Caused by error in sys_ui_action.66148b12bf3021000ba9dc2ecf0739cc.script at line 5`  
​  
`2: var errMsg = '';`   
`3: // Cannot set activity set's trigger type from rescind to something else (from backend)`   
`4: if(!current.isNewRecord() && previous.trigger_type == 'rescind' && current.trigger_type != 'rescind') {`   
`==> 5: errMsg = gs.getMessage("Trigger type of 'rescind' activity set cannot be changed");`   
`6: gs.addErrorMessage(errMsg);`   
`7: current.setAbortAction(true);`   
`8: throw new Error(errMsg);`  
  
`org.mozilla.javascript.EcmaError: Cannot find function getActivitySetTriggerType in object [object Object].`   
`Caused by error in sys_script.5703ffa253920010b814ddeeff7b1255.script at line 34`  
​  
`31: dependencies = String(current.activity_set_dependencies).split(",");`   
`32: for (i = 0; i < dependencies.length; i++)`   
`33: // Check if any of the dependency is of type 'rescind'`   
`==> 34: if (util.getActivitySetTriggerType(dependencies[i]) == 'rescind') {`   
`35: errMsg = gs.getMessage("Activity set cannot be dependent on activity set of type 'Rescind'");`   
`36: gs.addErrorMessage(errMsg);`   
`37: current.setAbortAction(true);`  
  
  
The above errors point to Business Rules:  
  
Verify 'rescind' activity set exists  
​https://instance\_name.service-now.com/sys\_script.do?sys\_id=5703ffa253920010b814ddeeff7b1255

  
Verify validity of dependency setting  
https://instance\_name .service-now.com/sys\_script.do?sys\_id=4cb7095687830010b0fb0c0626cb0b08  
  
which eventually call **Script Include 'hr\_ActivitySet'**  
https://instance\_name .service-now.com/sys\_script\_include.do?sys\_id=088df2fe534a22003066a5f4a11c08de

### Resolution

Script Include '**hr\_ActivitySet**' might have been customized and therefore it might be missing the 'getActivitySetTriggerType' function:

https://instance\_name .service-now.com/sys\_script\_include.do?sys\_id=088df2fe534a22003066a5f4a11c08de    
  
Revert it to OOB to fix this issue.

Note: _If the Script Include is OOTB and the issue persists, review related Business Rules and dependencies that call this Script Include. For example, verify the ‘rescind’ activity set and dependency settings, as these may cause the error._
