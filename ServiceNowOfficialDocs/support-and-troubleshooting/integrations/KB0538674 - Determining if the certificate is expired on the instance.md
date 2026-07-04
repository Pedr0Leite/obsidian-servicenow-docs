---
title: "Determining if the certificate is expired on the instance"
aliases:
  - KB0538674
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538674
kb_number: KB0538674
last_modified: 2024-02-01
---

## Determining if the certificate is expired on the instance

  

### Issue

Do you see a simple bind error message when using the test connection link in the LDAP Server record? Review this article for more information.

When the LDAP server certificate is expired on the instance or does not match the certificate currently being used by the LDAP server, it causes users to be unable to access the instance and the simple bind error message to be displayed.

The video below provides a walkthrough to renew the certificate and resolve the simple bind error message:

See the information below for additional context

### Cause

The certificate currently on the instance has expired or the certificate associated with the LDAP server has changed.

### Resolution

Contact the LDAP administrator to update the certificate for the associated LDAP server, and upload a new certificate to the instance.

See the [Upload a certificate to an instance](https://docs.servicenow.com/csh?topicname=t_UploadACertificateToAnInstance.html&version=latest "Upload a certificate to an instance") documentation for steps on how to upload the certificate.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Check the <strong>Expiration notification</strong> checkbox within the certificate record to receive an email notification when the certificate is about to expire.</td></tr></tbody></table>
