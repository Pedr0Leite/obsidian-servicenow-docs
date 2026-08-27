---
title: "Some vCenter name is vCenter@hostname and some are vCenter@ip_address"
aliases:
  - KB0743871
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743871
kb_number: KB0743871
last_modified: 2024-04-07
---

## Some vCenter name is vCenter@hostname and some are vCenter@ip\_address

  

### Issue

# Overview

Why are the vCenter names inconsistent when using discovery?

# vCenter discovery

There are two type of vCenter discovery.

I.  vCenter is hosted on a Windows Server

II.  vCenter is on a linux appliance

# Example

I.  When vCenter is installed on a Windows server. 

1.  You will need to have the Windows Server Credentials as well as the vCenter Credentials
2.  The windows credential is used to discovery the Windows server and check to see if there are any running process containing "vpxd
3.  If it detects the process "vpxd" it kick off the process classifier "vCenter"

           http://instance.service-now.com/discovery\_classy\_proc.do?sys\_id=9d5166150a0a0baf385aeb20686568b0&sysparm\_record\_target=discovery\_classy\_proc&sysparm\_record\_row=1&sysparm\_record\_rows=1&sysparm\_record\_list=nameCONTAINSvcenter%5EORDERBYorder

Since, vCenter is discovered via the process classifier name will be given in the following format [vCenter@hostname](mailto:vCenter@hostname)

II.  When vCenter is an appliance on a Linux Server

1.  We do not need the localhost credentials, only the vCenter credential
2.  Since we do not discover the host system we do not get the name of the host system.
3.  Since it's discovered without the discovering the host system the name will be [vCenter@ip\_address](mailto:vCenter@ip_address)
