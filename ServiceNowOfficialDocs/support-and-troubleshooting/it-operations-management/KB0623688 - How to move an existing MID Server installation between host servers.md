---
title: "How to move an existing MID Server installation between host servers"
aliases:
  - KB0623688
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623688
kb_number: KB0623688
last_modified: 2024-07-25
---

## How to move an existing MID Server installation between host servers

  

### Issue

It may be necessary to move an active MID Server installation from one host to another, perhaps to change data-centers, increase capacity, etc.

There are two ways to do this:

1.  Set up a new second MID server on the new host, that you would bring up, and then reconfigure all jobs in the instance to use the new MID Server instead. This migration could be a considerable amount of work depending on how many features use the MID Server, and how many individual jobs are configured within that feature.  
    This would not require any special tricks, as the forms where MID Servers are specified for particular jobs in the instance are fully documented, and the installation of the new MID Server can be done using the normal documented procedure.  
      
    
2.  Set up a new MID Server to appear identical to the existing MID Server, then shut down the existing MID Server, and bring up the replacement MID Server. All jobs in the instance will now be using the replacement MID Server, without having to do any changes in the instance, and in effect without the instance noticing at all.

**This article explains how to do the second method, to 'move' the existing MID Server to another host.**

In order to keep downtime to a minimum, you would need the replacement MID Server installation set up beforehand and configured to appear exactly like the existing MID Server, so that when you shut down the existing MID Server you can immediately start up the new one to replace it. The new MID installation must be manually set up as it cannot be allowed to be started until the existing MID Server is shut down.

Although copying the existing install folder to a new server is theoretically possible, a better approach would be to do a new clean install using the below process, to avoid bringing issues over from the old install, or files and setting not appropriate for the new host.

### Information required before starting

You will need the following information before starting:

1.  Take a copy of the .\\agent\\config.xml and .\\agent\\conf\\wrapper-override.conf files from the existing MID Server installation on the old server for reference.  
      
    
2.  Inspect the config.xml file, and from the parameters see which 'username' is being used by the MID Server to log into the instance. You will need to get hold of the password for that instance user.  
      
    
3.  If a Proxy Server is used then you will need to consider if that is still required from the new host server and if it is you will need to get hold of the password for the proxy server user. If a different proxy needs going through from the new server, then you will need to get similar proxy host, port, username and password details for that.  
      
    
4.  You will need remote access to both the existing and new host.

### Manual setup of the MID Server installation on the new host

Download the MID Server installation ZIP file to the new host using the link on the instance. **MID Server > Downloads >** Select the link matching the new server's OS.  
(Tip: Deliberately do this from the new host, as this is a good way to confirm the MID Server service will be able to download its auto-upgrade ZIP files in future from our install server.)  

Extract the ZIP file to the install location. e.g. C:\\ServiceNow\_MID\_Servers\\<instance-path>\\ and so the agent folder will be C:\\ServiceNow\_MID\_Servers\\<instance-path>\\agent\\

Open the agent\\config.xml file in a text editor, (ideally one such as Notepad++ or TextWrangler that knows how to colorize XML, as it will help find the parameters and avoid making mistakes)

In the 'REQUIRED Parameters' section, fill in the values of parameters 'url', 'mid.instance.username' and 'name' using the same values as the same file from the existing mid server. Type the 'mid.instance,password' in again as plaintext.

  <!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
       \* REQUIRED Parameters  
       \*  
       \* This section contains parameters that MUST be included in EVERY Mid Server  
       \* configuration.  
       \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->  
  
       <!-- Tells the MID server where to contact its associated Service-now instance.  Edit  
            this value to provide the URL of your organization's Service-now instance. -->  
       <parameter name\="url" value="**https://<instance-name>.service-now.com/**"/>  
  
       <!-- If your Service-now instance has authentication enabled (the normal case), set  
            these parameters to define the user name and password the MID server will use  
            to log into the instance.  -->  
        
       <parameter name\="mid.instance.username" value\="**mid\_user**"/>  
       <parameter encrypt\="true" name\="mid.instance.password" value\="**midpassword123**"/>  
     
       <!-- Defines the name by which your MID server is known on the Service-now instance.   
            Edit this value to provide the name you want, or leave it blank and the MID server  
            will make up a name. -->  
       <parameter name\="name" value\="**MID Server 1**"/>

