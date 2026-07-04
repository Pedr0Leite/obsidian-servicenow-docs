---
title: "User with \"snc_read_only\" role is unable to place ServiceNow requests."
aliases:
  - KB0696546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696546
kb_number: KB0696546
last_modified: 2024-09-20
---

## User with "snc\_read\_only" role is unable to place ServiceNow requests.

  

### Issue

# Symptoms

* * *

User with "snc\_read\_only" role is unable to place ServiceNow requests.

Error Shown:  'You cannot check out with an empty cart!'

# Release

* * *

Jakarta

# Cause

* * *

This is expected behavior as user's roles (read\_only) prevents write access to the instance as the request record is not created and hence below error is shown:

Error:  'You cannot check out with an empty cart!'

# Resolution

* * *

 Some tables can be exempted from begin read only by adding the tables name to property: glide.security.snc\_read\_only\_role.tables.exempt\_write  
[https://docs.servicenow.com/csh?topicname=c\_ReadOnlyRole.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ReadOnlyRole.html&version=latest)

Below tables needs to added to generate request, RITM and to start a workflow. 

1) glide.security.snc\_read\_only\_role.tables.exempt\_create   
Value = sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth, sc\_cart, sc\_req\_item, sc\_request, sc\_cart\_item, sc\_item\_option\_mtom, wf\_context, wf\_workflow\_version, wf\_workflow, wf\_variable, wf\_stage, wf\_activity, wf\_executing, wf\_log, sys\_mutex, wf\_history, wf\_transition\_history, wf\_command, sys\_attachment, sys\_number\_counter, task, sc\_item\_option, sc\_task,  sys\_trigger  
  
2)glide.security.snc\_read\_only\_role.tables.exempt\_write   
Value= sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth, sc\_cart, sc\_req\_item, sc\_request, sc\_cart\_item, sc\_item\_option\_mtom, wf\_context, wf\_workflow\_version, wf\_workflow, wf\_variable, wf\_stage, wf\_activity, wf\_executing, wf\_log, sys\_mutex, wf\_history, wf\_transition\_history, wf\_command, sys\_attachment, sys\_number\_counter, task, sc\_item\_option, sc\_task,  sys\_trigger  
  
3)glide.security.snc\_read\_only\_role.tables.exempt\_delete   
Value =sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth, sc\_cart\_item, sc\_item\_option\_mtom
