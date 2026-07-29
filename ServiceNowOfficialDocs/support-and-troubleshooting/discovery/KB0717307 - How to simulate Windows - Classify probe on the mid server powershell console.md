---
title: "How to simulate Windows - Classify probe on the mid server powershell console"
aliases:
  - KB0717307
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717307
kb_number: KB0717307
last_modified: 2025-01-03
---

## Issue

# Description

* * *

This article describes the procedure to simulate Windows - Classify probe on the mid servers powershell console. You can simulate how discovery runs using this procedure.

# Procedure

* * *

1) Run the current way discovery runs and time it:

1.1) Run "Windows - Classify" probe:  
        1.1.1) Login to the MID server  
        1.1.2) Open a PowerShell session: Click Start button and search for PowerShell ISE.  
        1.1.3) For clarification: all command should be done on the PowerShell session unless instructed otherwise.  
        1.1.4) Navigate to the MID scripts directory by running the command: cd <MID Install directory>\\scripts\\PowerShell\\  
        1.1.5) Load modules into the session by running the following commands:  
                  1.1.5.1) Import-Module .\\Credentials.psm1  
                  1.1.5.2) Import-Module .\\WMIFetch.psm1  
                  1.1.5.3) Import-Module .\\DiagnosticsUtil.psm1  
                  1.1.5.4) Import-Module .\\LaunchProc.psm1  
                  1.1.5.5) Import-Module .\\XMLUtil.psm1  
                  1.1.5.6) Import-Module .\\PSRemoteSession.psm1  
        1.1.6) Sets a value to a variable by running the command: $computer = "<IP>";  
        1.1.7) Sets a value to a variable by running the command: $cred = Get-Credential;  
        1.1.8) A new window pops and asks for the credentials, please enter credentials for that Windows server  
        1.1.9) At this point you have all the environment set up to simulate a probe run against the windows host.  
        1.1.10) Copy the text from the file "Windows – Classify.txt" (attachment) and paste it into the PowerShell session you opened in step 1.1.2.  
        1.1.11) Press Enter to make sure you are in a new line  
        1.1.12) Run the following command to see if you got any results:  
                    fetch -computer $computer -cred $cred;  
        1.1.13) This may take a while.  
        1.1.14) You may get some error messages, but you should get a string that represents an XML, please save this output. If you did not get an XML –                        please capture the results  
        1.1.15) If you did get an XML as a result, please run the following command to time the process:  
                    Measure-Command { fetch -computer $computer -cred $cred; }  
        1.1.16) You should get a respond which shows how long the fetch command run

# Additional Information

* * *

You can use the same method to simulate other Windows powershell probes as well.
