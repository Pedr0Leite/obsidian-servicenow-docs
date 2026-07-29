---
title: "Troubleshooting email issues with ServiceNow"
aliases:
  - KB0538136
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538136
kb_number: KB0538136
last_modified: 2025-02-08
---

## Troubleshooting email issues with ServiceNow

  

### Issue

This article guides you through the process of troubleshooting email with ServiceNow. It provides steps to help you eliminate common causes of your problem by verifying that the configuration of your networking is correct. 

**Symptoms:** 

Symptoms may include the following:

-   Cannot send email
-   Emails not being sent
-   Email is down
-   SMTP not working
-   Not receiving incoming mail
-   Inbound email not functioning
-   Instance stopped receiving email
-   Inbound email is not working
-   Inbound email is broken
-   Outbound email not working
-   Email is delayed

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that will help you eliminate possible causes and take corrective action as necessary. 

1.  Verify that the instance is enabled to send email. For more information, see [KB0524529: Verifying the instance is enabled to send email](/kb_view.do?sysparm_article=KB0524529&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524529+&sysparm_topic= "Verifying the instance is enabled to send email") or [KB0521775: Enabling Email Receiving](/kb_view.do?sysparm_article=KB0521775&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0521775+&sysparm_topic= "Enabling Email Receiving").
2.  Verify that you are using the correct credentials for email. For more information, see [KB0535520: Check email connection and credentials](/kb_view.do?sysparm_article=KB0535520&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=fd5f99ca80402d44c14db3a5dc083e480be997fba8aad4a52db173927f61ba62e6529796&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0535520&sysparm_topic= "Check email connection and credentials"), [KB0524524: Verifying custom POP settings](/kb_view.do?sysparm_article=KB0524524&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524524&sysparm_topic= "Verifying custom POP settings"), or [KB0524531: Verifying the instance has the proper custom SMTP server](/kb_view.do?sysparm_article=KB0524531&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524531+&sysparm_topic= "Verifying the instance has the proper custom SMTP server settings") [settings](/kb_view.do?sysparm_article=KB0524531&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524531+&sysparm_topic= "Verifying the instance has the proper custom SMTP server settings").
3.  Verify if email has been provisioned, if you are connected to the mail server, or if your mail server is able to process email. For more information, see [KB0524524: Verifying custom POP settings](/kb_view.do?sysparm_article=KB0524524&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524524&sysparm_topic= "Verifying custom POP settings") or [KB0524531: Verifying the instance has the proper custom SMTP server](/kb_view.do?sysparm_article=KB0524531&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524531+&sysparm_topic= "Verifying the instance has the proper custom SMTP server settings") [settings](/kb_view.do?sysparm_article=KB0524531&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0524531+&sysparm_topic= "Verifying the instance has the proper custom SMTP server settings").
4.  In addition to these steps, visit the troubleshooting notifications article for any additional information that may help: [KB0538135: Troubleshooting email notification failures in ServiceNow.](/kb_view.do?sysparm_article=KB0538135&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=2d5a96358048e544c14db3a5dc083e704ab425c7283d0b9c4fe783cd8644c4ed3a6556a1&sysparm_nameofstack=&sysparm_product=&sysparm_search=troubleshooting+email+notification+failures&sysparm_topic= "Troubleshooting email notification failures in ServiceNow")
