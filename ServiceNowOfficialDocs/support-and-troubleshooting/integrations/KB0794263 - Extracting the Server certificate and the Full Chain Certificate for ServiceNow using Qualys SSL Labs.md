---
title: "Extracting the Server certificate and the Full Chain Certificate for ServiceNow using Qualys SSL Labs"
aliases:
  - KB0794263
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794263
kb_number: KB0794263
last_modified: 2025-01-03
---

## Extracting the Server certificate and the Full Chain Certificate for ServiceNow using Qualys SSL Labs

  

### Summary

Server certificates are basically used to identify a server. A certificate file must contain the full chain – root CA, intermediate CA, and the origin server certificates. 

Qualys SSL Labs is an easy to use tool that allows you to run a comprehensive free SSL test for public web servers. Using Qualys SSL Labs, you can receive a Server certificate or a full chain certificate. 

### Release

All environments.

### Instructions

1\. _Where can I find the full chain certificate?_ 

Follow these steps to extract the full chain certificate:

\- Go to [SSL Server Test](https://www.ssllabs.com/ssltest/ "SSL Server Test")

\- Enter the Instance name and Run the test

\- Scroll down to **_Certification Paths_** and expand the view. Here you can see the full certificate chain. 

![](/sys_attachment.do?sys_id=88631f0d1bb28058d01143f6fe4bcbb3)

\- Click **_Download Chain_** to view the encoded certificate.

![](/sys_attachment.do?sys_id=98631f0d1bb28058d01143f6fe4bcbb5)

\- Copy all the text and put it in a text editor of your choice.

\- Save it as a PEM, CER or PFX extension. 

2\. _Where can I find the Server certificate in PEM format?_

Follow these steps to extract the Server certificate:

\- Go to [SSL Server Test](https://www.ssllabs.com/ssltest/ "SSL Server Test")

\- Enter the Instance name and Run the test

\- The second section which says 'Certificate #1' has the certificate listed under 'Server Key and Certificate #1'.

\- Click **_Download Server Certificate_** to view the encoded certificate.

![](/sys_attachment.do?sys_id=d0631f0d1bb28058d01143f6fe4bcbb7)
