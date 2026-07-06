---
title: "Global variables declared on onLoad client script are not accessible from another onChange client script"
aliases:
  - KB0749175
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749175
kb_number: KB0749175
last_modified: 2024-04-07
---

## Global variables declared on onLoad client script are not accessible from another onChange client script

  

### Issue

# Description

When a global variable is declared in an onLoad client script in the global application and tried to access it from another onChange client script in the same global application, it gives a 'variable\_name not defined error'.

Below is the example of scripts and the console error:

1\] onLoad client script: loadGlobalVariables

var testGlobalVar = {};  
function onLoad() {  
testGlobalVar.check = 'Load';  
console.log('\*\*\*\* Test onLoad => '+testGlobalVar);  
}

2\] onChange client script: onChangeGlobalVariable

function onChange(control, oldValue, newValue, isLoading) {  
if (isLoading || newValue == '') {  
return;  
}  
console.log("### BEFORE ONCHANGE => "+testGlobalVar.check);  
testGlobalVar.check = 'Change';  
console.log("#### AFTER ONCHANGE => "+testGlobalVar.check);  
  
}

**Console Error:**

![](sys_attachment.do?sys_id=87baeca6db42b450e515c223059619c7)

# Workaround

Use g\_scratchpad.testGlobalVar for accessing global variables across client scripts. The "g\_scratchpad" object works fine on a regular form like incident and on Service portal but it doesn't work on Service Catalog Form. An enhancement request is been created to enable g\_scratchpad on Service Catalog Form on platform view.

# Applicable Versions

Any version
