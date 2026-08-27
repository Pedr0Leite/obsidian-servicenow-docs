---
title: "Tailing a MID server log file on Linux and Windows"
aliases:
  - KB0534869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0534869
kb_number: KB0534869
last_modified: 2024-04-30
---

## Tailing a MID server log file on Linux and Windows

  

### Issue

At times when working with a customer to review MID server issues, it is useful to tail the MID server logfiles. This way, one can review what is happening in real time, as commands are being run through the MID server.

As new lines are written to the logfile, they will be displayed to the screen. 

Linux and Unix

On Linux and UNIX the tail command is available and is used as follows:

\# tail -f agent0.log.0

The last 10x lines of the file will be displayed, and further lines will be displayed as they are written into the logfile.

One can also use the grep command to filter for specific input. For instance, if you only wish to display any _Warning_ messages (ignoring the case sensitivy), use the following:

\# tail -f agent0.log.0 | grep -i "warning"

To break out of the command use the following:

<CTRL>c

Windows

On Windows there are a number of applications available that can provide the same functionality as the Linux tail command. Notepad++ has a plugin available called _Document Monitor, LogExpert, Tail for Win32_, etc.

However, it is also possible to tail a file directly using PowerShell, and this is done as follows, from a PowerShell command window:

PS C:\\ Get-Content agent0.log.0 -Wait

Unlike the Linux command, which displays only the last 10x lines of the file first while waiting for further input, the above command will display the whole contents of the file, before it reaches the last line of the file and awaits further input. Therefore if the file is large, be prepared for the whole contents of the file to be displayed to the screen first.

Like the tail command in Linux, it is also possible to filter for specific messages. For instance, if you only wish to display any _Warning_ messages (case insensitive), use the following:

PS C:\\ Get-Content agent0.log.0 -Wait | where { $\_ -match "warning" }

To break out of the command use the following:

<CTRL>c
