---
title: "Discovery Linux - Disks Probe not Returning any Information for CCISS Presented Disk Devices"
aliases:
  - KB0524388
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0524388
kb_number: KB0524388
last_modified: 2025-06-25
---

## Discovery Linux - Disks Probe not Returning any Information for CCISS Presented Disk Devices

  

### Issue

Discovery Linux Disks Probe Not Returning Any Information for CCISS-Presented Disk Devices

  
  
Overview

* * *

The Discovery Linux - Disks probe returns information for all **IDE** and **SCSI** based disk devices on the server being discovered. A customer reported that disks presented from **HP Smart Array Controllers** using the **CCISS** driver were not returning any information from the Discovery Linux - Disks probe.

Run the hd.sh Script on the Linux Host as the Discovery User

* * *

If no information is returned from the Linux - Disks probe, test the **hd.sh** shell script embedded in the probe.  Run the script natively as the Discovery user on the Linux host where data was not retreived to verify it is working normally.  

1.  On your ServiceNow instance, navigate to **Discovery Definition -> Probes**.  
     
2.  Locate the **Linux - Disks** probe.  
     
3.  Click **Probe Parameters -> hd.sh** to open the shell script embedded in the **Value** section of the form.  
     
4.  Select all (**<CTRL>A** on Windows, or **<CMD>A** on a Mac) and copy the text (**<CTRL>C** on Windows, or **<CMD>C** on a Mac).  
     
5.  Using a terminal emulator (such as PuTTY, or Terminal) login to the Linux host using the Discovery user account.  
     
6.  From the account, open an editor session (such as vi/vim/emacs) and paste the contents (**<CTRL>V** on Windows, or **<CMD>V** on a Mac) into the file.  
      
    The file should now contain the contents of the **hd.sh** shell script.  
     
7.  Save the file as **hd.sh** in the home directory of the Discovery user.  
     
8.  Make the **hd.sh** shell script executable and then run the script:  
      
    _**$ chmod +x hd.sh  
    **__**$ ./hd.sh**_ 
9.  Check for errors.  
      
    If no information is returned for the disks that are presented onto the system, try to run the script from the **root** account. If the results are the same from the **root** account, follow the next procedure, Determine How the Disk Devices are Presented to Linux. 

Determine How the Disk Devices are Presented to Linux

* * *

If disks are not displayed using the script, the disks may be presented as **non-IDE** and **non-SCSI** disks. This can happen when the disks are using proprietary hardware or drivers. 

1.  To determine if disks are using proprietary hardware or drivers, use the **root** account and type the following command:   
      
    _**\# fdisk -l**_  
     
2.  For the devices displayed, view the **device** column.  
      
    **IDE** drives are listed as **/dev/hdxn** (where **x** represents a letter such as a, b etc... and **n** represents a number).  
      
    **SCSI** drives are listed as **/dev/sdxn** (where **x** represents a letter such as a, b etc... and **n** represents a number).  
      
    If you see **IDE** or **SCSI** devices represented that are not displayed using the **hd.sh** script, please contact **ServiceNow Customer Support** for further assistance.  
      
    You may see disk devices represented that **do not** follow the above naming convention. This example shows disks presented from a **Compaq/HP Smart Array Raid Controller**, which uses the **CCISS** driver. Example device names:  
      
    _**/dev/cciss/c0d0p1  
      
    **__**/dev/cciss/c0d0p2**_

The **CCISS** driver was deprecated in later versions of the Linux kernal and replaced with the **HPSA** driver. The HPSA driver shows disks presented from a **Compaq/HP Smart Array Raid Controller** using the standard **SCSI** naming convention. For information about transitioning to the HPSA driver, see the Hewlett Packard document ['hpsa' - A SCSI-based Linux device driver for HP Smart Array Controllers](http://h20000.www2.hp.com/bc/docs/support/SupportManual/c02677069/c02677069.pdf "'hpsa' - A SCSI-based Linux device driver for HP Smart Array Controllers"). 

Solution and Workaround

* * *

The **CCISS** driver has been deprecated within the Linux kernel. ServiceNow will not build in the functionality to discover these devices using the base system **hd.sh** shell script.

**Permanent Solution:**

Upgrade to a newer Linux kernel that supports the **HPSA** driver and transition your existing **CCISS** devices to **HPSA** standard **SCSI** presented devices. For information about transitioning to the HPSA driver, see the Hewlett Packard document **['](http://h20000.www2.hp.com/bc/docs/support/SupportManual/c02677069/c02677069.pdf "'hpsa' - A SCSI-based Linux device driver for HP Smart Array Controllers")**[hpsa' - A SCSI-based Linux device driver for HP Smart Array Controllers](http://h20000.www2.hp.com/bc/docs/support/SupportManual/c02677069/c02677069.pdf "'hpsa' - A SCSI-based Linux device driver for HP Smart Array Controllers").

**Workaround:**

Build a custom probe and sensor pair to obtain the information.

Use the existing **Linux - Disks** probe and sensor pair to create a custom pair. Rename the existing pair, click on the record header, and select "**Insert and Stay**" to create new records. The **hd.sh** shell script contained in the probe parameters should be modified to detect **CCISS** presented disks. 

<table class="noteTable" align="left"><tbody><tr><td><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td><strong>Note</strong>:&nbsp;Do not modify the base system&nbsp;<strong>Linux - Disks</strong>&nbsp;probe and sensor pair. Changing the existing pair could affect future <span style="text-decoration: underline;"><span style="color: #0000ff;"><a title="upgrades" href="https://support.servicenow.com/kb_view.do?sysparm_article=KB0547245" target="_blank" rel="noopener noreferrer"><span style="color: #0000ff; text-decoration: underline;">upgrades</span></a></span></span> of the probes.</td></tr></tbody></table>

### Release

All

### Resolution

.
