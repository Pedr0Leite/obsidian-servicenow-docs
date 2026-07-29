---
title: "Perform an SNMP query from a Linux MID Server"
aliases:
  - KB0758402
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758402
kb_number: KB0758402
last_modified: 2025-07-24
---

## Perform an SNMP query from a Linux MID Server

  

### Issue

Get options on how to perform an SNMP query using noauth or noencrpt credentials on a Linux MID Server. 

### Release

### Resolution

Shazzam commands that verify credentials are hardcoded in JavaScript and not visible. An alternate way to test the credentials from the Linux MID Server is to either use snmpget or snmpwalk commands. 

Following are examples of SNMP v3 commands

1\. A general test of authentication and encryption credentials: 

snmpwalk -v 3 -a md5 -A PASSWORD -x des -X PASSWORD -u MYUSERNAME IP.ADD.RE.SS

2\. An snmpget query testing authentication and encryption: 

snmpget -v3 -l authPriv -u \[user name\] -a MD5 -A \[user password\] -x DES -X \[DES password\] \[IP address of host\] \[OID for update check\]

3\. An snmpget query testing authentication but no encryption:

snmpget -v3 -l authNoPriv -u \[user name\] -a MD5 -A \[MD5 hash of user password\] \[IP address of host\] \[OID for update check\]

4\. snmpget query testing no authentication and no encryption:

snmpget -v3 -l noAuthNoPriv -u \[User name\] \[IP address of the host\] \[OID for update check\]
