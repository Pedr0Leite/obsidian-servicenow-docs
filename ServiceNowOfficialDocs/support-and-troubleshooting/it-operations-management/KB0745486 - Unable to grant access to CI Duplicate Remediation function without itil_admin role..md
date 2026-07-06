---
title: "Unable to grant access to CI Duplicate Remediation function without itil_admin role."
aliases:
  - KB0745486
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745486
kb_number: KB0745486
last_modified: 2025-04-07
---

## Unable to grant access to CI Duplicate Remediation function without itil\_admin role.

  

### Issue

# Symptoms

Unable to grant access to CI Duplicate Remediation function without **itil\_admin** role.

# Cause

This is by design and hardcoded within ServiceNow. Therefore, there is no way to provide this capability without the **itil\_admin** role.

Code Excerpt  
12 <g2:evaluate var="jvar\_user\_has\_permissions" expression="gs.hasRole('**itil\_admin**')" />  
13  
14 <!-- Branch and display access denied message if needed -->  
15 <j2:if test="$\[jvar\_user\_has\_permissions == false\]" >  
16 <!-- Common 'browser unsupported' message page -->  
17 <g:inline template="cmdb\_access\_denied.xml"/>  
18 </j2:if>

# Additional Information

[Remediate a de-duplication task](https://docs.servicenow.com/csh?topicname=reconcile-dup-task.html&version=latest#reconcile-dup-task "Remediate a de-duplication task")