The "COMMON OPTIONAL Parameters" section is where Proxy server setting would need adding, if these are required for the new host. These may be different from the old host, for example, if you are moving between sites or data-centers. This is the proxy the MID Server would need to go via in order to contact the instance. If you need to fill these in you would need to remove the <!-- and --> comment tags from around them first.  
You may also have a higher setting for 'threads.max' to enter, compared to the default 25.

  <!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
       \* COMMON OPTIONAL Parameters  
       \*  
       \* This contains selected parameters that MAY be included in ANY Mid Server  
       \* configuration.  These parameters were chosen because they are commonly needed.  To  
       \* include any particular parameter or group of parameters, uncomment the parameter(s)  
       \* you want.  
       \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->  
  
       <!-- Controls the number of execution threads (simultaneous work) that may be used by  
            probes. -->  
        <parameter name\="threads.max" value\="**50**"/>  
       <!-- These parameters specify a proxy server the MID server will use BOTH for contacting  
            your Service-now instance AND for downloading upgrades. -->

       <parameter name\="mid.proxy.use\_proxy" value\="**true**"/>  
       <parameter name\="mid.proxy.host" value\="**proxy.<your-domain>.com**"/>  
       <parameter name\="mid.proxy.port" value\="**8080**"/>  
  
       <!-- Set these parameters ONLY if your proxy requires a user name and password. -->  
       <parameter name\="mid.proxy.username" value\="**proxy\_user**"/>  
       <parameter name\="mid.proxy.password" value\="**proxy\_password**" encrypt="true"/>  
   

The "REQUIRED Parameters that are AUTOMATICALLY filled in" section will be empty, but you will need to manually add the mid\_sys\_id parameter. Copy this line from your existing mid server config file. This is the key to fooling the instance into thinking this is the same MID Server as before.

<!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
       \* REQUIRED Parameters that are AUTOMATICALLY filled in.  
       \*  
       \* This section contains parameters that are required, but will be automatically filled in  
       \* after the MID server first made contacts to your Service-now instance.  
       \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->  
           <!-- Records the unique ID of the MID server's record on the Service-now instance.  On  
            installation of the MID server, this value should be empty.  The MID server  
            will fill in this value after it first contacts your Service-now instance. -->  
       <parameter name\="mid\_sys\_id" value\="**4ef8f4fadbfffa0062be3600ad961971**"/>

