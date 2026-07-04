---
title: "LDAP  - Evaluator: org.mozilla.javascript.EcmaError: \"ldapUtils\" is not defined ( Manager not getting updated from LDAP/AD)"
aliases:
  - KB0634725
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634725
kb_number: KB0634725
last_modified: 2024-04-07
---

## LDAP - Evaluator: org.mozilla.javascript.EcmaError: "ldapUtils" is not defined ( Manager not getting updated from LDAP/AD)

  

### Issue

# Symptoms

* * *

The following JavaScript exception is logged:

glide.scheduler.worker.1 Evaluator: org.mozilla.javascript.EcmaError: "ldapUtils" is not defined.   
Caused by error in sys\_transform\_script.483ba9e00fa0030058a2b36be1050e49.script at line 10   
  
7: // import and therefore all users should have been created and we should be able to   
8: // locate the manager at this point   
9: //global.LDAPUtils.processManagers();   
\==> 10: ldapUtils.processManagers();   
11: })(source, map, log, target); 

  

# Cause

* * *

The error occurs because the **processManagers** and **setManager** method calls are used in the **OnComplete** section, and the **LDAPUtils** may not be available outside the function calls.  
For example, a custom Transform Map may contain the ldapUtils definition **On Start:** 

(function runTransformScript(source, map, log, target /\*undefined onStart\*/ ) {   
// Add your code here   
gs.include("LDAPUtils");   
var ldapUtils = new LDAPUtils();   
ldapUtils.setLog(log);   
})(source, map, log, target); 

  

# Resolution

* * *

Move the function call from the **OnStart script**, so that **LDAPUtils** become available outside:  
i.e Please comment out the function in the OnStart Script.  
gs.include("LDAPUtils");   
var ldapUtils = new LDAPUtils();   
ldapUtils.setLog(log); 

#
