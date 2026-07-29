---
title: "SAM - Import User Subscriptions Scheduled is importing records because of the \"com.sn_sam_saas_int\" plugin being inactive."
aliases:
  - KB0964305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964305
kb_number: KB0964305
last_modified: 2024-05-13
---

## SAM - Import User Subscriptions Scheduled is importing records because of the "com.sn\_sam\_saas\_int" plugin being inactive.

  

### Issue

User Subscriptions weren't getting Imported in Quebec. As they did in Paris.

### Cause

User Subscriptions weren't getting Imported in Quebec.Because the plugin "SaaS license management integrations" has been moved store.

The related Integration profiles are present but upon checking the related profile you see an error message like in the screenshot.

  

![](sys_attachment.do?sys_id=cfd26428db78701092bb0b55ca961906)

### Resolution

Prior to "Quebec" we can still pull subscriptions even though the plugin "SaaS License Management Integrations (com.sn\_sam\_saas\_int)" was not installed.  
  
The Saas menu will still be available if just "SAM Pro" plugin is installed.  
  
Since Quebec, this is a must "SaaS License Management Integrations (com.sn\_sam\_saas\_int)" store application according to the PRB below.  
[https://support.servicenow.com/nav\_to.do?uri=%2Fproblem.do%3Fsysparm\_query%3Dnumber%3DPRB1443152](https://support.servicenow.com/nav_to.do?uri=%2Fproblem.do%3Fsysparm_query%3Dnumber%3DPRB1443152)  
  
See below.  
  
"If SaaS is not enabled,  
  
\--customers who have existing O365/Adobe integrations will not pull any delta or new subscriptions on upgrade to Quebec.  
\--Display an error message on integration profile for O365/ Adobe to indicate customers need to "Please activate the Software Asset Management - SaaS License Management Integrations from the store by clicking here <insert link> for this integration to work " Wording to be worked on"  
\--The scheduled job should gracefully fail"  
  
See the below doc too.  
  
[https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html)  
  
Customers, will have to install the "SaaS License Management Integrations (com.sn\_sam\_saas\_int)" plugin to further import software subscriptions.  
  
I have also tested the same OOB with just SAMP enabled on Quebec, and the store application is mandatory.

### Related Links

PRB1443152
