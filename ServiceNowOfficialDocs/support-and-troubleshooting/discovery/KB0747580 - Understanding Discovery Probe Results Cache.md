---
title: "Understanding Discovery Probe Results Cache"
aliases:
  - KB0747580
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747580
kb_number: KB0747580
last_modified: 2024-04-07
---

## Issue

# Description

1\. This article describes the procedure to convert a sys\_id to base64 using a script.

2\. This use case is helpful to understand the Discovery Probe Results Cache.

3\. Discovery uses XML documents for the payload, and more often than not, these are considerably large documents. However, sometimes when you look at the payload field of an ECC Queue input record you only see the word '_processed'_ there.

4\. Discovery Performance is improved by caching probes results on the instance and only processing results that have changed. Probe results that have not changed do not need sensor processing, and therefore, the sensor does not run. The cache is turned on by default for base system probes and sensors whose output is unlikely to change. The word '_Processed'_ means that the probe results of that specific configuration item (CI) are cached and have already been 'Processed' and the payload hasn't changed since.

5\. The probe results cache records are stored in the Probe Results Cache \[discovery\_probe\_results\_cache\] table in a Key/Value pair format. See the screenshot below

![](sys_attachment.do?sys_id=4a6c686edb42b450e515c223059619ee)

7\. The "Key" value is the concatenation of the probe sys\_id in base64 and the CI sys\_id in base64. The "Value" value is the MD5 Checksum of the probe result encoded in base64.

# Procedure

In Order to find the cached Result of probe or the CI , follow the below steps :

1) Grab the sys\_id of the CI and the probe and convert them to base64 using the Script below :

var ciSysId = '\[replace\_ci\_sys\_id\_here\]'; 

var probesysId=‘\[replace\_probe\_sys\_id\_here\]’;

var CisysIdAsBase64 = convertToHex(ciSysId); 

var ProbesysIdAsBase64 = convertToHex(probeSysId); 

function convertToHex(cleaned\_hex) 

{ 

var binary = new Array(); 

for (var i=0; i<cleaned\_hex.length/2; i++) { 

var h = cleaned\_hex.substr(i\*2, 2); 

binary\[i\] = parseInt(h,16); 

} 

var base64\_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" 

var input = binary 

var ret = new Array(); 

var i = 0; 

var j = 0; 

var char\_array\_3 = new Array(3); 

var char\_array\_4 = new Array(4); 

var in\_len = input.length; 

var pos = 0; 

 while (in\_len--) 

{ 

char\_array\_3\[i++\] = input\[pos++\]; 

if (i == 3) 

{ 

char\_array\_4\[0\] = (char\_array\_3\[0\] & 0xfc) >> 2; 

char\_array\_4\[1\] = ((char\_array\_3\[0\] & 0x03) << 4) + ((char\_array\_3\[1\] & 0xf0) >> 4); 

char\_array\_4\[2\] = ((char\_array\_3\[1\] & 0x0f) << 2) + ((char\_array\_3\[2\] & 0xc0) >> 6); 

char\_array\_4\[3\] = char\_array\_3\[2\] & 0x3f; 

for (i = 0; (i <4) ; i++) 

ret += base64\_chars.charAt(char\_array\_4\[i\]); 

i = 0; 

} 

} 

if (i) 

{ 

for (j = i; j < 3; j++) 

char\_array\_3\[j\] = 0; 

char\_array\_4\[0\] = (char\_array\_3\[0\] & 0xfc) >> 2; 

char\_array\_4\[1\] = ((char\_array\_3\[0\] & 0x03) << 4) + ((char\_array\_3\[1\] & 0xf0) >> 4); 

char\_array\_4\[2\] = ((char\_array\_3\[1\] & 0x0f) << 2) + ((char\_array\_3\[2\] & 0xc0) >> 6); 

char\_array\_4\[3\] = char\_array\_3\[2\] & 0x3f; 

for (j = 0; (j < i + 1); j++) 

ret += base64\_chars.charAt(char\_array\_4\[j\]); 

while ((i++ < 3)) 

ret += '='; 

} 

return ret; 

} 

2\. In the script, replace the variables CiSysId and ProbeSysId as required.

3\. Concatenate both the variables and you will get the 'Key' value populated in the discovery\_probe\_results\_cache table.

# Applicable Versions

All
