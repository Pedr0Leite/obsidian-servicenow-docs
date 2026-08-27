---
title: "Error - ldap://<ldap_server_ip>:<Port>/ Invalid credentials"
aliases:
  - KB0756703
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756703
kb_number: KB0756703
last_modified: 2024-04-07
---

## Error - ldap://:/ Invalid credentials

  

### Issue

When running a Test Connection Probe from LDAP Server administrators get an error as - ldap://<ldap\_server\_ip>:<Port>/ Invalid credentials

Make sure this user account has login and read access to the server

### Cause

In most of the cases the cause of the issue is the Login Distinguished Name and the Password doesn't match.

In some cases the error is misleading, in such cases cause of the issue could be user doesn't have a valid access to the starting search directory.

### Resolution

1.  Check the login distinguished name and password is correct.
2.  In cases where error is misleading check user has valid access to the starting search directory.
3.  Run LDAP Search command on the LDAP Server -   
    ldapsearch -x -D "<login\_distinguished\_name>" -w <Password> -H <LDAP Server:port> -b "<Starting Search Directory>""(&(objectClass=person))"
4.  Alternatively customer can install 3rd party LDAP Search tools like Jxplorer to check the issue further.
5.  To further debug administrators can enable LDAP debug system properties and check the issue in system logs.  
    Property Name - glide.ldap.debug  
    Type  - True/False.
