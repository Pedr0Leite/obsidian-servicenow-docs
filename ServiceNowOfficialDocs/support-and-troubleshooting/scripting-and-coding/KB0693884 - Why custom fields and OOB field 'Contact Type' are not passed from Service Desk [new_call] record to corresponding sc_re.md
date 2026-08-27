---
title: "Why custom fields and OOB field 'Contact Type' are not passed from Service Desk [new_call] record to corresponding sc_request/sc_req_item records?"
aliases:
  - KB0693884
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693884
kb_number: KB0693884
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

With "Service Desk Call" application, when we create a "new call, the user defined custom fields and out of the box provided "Contact Type" field are not transitioned/passed from "new\_call" record to corresponding sc\_request/sc\_req\_item records as expected.

# Release

* * *

Any supported release. 

# Cause

* * *

With "Service Desk Call" application, there is an out of the box provided business rule called "Link back to the call that generated it" ("/uri=sys\_script.do?sys\_id=8b073868eb100100fcfb858ad106fe13"). This business rule controls the logic of what data needs to be passed on to sc\_request record from new\_call record.

If you have customized this business rule, review your customization for any issues with data assignment, if possible, revert it to out of the box version.

Also this business rule has a condition as "current.special\_instructions.startsWith("NEW\_CALL\_REF:")". This condition is being setup in another out of the box business rule called "CallTypeChanged to Request" ("/uri=sys\_script.do?sys\_id=01175810eb100100fcfb858ad106fee3").

Hence, if you see in the sesson debug lines as below, then review the "CallTypeChanged to Request" business rule and if possible rever it to out of the box version.

02:46:43.211: BUSINESS RULE - Skipping execution of Link back to the call that generated it on sc\_request:REQ0755094; condition not satisfied: Condition: current.special\_instructions.startsWith("NEW\_CALL\_REF:")   
business rule02:46:43.212: Global === Skipping 'Link back to the call that generated it' on sc\_request:REQ0755094; condition not satisfied: Condition: current.special\_instructions.startsWith("NEW\_CALL\_REF:") 

# Resolution

* * *

Revert the "Link back to the call that generated it" and "CallTypeChanged to Request" business rules to the out of the box version.

If revrting to out of the box version is not possible due to your business requirement, then review your customizations in those business rules and merge it with out of the versions carefully, without altering the out of the box provided logic.

# Additional Information

* * *

[Service Desk Call](https://docs.servicenow.com/csh?topicname=c_ServiceDeskCall.html&version=latest "Service Desk Call")

[Business Rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business Rules")

[Revert the customization](<Revert a customization> "Revert the customization")

[Revert a change](https://docs.servicenow.com/csh?topicname=t_RevertAChange.html&version=latest "Revert a change")
