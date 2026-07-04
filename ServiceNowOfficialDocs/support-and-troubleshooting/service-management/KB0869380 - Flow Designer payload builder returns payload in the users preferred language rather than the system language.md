---
title: "Flow Designer payload builder returns payload in the users preferred language rather than the system language"
aliases:
  - KB0869380
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869380
kb_number: KB0869380
last_modified: 2024-01-03
---

## Flow Designer payload builder returns payload in the users preferred language rather than the system language

  

### Issue

You will recognise this issue when you have a Business rule configured to call the payload builder action in a subflow via

executeSubflow()

### Cause

The call to the subflow in the business rule is made via 

executeSubflow()

which runs synchronously

### Resolution

There are 3 possible solutions to this issue

# Trigger the subflow via a flow trigger.

This causes the subflow to run in a separate session as system (The subflow is configured to run as system) and thus does not user the language preference of the user  

# Alter the business rule to call the subflow asynchronously.  

The  [API Reference](https://developer.servicenow.com/dev.do#!/reference/api/paris/server/sn_fd-namespace/ScriptableFlowAPI#ScriptableFlow-executeSubflow "API Reference") tells us that `executeSubflow()` runs synchronously and thus in the context of the user  
  
If we instead use

```
startSubflow()
```

the subflow will be called asynchronously, and thus in the context of the system user.

# Add a 2 second timer at the beginning of the subflow.

This timer has the effect of breaking the execution from the current session and it will then run under the system user
