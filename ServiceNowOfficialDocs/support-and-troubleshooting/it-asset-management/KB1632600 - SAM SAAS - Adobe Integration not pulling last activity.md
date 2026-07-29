---
title: "SAM SAAS - Adobe Integration not pulling last activity"
aliases:
  - KB1632600
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1632600
kb_number: KB1632600
last_modified: 2024-02-12
---

## SAM SAAS - Adobe Integration not pulling last activity

  

### Issue

**Need to know how exactly the optimisation work for adobe subscriptions if last activity is not pulled for adobe subscription**

### Resolution

**Why servicenow does not pull last activity of adobe subscription in adobe integration?**

As there is no API from Adobe end to pull last activity of user, OOB servicenow does not pull last activity for adobe subscription user. You need to reach Adobe in order to get more information about this API.

**How will the optimisation work for adobe subscription in that case?**

Optimisation for Adobe will be done by using SCCM metering data;

[https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-saas-subscription-dash.html](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/sam-saas-subscription-dash.html)

If SCCM SG is connected then it is really a matter having the SCCM admin enable metering for a specific app or apps and then configuring a reclamation rule.  We will not pull in metering data from SCCM if there is no reclamation rule configured.  

[https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/t\_AddAReclamationRule.html](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/t_AddAReclamationRule.html "https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/task/t_addareclamationrule.html")

![](/sys_attachment.do?sys_id=93ff4ac2c310c610a9ea601bb001316a)
