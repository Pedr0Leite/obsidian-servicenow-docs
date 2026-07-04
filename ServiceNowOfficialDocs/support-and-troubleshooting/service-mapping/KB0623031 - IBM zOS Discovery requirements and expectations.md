---
title: "IBM z/OS Discovery requirements and expectations"
aliases:
  - KB0623031
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623031
kb_number: KB0623031
last_modified: 2025-12-09
---

## Issue

# Discovery Limitations

* * *

We have a limited support for the **z/OS** server. We can discover the following:

-   **Server information:** OS Type, OS Version, OS Revision, Host name, System name and Serial number.
-   **Network information:** IP address, MAC Address, NIC Name.
-   **File System:** File System, Total Space, Free Space, Mount On and File system type.
-   The pattern can discover the following hosted application: WAS, DB2 and MQ which running on z/OS.

# Prerequisites

* * *

This section describes some of the required prerequisites.

## Prerequisites for horizontal discovery IBM z/OS MF

The prerequisites, commands and permissions that the customer will need to provide for IBM z/OS MF host and hosted application detection are as follows:

**General**

-   USS service running on port 22 on Z/OS.
-   SSH Credentials.
-   User have permission to write to /tmp.
-   User have permission to see all users processes.
-   User have permission to run REXX scripts.

Commands:

We need permissions to run the following commands:

-   uname
-   hostname
-   sysvar SYSNAME
-   netstat
-   df
-   ls
-   cat
-   grep
-   ps
-   cut

Get OS Type

-   uname –I
-   uname –v
-   uname –rm
-   uname –s

Get machine name

hostname

Get system name

sysvar SYSNAME

Get CPU info

run REXX script

## Prerequisites for horizontal discovery IBM z/OS MF

Get network information

netstat -g | awk '{if (NR>4) print \\$1,\\$3}'

Get gateway information

netstat -r | awk '{if (NR>3) print \\$1,\\$2,\\$5}'

Get IP array

netstat -h | awk '{if (NR>4) print \\$1}' | grep -v '127.0.0.1'

Get interfaces

netstat -R ALL | awk '{if (NR>1) print \\$0}'

Get File System information

df -k  | awk '{print \\$1,\\$2}' |sed -e s'/(//' | sed -e s'/)//' 2> /dev/null

## Prerequisites for discovery of MQ on IBM z/OS MF

-   Permission to run MQ commands from oeconsol
-   Read permission for MQ folder

Get MQ name from netstat:

"netstat -a | grep "+$port

Get MQ file system: "

df -k | grep MQ"

Get queue manager name: 

"echo "+$netstat\_info\[1\].mq\_name+" | cut -c1-4"

Get MQ logical name:

"oeconsol '-"+$queue\_manager+" display qmgr ALL'  "

Get queue info:

"oeconsol '-"+$queue\_manager+" display queue ("+$entry\_point.queue\_name+") ALL'  | tr \\"(\\" \\"#\\" | tr \\")\\" \\"\\""

Get queue info: 

"oeconsol '-"+$queue\_manager+" display queue ("+$name+")'"

Get channel info: 

"oeconsol '-"+$queue\_manager+" display channel(\*)  CONNAME  where(QMNAME EQ "+$remote\_queue\_mngr\_name+")'"

Get local queue info: 

"oeconsol '-"+$queue\_manager+" display qlocal(\*) '"

## Prerequisites for discovery of DB2 on IBM z/OS MF

-   Get DB2 name from netstat command

## Prerequisites for discovery of WAS on IBM z/OS MF

-   Permission to run "oeconsol 'D OMVS,A=ALL' | grep "+$taskname
-   Read permission for WAS installation folder
-   Read permission for was.env file

## Commands permissions for discovery of WebSphere on IBM z/OS MF

Get task name from our listening port: 

netstat -a | grep "+$port+" | awk '{print $1}'

Get user name, pid and task name:

oeconsol 'D OMVS,A=ALL' | grep "+$taskname

Get processes attributes: 

ps -ef -o user,pid,ppid,comm | awk '{print $1,$2,$3,$4}'

Get version from script: 

$install\_dir+"/bin/versionInfo.sh | grep Version | tail -1"

Get version from version file (failover): 

$install\_dir+"/properties/version/BASE.product"

Get list of URI files: 

"ls "+$conf\_dir+"/\*/\*/applications/\*/deployments/\*/META-INF/application.xml | xargs grep \\"<context-root>/"+$uri\_search+"\\""+" 1>/tmp/app.txt 2>/dev/null; cat /tmp/app.txt"

Read wsdl files under our ear directory: 

$ear\_directory\_name+"/\*/\*/\*/wsdl/\*.wsdl"

## Resolution

XXXXX
