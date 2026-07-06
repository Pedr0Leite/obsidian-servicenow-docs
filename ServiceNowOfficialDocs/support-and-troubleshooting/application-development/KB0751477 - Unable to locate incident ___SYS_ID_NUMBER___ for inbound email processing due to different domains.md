---
title: "Unable to locate incident ___SYS_ID_NUMBER___ for inbound email processing due to different domains"
aliases:
  - KB0751477
  - Unable to locate incident for inbound email processing due to different domains
area: application-development
tags:
  - servicenow
  - support-kb
  - inbound-email
  - domain-separation
  - sys_email
  - sys_domain
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751477
kb_number: KB0751477
last_modified: 2026-05-06
---

## Unable to locate incident \_\_\_SYS\_ID\_NUMBER\_\_\_ for inbound email processing due to different domains

  

### Issue

**Steps to reproduce**

-   Check the sys\_email record
-   Check any affected incident number INCXXXXXXX
-   You will find it was not updated properly, the sys\_email record will show the next message:
-   Unable to locate incident \_\_\_SYS\_ID\_NUMBER\_\_\_ for inbound email processing

**Troubleshooting**

1.  Go to the sys email record: /sys\_email.do?xxxxxxx
2.  Identify the user field for that record
3.  Verify user has required roles to access incidents (itl, itil admin or admin)  
    -   If user has required roles continue below
    -   If user does not have the required roles add them and retest or reprocess the email.
4.  Identify the target record from the email (incident number)
5.  Right-click on 'Show XML'. You will see the next information:  
    If you go here, right-click the header, and select 'Show XML' you can see information similar to this
    
    <sys\_domain>XXXXXXXXXXX</sys\_domain>  
    <sys\_domain\_path>!!!/!!!/!!&/</sys\_domain\_path>
    
6.  Compare both the user domain and the incident domain and they will be different

![](sys_attachment.do?sys_id=a328f34a9328c7d0101833527cba10ff)

### Release

All releases 

### Cause

The incident belongs to a different domain than the user who sent the email

### Resolution

If you consider the user AAAA in the wrong domain or want to know why it is different than expected and when it has changed - you can enable auditing on the sys\_user table through the Dictionary entry here:

https://<instance-name>.service-now.com/sys\_dictionary\_list.do?xxxxx

Consider either changing the domain of the user, or the domain of the incident.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: This issue could occur after upgrading an instance or modifying the user records.</td></tr></tbody></table>

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: Ensure these actions are tested in sub-production instances before implemented in production environments.</td></tr></tbody></table>

## Related

- [[KB0755997 - Reply email is ignored and does not update target record]]
- [[KB0755180 - Inbound emails get processed irrespective of satisfied email filter conditions]]
- [[KB0520595 - Inbound Email overview and troubleshooting]]
- [[KB0538137 - Troubleshooting inbound email action issues]]
