---
title: "Javascript error onboarding module for a particular user, for admin works fine."
aliases:
  - KB1032497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1032497
kb_number: KB1032497
last_modified: 2025-09-03
---

## Javascript error onboarding module for a particular user, for admin works fine.

  

### Issue

Javascript error onboarding module for a particular user, for admin works fine.When navigating to esc portal and clicking on MyTodos 

observe errors.  
++++++++++++++  
Server JavaScript error Cannot read property "canRead" from undefined  
ErrorLine number 148 (sys\_script\_include.6f22781a77972300a25193df59106146.script)  
ErrorScript source code logged to browser console  
ErrorFailing widget: 'E-Sign Task' (a51a03aa771f2300f1b4e431a9106173) called from: 'HRJ Task E-Sign' (97d1c726779b2300f1b4e431a9106105) called from: 'HRM Task Activity' (be9a53ee738023002ceb31d7caf6a769) called from: 'To-dos task Line Item' (a4716c8f53d3130030f3ddeeff7b1288)  
+++++++++++++++

### Cause

The HR task under todos is an e-sign task, which is having a managed document.

But the **managed document was not linked to any pdf.**

### Resolution

Attached a correct pdf and verified that no javascript errors are coming in to-dos page.
