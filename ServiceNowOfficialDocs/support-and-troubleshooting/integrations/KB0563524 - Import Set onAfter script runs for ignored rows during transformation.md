---
title: "Import Set onAfter script runs for ignored rows during transformation"
aliases:
  - KB0563524
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563524
kb_number: KB0563524
last_modified: 2025-05-08
---

## Import Set onAfter script runs for ignored rows during transformation

  

### Issue

When transforming import set data, you can set the ignore object in the onBefore script to true to skip transforming that row. However, if an onAfter script is defined, this script runs even for skipped rows.  
  
See [Transform maps](https://docs.servicenow.com/csh?topicname=c_CreatingNewTransformMaps.html&version=latest) and [Map with transformation event scripts](https://docs.servicenow.com/csh?topicname=r_MapWithTransformationEventScripts.html&version=latest) for general information about transform map scripts. 

###   
Symptoms

The transform map onAfter script runs when the ignore object is set to true in the onBefore script.

### Cause

The onAfter script does not have access to the ignore object value from the onBefore script.

### Resolution

Include a check in the onAfter script to determine the import state of the source row. Ignored rows have a sys\_import\_state value of "ignored".  
  
For example, you can include the following code to exit the onAfter script if the row was ignored.

if (source.getValue("sys\_import\_state") === 'ignored')

return;
