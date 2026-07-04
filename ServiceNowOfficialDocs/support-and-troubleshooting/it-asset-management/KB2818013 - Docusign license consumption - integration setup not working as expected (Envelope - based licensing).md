---
title: "Docusign license consumption - integration setup not working as expected (Envelope - based licensing)"
aliases:
  - KB2818013
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2818013
kb_number: KB2818013
last_modified: 2026-05-20
---

## Issue

After the DocuSign integration with ServiceNow was configured, if the license consumption data is  reported on a per-user basis instead of being tracked according to the per-desired envelope usage. The customer wants to track consumption by envelope based on the data present in the samp\_docusign\_consumption.  
  

## Resolution

  
1\. Use the OOTB Docusign DocuSign Envelope Software Model instead of the Docusign E-Signature Pro Software Model to create Entitlements. 

2\. Run reconciliation to ensure DocuSign consumption is licensed as expected.

3\. Review the samp\_docusign\_consumption table for details such as status counts (Completed: 17,267, Declined: 95, Sent: 842, Voided: 3,302, Delivered: 83, Correct: 3).

4\. For unlicensed user subscriptions, add entitlements or mark the Software model as 'License under management' to false.

5\. Verify the resolution by checking if license consumption aligns with expectations.