Do not copy in the "keypairs.mid\_id" parameter, as that will cause problems (and just one of the reasons you don't simply copy the whole install folder).

Those are the vital parameters to allow the MID Server to log in and communicate with the instance. You may see other parameters that have been added, changed or set in the original MID Server's config.xml file. e.g. debug=true.  You may choose to also enter those parameters too if you need them, but that is not necessary as the instance records these parameters, and the mid server will synchronize those once it is up and running.

Save the changes.

Open the agent\\conf\\wrapper-override.conf file in a text editor.

Modifying the 'name' and 'displayname' is always a good idea, to avoid problems with conflicting service names when additional mid servers are installed on the same server, and to make it easier to identify which windows service matches which instance and installation. This doesn't have to match the existing MID Server install.

################################################################################  
\# Windows Service  
################################################################################  
\# The following properties must be unique per MID installed on the same system.  
#  
\# REQUIRED: Name token of the service  
wrapper.name=**snc\_mid\_<instance-name>\_1**  
\# REQUIRED: Display name of the service  
wrapper.displayname=**ServiceNow MID Server <instance-name> 1**

Since around the Geneva release the default java heap space (the amount of RAM the operating system allows the MID Server to use) defaults to 1GB. If your existing MID Server is still set on 512MB then this is a good opportunity to allow it to use 1GB, so don't change this. However if you were using a higher maxmemory setting in your existing MID Server, then un-comment and set this.

################################################################################  
\# System resources  
################################################################################  
\# Memory, CPU, etc. Remember to refer to < conf/wrapper.conf > for defaults.  
#  
\# OPTIONAL: Maximum Java Heap Size (in MB)  
wrapper.java.maxmemory=**2048**

Save the changes.

Do not start the MID server yet.

### Performing the changeover from the existing MID Server to the new one

This is the bit where you could have problems if the new MID Server does not come up. The assumption is that you have already tried this procedure out on a sub-production instance with one of its mid servers that presumably also needed moving, or installed an additional MID Server alongside the old one just for the sake of trying this out first.

If the new MID server does not work as expected, you can simply shut it down and start the old one again until you have the reason figured out.

1.  In the instance, open the MID Server form. You can use this to monitor the Up/Down status.
2.  On the new host, open a command prompt window (cmd.exe) run as administrator. Change directory to the agent folder of the new installation.
3.  On the existing MID Server host, stop the windows service. It will probably be called "ServiceNow MID Server" or similar. If you have more than one, be careful to have selected the right one. Refresh the services list to confirm the MID Server service has stopped.
4.  Immediately, on the new MID Server host, in a Command Prompt window, running as administrator, run start.bat
5.  In the instance, check to see if the MID Server comes back up. Keep refreshing the mid server form for a minute or 2 until Status=Up
6.  On the MID Server form, click 'Validate' in the related links, as if it were a new MID Server.
7.  Check the ECC Queue to see that the MID Server is now processing the jobs that were queued while the MID Server was down.

The MID Server downtime is not something that generally needs worrying about. Any jobs that were interrupted would be re-run, and any new jobs added to the ECC Queue while the MID Server was down will be run when the new MID Server came up again

### Potential Risks and other Questions

1. **The hostname and IP address of the MID Server's host will have changed. Is that going to cause a problem?**

If you have firewall rules implemented for the MID Server to access the instance or access some internal devices in order to do its jobs - e.g. Database server to import from - then those Firewall rules will need updating for the change in source hostname/IP address.

2\. **Does this change have any impact on inbound/outbound email?**

No. Emails do not go via the MID Server.

3. **Does this change have any impact on LDAP Authentication for users logging into the instance****?**

No. Real-time LDAP Authentication is not done via the MID Server, even if the MID Server is used for periodic user imports and the LDAP listener.

4\. **Is the MID server being used for anything I might not know about, that may be affected by the change?**

Possibly. The features the MID Server is used with are listed in the documentation - [Introducing the MID Server](https://docs.servicenow.com/csh?topicname=mid-server-landing.html&version=latest)

The following list URL has a filter that will show which kinds of probes and commands are being set via your MID Server in the last few days. This will help you identify some functions you were not aware you were using.  
/ecc\_queue\_list.do?sysparm\_query=topic!%3DHeartbeatProbe%5EORtopic%3DNULL%5Etopic!%3Dqueue.processing%5EORtopic%3DNULL%5Etopic!%3DSystemCommand%5EORtopic%3DNULL%5Etopic!%3Dqueue.stats%5EORtopic%3DNULL%5EGROUPBYtopic&sysparm\_first\_row=1&sysparm\_view=

5\. **What will happen with my Certificates?**

If you have added a Certificate to the cacerts file, using the Java keytool utility - e.g. for the Proxy server, or a database server - then this will need re-adding to the new installation. In theory the cacerts file can be copied. See [MID Servers and Certificates](https://support.servicenow.com/kb_view.do?sysparm_article=KB0863673 "MID Servers and Certificates").

6\. **What about all the extra JAR/Script/Script includes/MIB files added to the previous MID Server. Will they need adding too?**

Since around the Calgary release, all of these files in extlib should be added to the relevant table in the instance, and then they are automatically synchronized to all MID Servers, including the new one. If you have manually added files left over from before this feature was added to the product, then you should add those to the instance in the relevant tables.

If you have replaced JAR files from the lib folder of the MID Server for different versions, then see a better workaround in [KB0862383](https://support.servicenow.com/kb_view.do?sysparm_article=KB0862383 "KB0862383")
