---
title: "Why doesn't gs.log work?"
aliases:
  - KB0788208
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788208
kb_number: KB0788208
last_modified: 2025-08-20
---

## Why doesn't gs.log work?

  

When adding debug log statements to JavaScript code, it is common to use the gs.log() function. This function is only available in the instance application node and in global application scope. It is not possible to use it in the following situations, but there are alternatives:

### Scoped applications and code running as that scope

gs.log() cannot be used in Scoped scripts. The script will probably break with this error:

Function log is not allowed in scope xxx. Use gs.debug() or gs.info() instead.

**Solution**: **gs.debug() or gs.info()** can be used instead. They will also log to syslog, but with level field set as info or debug.

Note: These functions do not have the second parameter for 'source'. Instead the syslog record will use the scope name for the source field.

### Client-Side code

UI Policies, Client scripts, some UI Actions and other scripts run directly in the browser, not in the instance. If the code tries to run then you will see errors in the browser console, and if you try to use it in a script field you may see:

The object "gs" should not be used in client scripts. 

**Solution**: jslog(”message”) writes to console, and Alert(“message”) pops up a window. **console.log()** may be used instead, and will output to the Browser's debug console in its developer tools. 

### MID Server code

Probes, Patterns, Connector instances, and MID Server Script Includes all run in the MID Server, not in the instance. There is no GlideSession in the MID Server platform, so none of the gs.log, gs.info, gs.debug functions exist there.

If you put this in MID Server scripts, then you will see errors in the agent log like this:

MID Script Include 'gs' does not exist.  Marking it to prevent future queries.
org.mozilla.javascript.EcmaError: "gs" is not defined.
   Caused by error in Ad hoc script 'null' at line 1

==>   1: gs.log('hello');

**Solution**: Use **ms.log()** instead. The log entries will be found in the Agent Log of the MID Server.
