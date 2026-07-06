---
title: "How to Move the MID Server installation folder on a Windows host"
aliases:
  - KB0722880
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722880
kb_number: KB0722880
last_modified: 2024-04-07
---

## How to Move the MID Server installation folder on a Windows host

  

### Issue

You may need to move the MID Server installation folder to a different folder or disk on the same host server. This applies to a MID Server installed on Windows, however the general ideas remain the same for Linux.

### Release

**Any,** where a Windows hosted MID Server is installed. Versions prior to Geneva, or customers that don't run Discovery/Service Mapping, will not have a WMI Collector Service.  Versions from Orlando will not have a WMI Collector Service, as the PowerShell code in the main MID Server service is now used for all WMI probes/patterns.

### Cause

Valid reasons for needing to do this might be:

-   When you extracted the install ZIP file, you ended up with the zip file name as part of the folder name (easy mistake to make with Windows explorer).  
          e.g. C:\\Prod\_Disco\_MID\\**mid.madrid-12-18-2018\_01-07-2019\_0000.windows.x86-64**\\agent\\ -> C:\\Prod\_Disco\_MID\\agent\\
-   You included spaces and extended characters in the folder names, which causes problems for probes.  
          e.g. C:\\Bad Gottleuba-**Berggießhübel** MID Server\\agent -> C:\\East\_German\_MID\_Server\\agent
-   You installed within a **user profile**, such as on your user's Desktop or Download folder, which doesn't work well, even when the windows service is set to login as that user.  
          e.g. **C:\\Users\\Dave\\Desktop**\\agent\\ -> **C:\\ServiceNow\_MID\_Servers\\Prod\_Disco\_MID**\\agent\\
-   File permissions policy limitations on the current disk or folder may not meet the requirements. Perhaps causing problems for auto-upgrades.
-   You may need to move it to another disk due to underestimating how much disk space the MID Server would need, perhaps because you are needing to buffer large import sets, or use the Export Sets feature which must save files within the install folder. [MID Server system requirements](https://docs.servicenow.com/search?q=MID+Server+system+requirements "MID Server system requirements") suggests recommended minimums in various configurations.  
          e.g. **C:\\ServiceNow\_MID\_Servers**\\Prod\_Disco\_MID\\agent\\ -> **D:\\ServiceNow\_MID\_Servers**\\Prod\_Disco\_MID\\agent\\
-   ...and maybe others

### Resolution

Note: This is possible and safe to do, but I will leave it up to you to **decide if this process is more hassle than simply installing a new replacement MID Server in the right place**.

The only place a full path to a MID Server installation exists on the host is in the Registry keys that define the Windows Service. This procedure is based on manually moving the installation folder, and then updating the Windows Registry for the Windows Services to match the folder change.

The MID Server will have to be stopped while the change is made. You can't move files that are in use.

Warning: Any out-of-box code will use relative paths, relative to the agent folder.  This procedure assumes all custom code also uses relative paths. e.g. Powershell script locations in Orchestration activities, Export Set file paths, etc..

1.  Stop the relevant Services  
    1.  ServiceNow MID Server   
        1.  Open the Services Control Panel applet. Run: services.msc
        2.  Find the main MID Server service, and open it.   
            If the MID Server is named "Prod Disco MID" in the instance, and it was installed using the installer.bat installer, then:  
            Display name: "**ServiceNow MID Server\_Prod Disco MID**"  
            Service name: "**snc\_mid\_Prod Disco MID**"
        3.  Record the Service name
        4.  Confirm the Path to executable matches what you thought it was. If not you may be looking at the wrong MID Server Service.
        5.  Stop the MID Server Service
    2.  WMI Collector Service  
        1.  Find the WMI Collector Service. By default there is one, regardless of how many MID Servers are installed. There may be more than one. There may be none if you don't use any Discovery products, in which case ignore this bit.
        2.  Open each in turn until you find the one using the same agent folder in the Path to executable as your MID Server Service above
        3.  If there is only one, then the names are:
        4.  Display name: "**ServiceNow WMI Collector**"  
            Service name: "**ServiceNow WMI Collector**"
        5.  Record the Service name
        6.  Stop that WMI Collector Service, but only if it is using the binaries from this same MID Server install folder.

![](/sys_attachment.do?sys_id=7a0c642edb42b450e515c2230596191a)

Note: If anything else is locking files in the MID Server folder, you will first need to identify what they are and free up those locks. Resmon.exe will help identify the handles. This may be a command prompt, explorer windows, or an open file in a text editor for example.

1.  Move the installation folder  
    1.  Copy the agent folder. Don't try and actually move it, as you will almost certainly have file locks.
    2.  Paste it where you want it. 
    3.  Record the new path to the agent folder.
    4.  Delete the old folder. If Windows prevents you deleting some files, check you don't have any logs open. You may also need to stop other MID Server services which are sharing the WMI Collector Service. You may need to restart the host server to free up the locks.
2.  Modify the Registry  
    1.  Open the Registry Editor. Run: regedit.exe
    2.  Open this Key: Computer\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services
    3.  Find the keys within that with the Service Names **of both the ServiceNow MID Server service, and WMI Collector service**.
    4.  For each service   
        1.  Click the key, to display the data on the right side of the screen
        2.  Edit the ImagePath value to change the path. The main service value has the path in twice, so don't forget to modify both paths in the value.

![](/sys_attachment.do?sys_id=4b0c642edb42b450e515c22305961938)

1.  Update the Home Directory field on the MID Server record in the instance. This will avoid an 'Issues"record being automatically created for an unexpected folder change.  
    1.  Open a list of MID Server: MID **Server -> Servers**
    2.  **Personalize List Columns** to add the **Home Directory** column
    3.  Edit the folder patch from the list

![](sys_attachment.do?sys_id=8b0c642edb42b450e515c2230596193d)

1.  Start the Service again
2.  Check that the MID Server comes back Up again.
