---
title: "Petya Ransomware - Security Alert"
aliases:
  - KB0623433
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623433
kb_number: KB0623433
last_modified: 2025-01-03
---

## Issue

Petya Ransomware 

About Petya

* * *

A ransomware attack that began to spread in Europe on June 27, 2017 is showing potential to have a broader impact worldwide with several high-profile organizations already infected. Some reports are connecting this to a new variant of the “Petya” (or “Petrwrap”) malware, which was used in prior campaigns earlier this year. Others are saying it is a completely new variant never seen before. The malware uses delivery and propagation methods that exploit recently patched vulnerabilities.

There is some speculation that, like WannaCrypt, the Petya ransomware attack is also being spread using the EternalBlue exploit, which explains why it is spreading as quickly as WannaCry. For more information about WannaCry, see the ServiceNow knowledge article [KB0622722](https://support.servicenow.com/kb_view.do?sysparm_article=KB0622722 "KB0622722").

Based on early analysis of a few publicly available samples, the window of opportunity for response is extremely short. The malware automatically reboots systems after completing its encryption and propagation routines. Early research indicates this occurs within an hour post-infection.  
 

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle;"><strong>Note</strong>: The findings and recommendations are from a number of sources, however this campaign still is not yet fully understood and the situation may continue to evolve.</td></tr></tbody></table>

   
  

ServiceNow Response

* * *

ServiceNow does not use Windows-based computers in its production environment. As such, there is no direct threat to customer data hosted within ServiceNow’s subscription service. Nevertheless, ServiceNow has implemented IDS signatures, SPAM filters, and firewall rules to prevent, monitor and detect for signs of Petya-related activities.  

Recommendation to Customers

* * *

ServiceNow recommends that all customers running Windows patch their systems for MS17-010 as soon as possible. Researchers also recommend blocking inbound connections on TCP Port 445 and creating and maintaining back-ups so that if an infection occurs you can restore your data.

While the spread of Petya is unlikely within the ServiceNow environment, it is possible that customers using [inbound email actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "inbound email actions") could receive an infected email.  As such, ServiceNow also recommends implementing and configuring the [Email Filters plugin](https://support.servicenow.com/kb_view.do?sysparm_article=KB0549426 "Email Filters plugin") to help detect viruses and/or spam that may be directed toward the customer’s instance email address (for example, instance.name@service-now.com).

If you have specific questions, contact the ServiceNow Customer Support team. For a listing of global telephone numbers, refer to the Customer Support Contact Us page at [http://www.servicenow.com/support/contact-support.html](http://www.servicenow.com/support/contact-support.html "http://www.servicenow.com/support/contact-support.html").
