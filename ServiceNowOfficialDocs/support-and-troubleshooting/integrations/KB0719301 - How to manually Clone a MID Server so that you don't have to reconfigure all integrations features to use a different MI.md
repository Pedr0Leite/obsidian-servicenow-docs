---
title: "How to manually Clone a MID Server so that you don't have to reconfigure all integrations features to use a different MID Server on the sub-prod instance after an Instance Clone"
aliases:
  - KB0719301
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719301
kb_number: KB0719301
last_modified: 2025-07-07
---

## How to manually Clone a MID Server so that you don't have to reconfigure all integrations features to use a different MID Server on the sub-prod instance after an Instance Clone

  

### Issue

A lot of features that use MID Servers, mostly Integrations features, still specify the MID Server to use directly, using the sys\_id of the MID Server, and on a sub-prod instance after a clone, MID Servers with those sys\_ids will not exist. Those features will therefor not work on the sub-prod instance after a clone without re-configuring them to use a different MID Server.

For Discovery and Orchestration and other features updated to use MID Server Selection based on IP ranges, Applications and (possibly custom) Capabilities this isn't an issue. Unfortunately Import Set Data Sources, LDAP Import and Listener, RESTMessageV2 etc. don't currently.

### Cause

MID Servers can only connect to one instance, and are set up to point to a URL of an instance. When an instance has been Cloned-over, even though it is now a copy of some other instance, those original MID Servers will still be pointing to it. The MID Server from the instance that was the Source of the Clone will still be pointing to that source instance only. Since [PRB1287729 was fixed in Madrid](https://support.servicenow.com/kb_view.do?sysparm_article=KB0688954 "PRB1287729 was fixed in Madrid"), all MID Server related records are excluded from the clone and preserved on the target to ensure those MID Servers remain properly configured and working after the clone. You can read more in [KB0786475 MID Servers and Clones](https://support.servicenow.com/kb_view.do?sysparm_article=KB0786475 "KB0786475 MID Servers and Clones")

However records for e.g. LDAP Servers will have been copied, including the reference to the production MID Server sys\_id. Those records now have broken references to MID Servers that do not exist for the clone target instance. A [post clone cleanup script](https://docs.servicenow.com/search?q=Post-clone+cleanup+scripts "post clone cleanup script") could be written to swap out these sys\_ids each time, but below is another idea.

### Resolution

**Warning**: Before considering this, please investigate exactly what you are using these MID Servers for, and whether it is a good idea. You may accidentally cause integrations that should only be running on production to also start running from the sub-production cloned instance. I those integrations push to other production systems, you could cause horrendous data loss and corruption.

You can clone a MID Server installation, so that you end up with 2 separate installations, but each has the same sys\_id. So long as they never point to the same instance URL, that is not going to cause conflicts or problems.

-   -   In the Production instance (Clone source):  
        1.  Make note of the **sys\_id and Name of the MID Server record** (ecc\_agent table) in the Production instance (clone source)  
              
            
    -   In the Sub-Production instance (clone target):  
        1.  Navigate to **MID Server -> Servers**
        2.  Click '**New**' button to open a new record
        3.  **Fill in the 'Name'** only, exactly as it was entered in the Installer/config.xml/production instance.
        4.  Right click the header, and **Save**
        5.  Right click the header, and **Export -> XML** (this record), and save the file to disk  
            ![](sys_attachment.do?sys_id=3b5edd7cdb457410471f9c41ba9619ac)  
            
        6.  Click **Delete**, to delete the record. (You are going to import it again later)
        7.  In a Text Editor, Open the XML file just saved.
        8.  **Edit the sys\_id value** in the XML, to change it to the sys\_id of the production MID Server record  
              
            ![](/sys_attachment.do?sys_id=375edd7cdb457410471f9c41ba9619ae)  
              
            
        9.  **Save**
        10.  Navigate to MID Server -> Servers
        11.  Right click a column heading, and select **Import XML**
        12.  Specify the file you just edited, and **Upload  
               
             **
        13.  A MID Server Status record also needs creating, to let the MID Server appear on the MID Server Dashboard, and to avoid syslog errors relating to missing records in this table.   
             -   In the 'filter navigation' box, type "ecc\_agent\_status.do" and Enter.
             -   Select the new MID Server record in the MID Server field, and Submit  
                   
                 ![](sys_attachment.do?sys_id=335edd7cdb457410471f9c41ba9619b7)  
                   
                 
    -   On the MID Server host:  
        1.  Confirm this host is a different host to the production MID Server host
        2.  Install a new MID Server, [in the normal way](https://docs.servicenow.com/search?q=install+a+mid+server "in the normal way"), **but don't Start it yet**.  
            
            1.  Give it exactly the same Name.  
                
            2.  Click **"Next"** a few times and then **"Exit**".  \*\* **Don't click "Start MID Server"** \*\*
            
            ![](sys_attachment.do?sys_id=375edd7cdb457410471f9c41ba9619b5)
        3.  **Open the config.xml file** in a text editor. You will see the url, username/password, name, and proxy setting are filled in for you by the installer UI.  
            
            1.  Scroll to the end of the file
            2.  You will see a line: **<parameter name="mid\_sys\_id" value=""/>**. 
            3.  Enter the sys\_id of the production MID Server record in this parameter value:  
                <parameter name="mid\_sys\_id" value="_SYS\_ID\_OF\_MID\_SERVER_"/>  
                
            4.  Save the file  
                
            
            ![](sys_attachment.do?sys_id=3b5edd7cdb457410471f9c41ba9619b3)
        4.  From a Command Prompt window, running as Administrator, run start.bat  
              
            ![](/sys_attachment.do?sys_id=b75edd7cdb457410471f9c41ba96199d)  
              
            
    -   In the instance:  
        1.  Once the MID Server record appears **Up** in the list in the sub-prod/clone target instance, **Validate it  
            **  
            ![](sys_attachment.do?sys_id=3f5edd7cdb457410471f9c41ba9619b1)  
              
            
    -   You should now be able to test your features copied with the clone that are configured to use a MID Server with this sys\_id or Name.
    -   This MID Server will still be there is you clone over the instance again in future, because MDI Server records are excluded and preserved in clones, so the MID Server only needs to be set up this once.

### Related Links

Since the fix for [PRB1380840](https://support.servicenow.com/kb_view.do?sysparm_article=KB0792539 "PRB1380840") and [PRB1330396](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743123 "PRB1330396") in New York version, it is now not possible to have more than one MID Server with the same name running on the same host, even if they are for different instances. The MID Servers will deliberately fail to start. Therefore to implement this trick, separate host servers may be required.

Since around Orlando/Paris, it is not possible to just change the sys\_id in config.xml any more. If there is not already a record with that sys\_id, a random sys\_id record is created on startup. You need to have a matching ecc\_agent record in the instance with the same name and sys\_id first in order to prevent a new random sys\_id record being created. This process deliberately has you create a new empty mid server record because when a record is imported from the production instance additional field values carried over can cause issues.
