---
title: "Incoming emails with infected attachments are not marked as SPAM"
aliases:
  - KB0788052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788052
kb_number: KB0788052
last_modified: 2026-07-02
---

## Incoming emails with infected attachments are not marked as SPAM

  

### Issue

If using ServiceNow relay and when a user sends an email to the instance, those emails are scanned in the email infrastructure before reaching the instance.

If the email is identified as spam/infected, the header of the email will be populated with:

X-ServiceNow-Spam-Flag:YES,

X-ServiceNow-Virus:INFECTED

In some cases the email will not be marked as infected even it contains a malicious attachment.

### Cause

An incoming email is scanned by the system against the vendor's database of viruses, which gets updated based on whatever inputs they maintain.

Only if a virus has been updated in the vendor's database, then it is generally known and has a virus-like signature, for which it can be blocked. Otherwise it will pass through.

### Resolution

Upload the attachments in the below form so to get them added to the Vendor's database of known viruses and prevent the issue in future:  
[https://www.clamav.net/reports/malware](https://www.clamav.net/reports/malware)

### Related Links

[Email filters](https://docs.servicenow.com/bundle/utah-platform-administration/page/administer/notification/concept/c_EmailFilters.html "Email filters")

[Inbound email spam scoring and filtering](https://support.servicenow.com/kb_view.do?sysparm_article=KB0549426 "Inbound email spam scoring and filtering")

[Malicious email attachments fail to get extracted from the email log causing some files that are present in Phish emails to not get copied into security incidents](https://support.servicenow.com/kb_view.do?sysparm_article=KB1377392 "Malicious email attachments fail to get extracted from the email log causing some files that are present in Phish emails to not get copied into security incidents")
