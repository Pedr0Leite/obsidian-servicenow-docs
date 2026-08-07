---
title: "EMC Isilon discovery REST GET method returns nothing"
aliases:
  - KB0745013
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745013
kb_number: KB0745013
last_modified: 2024-04-07
---

## EMC Isilon discovery REST GET method returns nothing

  

### Issue

# Symptoms

Some of the steps for Isilon discovery use REST (GET method) to get device information.

These steps leverage Basic Authentication credentials that are created by the customer for authentication for REST methods. 

In some cases even with basic auth. credentials defined the REST method returns no information, where testing on 3rd party REST client does (For example on Postman).

The discovery log will look something like the below, the Red Box is the IP address of the host server. 

![](sys_attachment.do?sys_id=00ceb8a2db0ab450e515c22305961941)

# Release

All where this pattern is installed

# Cause

In some cases the Isilon device requires a certificate to be uploaded to the MID servers which execute the REST method. 

If there is none then we return nothing from discovery REST step for this device.

# Resolution

Create a certificate and upload to the MID server.   
Please see the Isilon documentation below on how to get a certificate for the device:

[EMC Isilon Certificates](http://doc.isilon.com/onefs/7.1.1/help/en-us/GUID-119BB455-BC73-4417-AA81-20E7381BAC18.html "EMC Isilon Certificates")

See the docs below on how to import certificate to ServiceNow MID server:

[Add SSL certificate to MID Server](https://docs.servicenow.com/csh?topicname=add-ssl-certificates.html&version=latest "Add SSL certificate to MID Server")
