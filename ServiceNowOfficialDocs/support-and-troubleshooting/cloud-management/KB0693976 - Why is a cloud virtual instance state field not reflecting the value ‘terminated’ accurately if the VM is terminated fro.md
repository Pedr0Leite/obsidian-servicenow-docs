---
title: "Why is a cloud virtual instance state field not reflecting the value ‘terminated’ accurately if the VM is terminated from Azure/AWS portals -outside of ServiceNow-?"
aliases:
  - KB0693976
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693976
kb_number: KB0693976
last_modified: 2024-04-07
---

## Issue

Scope > 

\----------

 If a VM is terminated in Azure/AWS portals the state value in the Azure Virtual Machine Instances list turns to Null instead of 'terminated'.

  

  

Conclusion > 

\-----------------

This is by design. If the VM is removed through ServiceNow "Terminate VM" UI Action, the state of the VM will be terminated. However since the change happened outside ServiceNow. By the time discovery runs the VM is no longer found, Discovery updates the state to empty if the VM is no longer found.
