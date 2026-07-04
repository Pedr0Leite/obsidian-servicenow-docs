---
title: "OOB reclamation rules for subscription products"
aliases:
  - KB0828042
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0828042
kb_number: KB0828042
last_modified: 2024-04-08
---

## Issue

We do not see OOB reclamation rules present for office 365 and adobe but your document seems to state so:

[https://docs.servicenow.com/csh?topicname=add-reclamation-rule-sub.html&version=latest.](https://docs.servicenow.com/csh?topicname=add-reclamation-rule-sub.html&version=latest.)

## Resolution

The OOB reclamation rules are provided only for a complete SAAS based product i.e., ones that do not have install records. As Microsoft and Adobe publisher are hybrid that is they can have subscriptions as well as installs. We do not provide OOB reclamation rules for these.

For reclamation of installs, it goes via reclamation rules that you will create based on the usage data that is brought in via a SCCM integration.  
Doc link to reclamation rule:  
[https://docs.servicenow.com/csh?topicname=t\_AddAReclamationRule.html&version=latest](https://docs.servicenow.com/csh?topicname=t_AddAReclamationRule.html&version=latest)  
Doc link to software usage:  
[https://docs.servicenow.com/csh?topicname=t\_ViewSoftwareUsage.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ViewSoftwareUsage.html&version=latest)
