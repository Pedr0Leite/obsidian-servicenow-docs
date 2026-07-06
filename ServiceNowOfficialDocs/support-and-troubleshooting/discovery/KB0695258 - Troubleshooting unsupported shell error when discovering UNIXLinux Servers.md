---
title: "Troubleshooting \"unsupported shell\" error when discovering UNIX/Linux Servers"
aliases:
  - KB0695258
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695258
kb_number: KB0695258
last_modified: 2026-02-26
---

## Troubleshooting "unsupported shell" error when discovering UNIX/Linux Servers

  

### Issue

Getting one of the following errors when discovering a device via SSH protocol:

(1) Unsupported shell, 'shell\_name', and probe parameter 'allow\_unsupported\_shells' is set to 'false'. Supported shells are \[ksh,bash,sh\]   
  
(2) No shell detected and probe parameter "allow\_unsupported\_shells' is set to false.  
  
(3) Shell is not in supported shell list

### Release

All currently supported environments.

### Resolution

(1) The first error is noticed when the shell\_name reported in the error is not part of the supported shells reported in the same error message (given that this shell is a known one like csh or tcsh), then check the MID Server parameter "**mid.ssh.shells\_supported**" (on the MID server that ran the discovery) where the supported shells are configured. This parameter defines the bourne-compatible shells supported by the MID Server and the default value is "**ksh,bash,sh**". You can then add your shell to the list. 

Please check our documentation for more information on the parameter: 

[MID Server parameters](https://www.servicenow.com/docs/r/servicenow-platform/mid-server/mid-server-parameters.html "MID Server parameters")

(2) This error means that over ssh, the device is not giving a specific shell to use. The action plan here would be to check the discovery user on the remote host and see what shell is specified in its configuration (/etc/passwd) and if there is no shell specified, add one of the supported shells in the file.

NOTE: 

There is a probe parameter called "allow\_unsupported\_shells" which is set on the probe itself and it allows SSH access to commands when a shell is not present on the remote system. This is usually used when discovering a network device without a defined shell. For more information on how and when to use this parameter, kindly refer to our documentation below:

[SSHCommand parameters](https://www.servicenow.com/docs/r/it-operations-management/discovery/r_Parameters.html "SSHCommand parameters")
