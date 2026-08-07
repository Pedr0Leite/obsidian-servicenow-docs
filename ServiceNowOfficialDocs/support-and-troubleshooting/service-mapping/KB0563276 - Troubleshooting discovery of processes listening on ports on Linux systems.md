---
title: "Troubleshooting discovery of processes listening on ports on Linux systems"
aliases:
  - KB0563276
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563276
kb_number: KB0563276
last_modified: 2026-05-26
---

## Troubleshooting discovery of processes listening on ports on Linux systems

  

### Issue

 

Service Mapping runs the command correctly, displays the process number in the result, but fails to extract it properly and displays an error message.

### Symptoms

The following discovery error is displayed: _Failed to find process on port. Failed to detect listening process. tcp 0 0 ::ffff:ip\_address LISTEN process\_num/process name._ 

### Release

### Cause

When running the netstat command on Linux systems, Service Mapping may encounter unexpected information related to **IPv6** in the result, which breaks the result parsing and prevents Service Mapping from detecting the process number.

### Resolution

A code fix for Geneva P4 and higher addresses the issue.

For earlier Geneva releases, the following solution uses an external command to override the ProcessOnPort command for Linux:

1.  Go to **System Definition > Tables**.
2.  In the **Name** field, search for sa\_mapping\_ext\_commands.
3.  Select the **Mapping External Discovery Commands** entry.
4.  Scroll down, and select the **Operating System Type.**
5.  On the **Reference specification** tab, set an additional condition:
    1.  Select **OR**.
    2.  From the first list, select **Element**.
    3.  For the operator, select **Is**.
    4.  From the second list, select **os\_type**.
    5.  Select **Update**.

![Dictionary Entry page](/sys_attachment.do?sys_id=daab69da47c94314d1a5ab29736d4325 "Dictionary Entry page")

1.  Go to **Service Mapping > External discovery commands**.
2.  Select **New**.
3.  In the **Name** field, enter **Process on port IPv6 - Linux**.
4.  Next to **Operating System Type**, select the padlock icon, and then select **Linux**.
5.  In the **Type** field, select **PROCESS\_ON\_PORT**.
6.  In the **Order** field, enter **\-1**.
7.  In the **Script** pane, paste the following script:

var logger = Packages.com.snc.sw.log.DiscoLog.getLogger("LinuxProcessOnPortCommand");  
logger.debugex("In external command process on port Linux");  
var portCommand = new Packages.com.snc.sw.commands.ProcessOnPortCommand();  
var input\_port = new JSON().decode(input);  
var portInt = +input\_port\['localPort'\];  
var portCommandArguments = new Packages.com.snc.sw.commands.arguments.PortCommandArguments(ctx, portInt);  
var filter = portCommandArguments.getFilter();  
var portCommandArguments2 = new Packages.com.snc.sw.commands.arguments.PortCommandArguments(ctx, portInt, input\_port\['localAddress'\], filter);  
var openPortsCommand = new Packages.com.snc.sw.commands.OpenPortsSshCommandLinux();  
var openPorts = openPortsCommand.execute(portCommandArguments2);  
if (openPorts.size() > 0) {  
 var proc = portCommand.execute(portCommandArguments2);  
 if (proc != null) {  
 var output = {};  
 output\['pid'\] = proc.pid;  
 output\['commandLine'\] = proc.commandLine;  
 output\['executable'\] = proc.executable;  
 output\['executablePath'\] = proc.executablePath;  
 output\['parentProcessId'\] = proc.parentProcessId;  
 output\['userName'\] = proc.userName;  
 output\['currentDir'\] = proc.currentDir;  
 output\['workingDir'\] = proc.workingDir;  
 if (proc.environmentVariables != null) {  
 var env = {};  
 for (var key in proc.environmentVariables.keySet()) {  
 var envVar = {};  
 envVar\['name'\] = key;  
 envVar\['value'\] = proc.environmentVariables\[key\];  
 env\[key\] = envVar;  
 }  
 output\['environmentVariables'\] = env;  
 }  
 output = new JSON().encodeObject(output);  
 logger.debugex("In external command process on port Linux - DONE");  
} else {  
// proc is null. try with similar ipv6 address  
//Packages.com.glide.util.Log.debug('try to find listening port on ipv6 address');  
var ipv6 = "::ffff:" + input\_port\['localAddress'\];  
var portCommandArguments3 = new Packages.com.snc.sw.commands.arguments.PortCommandArguments(ctx, portInt, ipv6, filter);  
 proc = portCommand.execute(portCommandArguments3);  
 if (proc != null) {  
 var output = {};  
 output\['pid'\] = proc.pid;  
 output\['commandLine'\] = proc.commandLine;  
 output\['executable'\] = proc.executable;  
 output\['executablePath'\] = proc.executablePath;  
 output\['parentProcessId'\] = proc.parentProcessId;  
 output\['userName'\] = proc.userName;  
 output\['currentDir'\] = proc.currentDir;  
 output\['workingDir'\] = proc.workingDir;  
 if (proc.environmentVariables != null) {  
 var env = {};  
 for (var key in proc.environmentVariables.keySet()) {  
 var envVar = {};  
 envVar\['name'\] = key;  
 envVar\['value'\] = proc.environmentVariables\[key\];  
 env\[key\] = envVar;  
 }  
 output\['environmentVariables'\] = env;  
 }  
 output = new JSON().encodeObject(output);  
 }  
 logger.debugex("In external command process on port Linux - DONE");  
 }  
}  
 

8\. In the **Order** field, enter **\-1**.

9\. Select **PROCESS\_ON\_PORT** from the **Type** list.

10\. Select **Update**.

![Scripts - Background window showing Process On Port IPV6 - Linux ](/sys_attachment.do?sys_id=2eab69da47c94314d1a5ab29736d438b "Scripts - Background window showing Process On Port IPV6 - Linux ")
