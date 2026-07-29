---
title: "Enabling SNC SSH to support newer and more secure cipher algorthms for the Discovery process (i.e AES 256 encryption)"
aliases:
  - KB0748632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748632
kb_number: KB0748632
last_modified: 2024-04-07
---

## Enabling SNC SSH to support newer and more secure cipher algorthms for the Discovery process (i.e AES 256 encryption)

  

### Issue

SNCSSH is a ServiceNow implementation of an SSH client and is active by default for all MID Servers on new instances, via a MID Server property. SNCSSH is part of the MID Server SSH Library and can be used in place of Legacy J2SSH. One of the advantages of using SNCSSH is its support for newer cipher algorithms compared to J2SSH. SNCSSH supports:  
  

`- Key Exchange Algorithms: diffie-hellman-group-exchange-sha1, diffie-hellman-group14-sha1, diffie-hellman-group-exchange-sha256, diffie-hellman-group1-sha1   - Signature Algorithms: ssh-dss, ssh-rsa   - Client-to-Server Cipher Algorithms: aes128-ctr, aes192-ctr, aes256-ctr, 3des-ctr, aes128-cbc, aes192-cbc, aes256-cbc, 3des-cbc, none   - Client-to-Server MAC Algorithms: hmac-sha1, hmac-sha1-96, hmac-sha2-256, hmac-sha2-512, hmac-md5, hmac-md5-96   - Client-to-Server Compression Algorithms: none`

  
The mid.property.ssh.use\_snc will determine if snc ssh will be used for probe-based discovery.  
The mid.sa.ssh.use\_sncssh will determine if snc ssh will be used for patterns-based discovery.  
  

Customers who have upgraded from older versions where J2SSH was the default library will not be forced to use SNC SSH and will need to manually enable SNC SSH if they wish to use it.

### Release

Available from Kingston onwards

### Resolution

We recommend that you take the following actions to enable SNC SSH for discovery:

1.  Log into your instance as an admin
2.  Go to Mid Servers > Properties (/ecc\_agent\_property\_list.do)
3.  Create/Configure the following properties:  
    \-mid.property.ssh.use\_snc = true  
    \-mid.sa.ssh.use\_sncssh = true

### Related Links

Please see KB0594703 if you want to know how to force AES 256 encryption for the communication between the mid server and the instance.
