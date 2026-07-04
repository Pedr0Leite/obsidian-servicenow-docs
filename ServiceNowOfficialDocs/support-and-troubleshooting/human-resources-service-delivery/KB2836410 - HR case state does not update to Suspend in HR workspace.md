---
title: "HR case state does not update to Suspend in HR workspace"
aliases:
  - KB2836410
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2836410
kb_number: KB2836410
last_modified: 2026-03-12
---

## HR case state does not update to Suspend in HR workspace

  

### Issue

**Problem**  
In the HR agent workspace, it is not possible to update the HR case state to suspend. The same action works in platform view outside the workspace.  
  
Steps to reproduce:  
1\. Go to HR agent workspace and open an HR case.  
2\. Select the **State** field and choose the option **Suspend**.  
3\. Select the reason and add a work note.  
4\. Select **Ok**.  
  

Result:

The State field does not update to Suspended.

### Release

N/A

### Cause

**Root Cause**  
The behavior is caused by a custom client script utilization in place of the out of box client script **Suspend Dialog Box.**  
  

### Resolution

**Steps to Resolve**  
1\. Disable the custom client script.  
2\. Enable the out of box client script **Suspend Dialog Box** (/nav\_to.do?uri=sys\_script\_client.do?sys\_id=165541030b6022006ec86f3ef6673afa)  
3\. Verify the case state updates to **Suspended** as expected after making these changes.  
  

### Related Links

[Suspend and resume an HR case](https://www.servicenow.com/docs/r/zurich/employee-service-management/hr-service-delivery/t_SuspendAndResumeAnHRCase.html "Suspend and resume an HR case")
