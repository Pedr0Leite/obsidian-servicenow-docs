---
title: "AIX server discovery is updating the CI with 'uname' and not the 'nslookup' commands"
aliases:
  - KB0783148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783148
kb_number: KB0783148
last_modified: 2024-04-07
---

## Issue

From OOB AIX Server Pattern it is updating the CI with the hostname. 

On Step 1. Unix\\Linux Name Formatting 

1.1. Get system info:  
It is using this command for: "uname -a", which displays computer system information.  
The result of this: "wanotesprd2".

1.2. Extract OS name from uname  
1.3. Extract hostname from uname  
1.4. Extract OS version from uname  
1.5. Create formattedHostname variable  
1.6. Decide whether to use the new name or the old one for formatting  
1.7. Format hostname w/ the following value:  
var rtrn = '';  
var hostnameFormatter = new Packages.com.glide.util.HostnameFormatter(${fqdnRegex});  
var source = (${computer\_system.managementIP})?${computer\_system.managementIP}:null;  
hostnameFormatter.setCase(${hostnameCase});  
hostnameFormatter.setIncludeDomain(${shouldIncludeDomain}=="true");  
hostnameFormatter.setSource(source);  
var formattedHostname = hostnameFormatter.format(${formattedHostname});  
rtrn = (formattedHostname)?formattedHostname.fFormattedName:${osHostname};  
  
2\. Insert OS name, version and name to cmdb\_ci\_aix\_server  
  
Step 3. DNS > 3.1. Get DNS name - format 1:  
It is using this "nslookup " + $computer\_system.managementIP  
The results of this "nunotes3.nu.com"

Fast forward to:

16\. UNIX - Find FQDN  
It will run the "unix\_fqdn.sh" 

  
17\. Update FQDN in AIX CI  
using this command  
$cmdb\_ci\_aix\_server\[\*\].fqdn

So this would bring back the fqdn (uname).

## Resolution

I created a couple of steps in the AIX Pattern:  
18\. Reference to library "PopulateAIXNamefromNSLookup"  
  
18.1. GetNamefromNSLookUP:  
"nslookup " + $computer\_system.managementIP  
This step basically gets the name from nslookup and then uses this variable 'serverNameTemp'  
  
  
18.2. AssignTempServer Name to AIX CI Name:  
Assigns the variable 'serverNameTemp' to the $cmdb\_ci\_aix\_server\[\*\].name
