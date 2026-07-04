---
title: "Verifying the instance has the proper custom SMTP server settings"
aliases:
  - KB0524531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0524531
kb_number: KB0524531
last_modified: 2025-10-16
---

## Verifying the instance has the proper custom SMTP server settings

  

### Issue

Verifying the instance has the proper custom SMTP server settings

### Symptoms

If your instance sends messages from an SMTP server your company maintains (rather than a ServiceNow SMTP server), verify your instance connects to the proper SMTP server.

### Release

All

### Resolution

If your instance sends messages from an SMTP server your company maintains (rather than a ServiceNow SMTP server), verify your instance connects to the proper SMTP server.

| System Property | Label | Setting Required |
| --- | --- | --- |
| glide.email.smtp.active | Enable email sending (SMTP). | **Yes** |
| glide.email.server | Outgoing (SMTP) mail server. Also used as incoming (POP) mail server if one is not specified. This server must be accessible from the service-now.com domain. SMTP requires port 25. POP requires port 110. | 
URL to your SMTP server.

For example,  
**smtp.yourdomain.com**.

 |
| glide.email.user | User email (eg. helpdesk@company.com) that is used to login to the SMTP server optionally. Select the "Authenticate with the SMTP server using the user name and password properties" checkbox to require SMTP authentication. The name part of this email e.g. "helpdesk" in "helpdesk@company.com" is used to log into the POP3 server. | 

Email address to use for SMTP authentication.

For example,  
**helpdesk@yourdomain.com**.

 |
| glide.email.user\_password | Outgoing (SMTP) mail server password. Also used as incoming (POP) mail server password if one is not specified. | Password for the SMTP server. Contact your SMTP server administrator for this value. |
