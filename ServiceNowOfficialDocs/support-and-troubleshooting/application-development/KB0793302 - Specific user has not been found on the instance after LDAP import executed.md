---
title: "Specific user has not been found on the instance after LDAP import executed"
aliases:
  - KB0793302
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793302
kb_number: KB0793302
last_modified: 2024-04-08
---

## Specific user has not been found on the instance after LDAP import executed

  

### Issue

LDAP import user has not been found in the instance.

### Cause

Filter condition does not match with the LDAP OU Definition

### Resolution

1\. Verify the if the user is Active and his/her distinguished name (DN) from the LDAP server.  
\- Login into instance  
\- Filter navigator > LDAP Server  
\- Select LDAP Server involved.

1.2 Click on ‘Browse’  
\- Using user = dmoreno@servicenow.com  
Filter: (&(objectClass=person)(objectClass=user)(userprincipalname=dmoreno@servicenow.com))

1.3) Click on:  
LDAP Nodes  
CN=Moreno\\, Dey,OU=(ORL) Users,OU=(ORL) Orlando Office  
We can confirm: User exists and it is Active:  
displayName Moreno, Joseph  
distinguishedName CN=Moreno\\, Dey,OU=(ORL) Users,OU=(ORL) Orlando Office,DC=US,DC=SN,DC=com  
userAccountControl 512 <<<<< This means that user is ACTIVE

2) Using the distinguished name (DN) information returned, we will inspect the LDAP server OU definitions to check if there is one that allows to get this particular DN:  
distinguishedName CN=Moreno\\, Dey,OU=(ORL) Users,OU=(ORL) Orlando Office,DC=US,DC=SN,DC=com

o Checking the LDAP Server ‘Test User LDAP ’ observe:  
\-- Starting search directory = DC=US,DC=SN,DC=com <<<<< This OK  
\-- Under ‘LDAP OU Definitions’ there is no one containing the pattern ‘ORL’ or anything related to Orlando Office in the LDAP filter.

A new OU Definition for the Orlando Office needs to be created.  
As an example, the LDAP filter should look like:  
(&(objectClass=person)(sn=\*)(OU=(ORL) Orlando Office)(!(objectClass=computer))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))

This will resolve the issue.

### Related Links

Additional information about this topic can be found on ServiceNow documentation:

[LDAP integration](https://docs.servicenow.com/csh?topicname=c_LDAPIntegration.html&version=latest "LDAP integration")
