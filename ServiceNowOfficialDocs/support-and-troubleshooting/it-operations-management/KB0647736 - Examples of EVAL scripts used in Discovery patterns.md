---
title: "Examples of EVAL scripts used in Discovery patterns"
aliases:
  - KB0647736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647736
kb_number: KB0647736
last_modified: 2025-11-17
---

## Examples of EVAL scripts used in Discovery patterns

  

### Issue

**Overview**

Service Mapping and Discovery use patterns to discover or map devices and applications in your organization. When you create or modify a pattern using the Pattern Designer, you can use EVAL scripts in pattern steps to evaluate strings in fields.

Use the eval() function for JavaScript as a parameter value.

This article describes how to apply EVAL scripts and provides examples of the most popular EVAL scripts for Java and for Groovy.

  

  

  

### Resolution

**Procedure**

1.  Type EVAL( and click the **Edit** icon ![](https://servicenow.suiteshare.net/bundle/kingston-it-operations-management/page/product/service-mapping/image/EvalEditIcon.png) next to the field.
2.  In the EVAL Script Editor window, ensure that the JavaScript mode is on or click Other for other types of scripts like Groovy.  
      
    ![](/sys_attachment.do?sys_id=835a2066db42b450e515c223059619f7)  
      
    
3.  Type the script in the editor pane.
4.  If necessary, use the **Search**, **Replace**, and **Format** buttons to modify the script. Linting and highlighting is available for JavaScript.
5.  Click **Apply**.  
      
      
    

**Examples of the most popular EVAL scripts for Java**

**To get device information via switch**

rtrn = "";
var type = ${proc\_scsi\_table\_disk\[\].type};
>switch (type){  case "cdrom":   rtrn = "cd";  
break;
case "CD-ROM":    rtrn = "cd";
break;
case "Direct-Access":    rtrn = "disk";
break;
default: rtrn = "logical";
}
)

  

**To change a list to a string** 

var rtrn = "";  
var array = ${temp\_description};  
var i;  
for (i=0; i<array.size() ; i++)  
rtrn = rtrn  + " \\n" + array.get(i); 

  

**To replace a string**

var name =${dep\_app1\[\].name};  
var rtrn;   
rtrn= name.replace('\_','#');

  

**To remove duplicates from a table by checking the specific name and version**

var tableWithoutDuplicates = '';
tableWithoutDuplicates =  DuplicateRemover.removeDuplicates(${PKG},\["name","version"\]);
CTX.setAttribute("PKG",  tableWithoutDuplicates);

  

**To remove duplicates from a table by checking the specific VIP server IP and serverPort**

var tableWithoutDuplicates = '';
tableWithoutDuplicates =  DuplicateRemover.removeDuplicates(${vserverServiceTable},\["vsvrName","serverIP", "serverPort"\]);
CTX.setAttribute("vserverServiceTable",  tableWithoutDuplicates);

  

**To format the system name**

  

var rtrn = '';
var hostnameFormatter = new Packages.com.glide.util.HostnameFormatter(${fqdnRegex});
hostnameFormatter.setCase(${hostnameCase});
hostnameFormatter.setIncludeDomain(${shouldIncludeDomain}=="true");
var formattedHostname = hostnameFormatter.format(${sysName});
rtrn = (formattedHostname)?formattedHostname.fFormattedName:'';

  

  

**To set the right status ID for the device for a** **failover**

  

 var rtrn = '';
if (${failureStatusId}=='0' || ${failureStatusId}=='1')
{
    rtrn='1';
}
else
{
   rtrn='2';
}

  

  

**To set the information (all interfaces) in one line**

  

var rtrn = '';
var interfaces = ${IfTable\[\*\].info}.toArray();
var line;
var i;
for ( i = 0; i < interfaces.length; i++ ){
rtrn+= interfaces\[i\] ;
 
if ( i % 2 == 1 ){
rtrn += '$$$$';
}
}

   

**To set a command to run all loadbalancer servers**

var rtrn = '';
 
var command =  "show lb vserver " + ${vserversTable\[\].vsvrName};
var rule\_def = CTX.getCommandManager().shellCommand(command, false, null, null, CTX);
rtrn = rule\_def; 

  

**To get information on all pool members** 

var rtrn = '';
 
try{
 
var command = "list sys db bigpipe.displayservicenames | grep value"
dummy= CTX.getCommandManager().shellCommand(command, false, null, null, CTX);
stat=dummy.split('"')\[1\]
 
var command = "modify sys db bigpipe.displayservicenames value false"
dummy= CTX.getCommandManager().shellCommand(command, false, null, null, CTX);
 
var command =  "list ltm pool all members | grep -e 'ltm pool' ':' 'address' 'state'";
var members\_def = CTX.getCommandManager().shellCommand(command, false, null, null, CTX);
 
var command = "modify sys db bigpipe.displayservicenames value " + stat
dummy = CTX.getCommandManager().shellCommand(command, false, null, null, CTX);
 
rtrn = members\_def;
} catch (e) {}

  

**To get clean sort** **description**

var rtrn = "";
var array = ${temp\_description};
var i;
for (i=0; i<array.size() ; i++)
rtrn = rtrn  + " \\n" + array.get(i); 

  

  

**To get the information on the edition of an application device**

  

var table = CTX.getAttribute("component\[\*\].str").toArray();
var edition;
for (var i =0; i<table.length; i++) {
var comp = table\[i\].toLowerCase();
if (comp.indexOf("coherence") > -1)
edition = "Suite";
else if (comp.indexOf("cluster") > -1)
edition = "Enterprise";
else
edition = "Standard";
}
edition;

  

**To translate a numeric MAC address to a standard format**

This eval script fixes the MAC address to the correct string (00:50:56:90:8B:16).

var mac = "005056908B16";
mac\_array = mac.match(/../g);
std\_format\_mac = mac\_array.join(":");

  

**Examples of the most popular EVAL scripts for Groovy**

**To remove new lines and spaces from a table**

This eval script removes \\n and the spaces from a table.

virtual\_server = ${servers\_groups\_table\[\].servers\_ports};
virtual\_server = virtual\_server.replaceAll('\\\\n','&')
virtual\_server = virtual\_server.replaceAll('\\\\s+',' ')
virtual\_server = virtual\_server.replaceAll('&','\\\\\\n')

  

return virtual\_server

  

**To get information with delimiter to split lines**

  

This eval script gets the information with a delimiter to split the lines. This information can be used later for parsing.

  

arry =  ${vserverFull\[\*\].info}
str = ""
 
for (i=0;i<arry.size();i++)
{
if (arry\[i\].contains('Type:'))
{
str = str + "####"+arry\[i\] + "\\n"
}
else
{
str =  str + arry\[i\]  + "\\n"
}
}
 
return str;

  

**To get the discovery type**

You can use this information later for finding the pattern run time.

ctx.getWork().getDiscoveryType(); 

  

**To determine a sudo user** 

You can use this script to find the privileged command to use.

return ${ctx}.getDiscoveryProvider(com.snc.sw.dto.ProviderType.SSH).getPrivilegedCommand();

  

**To transform an application path into a Windows path**

Replace forward slash </> with a backward slash <\\>.

${dep\_apps\[\].appdir}.replace('/',${fs})

  

**To replace WAR files with weblogic.xml information**

This eval script transforms files to folders after running the Weblogic.xml and removes the .war from the weburi Filed.

return ${uri\_table\[\].forEach}.replace(${substr},'')

  

**To iterate over a table and execute a shell command for each row**

This eval script is added to a transform table operation, where the same table (war\[\]) is used as the source and target field.

try {
return com.snc.sw.commands.SshCommand.getSSHProvider(ctx).execCommand(${war\[\].command});
}
catch (Exception e) {
return \\"None\\”;
}
