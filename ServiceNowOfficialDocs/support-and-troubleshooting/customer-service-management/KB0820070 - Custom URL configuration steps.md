---
title: "Custom URL configuration steps"
aliases:
  - KB0820070
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820070
kb_number: KB0820070
last_modified: 2026-05-11
---

## Custom URL configuration steps

  

### Issue

Steps to configure custom URL

### Release

All Releases

### Resolution

Custom URL Configuration Steps:

1\. Customer need to own or purchase a custom URL from a domain provider

2\. In ServiceNow, customer need to activate custom URL plugin (DO NOT activate - Custom URL - Internal)

3\. Go to Custom URL --> Custom URLs --> Add a Custom URL record by filling in Domain name(your custom URL) and choose a service portal URL (not mandatory) to redirect users to when they access the instance using custom URL.

![Custom URL configuration](sys_attachment.do?sys_id=aa38b4614770cb1011eaf24c736d4318 "Custom URL configuration")

4\. Click on Create.

5\. ServiceNow allows up to six hours to complete custom URL creation, although it typically takes less than 30 minutes to complete.

6\. The instance admins receive an email when the custom URL is "Active".

7\. Once the URL is "Active", you can mark it as instance URL by clicking the "Set instance URL" button. This will result in the custom URL being used for all outbound URLs.

8\. ServiceNow uses a certificate from LetsEncrypt for custom URL configuration.

If you decide to sign your own certificate  
Please follow the steps from the documentation:  
Infrastructure Security:  
[https://www.servicenow.com/docs/csh?topicname=infrastructure-security.html&version=latest](https://www.servicenow.com/docs/csh?topicname=infrastructure-security.html&version=latest)  
  
Generate a Certificate Signing Request:  
[https://www.servicenow.com/docs/csh?topicname=inf-sec-generate-csr.html&version=latest](https://www.servicenow.com/docs/csh?topicname=inf-sec-generate-csr.html&version=latest)

### Related Links

[Advanced email set up](https://www.servicenow.com/docs/csh?topicname=c_AlternateEmailConfigurations.html&version=latest)

[KB1002273 - Requesting Public key for DKIM custom domain via Service Catalog on Now Support](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002273)
