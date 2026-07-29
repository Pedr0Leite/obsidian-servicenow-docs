---
title: "Windows OS - Servers pattern throws the error \"JAVASCRIPT_CODE_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Insert System, OS and CPU data to cmdb_ci_win_server' at line 1\"
aliases:
  - KB0746266
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746266
kb_number: KB0746266
last_modified: 2024-04-07
---

## Windows OS - Servers pattern throws the error "JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Insert System, OS and CPU data to cmdb\_ci\_win\_server' at line 1"

  

### Issue

# Symptoms

Windows OS - Servers pattern logs show the below error:  
  

```
JAVASCRIPT_CODE_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Insert System, OS and CPU data to cmdb_ci_win_server' at line 1
```

  
Mid server logs throws the below error:  
  

```
Worker-Standard:HorizontalDiscoveryProbe-b32ed1f0db74b700b1acfbf9af9619a1 WARNING *** WARNING *** org.mozilla.javascript.EcmaError: "JSUtil" is not defined.Caused by error in Ad hoc script 'EvalClosure-Insert System, OS and CPU data to cmdb_ci_win_server' at line 1
```

# Cause

This happens when 'JSUtil' class is called from the mid server and it could not find the class.

# Resolution

Steps:  
  

1.  Go to 'Mid server' module in the instance.
2.  Open 'Script Includes'.
3.  Open the record 'JSUtil' and activate it.

```
 https://<instance-name>.service-now.com/nav_to.do?uri=ecc_agent_script_include.do?sys_id=1d5557480a0a0b84026940e176f072e9%26sysparm_view=discovery
```
