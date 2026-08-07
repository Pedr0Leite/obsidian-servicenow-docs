---
title: "SQL discovery fails with error  \"Failed to copy file X:/ServiceNow/Discovery/\"
aliases:
  - KB0747630
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747630
kb_number: KB0747630
last_modified: 2024-04-07
---

## SQL discovery fails with error "Failed to copy file X:/ServiceNow/Discovery/"

  

### Issue

# Symptoms

-   SQL DB pattern discovery fails with below errors 

xxxx-xx-xx xx:xx:xx: WMI command execution on host 10.10.10.10 failed. command: %SystemRoot%\\system32\\netstat -a -n -o | %SystemRoot%\\system32\\findstr /R ":1433" error: Unable to create remote process. command: cmd /C "%SystemRoot%\\system32\\netstat -a -n -o | %SystemRoot%\\system32\\findstr /R ":1433" > f80986262-f8cc-41f8-afff-44b53f470152.out 2>&1". Error code: Unknown failure (8)  
xxxx-xx-xx xx:xx:xx: Failed to find process on port. Failed to execute WMI command on host 10.59.23.56 command: %SystemRoot%\\system32\\netstat -a -n -o | %SystemRoot%\\system32\\findstr /R ":1433" error message: Unable to create remote process. command: cmd /C "%SystemRoot%\\system32\\netstat -a -n -o | %SystemRoot%\\system32\\findstr /R ":1433" > f80986262-f8cc-41f8-afff-44b53f470152.out 2>&1". Error code: Unknown failure (8)

xxxx-xx-xx xx:xx:xx: Put file on Windows host 10.10.10.10 failed. filePath: 64/msvcp100.dll error: Unable to execute the command. None of the command implementations was successful.  
Command NeebulaWMI.PutFileUsingAdminShare failed. System.Exception: Failed to copy file C:/ServiceNow/Discovery/xxxxxxxx/xxxxxxxxxxxxx/bin/sw\_wmi/bin/64/msvcp100.dll. Could not find a part of the path '\\\\10.10.10.10\\c$\\temp\\msvcp100.dll'.

# Release

-   All releases

# Environment

-   SQL DB installed on Windows host

# Cause

-   Patterns can run commands on a target server to collect data. Depending on the method used to collect the data, a new connection is created from the target back to the MID server to return the information.
-   While discovery executes, the process might need to download some files from MID server to Windows host to create the process of fetching data, Discovery process chooses to copy the files to a Temporary directory the host location **"'\\\\10.10.10.10\\c$\\temp\\"**
-   Below command is asking the target server to put msvcp100.dll from the MID server to the target. 

Failed to copy file C:/ServiceNow/Discovery/xxxxxxxx/xxxxxxxxxxxxx/bin/sw\_wmi/bin/64/msvcp100.dll. Could not find a part of the path '\\\\10.10.10.10\\c$\\temp\\msvcp100.dll'.

**The issue could be :**  

-   The admin$ is not accessible from the MID Server.  
-   The temp directory **"'\\\\10.10.10.10\\c$\\temp\\"** is not available on the host 
-   Something is broken on the host kernel level and Discovery could not execute the commands to create the process to fetch the data.

# Resolution

-   Try Restarting the Windows host
-   Perform a quick test from the MID Server by logging on with user 'xxxx\\snow' and verify if able to reach the admin share **"'\\\\10.10.10.10\\c$\\temp\\"** and copy a test file. 
-   Communicate with Windows admin and create temp directory under  **"'\\\\10.10.10.10\\c$\\** and test the Discovery
