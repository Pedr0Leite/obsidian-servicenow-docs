---
title: "Post-Cloning Checklist"
aliases:
  - KB0547597
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547597
kb_number: KB0547597
last_modified: 2026-05-11
---

## Post-Cloning Checklist

  

### Issue

A clone is a snapshot of a ServiceNow instance typically used to refresh your test or development environments. ServiceNow performs the cloning process, but there are several post-cloning tasks for you to perform as described in this article. For more information about cloning, see the [Cloning Resources Page](https://support.servicenow.com/kb_view.do?sysparm_article=KB0539837 "Cloning Resources Page").

Finally, if you clone frequently, it might be helpful to develop a script that automates the execution of these post-clone tasks, as described in the last section of this article.

### Post-clone tasks

Perform the following tasks after your production instance is cloned:

-   Update the welcome page
-   Change the email properties
-   Restrict user access
-   Modify LDAP to disable imports and updates.
-   Disable active scheduled jobs

### Welcome page

Verify that the welcome page message is active. Within each instance, welcome messages contain standard text that is displayed on the sign-in page for each instance, for example, text indicating that the instance is non-production or training.

1.  Navigate to **System UI > Welcome Page Content**.
2.  Open the **Welcome to** page.
3.  Select the **Active** checkbox.

**Email properties**

Email is disabled during the cloning process and must be re-enabled. The process of configuring email properties is different for ServiceNow email servers and custom email servers. Users with the admin role can change email properties.

**ServiceNow mail servers**

If your instance uses ServiceNow mail servers, most of the important email properties are configured automatically. Cloning does not overwrite the email settings of the target instance although it does disable email.

To enable email:

1.  Navigate to **System Properties > Email**.
2.  Configure the email properties:  
    
    -   Enable email sending (SMTP) (_**glide.email.smtp.active**_): Yes
    -   Enable email sending (POP3) (_**glide.email.read.active**_): Yes
    
    For more information, see [Email Properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties") in the product documentation.
    
3.  Click **Save**.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5; cellpadding: 2px;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> If the instance is a hosted development instance being cloned to production, <a title="log an incident" href="/kb_view.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer">log a Case</a> to have the mail server password set up.</td></tr></tbody></table>

**Custom mail servers**

If you are not using ServiceNow email servers, you must [configure](https://docs.servicenow.com/csh?topicname=t_ConfigureAnEmailAccount.html&version=latest "Configuring Email") several ServiceNow properties. Edit email properties to avoid unnecessary messages being sent or processed by the custom mail server.

1.  Navigate to **System Properties > Email**.
2.  Configure the email properties as described in the table below.  
    For more information, see [Email Properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties") in the product documentation.
3.  Click **Save**.

<table class="internalTable" style="border-style: solid; border-color: #000000;" border="1" cellspacing="0" cellpadding="4" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Property</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Setting required</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Enable email sending (SMTP)<br><p>(<em><strong><tt>glide.email.smtp.active</tt></strong></em>)</p></td><td style="vertical-align: middle; text-align: left;">Yes</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Enable email receiving (POP3)<br><p>(<em><strong><tt>glide.email.read.active</tt></strong></em>)</p></td><td style="vertical-align: middle; text-align: left;">Yes</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Outgoing (SMTP) mail server<br><p>(<em><strong><tt>glide.email.server</tt></strong></em>)</p></td><td style="vertical-align: middle; text-align: left;">URL to your SMTP server. For example, <span style="font-family: 'Andale Mono', monospace;">smtp.yourdomain.com</span>.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">User email (eg. helpdesk@company.com) that is used to login to the SMTP server optionally.<br><p>(<tt>glide.email.user</tt>)</p></td><td style="vertical-align: middle; text-align: left;">Email address to use for SMTP authentication. For example, <span style="font-family: 'Andale Mono', monospace;">smtp@yourdomain.com</span>. Define a different email account for each instance.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Outgoing (SMTP) mail server password.<br><p>(<em><strong><tt>glide.email.user_password</tt></strong></em>)</p></td><td style="vertical-align: middle; text-align: left;">Password for your SMTP server.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Email address to which all emails will be sent.<br><p>(<em><strong><tt>glide.email.test.user</tt></strong></em>)</p></td><td style="vertical-align: middle; text-align: left;">Email address to use for testing. Allows you to enable notification but direct all messages to a single mailbox.</td></tr></tbody></table>

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> Contact your mail administrator to set up the mail server password.</td></tr></tbody></table>

**User access**

Consider restricting user access to each environment using these guidelines:

-   **Development:** Lock out all accounts except for administrators
-   **Testing:** Lock out all accounts except for administrators and users actively involved in user acceptance testing for releases
-   **Training:** Lock out users not participating in training

User access can be restricted through a script or manually on a per-user basis.

**Update sets**

Update sets are used to track changes made to a specific instance. Transfer update sets between instances to move customizations from development to testing environments and then on to a production system.

If you ever plan to upgrade an instance version outside of cloning, do not delete update set records. The upgrade process uses the records to restore your customizations.

**LDAP**

Disable imports and updates in the development and testing instances.

1.  Navigate to **System LDAP > LDAP Servers** on a development or testing instance.
2.  Open each record and clear the **Active** checkbox.
3.  Click **Update**.

**Scheduled jobs**

Disable active scheduled jobs in the development and testing instances to avoid duplication of jobs and to provide a clean system for development. Always check for the instance name in the scheduled job so that the scripted schedule job runs only in one instance. In the example script below, the script runs only on the instance named my\_instance\_name.

1.  Navigate to **System Definition > Scheduled Jobs** in a development and testing instance.
2.  Open each active, scheduled job and clear the **Active** checkbox.
3.  Click **Update**.  
      
    **EXAMPLE SCRIPT THAT CHECKS FOR THE INSTANCE NAME**  
    
    doSomething();  
       
    function doSomething() {  
      var thisInstance = gs.getProperty("instance\_name");  
      var instanceToRunOn = "my\_instance\_name";  
      
      if (thisInstance != instanceToRunOn)   
        return;  
      
      //start processing here  
      gs.print('this is running');  
    }
    

**MID Servers**

If you are using MID servers for Discovery or Orchestration:

-   Ensure that the users configured on the MID servers in the config.xml file are also on the instance.
    
-   Empty the ecc\_sender folder on the MID Server queue. This gives the cloned instance a clear queue.
    

### Troubleshooting the MID Server

Ensure that your MID Server user credentials match the credentials that all the MID Servers connected to the target instance are configured to use. It is possible that the source MID Server user credentials copied into the target instance do not match those used by the existing set of target MID Servers. Check MID Server Issues on the MID Server dashboard for post-cloning errors pertaining to the current MID Servers. The MID Server Issue \[ecc\_agent\_issue\] table stores records of MID Servers that are down after an instance clone and publishes error messages regarding suspected issues with bad credentials. Error checking in this table only examines MID Servers that existed on the target instance prior to the clone. You can view records from the ecc\_agent\_issue table in the **MID Server Issues** related list in the MID Server form. The instance retains records in this table for 30 days.

### Automating configurations

If you clone frequently, it may be helpful to have a script that automates post-clone changes. The script must exist in your source instance so it is copied with the clone. Work with ServiceNow to add protection and ensure that you cannot run the script in your source instance. The following procedure includes a sample script that you can edit to fit your environment. Set the correct values in the first section.

Administrators can perform the following process. If the instance is running High Security, see [Elevated Privilege](https://docs.servicenow.com/csh?topicname=c_ElevatedPrivilege.html&version=latest "High Security Settings") in the product documentation.

1.  Copy the script to any text editor and save it with a file extension of _._js.
2.  Upload the file to your source instance by navigating to **System Definition > Upload File**.  
    This module uploads the file only to the current node.
3.  Navigate to **System Definition > Scripts - Background**. You might need to enable the **Scripts-Background** module, as described in [Enable or disable an application menu or module](https://docs.servicenow.com/csh?topicname=t_EnDisableAppMenuOrMod.html&version=latest).
4.  View and run the script.  
    
    //define the instance names here  
    var devInstance = "mydev";  
    var devEmailRedirect = "myemail@mycompany.com";  
    var qaInstance = "myqa";  
    var prodInstance = "my";  
       
    //get this instance's name  
    var thisInstance = gs.getProperty("instance\_name");  
    switch (thisInstance) {  
     case devInstance:  
      devConfig();  
      break;  
     case qaInstance:   
      qaConfig();  
      break;  
     case prodInstance:   
      gs.print("\*\*\*\* You're running this script in production, are you asking for trouble?");  
      break;  
     default:   
      gs.print("\*\*\*\* I don't understand what this instance is for: " + thisInstance);  
    }  
       
    function devConfig() {  
     //set the base color  
     gs.setProperty("css.base.color","mediumseagreen");  
        
     //disable email notifications  
     gs.setProperty("glide.email.read.active",false);  
      
     //disable all LDAP servers  
     var ldap = new GlideRecord("ldap\_server\_config");  
     ldap.query();  
     while (ldap.next()) {  
      active = false;  
      ldap.update();  
     }  
      
     //set header name  
     gs.setProperty("glide.product.description","DEV Instance");  
     gs.print("Applied Dev Configurations");  
    }  
      
    function qaConfig() {  
     //set the base color  
     gs.setProperty("css.base.color","darkred");  
     //redirect all messages  
     gs.setProperty("glide.email.test.user",devEmailRedirect );  
      
     //set header name  
     gs.setProperty("glide.product.description","QA Instance");  
     gs.print("Applied QA Configurations");  
    }
    

### Release

All Releases

### Resolution

Perform the following tasks after your production instance is cloned:

-   Update the welcome page
-   Change the email properties
-   Restrict user access
-   Modify LDAP to disable imports and updates.
-   Disable active scheduled jobs
