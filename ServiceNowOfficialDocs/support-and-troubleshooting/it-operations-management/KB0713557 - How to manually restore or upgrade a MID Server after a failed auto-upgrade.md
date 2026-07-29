---
title: "How to manually restore or upgrade a MID Server after a failed auto-upgrade"
aliases:
  - KB0713557
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713557
kb_number: KB0713557
last_modified: 2025-07-16
---

## How to manually restore or upgrade a MID Server after a failed auto-upgrade

  

### Issue

MID Server Manual Upgrade Steps, for issues where the expected Auto-Upgrade of the MID Server fails, or to repair a corrupted installation or missing files.

This procedure **should be considered a last resort**, and we would normally request you open a support Case in HI in order for the cause to be identified, as you may have to keep doing this on every upgrade if a mis-configuration causing it remains.

### Release

All releases

### Cause

There are several potential causes for a MID Server installation becoming corrupted or for an automatic upgrade to fail. Copying the agent0.log.0 and wrapper.log files from the mid server's agent\\logs folder, plus the upgrade-wrapper.log file from the temp folder if the upgrade service failed, will usually allow a specific PRB to be identified from the errors and logs seen. KB Articles specific to those PRBs may have less destructive workaround or ways to fix the MID Server so that it doesn't happen again.

Some of these causes can be resolved with this simple method, which can save a lot of time:  
[KB0779816 How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service, leaving the MID Server Down and the Service not running](https://support.servicenow.com/kb_view.do?sysparm_article=KB0779816 "KB0779816 How to continue a MID Server upgrade after it has crashed in the middle of the ServiceNow Platform Distribution Upgrade service, leaving the MID Server Down and the Service not running")  
[KB1646639 / PRB1734629  Mid server is failing with java.nio.file.FileSystemException, due to a file lock on wrapper.conf.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1646639) (fixed in Washington Patch 4)

**Note:** You may have seen other procedures that overwrite the existing files with new ones. The reasons this procedure is starting from a fresh folder, rather than overwriting the existing folder, is to be sure:

-   there are no file locks on the existing files.
-   we are not leaving extra files that should no longer be there in the new version
-   we are not keeping any corrupt or wrong temporary files that are generated on the fly while the MID Server was running

**Note:** This procedure also deliberately deletes the keystore, forcing the MID Server to recreate it, and requiring Validation again. This will mean any certificates added to the Unified Keystore, for the MID Server Web Server extension, for the web server's TLS certificate, and any certificate for mTLS authentication with the web server, will need manually adding again at the end.

### Resolution

Pre-Upgrade Steps: 

1.  Save logs and other details of the failed upgrade, so that it may be possible to find the cause later on.
2.  Gather the required information and configuration settings:  
    -   Instance Username and Password, for the instance user that the MID Server logs in as. This user will be shown on the mid server's form.
    -   Proxy server information if used, including the proxy server, username and password.
    -   Host server running the MID Server, the install folder and the Service name for it. The Home folder field is not on the MID Server form, but can easily be added to a list view.
    -   Have remote desktop access as an administrator to the host server.
3.  Backup the following files:  
    -   agent\\config.xml
    -   agent\\conf\\**wrapper-override.conf**
    -   agent\\jre\\lib\\security\\**cacerts  
        **Note: If the whole JRE folder is missing due to a failed upgrade, this file may be lost. So long as you never added additional certificates to this, that's OK.
4.  Download the current full MID Server package from your ServiceNow instance  
    -   Navigate to **MID Server - Downloads**
    -   Tick the checkbox at the bottom to unhide the Zip file links.
    -   Select the ZIP format link for your MID Server host's platform to download.
    -   Copy the ZIP file to the MID Server host.
    -   Extract the ZIP file to a temporary folder. Ensure there are no errors extracting the ZIP file.

Additional Steps, where the MID Server is still running and Up:

1.  Decide if it is really necessary to do these steps. There are usually other less destructive solutions once the cause is identified. This process will not solve network, communication or authentication issues.
2.  Make sure there are no scheduled jobs happening using the MID Server during the procedure especially if performing it in a PRODUCTION instance. Checking that no ECC Queue output records for the MID Server are currently in Ready or Processing state is also advised. Changing the ecc\_queue record's status to Error will prevent then being run as soon as the MID Server is back up.
3.  Stop the Mid Server service. 

Repair steps:

1.  Go to the existing MID Server installation folder, and rename the existing 'agent' folder and move it to a different location.  
    -   Use a name such as 'agent\_old-do\_not\_run' or similar so there is no confusion in future.
    -   If this is not possible because of files still in use by the operating system, then set the Service startup to Manual (so it doesn't run on startup), and restart the host server OS to free up the files.
2.  Move the recently extracted 'agent' folder to the original agent folder's location.
3.  Manually update the following files based on the information from the equivalent backup files, and credential information gathered earlier  
    -   config.xml  
        -   url, mid.instance.username, mid.instance.password, name
        -   mid\_sys\_id - needed to avoid the MID Server being seen as a duplicate)
        -   Other likely custom values:  
            -   mid.proxy.use\_proxy, and the various mid.proxy.\* parameters, if a Proxy is used between the MID Server and Instance
            -   threads.max, threads.expedited.max, threads.interactive.max if different from the defaults
            -   instance.date.format if different from the default
    -   conf/wrapper-override.conf  
        -   wrapper.name, wrapper.displayname.  
            **Note: These need to match the existing Windows Service name and display name**. If the upgrade failed due to a mismatch, then that can be corrected now to match the windows service.
4.  If you had a custom cacerts file, with SSL Certificates added to it, then copy the backup "cacerts" file over the one in the "agent\\jre\\lib\\security" folder. This is the Truststore, containing the standard set of Root CA certificates by default. You may have added internal root CA certificates, and any additional certificates required to allow connection to integration endpoints. This is different to the Unified Keystore.
5.  Start the MID Server Service
6.  Wait for the MID Server from in the instance to show the status Up. It is expected that the MID Server will restart itself after the first startup, so wait a few minutes for that to happen, and remain Up.  If it never comes up, check the agent0.log.0 and wrapper.log to understand why.
7.  Click **Validate** on the MID Server form. This will trigger another automatic restart of the MID Server, but afterwards it will be Up and the form should show it as Validated.

If you had added additional certificates in the Unified Keystore (quite rare), or were using a Custom Keypair (very rare):

1.  1.  Stop the mid server service on the host machine again
    2.  The agent\\bin\\scripts\\install-certificate.bat/.sh script can be used to add these back.
        1.  For adding back a custom keypair, see: [MID Server unified key store](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/mid-server/concept/mid-unified-keystore.html)
        2.  For adding back web server certificates, see: [Configure a secure MID Web Server extension](https://docs.servicenow.com/bundle/washingtondc-it-operations-management/page/product/event-management/task/configure-midwebserver-extension-secure.html)
    3.  Start the MID Server Service

### Related Links

If this procedure fails then you may need to install a new fresh MID Server, and then set up the Capabilities/IP Ranges/Applications similar to the broken MID Server, and then reconfigure features and jobs and clusters that used the broken MID Server to use the new one instead. Follow the usual fresh installation steps in the documentation:  
[Download the MID Server Files  
](https://docs.servicenow.com/search?q=Download+the+MID+Server+files "Download the MID Server Files")[MID Server Installation](https://docs.servicenow.com/search?q=MID+Server+installation "MID Server Installation")
