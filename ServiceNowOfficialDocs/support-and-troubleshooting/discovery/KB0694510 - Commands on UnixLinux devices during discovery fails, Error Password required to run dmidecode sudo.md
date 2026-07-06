---
title: "Commands on Unix/Linux devices during discovery fails,  Error: \"Password required to run dmidecode sudo\""
aliases:
  - KB0694510
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694510
kb_number: KB0694510
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Run discovery against Unix/Linux device where the credentials being used are of SSH Private Key type or regular SSH credentials. 

On commands that need sudo the command fails even though command is added to sudoers file with NOPASSWRD configured for them

You will see an error in the input payload of the discovery SSH commands probe, like:

-   Exit status 1. Password required to run \[SSH\_command\_attempted\] under sudo

                                            ![Error you will see in the payload](sys_attachment.do?sys_id=c59da8e2db82b450e515c2230596195a "Error you will see in the payload")

# Release

* * *

All

# Cause

* * *

The MID server fails to parse the output of the sudoers file correctly when there is a long line in the file and it prompts the user for a password. This happening when using SSH keys. 

If you run 'Sudo -l' on the target CI terminal for the user you are using to run discovery you will see an output of all commands that are in the sudoer file. 

If that list exceeds 255 characters then it will be truncated in the terminal and might miss some of the commands that are in the sudoer file

# Resolution

* * *

Add the following parameter to all MID servers that will run this command and use that private SSH credential.

Do Run the following steps:

1.  Go to the MID server record > Go to MID server's "Configuration Parameters" tab
2.  Click "New"
3.  Set value = 1023 (1024 characters, should be plenty)
4.  Select parameter "mid.ssh.terminal.width"
5.  Save
6.  You will have to restart all MID servers that this needs to be applied to after saving.

# Screenshot

* * *

  ![SSH Terminal Character Length Property](sys_attachment.do?sys_id=419da8e2db82b450e515c22305961960 "SSH Terminal Character Length Property")
