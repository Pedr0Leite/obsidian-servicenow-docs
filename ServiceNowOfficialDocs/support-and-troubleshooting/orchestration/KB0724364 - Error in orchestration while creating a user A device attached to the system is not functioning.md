---
title: "Error in orchestration while creating a user: A device attached to the system is not functioning"
aliases:
  - KB0724364
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724364
kb_number: KB0724364
last_modified: 2024-04-07
---

## Error in orchestration while creating a user: A device attached to the system is not functioning

  

### Issue

# Symptoms

* * *

While creating users in Active Directory through Orchestration workflow, it would below errors:  
  
{"result":"failure","errorMessage":"\\nA device attached to the system is not functioning.Stack Trace: at System.DirectoryServices.DirectoryEntry.CommitChanges()at CommitChanges(Object , Object\[\] )at System.Management.Automation.DotNetAdapter.AuxiliaryMethodInvoke(Object target, Object\[\] arguments, MethodInformation methodInformation, Object\[\] originalArguments)\\n"}   
  
![](sys_attachment.do?sys_id=545b286adb42b450e515c2230596193c)

# Release

* * *

All Versions

# Cause

* * *

The cause of this error message is because of sAMAccountName limitation from Active Directory end. The length of the filed should be limited to 20 characters.

# Resolution

* * *

In "Create AD Object" activity, there is "Object name" field. Whatever is provided in this filed will be sAMAccounrtName. Make sure the username provided here is less than 20 characters.

![](sys_attachment.do?sys_id=185b286adb42b450e515c22305961941)

# Additional Information

* * *

[Create AD Object activity](https://docs.servicenow.com/csh?topicname=r_CreateADObject.html&version=latest "Create AD Object activity")
