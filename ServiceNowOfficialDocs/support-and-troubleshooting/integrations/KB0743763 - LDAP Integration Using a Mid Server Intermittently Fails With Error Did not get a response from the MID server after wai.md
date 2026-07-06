---
title: "LDAP Integration Using a Mid Server Intermittently Fails With Error:  Did not get a response from the MID server after waiting for 55 seconds "
aliases:
  - KB0743763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743763
kb_number: KB0743763
last_modified: 2026-05-13
---

## LDAP Integration Using a Mid Server Intermittently Fails With Error: Did not get a response from the MID server after waiting for 55 seconds

  

### Issue

Observing the LDAP logs you periodically see the following error:

Error LDAP Server: LDAPServer-LDAP URL: ldap://ldapserver.test.corp failed scheduled connection test. ErrorCode: 40100. ErrorMessage: Did not get a response from the MID server after waiting for 55 seconds.

Repeatedly testing the LDAP connectivity from a browser shows the following failure for some of the tests:

https://<instancename>.service-now.com/security\_status.do?name=LDAPAuthStatus&action=testconnection

{   
"LDAPServer-LDAP" : \[ {  
"url" : "ldap://ldapserver.test.corp",  
"operational\_status" : true,  
"test\_error\_code" : 40100,   
"test\_error\_message" : "Did not get a response from the MID server after waiting for 55 seconds",   
"test\_success" : false   
} \]  
}  
  
Other times the same test passes fine:  
  
{   
"LDAPServer-LDAP" : \[ {  
"url" : "ldap://ldapserver.test.corp",  
"operational\_status" : true,  
"test\_error\_code" : 0,  
"test\_error\_message" : "Connected successfully",  
"test\_success" : true  
} \]  
}

This displays the intermittent nature of the failure.

This may also have led to an auto-generated alert Case in HI with the subject "AHA Audit Failed: LDAP Connectivity" because our monitoring is using the same test.

### Release

You have an LDAP integration that runs the LDAP connection through a mid server. Applies to any release. 

### Cause

1.  Go to **Mid Server > Servers** > select the mid server which hosts the LDAP server
2.  From under "**Related Links**" select "**Grab MID logs**"
    -   There should be two **Queue = output** lines, one with **Name = agent0.log.0** and one with **wrapper.log**
    -   After a few seconds there should be two **Queue = input** lines, one with **Name = agent0.log.0** and one with **wrapper.log**
    -   But in this case there are more than just the two Queue = input lines returned, for example there are four lines returned: two with Name = agent0.log.0 and two with wrapper.log
    -   If you see duplicated agent0.log.0 and wrapper.log records being returned then the solution provided in this KB needs to be implemented.

This may be caused by the Windows machine having two or more mid server JVMs (or, putting it another way, two or more Windows services) running out of the same mid server installation directory causing various issues with mid server responses.  In this case, causing delays to the responses to the LDAPConnectionTesterProbe (as seen in the ECC queue) causing the LDAP connection failure errors and multiple responses to the "Grab MID logs" requests.

To verify this go into the Windows Services on the mid server machine and right click on each of the mid server services you have in Running there then select Properties -> check the "Path to executable" for each Service - if two or more point to the same directory path then you have this issue.

### Resolution

Shutdown all but one of the mid server Services on the Windows machine where there are duplicated "Path to executable" Services, keeping just one of them running. Be sure to set the shutdown mid server Services to not restart automatically by setting Startup Type to "Disabled".

Repeating the "Grab MID logs" should no longer result in multiple agent0.log.0 and wrapper.log files being returned and the LDAP connection test failures should no longer be seen.
