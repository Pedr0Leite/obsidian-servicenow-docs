---
title: "MID server error: Unable to negotiate with ip address : no matching key exchange method found' when connecting to a Linux target machine"
aliases:
  - KB0693985
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693985
kb_number: KB0693985
last_modified: 2024-04-07
---

## Issue

In the MID server agent logs, you are seeing this error message while discovering a Linux machine:

_Unable to negotiate with ip address : no matching key exchange method found_

  

  

## Resolution

In order to resolve this issue, Please add the algorithms to the target Linux machine's ~/.ssh/config file by adding the following lines to the file: 

KexAlgorithms +diffie-hellman-group1-sha1 

KexAlgorithms +diffie-hellman-group14-sha1 

KexAlgorithms +diffie-hellman-group-exchange-sha1 

KexAlgorithms +diffie-hellman-group-exchange-sha256
