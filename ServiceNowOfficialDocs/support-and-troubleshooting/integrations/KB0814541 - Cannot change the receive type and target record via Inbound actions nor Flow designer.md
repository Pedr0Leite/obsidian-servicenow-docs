---
title: "Cannot change the receive type and target record via Inbound actions nor Flow designer"
aliases:
  - KB0814541
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814541
kb_number: KB0814541
last_modified: 2024-04-08
---

## Cannot change the receive type and target record via Inbound actions nor Flow designer

  

### Issue

-   The email target is not updated via Inbound actions:

email.target\_table = 'incident';  
email.instance = incidentRec.sys\_id; //sys\_id of the related incident  
email.update();

-   Changing the receive type via Inbound Email trigger in flow designer as below does not change the record and it is keeping it as New/Forward:

![](sys_attachment.do?sys_id=3574ac0ddbc8f0d016d2a345ca961900)

### Cause

-   The email target is not updated via Inbound actions :  Expected behavior as the email target found by the classification is updated in the email record AFTER the script has run so it is likely overwriting. In a 'new' email no target is found (since reply prefix does not exist), so the target is saved as empty. More information in our official documentation page: 

[Inbound email flows take priority over inbound email actions. If you create flows with inbound email triggers, emails are first processed by the inbound email triggers before they are processed by inbound email actions.](https://docs.servicenow.com/csh?topicname=inbound-action-processing.html&version=latest "Note: Inbound email flows take priority over inbound email actions. If you create flows with inbound email triggers, emails are first processed by the inbound email triggers before they are processed by inbound email actions.")

-   It would be alright to update an existing ticket with a FW email. However, using a new email to update an existing ticket is not recommended since it would go against the normal inbound email processing flow.

-   If you absolutely have to update an existing ticket with a new email, then you would have to add additional code to your inbound action to find and then update the correct record using GlideRecord based on unique values that you check for in the incoming email. 

### Resolution

Include  the step wait for condition state processed and then you could set even the target record and the receive type. 

  
![](sys_attachment.do?sys_id=8a74ac0ddbc8f0d016d2a345ca961901)
