---
title: "Review the agent log for MID Server errors "
aliases:
  - KB0535148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535148
kb_number: KB0535148
last_modified: 2026-05-26
---

## Review the agent log for MID Server errors

  

### Issue

If your MID Server has started, but it didn't connect to your ServiceNow instance, check the agent log for MID Server errors. 

Find the agent log by going to your MidServer **agent** folder and then to the **logs** subfolder. 

**Before you begin**

Review the following product documentation to see if this addresses your issue: [MID Server Installation](https://docs.servicenow.com/csh?topicname=mid-server-installation.html&version=latest "MID Server Installation")

#### Video Tutorial: How to Troubleshoot MID Server Issues

### Release

### Resolution

To review the agent log in your MID Server for errors:

1.  Locate the logs in the _logs_ folder inside your MID Server files.  
      
    ![](/sys_attachment.do?sys_id=6d7c55e3477e6a14b8a4aa25126d43ca)  
      
    
2.  Locate the agent0.log file inside the logs folder. This is where the MID Servers logs are recorded.  
      
    ![](/sys_attachment.do?sys_id=b97c55e3477e6a14b8a4aa25126d43cf)

The MID Server has already tried and failed several times to complete the startup sequence, which is why this information is repeated in the log when there is an error.

Look for the first error in the startup sequence, which is this warning:

Could not authenticate user 'USERNAMEHERE' on the ServiceNow instance. 

This error indicates that there is an issue with the user account.

1.  Check if the user exists.
2.  If not, create the user and verify that the user name and password _exactly_ match those in the config XML file. 
3.  If a matching user already exists, check that it is **Active** and _not_ **Locked out**.
4.  Restart the service and go into your instance to see if the MID Server connected.

If your MID Server is still not connected, go back to the agent log to find the first error after the restart.

You may see a different error:

Warning: SOAP Server error reported by ServiceNow instance, user 'USERNAMEHERE' may be missing the 'soap\_script' role.

This indicates that there's a problem with the user's role.

To fix this:

1.  Assign the **mid\_server** role to the user, which inherits all other required roles, including the missing **soap\_script** role.
2.  Restart the service.
3.  Go into your instance to see if the MID Server connected.
4.  If it's listed with a **Status** of **Up**, the issue is resolved.
