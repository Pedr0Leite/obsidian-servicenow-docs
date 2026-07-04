---
title: "Pattern discovery error: \"all commands failed on host\" or \"all command implementations\""
aliases:
  - KB0656183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656183
kb_number: KB0656183
last_modified: 2026-07-02
---

## Pattern discovery error: "all commands failed on host" or "all command implementations"

  

### Issue

During pattern discovery on a device, one of the following errors may appear:

-   All command implementations  
-   all commands failed on host

For example:

all commands failed on host <IP\_ADDRESS>. command type: <COMMAND\_TYPE>. command track:  
ShellCommand\\(NotRelevant),  
WindowsShellCommand\\(NotRelevant),;input 

The command output shows \`NotRelevant\` for every command implementation, meaning no command implementation was attempted. This occurs because the operating system class of the target device is not associated with any command in the sa\_mapping\_ext\_commands table. 

### Release

All Supported Releases

### Resolution

The table \[sa\_mapping\_ext\_commands\] contains the list of commands patterns will execute, and the operating system classes that those commands are relevant for.

In order to relate a command for the a custom class, the following steps must be followed: 

1.  (If a custom class) Create a new record for the new Operating System Class in the \[sys\_choice\] table:   
    1.  Navigate to the \[sys\_choice\] table. 
    2.  Add a new record with the following details:   
        Table = Mapping Discovery Commands \[sa\_mapping\_ext\_commands\].   
        Element = os\_class\_name.   
        Value = the new table name.  
2.  Add the new class to the desired command:   
    1.  Navigate to the \[sa\_mapping\_ext\_commands\] table. 
    2.  Click on the relevant command, for example, Shell. 
    3.  Add the new class to the Operating System Class Name list.
